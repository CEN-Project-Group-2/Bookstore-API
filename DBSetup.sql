CREATE DATABASE geek_text;
USE geek_text;
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON geek_text.* TO 'user'@'localhost'