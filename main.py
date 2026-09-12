import os

import pandas as pd
import logging
from pathlib import Path
from scripts import downloader

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    try:
        url = "erfan4524/e-commerce-sales-data-analysis-and-eda"
        data_path = 'data/'

        downloader.dataset_download(url, output_dir=data_path)

        df_ls = {}
        for file in Path(data_path).iterdir():
            file_name = Path(file).name
            if file_name == ".complete" or file_name == "clean_final_data.csv":
                continue
            else:
                logger.info(f"CSV file founded: {file_name}")
                df_ls[file_name] = pd.read_csv(f"{data_path}/{file_name}")
                logger.info(f"Added into df_ls")

    except Exception as e:
        logger.error(f"An exception occurred: {e}")

if __name__ == "__main__":
    main()