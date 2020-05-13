USE puzzlegame;

/* DROP */

-- Drop Table: Player --
DROP TABLE IF EXISTS puzzlegame.player;

-- Drop Table: Web History --
DROP TABLE IF EXISTS puzzlegame.web_history; 


/* CREATE */
-- Create Table: Player --
CREATE TABLE IF NOT EXISTS player (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	score INT NOT NULL, 
	ipaddr VARCHAR(255) NOT NULL, 
	country VARCHAR(255), 
	region VARCHAR(255), 
	city VARCHAR(255) 
);

-- Create Table: Web History --
CREATE TABLE IF NOT EXISTS web_history (
	no INT AUTO_INCREMENT PRIMARY KEY,
	pid INT NOT NULL,
	tabid INT NOT NULL,
    domain VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    viewdate DATETIME NOT NULL
);
