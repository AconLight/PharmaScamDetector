CREATE TABLE if not exists ppp_pharma_company (
    id INT GENERATED ALWAYS AS IDENTITY,
    ppp_id INT,
    pharma_company_id INT,
    PRIMARY KEY(id)
);