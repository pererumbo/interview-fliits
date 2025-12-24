from db_helper import execute, fetch_df

def main():
    print("🔍 Comprobando conexión a la base de datos...")

    # --------------------------------------------------
    # 1) CREATE TABLE
    # --------------------------------------------------
    create_sql = """
    DROP TABLE IF EXISTS check_table;
    CREATE TABLE check_table (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        value INT NOT NULL
    );
    """
    execute(create_sql)
    print("✅ CREATE TABLE OK")

    # --------------------------------------------------
    # 2) INSERT
    # --------------------------------------------------
    insert_sql = """
    INSERT INTO check_table (name, value)
    VALUES
        ('alpha', 10),
        ('beta', 20),
        ('gamma', 30);
    """
    execute(insert_sql)
    print("✅ INSERT OK")

    # --------------------------------------------------
    # 3) SELECT con pandas
    # --------------------------------------------------
    select_sql = "SELECT * FROM check_table ORDER BY id;"
    df = fetch_df(select_sql)
    print("\n✅ SELECT con pandas OK")
    print(df)

    print("\n🎉 Todo está listo para la entrevista técnica 🚀")

if __name__ == "__main__":
    main()
