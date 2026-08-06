
from logger import logger
from helper_functions import *

def clean_data(df):

    logger.info("Cleaning started")

    rows_before = len(df)

    df = df.drop_duplicates()

    logger.info(f"Removed {rows_before-len(df)} duplicate rows")

    df = convert_datetime(df)

    df = calculate_trip_duration(df)

    df = remove_invalid_rows(df)

    logger.info("Cleaning completed")

    return df
