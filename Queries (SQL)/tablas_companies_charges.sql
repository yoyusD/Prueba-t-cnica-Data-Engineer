CREATE TABLE companies (
company_id VARCHAR(40) PRIMARY KEY,
company_name VARCHAR(130)
);

CREATE TABLE charges (
id VARCHAR(40) PRIMARY KEY,
company_id VARCHAR(40) NOT NULL,
amount DECIMAL(37,2) NOT NULL,
status VARCHAR(30) NOT NULL,
created_at TIMESTAMP,
updated_at TIMESTAMP, 
CONSTRAINT fk_company
FOREIGN KEY (company_id)
REFERENCES companies(company_id)
);