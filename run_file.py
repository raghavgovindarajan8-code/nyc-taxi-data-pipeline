
import sys
sys.path.append("python")

from logger import logger
from data_loader import load_data
from ddq import run_ddq
from data_cleaning import clean_data

logger.info("Pipeline Started")

taxi_df, zone_df = load_data()

taxi_df = run_ddq(taxi_df)

logger.info("Starting cleaning")

taxi_df = clean_data(taxi_df)

logger.info("Saving cleaned dataset")

taxi_df.to_csv("output/cleaned_data.csv", index=False)

logger.info("Pipeline completed successfully")

print("\nPipeline completed successfully!")
