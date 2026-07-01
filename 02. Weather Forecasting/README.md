# Weather Forecasting

![Track](https://img.shields.io/badge/Track-Programming%20Python-1F6FEB)
![App](https://img.shields.io/badge/App-CLI%20Weather-2A9D8F)
![API](https://img.shields.io/badge/API-OpenWeather-F4A261)

## Overview
This folder contains Python scripting projects, including a command-line weather app that uses the OpenWeather API.

## Files
- `openweather_forecast.py`: Main CLI program to fetch and display weather forecast details.
- `us_state_lookup.py`: Helper module that converts full US state names to 2-letter abbreviations.
- `.env` (optional, local-only): Stores API credentials using `API_KEY='your_key_here'`.

## OpenWeather Forecast Program
The forecast script:
- Prompts for location in `city, state` format.
- Accepts either state abbreviation (`CO`) or full state name (`Colorado`).
- Prompts for how many days to display (1-5).
- Calls OpenWeather Geocoding + 5-day Forecast APIs.
- Summarizes daily conditions, min/max temperature, and average humidity.

## Outcome Highlights
- Supports 51 normalized US location inputs (50 states + District of Columbia).
- Produces up to 5 daily forecast summaries per run from 3-hour interval API data.
- Includes resilient key handling with two fallback paths: one-run paste or saved `.env` update.

## API Key Options
The program supports two API key paths:
1. Existing `.env` file with `API_KEY`.
2. Interactive fallback if key is missing:
   - Paste key for current run only, or
   - Save key into a new or updated `.env` file.

## Run Instructions
From the repository root:

```bash
python3 "2. Weather Forecasting/openweather_forecast.py"
```

Or from this folder:

```bash
python3 openweather_forecast.py
```

## Input Examples
- `Denver, CO`
- `Denver, Colorado`

## Security Note
- Keep `.env` local and untracked.
- If an API key is ever exposed in version control, rotate it immediately and replace local credentials.
