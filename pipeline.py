import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from sqlalchemy import create_engine, text

# 1. Database Connection Setup
USER = "root"
PASSWORD = "12345"
HOST = "localhost"
PORT = "3306"
DATABASE = "climate_db"

engine_url = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(engine_url)

# 2. SQL Query (Aggregating all cities across 30 years)
query = """
SELECT 
    RecordDate, 
    AVG(AverageTemperature) AS AverageTemperature
FROM GlobalLandTemperaturesByCity
WHERE RecordDate BETWEEN '1983-01-01' AND '2013-12-31'
GROUP BY RecordDate
ORDER BY RecordDate;
"""

try:
    print("Extracting multi-decade climate records from database...")
    with engine.connect() as connection:
        df = pd.read_sql(text(query), con=connection)
    
    print(f"Data Payload Verified: {len(df)} records compiled.")
    
    # 3. Data Formatting for Time-Series Analysis
    df['RecordDate'] = pd.to_datetime(df['RecordDate'])
    df = df.sort_values('RecordDate')

    # Statistical Thresholding (Anomalies defined as > 1.5 standard deviations above baseline)
    baseline_mean = df['AverageTemperature'].mean()
    baseline_std = df['AverageTemperature'].std()
    anomaly_threshold = baseline_mean + (1.5 * baseline_std)
    df['Is_Anomaly'] = df['AverageTemperature'] > anomaly_threshold

    # 4. Professional Chart Layout Design
    # Using a clean white grid canvas with custom font sizing parameters
    sns.set_theme(style="white", rc={"grid.color": "#eaeaea", "axes.grid": True})
    fig, ax = plt.subplots(figsize=(15, 7), dpi=120)

    # Plot the 30-Year Trend Line with a deep professional navy blue accent
    sns.lineplot(
        data=df, 
        x='RecordDate', 
        y='AverageTemperature', 
        color='#0f2042', 
        linewidth=2, 
        alpha=0.85,
        label='Global Monthly Average Temp (°C)',
        ax=ax
    )

    # Injecting a secondary rolling trend line to visually smooth out raw seasonal variations
    df['12M_Rolling_Avg'] = df['AverageTemperature'].rolling(window=12, center=True).mean()
    sns.lineplot(
        data=df,
        x='RecordDate',
        y='12M_Rolling_Avg',
        color='#e67e22',
        linewidth=2.5,
        linestyle='--',
        label='12-Month Deseasonalized Macro Trend',
        ax=ax
    )

    # 5. Programmatic Coral Red Anomaly Highlight Shading
    in_anomaly = False
    start_date = None

    for idx, row in df.iterrows():
        if row['Is_Anomaly'] and not in_anomaly:
            start_date = row['RecordDate']
            in_anomaly = True
        elif not row['Is_Anomaly'] and in_anomaly:
            ax.axvspan(start_date, row['RecordDate'], color='#ff4d4d', alpha=0.18, label='Thermal Anomaly Event')
            in_anomaly = False

    if in_anomaly:
        ax.axvspan(start_date, df['RecordDate'].iloc[-1], color='#ff4d4d', alpha=0.18, label='Thermal Anomaly Event')

    # 6. Advanced Typography, Clean Labels, and Grid Polish
    ax.set_title('GLOBAL CLIMATE TREND REGRESSION ANALYSIS (1983 - 2013)', fontsize=16, fontweight='bold', color='#1a1a1a', pad=20, loc='left')
    ax.set_xlabel('Timeline Horizon (By Calendar Year)', fontsize=12, fontweight='semibold', labelpad=12, color='#333333')
    ax.set_ylabel('Aggregated Temperature Profile (°C)', fontsize=12, fontweight='semibold', labelpad=12, color='#333333')

    # Formatting Time-Axis ticks cleanly into 3-year leaps
    ax.xaxis.set_major_locator(mdates.YearLocator(3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.xticks(rotation=0, fontsize=10, color='#555555')
    plt.yticks(fontsize=10, color='#555555')

    # De-clutter and clean legend layers
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#e0e0e0', fontsize=10)

    # Remove outer graph box spines for a modern, minimalistic report feel
    sns.despine(left=True, bottom=True)
    plt.tight_layout()

    # Render Output Canvas
    print("Generating report visualization canvas...")
    plt.show()

except Exception as e:
    print(f"Pipeline Interrupted: {e}")
finally:
    engine.dispose()
