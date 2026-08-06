
import pandas as pd
from logger import logger

def load_data():

    logger.info("Loading taxi trip data")
    taxi_df = pd.read_csv("data/taxi_trip_data.csv")

    logger.info("Loading taxi zone data")
    zone_df = pd.read_csv("data/taxi_zone_geo.csv")

    logger.info("Datasets loaded successfully.")

    return taxi_df, zone_df
