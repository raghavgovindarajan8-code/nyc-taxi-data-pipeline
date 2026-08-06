
CREATE TABLE taxi_trip_data (
    vendor_id INT,
    pickup_datetime DATETIME,
    dropoff_datetime DATETIME,
    passenger_count INT,
    trip_distance FLOAT,
    rate_code INT,
    store_and_fwd_flag VARCHAR(5),
    payment_type INT,
    fare_amount FLOAT,
    extra FLOAT,
    mta_tax FLOAT,
    tip_amount FLOAT,
    tolls_amount FLOAT,
    imp_surcharge FLOAT,
    total_amount FLOAT,
    pickup_location_id INT,
    dropoff_location_id INT,
    trip_duration_minutes FLOAT
);
