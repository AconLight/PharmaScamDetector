CREATE TABLE if not exists pharma_company (
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(64) not null,
    PRIMARY KEY(id)
);