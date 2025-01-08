# Football Match Predictor

## Data Retrieval
- Developed a script to fetch data via API calls.
- Stored the data in the `data` folder in both CSV and JSON formats.

## Data Cleaning
- Developed a script for data cleaning.
- Cleaned data is stored in the `data` folder.

## Feature Engineering
- Created a new CSV containing the league table.

## Streamlit Web Page
- Created a simple web page to display league standings.

## Project Structure
```
.
├── README.md
├── app
│   └── main.py
├── config.json
├── data
│   ├── serie_a_league_table.csv
│   ├── serie_a_matches.csv
│   ├── serie_a_matches.json
│   └── serie_a_matches_cleaned.csv
├── model
└── scripts
    ├── 01_get_data.py
    ├── 02_data_cleaning.ipynb
    └── 03_feature_engineering.py
```