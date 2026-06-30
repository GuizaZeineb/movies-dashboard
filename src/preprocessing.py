import pandas as pd


def preprocess(df):

    df = df.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Clean column names
    df.columns = df.columns.str.strip()

    # Date conversion
    df["Release_Date"] = pd.to_datetime(
        df["Release_Date"],
        errors="coerce"
    )

    df["Release_Year"] = (
        df["Release_Date"]
        .dt.year
    )

    # Missing values
    df["Genre"] = (
        df["Genre"]
        .fillna("Unknown")
    )

    df["Overview"] = (
        df["Overview"]
        .fillna("No description available")
    )

    return df