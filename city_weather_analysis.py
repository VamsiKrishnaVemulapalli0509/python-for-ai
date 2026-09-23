import os

import json

import requests

import pandas as pd

# ---------------------------------------------------------

# 1. PIPELINE CONFIGURATION

# ---------------------------------------------------------

CITY_NAME = "Yanam"

LATITUDE = 17.3850    # Update with your latitude

LONGITUDE = 78.4867   # Update with your longitude

DATA_DIR = "data"

os.makedirs(DATA_DIR, exist_ok=True)

# Open-Meteo Weather Forecast API Endpoint

API_URL = "https://api.open-meteo.com/v1/forecast"

params = {

    "latitude": LATITUDE,

    "longitude": LONGITUDE,

    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode",

    "timezone": "auto"

}

# ---------------------------------------------------------

# 2. API REQUEST & RAW DATA INGESTION

# ---------------------------------------------------------

print(f"[INFO] Fetching 7-day weather forecast for {CITY_NAME}...")

response = requests.get(API_URL, params=params)

if response.status_code == 200:

    raw_data = response.json()

    

    # Save raw JSON

    raw_json_path = os.path.join(DATA_DIR, "weather_7day_raw.json")

    with open(raw_json_path, "w") as f:

        json.dump(raw_data, f, indent=4)

    print(f"[SUCCESS] Raw JSON data saved to {raw_json_path}")

else:

    raise Exception(f"[ERROR] API request failed with status code: {response.status_code}")

# ---------------------------------------------------------

# 3. DATA PARSING & CLEANING (PANDAS)

# ---------------------------------------------------------

daily_data = raw_data.get("daily", {})

df = pd.DataFrame({

    "date": daily_data.get("time", []),

    "max_temp_c": daily_data.get("temperature_2m_max", []),

    "min_temp_c": daily_data.get("temperature_2m_min", []),

    "precipitation_mm": daily_data.get("precipitation_sum", []),

    "weather_code": daily_data.get("weathercode", [])

})

# Feature Engineering: Calculate daily temperature range

df["temp_range_c"] = df["max_temp_c"] - df["min_temp_c"]

# Clean CSV Export

cleaned_csv_path = os.path.join(DATA_DIR, "weather_7day_cleaned.csv")

df.to_csv(cleaned_csv_path, index=False)

print(f"[SUCCESS] Cleaned forecast saved to {cleaned_csv_path}")

# ---------------------------------------------------------

# 4. STATISTICAL SUMMARY & AGGREGATIONS

# ---------------------------------------------------------

summary_stats = pd.DataFrame({

    "metric": [

        "avg_max_temp_c",

        "avg_min_temp_c",

        "highest_temp_c",

        "lowest_temp_c",

        "total_precipitation_mm"

    ],

    "value": [

        round(df["max_temp_c"].mean(), 2),

        round(df["min_temp_c"].mean(), 2),

        df["max_temp_c"].max(),

        df["min_temp_c"].min(),

        round(df["precipitation_mm"].sum(), 2)

    ]

})

summary_csv_path = os.path.join(DATA_DIR, "weather_summary.csv")

summary_stats.to_csv(summary_csv_path, index=False)

print(f"[SUCCESS] Summary metrics saved to {summary_csv_path}")

print("\n--- 7-DAY FORECAST PREVIEW ---")

print(df.head(7))
