-- =========================================================
-- ICICI PRUDENTIAL
-- RAW DATA INGESTION
-- =========================================================

USE DATABASE ICICI_PRUDENTIAL;
USE SCHEMA RAW;


-- =========================================================
-- 1. CUSTOMER DATA VALIDATION
-- =========================================================

COPY INTO CUSTOMER_RAW
FROM @CUSTOMER_S3_STAGE
FILE_FORMAT = (FORMAT_NAME = 'CUSTOMER_CSV_FORMAT')
VALIDATION_MODE = 'RETURN_ERRORS';


-- =========================================================
-- 2. CUSTOMER DATA LOAD
-- =========================================================

COPY INTO CUSTOMER_RAW
FROM @CUSTOMER_S3_STAGE
FILE_FORMAT = (FORMAT_NAME = 'CUSTOMER_CSV_FORMAT')
ON_ERROR = 'ABORT_STATEMENT';