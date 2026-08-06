
---------------------------------------------------------
-- DATA QUALITY CHECKS (Pre-Pipeline Validation)
---------------------------------------------------------

-- Row Count
SELECT COUNT(*) AS total_rows
FROM taxi_trip_data;

---------------------------------------------------------

-- Duplicate Count
SELECT COUNT(*) -
COUNT(DISTINCT
VendorID,
pickup_datetime,
dropoff_datetime,
passenger_count,
trip_distance,
RatecodeID,
store_and_fwd_flag,
PULocationID,
DOLocationID,
payment_type,
fare_amount,
extra,
mta_tax,
tip_amount,
tolls_amount,
improvement_surcharge,
total_amount
) AS duplicate_rows
FROM taxi_trip_data;

---------------------------------------------------------

-- Null Count
SELECT
SUM(CASE WHEN VendorID IS NULL THEN 1 ELSE 0 END) AS VendorID_nulls,
SUM(CASE WHEN pickup_datetime IS NULL THEN 1 ELSE 0 END) AS pickup_nulls,
SUM(CASE WHEN dropoff_datetime IS NULL THEN 1 ELSE 0 END) AS dropoff_nulls,
SUM(CASE WHEN passenger_count IS NULL THEN 1 ELSE 0 END) AS passenger_nulls,
SUM(CASE WHEN trip_distance IS NULL THEN 1 ELSE 0 END) AS distance_nulls,
SUM(CASE WHEN fare_amount IS NULL THEN 1 ELSE 0 END) AS fare_nulls,
SUM(CASE WHEN total_amount IS NULL THEN 1 ELSE 0 END) AS total_nulls
FROM taxi_trip_data;
