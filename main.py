from src.extract import extract
from src.transform import transform
from src.load_sql import load_sql

df = extract("data/train.csv")
df = transform(df)

load_sql(df)