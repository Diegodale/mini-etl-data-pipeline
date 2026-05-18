import pandas as pd

def transform(df):

    # 1. Convertiamo le date
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

    # 2. Creiamo nuova feature: tempo di consegna
    df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

    # 3. Pulizia dati
    df = df.dropna()

    # 4. Reset index (buona pratica)
    df = df.reset_index(drop=True)

    print("Transform completato")
    print(df.head())

    return df