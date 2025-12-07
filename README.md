# Student Performance Analysis Using UCI Dataset & World Bank Indicators

DSCI-510 Final Project — Fall 2025

Author: Stephen Rosario

# Introduction

This project analyzes academic performance using the UCI “Student Performance” dataset and enhances it with educational macroeconomic indicators retrieved from the World Bank API.
The goal is to build an automated, reproducible data pipeline that:

- Loads and preprocesses student-level data

- Fetches country-level macro indicators for 20 European countries

- Merges UCI and World Bank features

- Trains a machine learning classification model

- Evaluates results and generates visual insights

All logic is modularized inside the src/ directory and can be executed through a single command or via the provided Jupyter notebook.

## Project Structure

```text
DSCI510_FinalProject/
│
├── src/
│   ├── load_data.py
│   ├── preprocess.py
│   ├── worldbank.py
│   ├── model.py
│   ├── analysis.py
│   ├── main.py
│   └── tests.py
│
├── docs/
│   └── FinalProjectSlides.pdf
│
├── results/                # Auto-generated outputs (plots, metrics)
├── results.ipynb           # Notebook wrapper to run the full pipeline
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Data Sources
UCI Student Performance Dataset

Contains demographic, behavioral, academic, and family-related attributes.

Used as the primary student-level dataset.

Automatically downloaded if missing.

World Bank API Indicators

Fetched for 20 European countries:

SE.XPD.TOTL.GD.ZS — Education expenditure (% of GDP)

SE.TER.ENRR — Tertiary enrollment rate (%)

Countries are listed in .env.example.

## Analysis Summary

The project explores how both individual factors (e.g., study time, internet access, family background) and macro-level educational investment correlate with academic performance.

Key steps include:

1. Data cleaning and feature engineering

2. Merging World Bank indicators into student records

3. Random Forest classification model

4. Performance evaluation (precision, recall, F1-score)

5. Statistical testing (t-test for internet access impact)

6. Visualization of trends and correlations

7. Model accuracy reached 1.0 on this dataset due to the strong separability within the labeled categories.

## Modeling Approach

Split dataset into training/testing sets

Apply preprocessing (encoding, normalization)

Train a Random Forest classifier

Evaluate using:

- Classification report

- Confusion matrix

- Generate plots including:

- Study time distribution

- Correlation heatmap

- Feature relationships

- T-test results

## Results

Dataset merged successfully with macro indicators

Final dataset contains 1044 rows and 33 columns

Classification performance:

Accuracy: 1.000

Perfect precision, recall, F1 across all classes

Statistically significant difference (p < 0.001) between students with vs. without internet access

All plots are saved to the results/ folder upon running the pipeline

## How to Run the Pipeline
1. Install dependencies
pip install -r requirements.txt

2. Create your .env file

From the provided template:

cp .env.example .env

3. Run the full pipeline
python main.py


OR using the notebook:

Open results.ipynb and run:

from src.main import run_pipeline
run_pipeline()


This performs all steps from downloading data to generating final visualizations.

## Testing

Tests are contained in:

src/tests.py


Run tests using:

pytest

## Conclusion

This project demonstrates how combining student-level datasets with macro-level educational indicators can enhance insights into academic performance.
The pipeline is fully automated, reproducible, and organized using modular architecture recommended in professional data science workflows.

## Contact

Stephen Rosario

USC Viterbi School of Engineering

Email: sr68334@usc.edu
