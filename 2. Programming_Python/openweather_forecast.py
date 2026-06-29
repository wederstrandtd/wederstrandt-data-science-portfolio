"""
Author: David Wederstrandt
Project: OpenWeather Forecast CLI
Course Folder: 2. Programming_Python

Purpose:
- Prompt for location and forecast days.
- Retrieve forecast data from OpenWeather.
- Support API key from .env or interactive fallback.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import urlopen

from us_state_lookup import normalize_state_input


class OpenWeatherClient:
    def __init__(self, api_key: str, units: str = "imperial") -> None:
        if not api_key:
            raise ValueError("Missing OpenWeather API key in .env file")
        self.api_key = api_key
        self.units = units

    def _get_json(self, url: str) -> dict[str, Any]:
        try:
            with urlopen(url) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            raise RuntimeError(f"API request failed: HTTP {exc.code}") from exc
        except URLError as exc:
            raise RuntimeError(f"Network error: {exc.reason}") from exc

    def get_coordinates(self, city: str, state: str, country: str = "US") -> tuple[float, float, str]:
        query = quote(f"{city},{state},{country}")
        geo_url = (
            "https://api.openweathermap.org/geo/1.0/direct"
            f"?q={query}&limit=1&appid={self.api_key}"
        )
        geo_data = self._get_json(geo_url)

        if not geo_data:
            raise RuntimeError("No location found. Check your city and state format.")

        location = geo_data[0]
        lat = location["lat"]
        lon = location["lon"]
        location_name = f"{location.get('name', city)}, {location.get('state', state)}"
        return lat, lon, location_name

    def get_forecast(self, lat: float, lon: float) -> dict[str, Any]:
        forecast_url = (
            "https://api.openweathermap.org/data/2.5/forecast"
            f"?lat={lat}&lon={lon}&units={self.units}&appid={self.api_key}"
        )
        return self._get_json(forecast_url)


def read_api_key_from_env(start_dir: Path) -> str:
    """Read API_KEY from the nearest .env in start_dir or its parents."""
    for directory in [start_dir, *start_dir.parents]:
        env_path = directory / ".env"
        if not env_path.exists():
            continue

        for line in env_path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue

            key, value = stripped.split("=", 1)
            if key.strip() == "API_KEY":
                return value.strip().strip("\"'")

    return ""


def save_api_key_to_env(env_path: Path, api_key: str) -> None:
    api_line = f"API_KEY='{api_key}'"

    if env_path.exists():
        lines = env_path.read_text(encoding="utf-8").splitlines()
        updated = False
        for index, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("API_KEY") and "=" in stripped:
                lines[index] = api_line
                updated = True
                break

        if not updated:
            lines.append(api_line)

        env_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    env_path.write_text(api_line + "\n", encoding="utf-8")


def get_api_key_with_fallback(start_dir: Path) -> str:
    api_key = read_api_key_from_env(start_dir)
    if api_key:
        print("Using API_KEY from .env file.")
        return api_key

    print("No API_KEY was found in a .env file.")
    print("Option 1: Paste your API key for this run only.")
    print("Option 2: Create or update a .env file with your API key.")

    while True:
        choice = input("Choose 1 or 2: ").strip()

        if choice == "1":
            pasted_key = input("Paste your OpenWeather API key: ").strip().strip("\"'")
            if pasted_key:
                print("Using the pasted API key for this run only.")
                return pasted_key
            print("API key cannot be empty.")
            continue

        if choice == "2":
            pasted_key = input("Enter the API key to save in .env: ").strip().strip("\"'")
            if not pasted_key:
                print("API key cannot be empty.")
                continue

            env_path = start_dir / ".env"
            save_api_key_to_env(env_path, pasted_key)
            print(f"Saved API_KEY to {env_path}")
            return pasted_key

        print("Invalid choice. Enter 1 or 2.")


def parse_city_state(user_input: str) -> tuple[str, str]:
    if "," not in user_input:
        raise ValueError("Please use format: city, state")

    city, state = [part.strip() for part in user_input.split(",", 1)]
    if not city or not state:
        raise ValueError("Both city and state are required. Example: Denver, CO")

    return city, normalize_state_input(state)


def summarize_by_day(forecast_payload: dict[str, Any], days: int) -> list[dict[str, Any]]:
    entries = forecast_payload.get("list", [])
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for item in entries:
        dt_txt = item.get("dt_txt")
        if not dt_txt:
            continue
        day_key = dt_txt.split(" ", 1)[0]
        grouped[day_key].append(item)

    day_keys = sorted(grouped.keys())[:days]
    summaries: list[dict[str, Any]] = []

    for day in day_keys:
        day_entries = grouped[day]
        temps_min = [entry["main"]["temp_min"] for entry in day_entries if "main" in entry]
        temps_max = [entry["main"]["temp_max"] for entry in day_entries if "main" in entry]
        humidities = [entry["main"]["humidity"] for entry in day_entries if "main" in entry]

        descriptions = [
            entry.get("weather", [{}])[0].get("description", "")
            for entry in day_entries
            if entry.get("weather")
        ]
        common_desc = Counter(descriptions).most_common(1)[0][0] if descriptions else "n/a"

        summaries.append(
            {
                "date": day,
                "temp_min": min(temps_min) if temps_min else None,
                "temp_max": max(temps_max) if temps_max else None,
                "humidity_avg": sum(humidities) / len(humidities) if humidities else None,
                "description": common_desc,
            }
        )

    return summaries


def prompt_for_days() -> int:
    while True:
        raw = input("How many days do you want to see? (1-5): ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("Enter a whole number between 1 and 5.")
            continue

        if 1 <= value <= 5:
            return value

        print("OpenWeather 5-day forecast supports 1 to 5 days.")


def main() -> None:
    api_key = get_api_key_with_fallback(Path.cwd())

    location_input = input(
        "Enter city and state in format 'city, state' (example: Denver, CO or Denver, Colorado): "
    ).strip()
    try:
        city, state = parse_city_state(location_input)
    except ValueError as exc:
        print(exc)
        sys.exit(1)

    days = prompt_for_days()

    client = OpenWeatherClient(api_key=api_key)

    try:
        lat, lon, location_name = client.get_coordinates(city=city, state=state)
        forecast = client.get_forecast(lat=lat, lon=lon)
    except RuntimeError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    summaries = summarize_by_day(forecast, days)
    if not summaries:
        print("No forecast data returned.")
        sys.exit(1)

    units_symbol = "F" if client.units == "imperial" else "C"
    print(f"\nForecast for {location_name} ({days} day(s))")
    print("-" * 55)

    for day in summaries:
        pretty_date = datetime.strptime(day["date"], "%Y-%m-%d").strftime("%a %b %d, %Y")
        t_min = f"{day['temp_min']:.1f}°{units_symbol}" if day["temp_min"] is not None else "n/a"
        t_max = f"{day['temp_max']:.1f}°{units_symbol}" if day["temp_max"] is not None else "n/a"
        humidity = f"{day['humidity_avg']:.0f}%" if day["humidity_avg"] is not None else "n/a"

        print(f"{pretty_date}")
        print(f"  Condition: {day['description']}")
        print(f"  Temp Min : {t_min}")
        print(f"  Temp Max : {t_max}")
        print(f"  Humidity : {humidity}")
        print()


if __name__ == "__main__":
    main()
