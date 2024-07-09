CREATE DATABASE dam_data;

USE dam_data;

CREATE TABLE dams (
    dam_id VARCHAR(20) PRIMARY KEY,
    dam_name VARCHAR(255),
    full_volume INT,
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6)
);

CREATE TABLE latest_data (
    dam_id VARCHAR(20) PRIMARY KEY,
    dam_name VARCHAR(255),
    date DATE,
    storage_volume DECIMAL(10, 3),
    percentage_full DECIMAL(6, 2),
    storage_inflow DECIMAL(10, 3),
    storage_release DECIMAL(10, 3),
    FOREIGN KEY (dam_id) REFERENCES dams(dam_id)
);

CREATE TABLE dam_resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    dam_id VARCHAR(20),
    date DATE,
    storage_volume DECIMAL(10, 3),
    percentage_full DECIMAL(6, 2),
    storage_inflow DECIMAL(10, 3),
    storage_release DECIMAL(10, 3),
    FOREIGN KEY (dam_id) REFERENCES dams(dam_id)
);


SELECT * FROM dams;
SELECT * FROM latest_data;
SELECT * FROM dam_resources;


SELECT COUNT(*) FROM dams;
SELECT COUNT(*) FROM latest_data;
SELECT COUNT(*) FROM dam_resources;