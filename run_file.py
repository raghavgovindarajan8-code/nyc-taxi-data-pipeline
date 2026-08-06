
import sys
sys.path.append("python")

from logger import logger
from data_loader import load_data
from data_cleaning import clean_data

logger.info("Pipeline Started")

taxi_df, zone_df = load_data()

taxi_df = clean_data(taxi_df)

taxi_df.to_csv("output/cleaned_data.csv", index=False)

logger.info("Output saved")

print("Pipeline completed successfully!")
