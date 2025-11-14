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
├── data/                  # Raw and processed datasets (not tracked in Git)
│   ├── student-mat.csv
│   ├── student-por.csv
│   ├── government_spending.csv
│   └── enrollment_rate.csv
│
├── src/                   # Source code
│   ├── __init__.py
│   ├── load.py
│   ├── process.py
│   ├── worldbank.py
│   └── tests.py
│
├── main.py                # Script for loading data and running the model
├── requirements.txt       # Python dependencies
├── .gitignore             # Files and folders to exclude from Git
├── README.md              # Project documentation
└── doc/                   # Final progress report (PDF)


## Setup Instructions ##

1. Clone the repo:
   ```bash
   git clone https://github.com/stephen-rosario/DSCI510_FinalProject.git
   cd DSCI510_FinalProject

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the project
   ```bash
   python main.py
