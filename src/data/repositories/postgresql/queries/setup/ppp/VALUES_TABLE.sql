CREATE TABLE if not exists ppp_values (
    id INT GENERATED ALWAYS AS IDENTITY,
    ppp_id INT,
    attribute_name VARCHAR(64) not null,
    attribute_type VARCHAR(64) not null,
    attribute_value VARCHAR(64) not null,
    PRIMARY KEY(id)
);