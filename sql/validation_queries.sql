
-- Total number of records
SELECT COUNT(*) AS total_records
FROM taxi_trip_data;

-- Average fare
SELECT AVG(fare_amount) AS average_fare
FROM taxi_trip_data;

-- Maximum trip distance
SELECT MAX(trip_distance) AS max_trip_distance
FROM taxi_trip_data;

-- Minimum total amount
SELECT MIN(total_amount) AS minimum_total_amount
FROM taxi_trip_data;

-- Invalid passenger counts
SELECT COUNT(*) AS invalid_passenger_count
FROM taxi_trip_data
WHERE passenger_count <= 0;

-- Invalid fare amounts
SELECT COUNT(*) AS invalid_fare_count
FROM taxi_trip_data
WHERE fare_amount <= 0;

-- Invalid trip distances
SELECT COUNT(*) AS invalid_trip_distance_count
FROM taxi_trip_data
WHERE trip_distance <= 0;

-- Average trip duration
SELECT AVG(trip_duration_minutes) AS average_trip_duration
FROM taxi_trip_data;
