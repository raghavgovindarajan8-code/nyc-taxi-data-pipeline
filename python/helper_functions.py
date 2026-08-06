
import pandas as pd

def convert_datetime(df):
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
    df["dropoff_datetime"] = pd.to_datetime(df["dropoff_datetime"])
    return df

def calculate_trip_duration(df):
    df["trip_duration_minutes"] = (
        df["dropoff_datetime"] - df["pickup_datetime"]
    ).dt.total_seconds() / 60
    return df

def remove_invalid_rows(df):

    df = df[df["trip_duration_minutes"] > 0]

    df = df[df["passenger_count"] > 0]

    df = df[df["fare_amount"] > 0]

    df = df[df["trip_distance"] > 0]

    return df
