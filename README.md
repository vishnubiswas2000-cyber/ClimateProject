# Climate Anomaly Detection

Advanced time-series analysis pipeline for detecting climate anomalies.

## Overview

This project implements a reproducible pipeline for detecting anomalies in climate time-series data. It combines data ingestion, preprocessing, feature engineering, statistical modeling, and visualization to identify unusual events or structural changes in climate signals.

Key goals:
- Provide a clear, modular pipeline that can be adapted to different climate variables and datasets.
- Produce interpretable anomaly scores and visualizations for exploration and reporting.
- Make it easy to reproduce experiments and extend the pipeline with new models.

## Repository Contents

- `pipeline.py` — Main pipeline orchestrator: loads data, runs preprocessing, extracts features, fits models, and outputs results.
- `DataBase.sql` — SQL file describing the database or example schema used to store raw/processed data.

## Features

- Data ingestion and validation
- Time-series preprocessing (resampling, interpolation, detrending)
- Feature extraction (statistical and time-series-specific features)
- Multiple anomaly detection strategies (statistical tests, residual analysis, model-based scores)
- Visualization and reporting of detected anomalies

## Installation

1. Create and activate a Python 3.9+ virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\\Scripts\\activate     # Windows (PowerShell)
```

2. Install dependencies (example):

```bash
pip install pandas numpy scipy matplotlib seaborn scikit-learn statsmodels sqlalchemy
```

Adjust the package list to match `pipeline.py`'s imports if additional libraries are required.

## Usage

Run the pipeline from the project root:

```bash
python pipeline.py
```

Behavior and configurable options (input paths, model choices, thresholds) are defined inside `pipeline.py`. Edit configuration variables at the top of that file or modify the pipeline to accept CLI arguments.

## Pipeline Overview

Typical steps performed by `pipeline.py`:

1. Load raw data and/or connect to the database described in `DataBase.sql`.
2. Clean and resample time-series (handle missing values, align timestamps).
3. Apply detrending and seasonal decomposition where appropriate.
4. Extract features (rolling statistics, spectral features, autocorrelation, etc.).
5. Fit models or compute statistical tests to produce anomaly scores.
6. Flag anomalies using configurable thresholds and output summaries and plots.

Outputs: CSV files of anomaly scores, figures showing anomalies over time, and optional database writes for record keeping.

## Example Configuration

- Input data path: modify the path variable in `pipeline.py` to point to your CSV or database source.
- Output directory: configure the pipeline's output folder for results and figures.
- Model choice: enable or disable specific detectors in `pipeline.py`.

## Results and Interpretation

The pipeline provides anomaly scores rather than binary labels by default. This lets you:

- Rank events by severity
- Tune thresholds for precision/recall tradeoffs
- Combine multiple detectors (ensemble) and use consensus rules

Interpretation tips:
- Inspect flagged windows with domain context (e.g., sensor maintenance, known climate events).
- Visualize raw series with flagged timestamps to check for false positives caused by preprocessing artefacts.

## Extending the Project

- Add new feature extractors or model wrappers in separate modules and import them into `pipeline.py`.
- Replace static configuration with a YAML/JSON config file or CLI flags for reproducible experiments.
- Add unit tests for preprocessing and scoring modules.

## Contributing

Contributions are welcome. Please open issues for bug reports or feature requests, and submit pull requests for fixes or enhancements.

## License

Specify your license here (e.g., MIT, Apache-2.0) or remove this section if not applicable.

## Contact

For questions or collaboration, open an issue or contact the repository maintainer.
