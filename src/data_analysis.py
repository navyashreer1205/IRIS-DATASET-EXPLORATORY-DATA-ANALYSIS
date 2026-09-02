import pandas as pd
import numpy as np


def load_dataset(file_path):
    """Load the Iris dataset."""
    return pd.read_csv(file_path)


def check_missing_values(df):
    """Return the number of missing values in each column."""
    return df.isnull().sum()


def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates()


def descriptive_statistics(df):
    """Return descriptive statistics for numerical columns."""
    return df.describe()


def correlation_matrix(df):
    """Return the correlation matrix."""
    numeric_df = df.select_dtypes(include=np.number)
    return numeric_df.corr()