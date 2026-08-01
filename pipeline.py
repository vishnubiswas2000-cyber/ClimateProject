import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine, text

# 1. Define database connection credentials
USER = "root"
PASSWORD = "12345"
HOST = "localhost"
PORT = "3306"
DATABASE = "climate_db"

# 2. Create the SQLAlchemy connection engine
engine_url = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(engine_url)

# 3. Define your optimized SQL query (Aggregated for all cities)
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
    print("Connecting to database and executing queries...")
    with engine.connect() as connection:
        # Clear out standard select limits safely
        connection.execute(text("SET SQL_SELECT_LIMIT = DEFAULT;"))
        
        # Run a quick diagnostic check to see what data ACTUALLY exists in your table
        diagnostic = connection.execute(text(
            "SELECT COUNT(*), MIN(RecordDate), MAX(RecordDate) FROM GlobalLandTemperaturesByCity;"
        )).fetchone()
        
        print("\n--- DATABASE DIAGNOSTIC INFO ---")
        print(f"Total rows in table: {diagnostic[0]}")
        print(f"Earliest Date available: {diagnostic[1]}")
        print(f"Latest Date available: {diagnostic[2]}")
        print("--------------------------------\n")
        
        # Pull data directly into the DataFrame
        df = pd.read_sql(text(query), con=connection)
    
    # 5. Verify the data load
    print("--- Data Pipeline Success ---")
    print(f"Total Rows Retrieved for Graph: {len(df)}")
    
    if len(df) == 0:
        print("⚠️ No rows returned. Your date filter might not match the table's format.")
    else:
        print(f"Timeline Bounds in DataFrame: {df['RecordDate'].min()} to {df['RecordDate'].max()}")
        
        # Ensure data types are optimized for time-series analysis
        df['RecordDate'] = pd.to_datetime(df['RecordDate'])
        df = df.sort_values('RecordDate')

        # Define Your Anomaly Logic
        mean_temp = df['AverageTemperature'].mean()
        std_temp = df['AverageTemperature'].std()
        threshold = mean_temp + (2 * std_temp)
        df['Is_Anomaly'] = df['AverageTemperature'] > threshold

        # Initialize the Plot Layout
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(14, 6), dpi=100)

        # Plot the temperature trend line
        sns.lineplot(
            data=df, 
            x='RecordDate', 
            y='AverageTemperature', 
            color='#1f77b4', 
            linewidth=1.5, 
            label='Average Temperature (°C)'
        )

        # Shading the Anomaly Dates
        in_anomaly = False
        start_date = None

        for idx, row in df.iterrows():
            if row['Is_Anomaly'] and not in_anomaly:
                start_date = row['RecordDate']
                in_anomaly = True
            elif not row['Is_Anomaly'] and in_anomaly:
                plt.axvspan(start_date, row['RecordDate'], color='red', alpha=0.3, label='Detected Anomaly')
                in_anomaly = False

        if in_anomaly:
            plt.axvspan(start_date, df['RecordDate'].iloc[-1], color='red', alpha=0.3)

        # Clean and Label the Visualization
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        if by_label:
            plt.legend(by_label.values(), by_label.keys(), loc='upper left', frameon=True)

        plt.title('Global Climate Trend Line with Highlighted Anomalies', fontsize=14, pad=15)
        plt.xlabel('Timeline (Record Date)', fontsize=11)
        plt.ylabel('Temperature (°C)', fontsize=11)
        plt.tight_layout()

        print("Generating plot window...")
        plt.show()

except Exception as e:
    print(f"Pipeline Error: {e}")

finally:
    engine.dispose()
