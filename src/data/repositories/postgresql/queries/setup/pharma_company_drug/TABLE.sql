CREATE TABLE if not exists pharma_company_drug (
    id INT GENERATED ALWAYS AS IDENTITY,
    pharma_company_id INT,
    drug_id INT,
    PRIMARY KEY(id)
);