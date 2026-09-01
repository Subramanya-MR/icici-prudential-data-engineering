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



-- =========================================================
-- 1.PREMIUM DATA VALIDATION
-- =========================================================

COPY INTO PREMIUM_RAW
FROM @PREMIUM_S3_STAGE
FILE_FORMAT = (FORMAT_NAME = 'PREMIUM_CSV_FORMAT')
VALIDATION_MODE = 'RETURN_ERRORS';


-- =========================================================
-- 2.PREMIUM DATA LOAD
-- =========================================================

COPY INTO PREMIUM_RAW
FROM @PREMIUM_S3_STAGE
FILE_FORMAT = (FORMAT_NAME = 'PREMIUM_CSV_FORMAT')
ON_ERROR = 'ABORT_STATEMENT';