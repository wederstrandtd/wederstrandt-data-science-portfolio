"""
Author: David Wederstrandt
Project: OpenWeather State Input Normalization
Course Folder: 2. Programming_Python

Purpose:
- Map US state names to 2-letter abbreviations.
- Accept full state names or abbreviations from user input.
"""

from __future__ import annotations

STATE_TO_ABBR = {
    "alabama": "AL",
    "alaska": "AK",
    "arizona": "AZ",
    "arkansas": "AR",
    "california": "CA",
    "colorado": "CO",
    "connecticut": "CT",
    "delaware": "DE",
    "florida": "FL",
    "georgia": "GA",
    "hawaii": "HI",
    "idaho": "ID",
    "illinois": "IL",
    "indiana": "IN",
    "iowa": "IA",
    "kansas": "KS",
    "kentucky": "KY",
    "louisiana": "LA",
    "maine": "ME",
    "maryland": "MD",
    "massachusetts": "MA",
    "michigan": "MI",
    "minnesota": "MN",
    "mississippi": "MS",
    "missouri": "MO",
    "montana": "MT",
    "nebraska": "NE",
    "nevada": "NV",
    "new hampshire": "NH",
    "new jersey": "NJ",
    "new mexico": "NM",
    "new york": "NY",
    "north carolina": "NC",
    "north dakota": "ND",
    "ohio": "OH",
    "oklahoma": "OK",
    "oregon": "OR",
    "pennsylvania": "PA",
    "rhode island": "RI",
    "south carolina": "SC",
    "south dakota": "SD",
    "tennessee": "TN",
    "texas": "TX",
    "utah": "UT",
    "vermont": "VT",
    "virginia": "VA",
    "washington": "WA",
    "west virginia": "WV",
    "wisconsin": "WI",
    "wyoming": "WY",
    "district of columbia": "DC",
}

ABBR_TO_STATE = {abbr: name.title() for name, abbr in STATE_TO_ABBR.items()}


def normalize_state_input(state_input: str) -> str:
    cleaned = " ".join(state_input.strip().split())
    if not cleaned:
        raise ValueError("State is required.")

    upper = cleaned.upper()
    if len(upper) == 2 and upper.isalpha() and upper in ABBR_TO_STATE:
        return upper

    key = cleaned.lower()
    if key in STATE_TO_ABBR:
        return STATE_TO_ABBR[key]

    raise ValueError(
        "State must be a valid US state name or 2-letter abbreviation (example: Colorado or CO)."
    )
