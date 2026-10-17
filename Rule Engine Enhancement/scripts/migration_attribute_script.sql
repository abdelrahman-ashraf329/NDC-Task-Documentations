DROP PROCEDURE IF EXISTS migrateAttributes;

DELIMITER $$

CREATE PROCEDURE migrateAttributes(IN attrId INTEGER) migrateAttributes:
BEGIN
    DECLARE currentIpAddress VARCHAR(255);
    DECLARE isMigrated BOOLEAN DEFAULT FALSE;
    
    SELECT SUBSTRING_INDEX(USER(), '@', -1) INTO currentIpAddress;
    
    IF currentIpAddress = 'ndc-prd-ne-bastion.internal.cloudapp.net' THEN
		LEAVE migrateAttributes;   
    END IF;
    
    SET isMigrated = EXISTS (
    SELECT 1
    FROM wonderdb.TT_TS_RULE_CRITERIA
    WHERE RULES_ATTR_UID = attrId
      AND CRITERIA_VALUE REGEXP '^[0-9]+$'
		);
        
	IF isMigrated = 1 THEN
		LEAVE migrateAttributes;   
    END IF;
    
    -- =========================================================
	-- 1. backup
	-- =========================================================
    IF attrId = 1 THEN
    -- AirlineCode
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_1_20260531;

		CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_1_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;

	END IF;
    
    IF attrId = 2 THEN
    -- AirlineName
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_2_20260531;
        
        CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_2_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;
        
    END IF;
    
    IF attrId = 13 THEN
    -- dealCode
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_13_20260531;
        
        CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_13_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;
        
    END IF;
    
    IF attrId = 14 THEN
    -- destinationAirport
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_14_20260531;
        
        CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_14_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;
        
    END IF;
    
    IF attrId = 15 THEN
    -- destinationCity
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_15_20260531;
        
        CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_15_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;
        
    END IF;
    
    IF attrId = 16 THEN
    -- destinationCountry
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_16_20260531;

		CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_16_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;
    END IF;
    
    IF attrId = 20 THEN
    -- nationality
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_20_20260531;

		CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_20_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;
    END IF;
    
    IF attrId = 27 THEN
    -- originAirport
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_27_20260531;

		CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_27_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;
    END IF;
    
    IF attrId = 28 THEN
    -- originCity
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_28_20260531;

		CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_28_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;
    END IF;
    
    IF attrId = 29 THEN
    -- originCountry
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_29_20260531;

		CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_29_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;
    END IF;
    
    IF attrId = 30 THEN
    -- pcc
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_30_20260531;

		CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_30_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;
    END IF;
    
    IF attrId = 32 THEN
    -- supplier
		DROP TABLE IF EXISTS wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_32_20260531;

		CREATE TABLE wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_32_20260531
		SELECT *
		FROM wonderdb.TT_TS_RULE_CRITERIA
		WHERE RULES_ATTR_UID = attrId;

	END IF;
    -- =========================================================
	-- 2. calculate count of all values splitted by comma
	-- =========================================================
		DROP TEMPORARY TABLE IF EXISTS TEMP_01;
		CREATE TEMPORARY TABLE TEMP_01
		WITH RECURSIVE split_data AS (
			-- First split
			SELECT
				RULE_CRITERIA_UID,
				TRIM(
					REGEXP_REPLACE(
						SUBSTRING_INDEX(CRITERIA_VALUE, ',', 1),
						'[[:space:]]+',
						' '
					)
				) AS VALUE_ITEM,

			   SUBSTRING(
					CRITERIA_VALUE,
					LENGTH(SUBSTRING_INDEX(CRITERIA_VALUE, ',', 1)) + 2
				) AS REMAINING
			FROM TT_TS_RULE_CRITERIA
			WHERE RULES_ATTR_UID = attrId

			UNION ALL

			-- Remaining values
			SELECT
				RULE_CRITERIA_UID,
			   TRIM(
					REGEXP_REPLACE(
						SUBSTRING_INDEX(REMAINING, ',', 1),
						'[[:space:]]+',
						' '
					)
				) AS VALUE_ITEM,

			   SUBSTRING(
					REMAINING,
					LENGTH(SUBSTRING_INDEX(REMAINING, ',', 1)) + 2
				) AS REMAINING
			FROM split_data
			WHERE REMAINING IS NOT NULL
			  AND REMAINING <> ''
		)

		SELECT
			RULE_CRITERIA_UID,
			COUNT(*) AS VALUE_COUNT
		FROM split_data
		WHERE VALUE_ITEM <> ''
		GROUP BY RULE_CRITERIA_UID;

		-- =========================================================
		-- 3. Split values into rows
		-- =========================================================
		DROP TEMPORARY TABLE IF EXISTS TEMP_02;
		CREATE TEMPORARY TABLE TEMP_02
		WITH RECURSIVE split_data AS (
			-- First value
			SELECT
				RULE_CRITERIA_UID,
				TRIM(
					REGEXP_REPLACE(
						SUBSTRING_INDEX(CRITERIA_VALUE, ',', 1),
						'[[:space:]]+',
						' '
					)
				) AS VALUE_ITEM,

				SUBSTRING(
					CRITERIA_VALUE,
					LENGTH(SUBSTRING_INDEX(CRITERIA_VALUE, ',', 1)) + 2
				) AS REMAINING
			FROM TT_TS_RULE_CRITERIA WHERE RULES_ATTR_UID = attrId

			UNION ALL

			-- Remaining values
			SELECT
				RULE_CRITERIA_UID,
				TRIM(
					REGEXP_REPLACE(
						SUBSTRING_INDEX(REMAINING, ',', 1),
						'[[:space:]]+',
						' '
					)
				) AS VALUE_ITEM,

				SUBSTRING(
					REMAINING,
					LENGTH(SUBSTRING_INDEX(REMAINING, ',', 1)) + 2
				) AS REMAINING
			FROM split_data
			WHERE REMAINING IS NOT NULL
			  AND REMAINING <> ''
		)
		SELECT
			RULE_CRITERIA_UID,
			VALUE_ITEM
		FROM split_data
		WHERE VALUE_ITEM <> '';

		IF attrId = 1 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.CONTENT_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_TS_AIRLINES b on a.VALUE_ITEM = b.AIRLINE_CODE;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.CONTENT_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_TS_AIRLINES b on a.VALUE_ITEM = b.AIRLINE_CODE;
            
        END IF;
        
        IF attrId = 2 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.CONTENT_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_TS_AIRLINES b on a.VALUE_ITEM = b.AIRLINE_NAME;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.CONTENT_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_TS_AIRLINES b on a.VALUE_ITEM = b.AIRLINE_NAME;
        END IF;
        
        IF attrId = 13 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.DEAL_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_TS_GDS_DEALCODE b on a.VALUE_ITEM = b.DEALCODE;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.DEAL_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_TS_GDS_DEALCODE b on a.VALUE_ITEM = b.DEALCODE;
        END IF;
        
        IF attrId = 14 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.AIRPORT_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_AIRPORT_DETAILS b on a.VALUE_ITEM = b.AIRPORT_NAME;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.AIRPORT_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_AIRPORT_DETAILS b on a.VALUE_ITEM = b.AIRPORT_NAME;
        END IF;
        
        IF attrId = 15 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.CITY_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_CITY b on a.VALUE_ITEM = b.CITY_NAME;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.CITY_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_CITY b on a.VALUE_ITEM = b.CITY_NAME;
        END IF;
        
         IF attrId = 16 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.COUNTRY_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_COUNTRY b on a.VALUE_ITEM = b.COUNTRY_NAME;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.COUNTRY_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_COUNTRY b on a.VALUE_ITEM = b.COUNTRY_NAME;
        END IF;
        
        IF attrId = 20 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.COUNTRY_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_COUNTRY b on a.VALUE_ITEM = b.COUNTRY_NAME;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.COUNTRY_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_COUNTRY b on a.VALUE_ITEM = b.COUNTRY_NAME;
        END IF;

		IF attrId = 27 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.AIRPORT_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_AIRPORT_DETAILS b on a.VALUE_ITEM = b.AIRPORT_NAME;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.AIRPORT_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_AIRPORT_DETAILS b on a.VALUE_ITEM = b.AIRPORT_NAME;
        END IF;
        
        
        IF attrId = 28 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.CITY_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_CITY b on a.VALUE_ITEM = b.CITY_NAME;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.CITY_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_CITY b on a.VALUE_ITEM = b.CITY_NAME;
        END IF;

		IF attrId = 29 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.COUNTRY_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_COUNTRY b on a.VALUE_ITEM = b.COUNTRY_NAME;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.COUNTRY_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_COUNTRY b on a.VALUE_ITEM = b.COUNTRY_NAME;
        END IF;

		IF attrId = 30 THEN
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.CREDENTIAL_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_TS_SUPPLIER_CREDENTIAL b on a.VALUE_ITEM = b.CREDENTIAL_NAME;
            
            delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
            
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.CREDENTIAL_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_TS_SUPPLIER_CREDENTIAL b on a.VALUE_ITEM = b.CREDENTIAL_NAME;
        END IF;
		
		IF attrId = 32 THEN
        
			-- preprocessing step (update all JazeeraAirwaysUAE value to be JazeeraAirways
			update TEMP_02 set VALUE_ITEM = 'JazeeraAirways' where VALUE_ITEM = 'JazeeraAirwaysUAE';

			DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.SUPPLIER_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_TS_SUPPLIER b on a.VALUE_ITEM = b.SUPPLIER_NAME;
		
			-- preprocessing step (delete all deleted suppliers)
			delete from TEMP_02 where VALUE_ITEM in 
            (select VALUE_ITEM from TEMP_03 where VALUE_ITEM_ID is null);
			
            DROP TEMPORARY TABLE IF EXISTS TEMP_03;
			CREATE TEMPORARY TABLE TEMP_03
			SELECT 
				a.RULE_CRITERIA_UID,
				a.VALUE_ITEM,
				b.SUPPLIER_ID VALUE_ITEM_ID
			FROM TEMP_02 a
			LEFT JOIN TT_TS_SUPPLIER b on a.VALUE_ITEM = b.SUPPLIER_NAME;
            
		END IF;

		-- =========================================================
		-- 4. Final valid value ID per rule
		-- =========================================================
		DROP TEMPORARY TABLE IF EXISTS TEMP_04;
		CREATE TEMPORARY TABLE TEMP_04
		SELECT 
			a.RULE_CRITERIA_UID,
			GROUP_CONCAT(
				DISTINCT VALUE_ITEM_ID
				ORDER BY VALUE_ITEM_ID
				SEPARATOR ','
			) AS final_value_item_ids
		FROM TEMP_03 a
		where a.VALUE_ITEM_ID is not null
		group by a.RULE_CRITERIA_UID;

		-- =========================================================
		-- 5. update the CRITERIA_VALUE 
		-- =========================================================
		
        DELETE FROM TT_TS_RULE_CRITERIA
		WHERE RULE_CRITERIA_UID IN (
			SELECT RULE_CRITERIA_UID FROM (
				SELECT a.RULE_CRITERIA_UID
				FROM TT_TS_RULE_CRITERIA a
				LEFT JOIN TEMP_04 b ON a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
				WHERE a.RULES_ATTR_UID = attrId
				  AND b.RULE_CRITERIA_UID IS NULL
			) AS rows_to_delete
		);
        
		update TT_TS_RULE_CRITERIA a
		inner join TEMP_04 b on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
		set a.CRITERIA_VALUE = b.final_value_item_ids WHERE RULES_ATTR_UID = attrId;
		
END$$

DELIMITER ;



/***** Rollback FOR Supplier ****/
/*update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_32_20260526 b on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 32;*/

/******** Rollback For AirlineCode *********/
/*update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_1_20260531 b on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 1; */

/******** Rollback For AirlineNames *********/

/*update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_2_20260531 b on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 2;*/


/******** Rollback For dealCode *********/
/* update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_13_20260531 b 
on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 13;*/


/******** Rollback For destinationAirport *********/
/* update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_14_20260531 b 
on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 14;*/

/******** Rollback For destinationCity *********/
/* update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_15_20260531 b 
on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 15;*/


/******** Rollback For destinationCountry *********/
/* update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_16_20260531 b 
on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 16;*/

/******** Rollback For nationality *********/
/* update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_20_20260531 b 
on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 20;*/


/******** Rollback For originAirport *********/
/* update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_27_20260531 b 
on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 27;*/

/******** Rollback For originCity *********/
/* update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_28_20260531 b 
on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 28;*/

/******** Rollback For originCountry *********/
/* update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_29_20260531 b 
on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 29;*/

/******** Rollback For pcc *********/
/* update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_30_20260531 b 
on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 30;*/

/******** Rollback For supplier *********/
/* update TT_TS_RULE_CRITERIA a
inner join wonderdb.TT_TS_RULE_CRITERIA_BACKUP_ATTR_32_20260531 b 
on a.RULE_CRITERIA_UID = b.RULE_CRITERIA_UID
set a.CRITERIA_VALUE = b.CRITERIA_VALUE WHERE a.RULES_ATTR_UID = 32;*/

SET SESSION cte_max_recursion_depth = 10000;

CALL migrateAttributes(32);

SELECT * FROM wonderdb.TT_TS_RULE_CRITERIA WHERE RULES_ATTR_UID = 32;
