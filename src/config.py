"""
config.py

Central place for all constant configuration values:
- project paths
- data file paths
- World Bank configuration
- plot output filenames
"""

from pathlib import Path

# -------------------------------------------------------------------
# Base directories
# -------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Local data directory (NOT tracked in git – should be in .gitignore)
DATA_DIR = PROJECT_ROOT / "data"

# Results / plots directory
RESULTS_DIR = PROJECT_ROOT / "results"

# -------------------------------------------------------------------
# Raw data file paths (inside DATA_DIR)
# -------------------------------------------------------------------
MAT_FILE = DATA_DIR / "student-mat.csv"
POR_FILE = DATA_DIR / "student-por.csv"

# -------------------------------------------------------------------
# World Bank configuration
# -------------------------------------------------------------------
# Indicators: mapping WB code -> column name used in our dataframe
WORLD_BANK_INDICATORS = {
    "SE.XPD.TOTL.GD.ZS": "edu_spend_pct_gdp",     # Gov. education spend (% GDP)
    "SE.TER.ENRR": "tertiary_enrollment",         # Gross tertiary enrollment (%)
}

# 20 European countries around Portugal / EU context
WORLD_BANK_EUROPE_20 = [
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

# -------------------------------------------------------------------
# Plot filenames (saved inside RESULTS_DIR)
# -------------------------------------------------------------------
CORRELATION_HEATMAP_FILE = "correlation_heatmap.png"
GRADE_DISTRIBUTION_FILE = "grade_distribution.png"
STUDYTIME_BOXPLOT_FILE = "studytime_boxplot.png"

