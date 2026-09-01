-- =========================================================
-- ICICI PRUDENTIAL
-- RAW TABLE DEFINITIONS
-- =========================================================

USE DATABASE ICICI_PRUDENTIAL;
USE SCHEMA RAW;


-- =========================================================
-- 1. CUSTOMER RAW
-- Source: Customer / CRM
-- Format: CSV
-- =========================================================

CREATE OR REPLACE TABLE CUSTOMER_RAW (
    customer_id       VARCHAR(50),
    first_name        VARCHAR(100),
    last_name         VARCHAR(100),
    full_name          VARCHAR(200),
    gender             VARCHAR(20),
    date_of_birth      DATE,
    phone_number       VARCHAR(30),
    email              VARCHAR(255),
    city               VARCHAR(100),
    state              VARCHAR(100),
    pincode             VARCHAR(20),
    occupation         VARCHAR(100),
    annual_income      NUMBER(18,2),
    customer_status    VARCHAR(50),
    customer_since     DATE,
    source_system      VARCHAR(100),
    created_at         TIMESTAMP_NTZ,
    updated_at         TIMESTAMP_NTZ
);


-- =========================================================
-- 2. POLICY RAW
-- Source: Policy Administration System
-- Format: CSV
-- =========================================================

CREATE OR REPLACE TABLE POLICY_RAW (
    policy_id             VARCHAR(50),
    policy_number         VARCHAR(100),
    customer_id           VARCHAR(50),
    agent_id              VARCHAR(50),
    branch_id             VARCHAR(50),
    policy_type           VARCHAR(100),
    policy_start_date     DATE,
    policy_end_date       DATE,
    policy_term_years     NUMBER(5,0),
    sum_assured           NUMBER(18,2),
    annual_premium        NUMBER(18,2),
    premium_frequency     VARCHAR(50),
    premium_amount        NUMBER(18,2),
    payment_method        VARCHAR(50),
    policy_status         VARCHAR(50),
    source_system         VARCHAR(100),
    created_at            TIMESTAMP_NTZ,
    updated_at            TIMESTAMP_NTZ
);


-- =========================================================
-- 3. PREMIUM RAW
-- Source: Premium / Billing System
-- Format: CSV
-- =========================================================

CREATE OR REPLACE TABLE PREMIUM_RAW (
    payment_id               VARCHAR(50),
    policy_id                VARCHAR(50),
    customer_id              VARCHAR(50),
    payment_date             DATE,
    due_date                 DATE,
    premium_amount           NUMBER(18,2),
    payment_method           VARCHAR(50),
    payment_status           VARCHAR(50),
    transaction_reference    VARCHAR(100),
    receipt_number           VARCHAR(100),
    source_system            VARCHAR(100),
    created_at               TIMESTAMP_NTZ,
    updated_at               TIMESTAMP_NTZ
);


-- =========================================================
-- 4. CLAIMS RAW
-- Source: Claims System
-- Format: CSV
-- =========================================================

CREATE OR REPLACE TABLE CLAIMS_RAW (
    claim_id             VARCHAR(50),
    policy_id            VARCHAR(50),
    customer_id          VARCHAR(50),
    claim_number         VARCHAR(100),
    claim_date           DATE,
    claim_type           VARCHAR(100),
    claim_reason         VARCHAR(500),
    claim_amount         NUMBER(18,2),
    approved_amount      NUMBER(18,2),
    claim_status         VARCHAR(50),
    settlement_date      DATE,
    source_system        VARCHAR(100),
    created_at           TIMESTAMP_NTZ,
    updated_at           TIMESTAMP_NTZ
);


-- =========================================================
-- 5. AGENT RAW
-- Source: Agent / Branch System
-- Format: JSON
--
-- Complete JSON record is preserved in VARIANT.
-- =========================================================

CREATE OR REPLACE TABLE AGENT_RAW (
    raw_data VARIANT
);


-- =========================================================
-- 6. INVESTMENT RAW
-- Source: Investment / ULIP System
-- Format: JSON
--
-- Complete JSON record is preserved in VARIANT.
-- =========================================================

CREATE OR REPLACE TABLE INVESTMENT_RAW (
    raw_data VARIANT
);