import wbdata
import pandas as pd

def fetch_indicator(indicator_code, country="PT", start=2010, end=2020):
    # Get the full dataset (note: no convert_date)
    data = wbdata.get_dataframe({indicator_code: "value"}, country=country)

    # Reset index to access date
    data = data.reset_index()

    # Convert 'date' column to datetime manually
    data['date'] = pd.to_datetime(data['date'], format='%Y')

    # Extract year and filter
    data['year'] = data['date'].dt.year
    data = data[(data['year'] >= start) & (data['year'] <= end)]

    # Drop unnecessary columns
    if 'country' in data.columns:
        data = data.drop(columns='country')

    return data[['year', 'value']].sort_values('year').reset_index(drop=True)

