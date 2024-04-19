-- Shows grants for these users
SHOW GRANTS FOR 'user_0d_1'@'localhost'
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Creates a new user
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'locahost';
FLUSH PRIVILEGES;

-- read user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2';

-- FORCE NAME
CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);

-- ID NOT NULL
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);

--Unique id
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE(id)
);

-- states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id)
);

--CITIES TABLE
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id),
    FOREIGN KEY(state_id)
        REFERENCES states(id)
)

-- cities of california
SELECT id, name FROM cities

-- join
SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC;

-- GENRE
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id

-- my genres
SELECT tv_shows.title, tv_genres.name 
FROM tv_shows
INNER JOIN tv_genres
ON tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC