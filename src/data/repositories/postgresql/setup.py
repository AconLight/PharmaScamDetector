from src.data.repositories.postgresql.connect import postgresql_connect
from src.data.repositories.postgresql.load_query import query


def setup():
    db = postgresql_connect()
    db.execute(query('setup', 'CREATE_DRUG.sql'))
    db.execute(query('setup', 'CREATE_PHARMA_COMPANY.sql'))
    db.execute(query('setup', 'CREATE_PPP.sql'))
    db.execute(query('setup', 'CREATE_PPP_PHARMA_COMPANY_association.sql'))
    db.execute(query('setup', 'CREATE_PHARMA_COMPANY_DRUG_association.sql'))
