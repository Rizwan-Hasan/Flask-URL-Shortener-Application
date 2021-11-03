CREATE DATABASE  IF NOT EXISTS `URL-Shortener`;

USE `URL-Shortener`;

DROP TABLE IF EXISTS URLTABLE;
DROP TRIGGER IF EXISTS DATE_INSERT_AUTOMATION;
DROP TRIGGER IF EXISTS DATE_UPDATE_AUTOMATION;

-- Creating table for storing URL
CREATE TABLE URLTABLE
(
    ID         INT          NOT NULL PRIMARY KEY,
    URL        VARCHAR(300) NOT NULL UNIQUE,
    SHORT_URL  VARCHAR(7)   NOT NULL UNIQUE,
    ENTRY_DATE DATE
);

-- Creating trigger for automating date insertion
Delimiter ///
CREATE TRIGGER DATE_INSERT_AUTOMATION
    BEFORE INSERT
    ON URLTABLE
    FOR EACH ROW
BEGIN
    IF (NEW.ENTRY_DATE IS NULL) THEN
        SET NEW.ENTRY_DATE = CURRENT_DATE();
    ELSEIF (NEW.ENTRY_DATE <= CURRENT_DATE()) THEN
        SET NEW.ENTRY_DATE = NEW.ENTRY_DATE;
    ELSE
        SIGNAL SQLSTATE '23000' set message_text = 'Date can not be in future!';
    END IF;
END;
///

-- Creating trigger for automating date update
Delimiter ///
CREATE TRIGGER DATE_UPDATE_AUTOMATION
    BEFORE UPDATE
    ON URLTABLE
    FOR EACH ROW
BEGIN
    IF (NEW.ENTRY_DATE <= CURRENT_DATE()) THEN
        SET NEW.ENTRY_DATE = NEW.ENTRY_DATE;
    ELSE
        SIGNAL SQLSTATE '23000' set message_text = 'Date can not be in future!';
    END IF;
END;
///
