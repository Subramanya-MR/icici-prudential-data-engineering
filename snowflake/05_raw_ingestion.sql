-- =========================================================
-- ICICI PRUDENTIAL
-- RAW DATA INGESTION
-- =========================================================

USE DATABASE ICICI_PRUDENTIAL;
USE SCHEMA RAW;


-- =========================================================
-- 1. CUSTOMER DATA LOAD
-- =========================================================

COPY INTO CUSTOMER_RAW
FROM @CUSTOMER_S3_STAGE
FILE_FORMAT = (FORMAT_NAME = 'CUSTOMER_CSV_FORMAT')
ON_ERROR = 'ABORT_STATEMENT';



-- =========================================================
-- 2.PREMIUM DATA LOAD
-- =========================================================

COPY INTO PREMIUM_RAW
FROM @PREMIUM_S3_STAGE
FILE_FORMAT = (FORMAT_NAME = 'PREMIUM_CSV_FORMAT')
ON_ERROR = 'ABORT_STATEMENT';


-- =========================================================
-- 3. POLICY DATA LOAD
-- =========================================================

COPY INTO POLICY_RAW
FROM @POLICY_S3_STAGE
FILE_FORMAT = (FORMAT_NAME = 'POLICY_CSV_FORMAT')
ON_ERROR = 'ABORT_STATEMENT';


-- =========================================================
-- 4. CLAIMS DATA LOAD
-- =========================================================

COPY INTO CLAIMS_RAW
FROM @CLAIMS_S3_STAGE
FILE_FORMAT = (FORMAT_NAME = 'CLAIMS_CSV_FORMAT')
ON_ERROR = 'ABORT_STATEMENT';


