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

- `data/` - Contains student and macroeconomic CSV data (not tracked in Git)
- `src/` - Source code modules:
  - `load.py` - Loads and merges student datasets
  - `process.py` - Data processing, feature engineering, and model training
  - `worldbank.py` - Fetches World Bank API data
  - `tests.py` - Unit tests for project modules
- `main.py` - Main script to run data loading and model pipeline
- `requirements.txt` - Lists Python dependencies
- `.gitignore` - Specifies files and folders to exclude from version control
- `doc/` - Contains the final progress report (PDF)
- `README.md` - Project overview and setup instructions


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

## Testing

Tests are located in `src/tests.py`.

**Important**: You must manually place `student-mat.csv` and `student-por.csv` in the `data/` folder before running the tests, as these files are not committed to the repo per project requirements.

To run the tests:

```bash
python -m unittest src/tests.py

