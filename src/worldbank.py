import requests
import pandas as pd

def fetch_indicator(indicator_code: str, country_code: str = "PRT", start_year: int = 2010, end_year: int = 2023) -> pd.DataFrame:
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}"
    params = {
        "format": "json",
        "date": f"{start_year}:{end_year}",
        "per_page": 100
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")

    data = response.json()[1] 
    records = [
        {"year": int(entry["date"]), "value": entry["value"]}
        for entry in data if entry["value"] is not None
    ]

    df = pd.DataFrame(records).sort_values("year").reset_index(drop=True)
    return df

