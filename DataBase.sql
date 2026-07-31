-- LOAD DATA LOCAL INFILE 'C:/Job/job google/Learning/Project/Climate Anomaly Detection (Advanced Time-Series Analysis)/Try2/Dataset/GlobalLandTemperaturesByCity.csv'
-- INTO TABLE GlobalLandTemperaturesByCity
-- FIELDS TERMINATED BY ','
-- OPTIONALLY ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 LINES
-- (@vRecordDate, @vAvgTemp, @vAvgTempUncert, City, Country, Latitude, Longitude)
-- SET 
--   RecordDate = STR_TO_DATE(@vRecordDate, '%Y-%m-%d'),
--   AverageTemperature = NULLIF(@vAvgTemp, ''),
--   AverageTemperatureUncertainty = NULLIF(@vAvgTempUncert, '');


-- EXPLAIN ANALYZE 
-- SELECT * FROM GlobalLandTemperaturesByCity 
-- WHERE   RecordDate BETWEEN '1983-01-01' AND '2013-12-31';

-- CREATE INDEX idx_city_date ON GlobalLandTemperaturesByCity (City, RecordDate);

SELECT * FROM GlobalLandTemperaturesByCity 
  -- WHERE  RecordDate BETWEEN '1983-01-01' AND '2013-12-31';
