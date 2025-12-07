import wbdata
import pandas as pd

# World Bank indicator codes:
#   SE.XPD.TOTL.GD.ZS  -> Government education spending (% of GDP)
#   SE.TER.ENRR        -> Gross tertiary enrollment (%)
INDICATORS = {
    "SE.XPD.TOTL.GD.ZS": "edu_spend_pct_gdp",
    "SE.TER.ENRR": "tertiary_enrollment",
}

# 20 European countries geographically/economically close to Portugal
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
) -> pd.DataFrame:
    """
    Fetch World Bank macro-education indicators for 20 European countries.

    This version is compatible with older versions of wbdata that do NOT
    accept keyword args like `data_date` or `convert_date`.
    """
    if countries is None:
        countries = EUROPE_20
    if indicators is None:
        indicators = INDICATORS

    # Must avoid keyword args due to version inconsistencies
    df = wbdata.get_dataframe(indicators, country=countries)

    # Reset index so "country" becomes a column
    df = df.reset_index()

    # Standardize column names
    if "country" in df.columns:
        df = df.rename(columns={"country": "country_code"})

    # Drop date column if present
    if "date" in df.columns:
        df = df.drop(columns=["date"])

    return df


def merge_macro_features(
    student_df: pd.DataFrame,
    macro_df: pd.DataFrame,
    strategy: str = "mean",
) -> pd.DataFrame:
    """
    Merge macro-level education indicators into the student dataframe.

    Since the UCI dataset contains only Portuguese students, we attach the
    *regional averages* for the 20 European macro-education indicators.
    """
    df = student_df.copy()

    if strategy == "mean":
        macro_means = macro_df[INDICATORS.values()].mean()
        for col, value in macro_means.items():
            df[col] = value
    else:
        raise ValueError(f"Unsupported merge strategy: {strategy}")

    return df

