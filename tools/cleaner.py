import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger(__name__)

def view_data(df: pd.DataFrame):
    print("===========HEAD==============")
    print(df.head(5))
    print("===========SHAPE==============")
    print(f"Dimension: {df.shape}")
    print("===========DESCRIBE==============")
    print(df.describe(include='all'))
    print("===========INFO==============")
    print(df.info()) #type: ignore
    print("===========TOTAL_NULL_SUM==============")
    print(df.isna().sum())

def column_format(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip()
    logger.info("Columns formatted")
    return df

def clean_customer(df: pd.DataFrame) -> pd.DataFrame:
    df = column_format(df)
    df = df.drop_duplicates(keep='first')
    logger.info("Dropped duplicates")
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    logger.info("Filled Age NaN values to mean")
    df['Age'] = df['Age'].astype(int)
    logger.info("Changed Age dtype to int")
    df = df.drop_duplicates(subset='City')
    logger.info("Dropped NaN values from City")
    df['SignupDate'] = pd.to_datetime(df['SignupDate'])
    logger.info("Formatted SignupDate to type datetime")
    return df