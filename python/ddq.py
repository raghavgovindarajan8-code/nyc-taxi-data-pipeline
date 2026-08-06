
from logger import logger

def run_ddq(df):

    row_count = len(df)
    duplicate_count = df.duplicated().sum()
    total_nulls = int(df.isnull().sum().sum())

    print("\n==============================")
    print("      DATA HEALTH REPORT")
    print("==============================")
    print(f"Rows Loaded      : {row_count:,}")
    print(f"Duplicates       : {duplicate_count:,}")
    print(f"Null Values      : {total_nulls:,}")

    if row_count == 0:
        status = "FAILED"
    else:
        status = "SUCCESS"

    print(f"Pipeline Status  : {status}")
    print("==============================\n")

    logger.info(f"Rows Loaded: {row_count}")
    logger.info(f"Duplicates: {duplicate_count}")
    logger.info(f"Null Values: {total_nulls}")
    logger.info(f"Pipeline Status: {status}")

    if duplicate_count > 0:
        logger.warning(f"{duplicate_count} duplicate rows detected. Cleaning step will remove them.")

    if total_nulls > 0:
        logger.warning(f"{total_nulls} null values detected.")

    if row_count == 0:
        raise Exception("No data loaded. Pipeline stopped.")

    return df
