from sqlalchemy import create_engine, text


def postgresql_connect():
    engine = create_engine(
        "postgresql://postgres:anorektyk@localhost:5432/pharma",
        isolation_level="SERIALIZABLE",
    )
    with engine.connect() as conn:
        return conn
