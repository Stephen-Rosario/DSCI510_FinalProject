import wbdata
import pandas as pd
from datetime import datetime

# World Bank indicator codes:
#   SE.XPD.TOTL.GD.ZS  -> Government education spending (% of GDP)
#   SE.TER.ENRR        -> Gross tertiary enrollment (%)
INDICATORS = {
    "SE.XPD.TOTL.GD.ZS": "edu_spend_pct_gdp",
    "SE.TER.ENRR": "tertiary_enrollment",
}

# 20 European countries geographically & economically closest to Portugal
# (Iberian, Western, Central and Northern Europe)
EUROPE_20 = [
    "PRT",  # Portugal
    "ESP",  # Spain
    "FRA",  # France
    "DEU",  # Germany
    "ITA",  # Italy
    "GBR",  # United Kingdom
    "IRL",  # Ireland
    "BEL",  # Belgium
    "NLD",  # Netherlands
    "LUX",  # Luxembourg
    "CHE",  # Switzerland
    "AUT",  # Austria
    "DNK",  # Denmark
    "SWE",  # Sweden
    "NOR",  # Norway
    "FIN",  # Finland
    "CZE",  # Czech Republic
    "POL",  # Poland
    "HUN",  # Hungary
    "GRC",  # Greece
]


def fetch_worldbank_data(
    countries: list[str] | None = None,
    indicators: dict[str, str] | None = None,
    year: int | None = None,
) -> pd.DataFrame:
    """
    Fetch World Bank macro-education indicators for a set of European countries.

    Parameters
    ----------
    countries : list of str, optional
        ISO3 country codes. Defaults to EUROPE_20.
    indicators : dict, optional
        Mapping of World Bank indicator code -> friendly column name.
        Defaults to INDICATORS.
    year : int, optional
        Year to query. Defaults to last full year.

    Returns
    -------
    pandas.DataFrame
        One row per (country, year) with columns:
        ['country', 'year', 'edu_spend_pct_gdp', 'tertiary_enrollment']
    """
    if countries is None:
        countries = EUROPE_20
    if indicators is None:
        indicators = INDICATORS

    if year is None:
        year = datetime.now().year - 1  # last complete year

    # wbdata expects (start_year, end_year)
    df = wbdata.get_dataframe(
        indicators,
        country=countries,
        data_date=(year, year),
        convert_date=True,
    )

    # Index is multi-index (country, date) -> reset
    df = df.reset_index().rename(columns={"country": "country_code", "date": "year"})
    # Keep just year (not full datetime)
    df["year"] = df["year"].dt.year

    return df


def merge_macro_features(
    student_df: pd.DataFrame,
    macro_df: pd.DataFrame,
    strategy: str = "mean",
) -> pd.DataFrame:
    """
    Merge macro-level education indicators into the student dataframe.

    Because the UCI student dataset only covers Portuguese schools (no per-student
    country code), we attach *regional averages* from the 20-country set.

    Parameters
    ----------
    student_df : DataFrame
        Student-level data.
    macro_df : DataFrame
        Output from fetch_worldbank_data().
    strategy : {'mean'}
        How to aggregate country-level indicators into a single context value.

    Returns
    -------
    DataFrame
        student_df with extra columns for each macro indicator.
    """
    df = student_df.copy()

    if strategy == "mean":
        # Compute regional averages across the 20 European countries
        macro_means = macro_df[INDICATORS.values()].mean()
        for col, value in macro_means.items():
            df[col] = value
    else:
        raise ValueError(f"Unsupported merge strategy: {strategy}")

    return df
