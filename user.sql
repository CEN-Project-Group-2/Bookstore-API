use geek_text;

CREATE TABLE Users (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    created_at DATE,
    deleted_at DATE,
    PRIMARY KEY (id)
);
