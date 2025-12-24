import psycopg2
import pandas as pd

# ======================================================
# CONFIGURACIÓN DB (el candidato debe editar esto)
# ======================================================
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "public"
DB_USER = "postgres"
DB_PASSWORD = "password"

# ======================================================
# CONEXIÓN
# ======================================================
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
    )

# ======================================================
# EJECUCIÓN SQL (CREATE / INSERT / UPDATE / DELETE)
# ======================================================
def execute(sql: str, params=None):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
        conn.commit()
    finally:
        conn.close()


# ======================================================
# SELECT → pandas DataFrame
# ======================================================
def fetch_df(sql: str) -> pd.DataFrame:
    conn = get_connection()
    try:
        return pd.read_sql(sql, conn)
    finally:
        conn.close()
