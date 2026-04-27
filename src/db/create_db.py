import psycopg2

from src.db.database import engine, Base
from src.db import models

DB_USER = "postgres"
DB_PASSWORD = "0174"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "ml_project_db"


def create_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )

    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
    exists = cur.fetchone()

    if not exists:
        cur.execute(f'CREATE DATABASE "{DB_NAME}"')
        print(f"Base '{DB_NAME}' créée avec succès.")
    else:
        print(f"La base '{DB_NAME}' existe déjà.")

    cur.close()
    conn.close()


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables créées avec succès.")


if __name__ == "__main__":
    create_database()
    create_tables()