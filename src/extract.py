import pandas as pd

def extract(path):
    df = pd.read_csv(path)

    print("Dataset caricato correttamente")
    print(f"Dimensioni: {df.shape}")

    return df