use geek_text;

CREATE TABLE users (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    created_at DATE,
    deleted_at DATE,
    PRIMARY KEY (id)
);

INSERT INTO users (name, created_at, deleted_at)
VALUES ('Bill', '2023-06-06', NULL);

INSERT INTO users (name, created_at, deleted_at)
VALUES ('Jim', '2023-06-07', NULL);

INSERT INTO users (name, created_at, deleted_at)
VALUES ('Phil', '2023-06-08', NULL);

INSERT INTO users (name, created_at, deleted_at)
VALUES ('Kevin', '2023-06-09', NULL);

INSERT INTO users (name, created_at, deleted_at)
VALUES ('Kayle', '2023-06-10', NULL);