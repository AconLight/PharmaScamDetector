CREATE TABLE if not exists drug (
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(64) not null,
    PRIMARY KEY(id)
);