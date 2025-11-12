import requests
import pandas as pd

def get_world_bank_indicator(country_code, indicator_code, start_year=2010, end_year=2023):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}"
    params = {
        "format": "json",
        "date": f"{start_year}:{end_year}",
        "per_page": 500
    }

    response = requests.get(url, params=params)
    data = response.json()

    if not isinstance(data, list) or len(data) < 2:
        raise ValueError(f"No data returned from World Bank API for {indicator_code}")

    records = [
        {"year": entry["date"], "value": entry["value"]}
        for entry in data[1]
        if entry["value"] is not None
    ]

    return pd.DataFrame(records)

if __name__ == "__main__":
    portugal_code = "PRT"

    print("Fetching government expenditure on education...")
    edu_gdp = get_world_bank_indicator(portugal_code, "SE.XPD.TOTL.GD.ZS")
    edu_gdp.to_csv("data/portugal_edu_spending.csv", index=False)

    print("Fetching tertiary enrollment...")
    tertiary_enroll = get_world_bank_indicator(portugal_code, "SE.TER.ENRR")
    tertiary_enroll.to_csv("data/portugal_tertiary_enroll.csv", index=False)

    print("Done!")
