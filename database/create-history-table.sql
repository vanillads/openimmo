CREATE TABLE immo.properties_history LIKE immo.suivi;

ALTER TABLE immo.properties_history MODIFY COLUMN myid varchar(255) NOT NULL,
   DROP PRIMARY KEY, ENGINE = MyISAM, ADD action VARCHAR(8) DEFAULT 'insert' FIRST,
   ADD revision INT(6) NOT NULL AUTO_INCREMENT AFTER action,
   ADD dt_datetime DATETIME NOT NULL AFTER revision,
   ADD PRIMARY KEY (myid, revision);
