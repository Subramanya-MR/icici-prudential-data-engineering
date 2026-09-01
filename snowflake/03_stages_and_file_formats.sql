-- =========================================================
-- ICICI PRUDENTIAL
-- EXTERNAL STAGES & FILE FORMATS
-- =========================================================

USE DATABASE ICICI_PRUDENTIAL;
USE SCHEMA RAW;


-- ---------------------------------------------------------
-- CUSTOMER S3 STAGE
-- ---------------------------------------------------------

CREATE OR REPLACE STAGE CUSTOMER_S3_STAGE
    URL = 's3://icici-prudential-data/customer/2026/08/26/'
    STORAGE_INTEGRATION = ICICI_S3_INTEGRATION;


-- ---------------------------------------------------------
-- CUSTOMER CSV FILE FORMAT
-- ---------------------------------------------------------

CREATE OR REPLACE FILE FORMAT CUSTOMER_CSV_FORMAT
    TYPE = CSV
    SKIP_HEADER = 1
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    TRIM_SPACE = TRUE;



-- ---------------------------------------------------------
-- POLICY S3 STAGE
-- ---------------------------------------------------------

CREATE OR REPLACE STAGE POLICY_S3_STAGE
    URL = 's3://icici-prudential-data/ policy/2026/08/26/'
    STORAGE_INTEGRATION = ICICI_S3_INTEGRATION;


-- ---------------------------------------------------------
-- POLICY CSV FILE FORMAT
-- ---------------------------------------------------------

CREATE OR REPLACE FILE FORMAT POLICY_CSV_FORMAT
    TYPE = CSV
    SKIP_HEADER = 1
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    TRIM_SPACE = TRUE;




-- ---------------------------------------------------------
-- PREMIUM S3 STAGE
-- ---------------------------------------------------------

CREATE OR REPLACE STAGE PREMIUM_S3_STAGE
    URL = 's3://icici-prudential-data/premium/2026/08/26/'
    STORAGE_INTEGRATION = ICICI_S3_INTEGRATION;


-- ---------------------------------------------------------
-- PREMIUM CSV FILE FORMAT
-- ---------------------------------------------------------

CREATE OR REPLACE FILE FORMAT PREMIUM_CSV_FORMAT
    TYPE = CSV
    SKIP_HEADER = 1
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    TRIM_SPACE = TRUE;