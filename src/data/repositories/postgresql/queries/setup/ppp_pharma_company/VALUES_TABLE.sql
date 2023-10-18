CREATE TABLE if not exists ppp_pharma_company_values (
    id INT GENERATED ALWAYS AS IDENTITY,
    ppp_pharma_company_id INT,
    attribute_name VARCHAR(64) not null,
    attribute_type VARCHAR(64) not null,
    attribute_value VARCHAR(64) not null,
    PRIMARY KEY(id)
);