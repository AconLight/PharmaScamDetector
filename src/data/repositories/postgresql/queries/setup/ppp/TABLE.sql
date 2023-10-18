CREATE TABLE if not exists ppp (
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(64) not null,
    PRIMARY KEY(id)
);