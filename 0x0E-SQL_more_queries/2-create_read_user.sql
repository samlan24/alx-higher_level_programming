-- creates a database and a user and grants privileges to them

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'hbtn_0d_2' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT on *.* TO 'user_0d_2'@'hbtn_0d_2' WITH GRANT OPTION;
