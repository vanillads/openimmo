DROP TRIGGER IF EXISTS immo.data__ai;
DROP TRIGGER IF EXISTS immo.data__au;
DROP TRIGGER IF EXISTS immo.data__bd;

CREATE TRIGGER immo.data__ai AFTER INSERT ON immo.properties FOR EACH ROW
    INSERT INTO immo.properties_history SELECT 'insert', NULL, NOW(), d.*
    FROM immo.properties AS d WHERE d.myid = NEW.myid;

CREATE TRIGGER immo.data__au AFTER UPDATE ON immo.properties FOR EACH ROW
    INSERT INTO immo.properties_history SELECT 'update', NULL, NOW(), d.*
    FROM immo.properties AS d WHERE d.myid = NEW.myid;

CREATE TRIGGER immo.data__bd BEFORE DELETE ON immo.properties FOR EACH ROW
    INSERT INTO immo.properties_history SELECT 'delete', NULL, NOW(), d.*
    FROM immo.properties AS d WHERE d.myid = OLD.myid;
