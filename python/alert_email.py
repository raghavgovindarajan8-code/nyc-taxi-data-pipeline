
from logger import logger

def send_alert(message):
    logger.error(message)
    print("ALERT:", message)
