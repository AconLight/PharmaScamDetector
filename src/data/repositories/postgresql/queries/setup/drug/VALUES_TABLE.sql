CREATE TABLE if not exists drug_values (
    id INT GENERATED ALWAYS AS IDENTITY,
    drug_id INT,
    attribute_name VARCHAR(64) not null,
    attribute_type VARCHAR(64) not null,
    attribute_value VARCHAR(64) not null,
    PRIMARY KEY(id)
);