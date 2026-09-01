-- =========================================================
-- ICICI PRUDENTIAL
-- SNOWFLAKE STORAGE INTEGRATION
-- AWS S3 → SNOWFLAKE
-- =========================================================

USE DATABASE ICICI_PRUDENTIAL;
USE SCHEMA RAW;

CREATE OR REPLACE STORAGE INTEGRATION ICICI_S3_INTEGRATION
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = 'S3'
    ENABLED = TRUE
    STORAGE_AWS_ROLE_ARN =
        'arn:aws:iam::805493112552:role/ICICI_ROLE'
    STORAGE_ALLOWED_LOCATIONS = (
        's3://icici-prudential-data/'
    );

DESC INTEGRATION ICICI_S3_INTEGRATION;