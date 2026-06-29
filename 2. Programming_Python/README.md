# Programming Python

## Overview
This folder contains Python coursework artifacts and a command-line weather project that uses the OpenWeather API.

## Files
- `openweather_forecast.py`: Main CLI program to fetch and display weather forecast details.
- `us_state_lookup.py`: Helper module that converts full US state names to 2-letter abbreviations.
- `.env` (optional): Stores API credentials using `API_KEY='your_key_here'`.

## OpenWeather Forecast Program
The forecast script:
- Prompts for location in `city, state` format.
- Accepts either state abbreviation (`CO`) or full state name (`Colorado`).
- Prompts for how many days to display (1-5).
- Calls OpenWeather Geocoding + 5-day Forecast APIs.
- Summarizes daily conditions, min/max temperature, and average humidity.

## API Key Options
The program supports two API key paths:
1. Existing `.env` file with `API_KEY`.
2. Interactive fallback if key is missing:
   - Paste key for current run only, or
   - Save key into a new or updated `.env` file.

## Run Instructions
From the repository root:

```bash
python3 "2. Programming_Python/openweather_forecast.py"
```

Or from this folder:

```bash
python3 openweather_forecast.py
```

## Input Examples
- `Denver, CO`
- `Denver, Colorado`
