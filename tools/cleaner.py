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
    logger.info("Filled Age Null values to mean")
    df['Age'] = df['Age'].astype(int)
    logger.info("Changed Age dtype to int")
    df = df.dropna(subset='City')
    logger.info("Dropped Null values from City")
    df['SignupDate'] = pd.to_datetime(df['SignupDate'])
    logger.info("Formatted SignupDate to type datetime")
    return df

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    column_format(df)
    df = df.drop_duplicates(keep='last')
    logger.info("Dropped duplicates")
    df = df.dropna(subset='OrderDate')
    logger.info("Dropped OrderDate Null values")
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    logger.info("Formatted OrderDate dtype to date")
    df['Discount'] = df['Discount'].fillna(0)
    logger.info("Filled Discount Null values with 0")
    df['Discount'] = df['Discount'] * 100
    df['Discount'] = df['Discount'].astype(str)
    df['Discount'] = df['Discount'] + '%'
    logger.info("Formatted Discount to percentage value")
    df = df.dropna(subset='Quantity')
    df['Quantity'] = df['Quantity'].astype(int)
    logger.info("Changed dtype from float to int for Quantity column")
    df = df.drop(df[df['Quantity'] < 1].index)
    logger.info("Dropped outlier values in Quantity column")
    df['PaymentMethod'] = df['PaymentMethod'].fillna('Cash')
    logger.info("Filled Null value from PaymentMethod to Cash")
    return df #type: ignore

def clean_payments(df: pd.DataFrame) -> pd.DataFrame:
    pass