# Student Performance Predictor

This project was developed for USC’s DSCI-510 Final Project. It explores how student-level and macroeconomic factors influence academic outcomes. Using classification models, we aim to identify students at risk of poor performance and uncover what features contribute most to success.

## Project Overview

We combine:
- **Student-level data**: From the UCI Student Performance Dataset (Portuguese and Math tracks).
- **Macro-level data**: World Bank API data for:
  - Government expenditure on education (% of GDP)
  - Tertiary school enrollment (% gross)

The final goal is to categorize student final performance (`G3`) into three labels — *poor*, *average*, and *excellent* — and evaluate the effectiveness of a Random Forest classifier.

## Project Structure

DSCI510_FinalProject/
│
├── data/ # Raw data files (excluded via .gitignore)
├── results/ # Generated outputs (excluded via .gitignore)
├── doc/
│ └── progress_report.pdf
├── src/
│ ├── load.py # Functions to load and merge student datasets
│ ├── process.py # Data preprocessing, feature engineering, ML training & evaluation
│ ├── worldbank.py # Functions to fetch macro indicators from World Bank API
│
├── main.py # Main entry point for data loading, API call, and basic display
├── tests.py # Unit tests for key functions
├── requirements.txt
├── README.md
└── .gitignore

## Setup Instructions ##

1. Clone the repo:
   ```bash
   git clone https://github.com/stephen-rosario/DSCI510_FinalProject.git
   cd DSCI510_FinalProject

2. Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the project
   python main.py


