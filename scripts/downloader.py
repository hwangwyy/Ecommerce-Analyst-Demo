import kagglehub
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def dataset_download(url: str, output_dir: str):
    try:
        if not Path(output_dir).exists():
            kagglehub.dataset_download(url, output_dir=output_dir)
            logger.info(f"Dataset downloaded at {output_dir}")
        else:
            logger.info(f"Dataset is already downloaded at {output_dir}")
    except Exception as e:
        logger.error(f"An exception occurred: {e}")
