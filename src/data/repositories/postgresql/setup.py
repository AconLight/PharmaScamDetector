from src.data.repositories.postgresql.connect import postgresql_engine
from src.data.repositories.postgresql.load_query import query


def setup():
    with postgresql_engine().connect() as db:

        # entity
        db.execute(query(['setup', 'drug'], 'TABLE'))
        db.execute(query(['setup', 'drug'], 'VALUES_TABLE'))
        db.execute(query(['setup', 'pharma_company'], 'TABLE'))
        db.execute(query(['setup', 'pharma_company'], 'VALUES_TABLE'))
        db.execute(query(['setup', 'ppp'], 'TABLE'))
        db.execute(query(['setup', 'ppp'], 'VALUES_TABLE'))

        # association
        db.execute(query(['setup', 'ppp_pharma_company'], 'TABLE'))
        db.execute(query(['setup', 'ppp_pharma_company'], 'VALUES_TABLE'))
        db.execute(query(['setup', 'pharma_company_drug'], 'TABLE'))
        db.execute(query(['setup', 'pharma_company_drug'], 'VALUES_TABLE'))

        # example populate
        db.execute(query(['create', 'drug'], 'ONE_ENTRY'), name="example")
        db.execute(query(['create', 'pharma_company'], 'ONE_ENTRY'), name="example")
        db.execute(query(['create', 'ppp'], 'ONE_ENTRY'), name="example")
        db.execute(query(['associate', 'ppp_pharma_company'], 'ONE_ENTRY'), ppp_id=1, pharma_company_id=1)
        db.execute(query(['associate', 'pharma_company_drug'], 'ONE_ENTRY'), pharma_company_id=1, drug_id=1)
