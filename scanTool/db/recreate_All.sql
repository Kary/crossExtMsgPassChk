-- source file.sql

USE crossExtMsgPassChk;

DROP TABLE IF EXISTS ExtResult;

CREATE TABLE `ExtResult` (
  `num` int NOT NULL AUTO_INCREMENT,
  `extFolderName` varchar(39) NOT NULL,
  `ecInlineScript` tinyint(1) DEFAULT 0,
  `devInlineScript` tinyint(1) DEFAULT 0,
  `staticCheck` varchar(1) DEFAULT 'U',
  `manualCheck` varchar(1) DEFAULT 'U',
  `comment` varchar(200) DEFAULT '',
  PRIMARY KEY (`num`)
);


DROP TABLE IF EXISTS HtmlResult;

CREATE TABLE `HtmlResult` (
  `num` int NOT NULL AUTO_INCREMENT,
  `extFolderName` varchar(39) NOT NULL,
  `html` varchar(500) NOT NULL,
  `ec` tinyint(1) DEFAULT 0,
  `cs` tinyint(1) DEFAULT 0,
  `dev` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`num`)
);


DROP TABLE IF EXISTS JsContent;

CREATE TABLE `JsContent` (
  `num` int NOT NULL AUTO_INCREMENT,
  `extFolderName` varchar(39) NOT NULL,
  `js` varchar(500) NOT NULL,
  `tableType` varchar(1) DEFAULT 'U',
  `jsKey` varchar(500) DEFAULT NULL,
  `jsValue` varchar(500) DEFAULT NULL,
  `sLine` int DEFAULT '0',
  `sCol` int DEFAULT '0',
  `eLine` int DEFAULT '0',
  `eCol` int DEFAULT '0',
  PRIMARY KEY (`num`)
);


DROP TABLE IF EXISTS JsResult;

CREATE TABLE `JsResult` (
  `num` int NOT NULL AUTO_INCREMENT,
  `extFolderName` varchar(39) NOT NULL,
  `js` varchar(500) NOT NULL,
  `md5` varchar(32) DEFAULT NULL,
  `sExtFolderName` varchar(39) NOT NULL,
  `sJs` varchar(500) NOT NULL,
  `esprima` varchar(1) DEFAULT 'U',
  `duplicate` tinyint(1) DEFAULT 0,
  `ec` tinyint(1) DEFAULT 0,
  `cs` tinyint(1) DEFAULT 0,
  `dev` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`num`)
);
-- mysqldump -u crossExtMsgPassChk -p crossExtMsgPassChk JsResult > JsResultBackup_<Num>.sql
