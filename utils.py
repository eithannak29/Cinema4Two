import pandas as pd
import string

def extract_title_year(title):
    year = title[-5:-1]
    title = title[:-6]
    return pd.Series([title, year])

def remove_punctuation(s):
    if not isinstance(s, str):
        s = str(s)
    return s.translate(str.maketrans('', '', string.punctuation))

def prepare_data(df):
    df[['title', 'year']] = df['title'].apply(extract_title_year)
    return df