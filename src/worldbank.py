"""
worldbank.py

Helper for fetching macro-level indicators from the World Bank API and
returning a tidy dataframe suitable for merging with student data.
"""

from __future__ import annotations

from typing import Iterable, Mapping, Optional

import pandas as pd
import wbdata

from .config import WORLD_BANK_INDICATORS, WORLD_BANK_EUROPE_20


def fetch_worldbank_data(
    countries: Optional[Iterable[str]] = None,
    indicators: Optional[Mapping[str, str]] = None,
    start_year: int = 2010,
    end_year: int = 2019,
) -> pd.DataFrame:
    """
    Fetch World Bank indicators for a set of countries and years.

    Parameters
    ----------
    countries : iterable of country ISO3 codes or None
        If None, uses WORLD_BANK_EUROPE_20 from config.py.
    indicators : mapping of indicator_code -> column_name or None
        If None, uses WORLD_BANK_INDICATORS from config.py.
    start_year : int
        Start year for the time window.
    end_year : int
        End year for the time window.

    Returns
    -------
    pd.DataFrame
        One row per country with mean indicator values over the period.
        Columns are the indicator "friendly" names from `indicators`.
    """
    if countries is None:
        countries = WORLD_BANK_EUROPE_20
    if indicators is None:
        indicators = WORLD_BANK_INDICATORS

    # World Bank expects a list, not any iterator
    countries = list(countries)

    # Query over a time range; returns a multi-index (date, country)
    data = wbdata.get_dataframe(
        indicators,
        country=countries,
        convert_date=True,
        data_date=(pd.Timestamp(start_year, 1, 1), pd.Timestamp(end_year, 12, 31)),
    )

    if data.empty:
        # Fail soft: return empty dataframe with expected columns
        cols = list(indicators.values())
        return pd.DataFrame(columns=cols)

    # Collapse to one row per country using mean over the period
    data = (
        data.reset_index()
        .rename(columns={"country": "country_code"})
        .groupby("country_code", as_index=False)[list(indicators.values())]
        .mean()
    )

    return data
