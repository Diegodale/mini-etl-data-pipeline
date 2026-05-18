from src.extract import extract
from src.transform import transform

df = extract("data/train.csv")
df = transform(df)