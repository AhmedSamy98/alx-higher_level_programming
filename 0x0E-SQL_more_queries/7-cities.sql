-- Creates the database hbtn_0d_usa
-- and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;


-- Create table 'cities' in db 'hbtn_0d_usa'
-- state_id INT not null, foreign key that references id of 'states' table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    `id` INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
