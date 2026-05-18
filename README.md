# Mini ETL Data Pipeline

This project is a simple end-to-end ETL (Extract, Transform, Load) pipeline built with Python.

It simulates a real-world data engineering workflow using a Kaggle sales dataset.

---

## 🚀 Project Workflow

The pipeline follows these steps:

### 1. Extract
- Load raw CSV data using Pandas

### 2. Transform
- Convert date columns to proper datetime format
- Create new feature: Delivery Days (difference between order and shipping date)
- Clean missing values
- Reset dataset index

### 3. Load
- Store cleaned data into a SQL database (SQLite)

---

## 🛠️ Tech Stack

- Python
- Pandas
- SQLite
- Git & GitHub

---

## 📁 Project Structure

mini-etl-data-pipeline/
│
├── data/
│ └── train.csv
│
├── src/
│ ├── extract.py
│ ├── transform.py
│ ├── load_sql.py
│
├── main.py
└── requirements.txt


---

## 📊 Dataset

The dataset is taken from Kaggle and contains sales order information including:

- Order details
- Customer information
- Product categories
- Sales values
- Shipping dates

---

## 🎯 Goal of the Project

The main objective is to demonstrate a basic data engineering workflow by building a simple ETL pipeline using Python.

This project helps practice:
- Data cleaning
- Data transformation
- Pipeline structuring
- SQL data loading

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install pandas
