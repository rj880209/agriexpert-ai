"""
Weather services for AgriExpert AI - Open-Meteo API integration
"""

import requests
from datetime import datetime
from config import WEATHER_THRESHOLDS


def geocode_location(place: str) -> dict | None:
    """Convert a place name to lat/lon using Open-Meteo geocoding."""
    try:
        resp = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": place, "count": 1, "language": "en"},
            timeout=5,
        )
        data = resp.json()
        if data.get("results"):
            r = data["results"][0]
            return {
                "lat": r["latitude"],
                "lon": r["longitude"],
                "name": r.get("name", place),
                "country": r.get("country", ""),
            }
    except Exception:
        pass
    return None


def fetch_weather_forecast(lat: float, lon: float) -> dict | None:
    """Fetch 7-day hourly forecast from Open-Meteo."""
    try:
        resp = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "hourly": "temperature_2m,precipitation,wind_speed_10m,relative_humidity_2m",
                "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum,wind_speed_10m_max",
                "timezone": "auto",
                "forecast_days": 7,
            },
            timeout=8,
        )
        return resp.json()
    except Exception:
        return None


def analyze_weather_alerts(forecast: dict) -> dict:
    """Parse forecast data and detect frost / heavy-rain events."""
    alerts = {"frost": [], "heavy_rain": [], "summary": []}
    daily = forecast.get("daily", {})
    dates = daily.get("time", [])
    temp_mins = daily.get("temperature_2m_min", [])
    temp_maxs = daily.get("temperature_2m_max", [])
    precip_sums = daily.get("precipitation_sum", [])
    wind_maxs = daily.get("wind_speed_10m_max", [])

    for i, date in enumerate(dates):
        t_min = temp_mins[i] if i < len(temp_mins) else None
        t_max = temp_maxs[i] if i < len(temp_maxs) else None
        rain = precip_sums[i] if i < len(precip_sums) else 0
        wind = wind_maxs[i] if i < len(wind_maxs) else 0

        day_label = datetime.strptime(date, "%Y-%m-%d").strftime("%A, %b %d")

        # Check for frost
        if t_min is not None and t_min <= WEATHER_THRESHOLDS["frost_warning"]:
            severity = (
                "🔴 SEVERE"
                if t_min <= WEATHER_THRESHOLDS["frost_severe"]
                else "🟡 WARNING"
            )
            alerts["frost"].append({
                "date": day_label,
                "temp_min": t_min,
                "severity": severity,
            })

        # Check for heavy rain
        if rain >= WEATHER_THRESHOLDS["heavy_rain_warning"]:
            severity = (
                "🔴 SEVERE"
                if rain >= WEATHER_THRESHOLDS["heavy_rain_severe"]
                else "🟡 WARNING"
            )
            alerts["heavy_rain"].append({
                "date": day_label,
                "precip_mm": rain,
                "wind_kmh": wind,
                "severity": severity,
            })

        alerts["summary"].append({
            "date": day_label,
            "min": t_min,
            "max": t_max,
            "rain": rain,
            "wind": wind,
        })

    return alerts


def build_weather_context(alerts: dict, location_name: str) -> str:
    """Build a context string injected into every chat message so the AI can reference live weather."""
    parts = [f"\n[LIVE WEATHER DATA for {location_name} — next 7 days]"]

    if alerts["frost"]:
        parts.append("⚠️ FROST ALERTS:")
        for f in alerts["frost"]:
            parts.append(
                f"  • {f['severity']} on {f['date']}: min temp {f['temp_min']}°C"
            )

    if alerts["heavy_rain"]:
        parts.append("⚠️ HEAVY RAIN ALERTS:")
        for r in alerts["heavy_rain"]:
            parts.append(
                f"  • {r['severity']} on {r['date']}: {r['precip_mm']} mm rain, wind {r['wind_kmh']} km/h"
            )

    if not alerts["frost"] and not alerts["heavy_rain"]:
        parts.append("✅ No frost or heavy-rain warnings in the next 7 days.")

    parts.append("\n7-Day Overview:")
    for s in alerts["summary"]:
        parts.append(
            f"  {s['date']}: {s['min']}–{s['max']}°C, rain {s['rain']} mm, wind {s['wind']} km/h"
        )

    parts.append(
        "\nUse this weather data to adjust irrigation scheduling, warn about frost-sensitive crops, and recommend pest/disease prevention tied to rain events.\n"
    )
    return "\n".join(parts)
