import pandas as pd


def preprocess(df):

    df = df.copy()


    # -------------------------
    # Date processing
    # -------------------------

    df["Release_Date"] = pd.to_datetime(
        df["Release_Date"],
        errors="coerce"
    )

    df["Release_Year"] = (
        df["Release_Date"]
        .dt.year
        .astype("Int64")
    )


    # -------------------------
    # Numeric columns
    # -------------------------

    df["Vote_Count"] = pd.to_numeric(
        df["Vote_Count"],
        errors="coerce"
    ).astype("Int64")


    df["Vote_Average"] = pd.to_numeric(
        df["Vote_Average"],
        errors="coerce"
    )


    df["Popularity"] = pd.to_numeric(
        df["Popularity"],
        errors="coerce"
    )


    # -------------------------
    # Missing values
    # -------------------------

    df["Genre"] = (
        df["Genre"]
        .fillna("Unknown")
    )


    df["Overview"] = (
        df["Overview"]
        .fillna("No description available")
    )


    return df