
import logging
import os

os.makedirs("output", exist_ok=True)

logging.basicConfig(
    filename="output/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
