import sqlite3

def load_sql(df, db_name = "sales.db"):
    conn = sqlite3.connect(db_name)

    # salva la tabella
    df.to_sql("orders", conn, if_exists="replace", index=False)

    conn.close()

    print("Dati caricati nel database SQL (SQLite)")