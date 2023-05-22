-- Delete the database if it already exists
DROP DATABASE IF EXISTS HCIS;

-- Create a new database
CREATE DATABASE HCIS;

-- Select the new database
USE HCIS;


-- Delete the tables if they already exist
DROP TABLE IF EXISTS PATIENTS;
DROP TABLE IF EXISTS ADMISSIONS;
DROP TABLE IF EXISTS PROCEDURES;
DROP TABLE IF EXISTS DIAGNOSIS;
DROP TABLE IF EXISTS PRESCRIPTIONS;

-- Create the tables
CREATE TABLE PATIENTS (
    subject_id INT PRIMARY KEY NOT NULL,
    lang VARCHAR(50),
    religion VARBINARY(100),
    marital_status VARCHAR(50),
    ethnicity VARCHAR(50)
) ENGINE=InnoDB ROW_FORMAT=DYNAMIC;

CREATE TABLE ADMISSIONS (
    hadm_id INT PRIMARY KEY,
    subject_id INT,
    admittime TEXT,
    dischtime TEXT,
    deathtime TEXT,
    admission_type VARCHAR(50),
    admission_location VARCHAR(50),
    discharge_location VARCHAR(50),
    edregtime TEXT,
    edouttime TEXT,
    diagnosis VARCHAR(255),
    hospital_expire_flag BOOLEAN,
    has_chartevents_data BOOLEAN,
    FOREIGN KEY (subject_id) REFERENCES PATIENTS (subject_id)
) ENGINE=InnoDB;

CREATE TABLE DIAGNOSIS (
    icd9_code VARCHAR(10) PRIMARY KEY,
    short_title VARCHAR(255),
    long_title TEXT,
    subject_id INT,
    hadm_id INT,
    FOREIGN KEY (subject_id) REFERENCES PATIENTS (subject_id),
	FOREIGN KEY (hadm_id) REFERENCES ADMISSIONS (hadm_id)
) ENGINE=InnoDB;

CREATE TABLE PROCEDURES (
    icd9_code VARCHAR(10) PRIMARY KEY,
    short_title VARCHAR(255),
    long_title TEXT,
    subject_id INT,
    hadm_id INT,
    FOREIGN KEY (subject_id) REFERENCES PATIENTS (subject_id),
	FOREIGN KEY (hadm_id) REFERENCES ADMISSIONS (hadm_id)
) ENGINE=InnoDB;

CREATE TABLE PRESCRIPTIONS (
    subject_id INT PRIMARY KEY,
    hadm_id INT,
    startdate TEXT,
    enddate TEXT,
    drug_type VARCHAR(50),
    drug TEXT,
    drug_name_poe TEXT,
    drug_name_generic TEXT,
    formulary_drug_cd VARCHAR(50),
    gsn INT, 
    ndc INT, 
    prod_strength TEXT,
    dose_val_rx FLOAT,
    dose_unit_rx TEXT,
    form_val_disp FLOAT, 
    form_unit_disp TEXT,
    route TEXT,
    FOREIGN KEY (subject_id) REFERENCES PATIENTS (subject_id),
	FOREIGN KEY (hadm_id) REFERENCES ADMISSIONS (hadm_id)
) ENGINE=InnoDB;