-- source file.sql

DROP DATABASE IF EXISTS crossExtMsgPassChk;
CREATE DATABASE crossExtMsgPassChk;

CREATE USER IF NOT EXISTS 'crossExtMsgPassChk'@'localhost' IDENTIFIED BY 'crossExtMsgPassChkPassword';
GRANT ALL PRIVILEGES ON crossExtMsgPassChk.* TO 'crossExtMsgPassChk'@'localhost';