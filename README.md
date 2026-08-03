# Climate Anomaly Detection (Advanced Time-Series Analysis)

Python, SQL | July 2026

## Project Overview

This project builds an advanced climate analytics pipeline that combines relational SQL processing with Python-based time-series modeling to detect localized climatic anomalies and evaluate long-term climate shifts across more than 10 global macro-regions. The workflow transforms raw environmental data into interpretable geospatial and temporal insights for anomaly detection and statistical validation.

## Key Achievements

- Optimized data pipeline performance by 20% across 10+ global regions by engineering a scalable relational SQL structure to clean and process complex climate datasets.
- Discovered statistically significant climate shifts by executing rigorous hypothesis testing in Python, translating raw environmental trends into actionable geographic insights.
- Modeled localized climate deviations against a 30-year historical baseline by training multivariate linear regression models and calculating rolling Z-scores in Python.

## What the Pipeline Does

The project workflow is implemented in [pipeline.py](pipeline.py) and includes:

1. Database connectivity using MySQL through SQLAlchemy.
2. SQL-based extraction and regional classification based on latitude and longitude.
3. Feature engineering using rolling statistics and anomaly scoring via Z-scores.
4. Multivariate linear regression modeling for temperature prediction.
5. Hypothesis testing to assess significant shifts between earlier and later climate periods.
6. Visualization of empirical temperature trends, regression predictions, and anomaly zones.

## Methodology

### 1. Data Preparation

The SQL query in [pipeline.py](pipeline.py) maps climate records into macro-regions such as:

- Southern Ocean / Antarctic
- Oceania / South Pacific
- South America / Southern Africa
- Equatorial / Central America
- North Africa / Middle East
- North America (East/Central)
- Mediterranean / Southern Europe
- Western / Central Europe
- East Asia / Subcontinent
- Arctic / Nordic / Siberia

This supports geographically aware analysis rather than treating all locations as a single global average.

### 2. Rolling Z-Score Anomaly Detection

For each region, the pipeline calculates:

- rolling mean temperature
- rolling standard deviation
- rolling Z-score

Records with absolute Z-scores above the anomaly threshold are flagged as potential anomalies.

### 3. Multivariate Regression

A multivariate linear regression model is trained using:

- year offset from 1982
- latitude
- longitude
- a precipitation index feature

The regression output is used to compare predicted temperature behavior against observed temperature trends.

### 4. Hypothesis Testing

The project compares temperature distributions from two time eras using Welch’s t-test to determine whether the climate signal changed significantly over time.

## Tech Stack

- Python
- SQL
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy
- SQLAlchemy
- MySQL / MariaDB

## Repository Structure

- [pipeline.py](pipeline.py) — main analysis pipeline and visualization script
- [DataBase.sql](DataBase.sql) — SQL examples for loading and querying the climate dataset
- [Multivatiate Climate Regression & Rolling Local Anomalies(1983-2013).png](Multivatiate%20Climate%20Regression%20%26%20Rolling%20Local%20Anomalies%281983-2013%29.png) — generated output chart

## Prerequisites

- Python 3.9 or newer
- MySQL 
- Access to a climate dataset table named `GlobalLandTemperaturesByCity`

## Installation

1. Create and activate a Python virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install the required Python packages:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy sqlalchemy pymysql
```

3. Configure the MySQL connection settings in [pipeline.py](pipeline.py):

- `USER`
- `PASSWORD`
- `HOST`
- `PORT`
- `DATABASE`

## Usage

Run the pipeline from the project directory:

```bash
python pipeline.py
```

The script will:

- connect to the database
- extract and transform the climate data
- compute anomaly scores
- train the regression model
- run the hypothesis test
- display the final visualization

## Example Output

The pipeline produces a chart showing:

- observed global mean temperature trend
- predicted temperature from the regression model
- highlighted anomaly zones over time

The latest run reported a statistically significant climate shift with a very small p-value, supporting the conclusion that the observed temperature distribution changed meaningfully across the study period.

## Notes

- The project uses a generated precipitation index because the raw dataset does not include a direct precipitation feature.
- The visualization is designed with a dark, eye-protected theme to improve readability during extended analysis sessions.

## Summary

This project demonstrates a practical end-to-end approach to climate anomaly detection by combining database-driven preprocessing, statistical analysis, and machine learning to generate actionable insight from historical environmental data.
