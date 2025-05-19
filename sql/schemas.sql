USE mydatabase;

CREATE TABLE districts (
    district_id INT PRIMARY KEY auto_increment,
    district_name VARCHAR(30) not null,
    area int not null,
    registered_residents int not null);

CREATE TABLE plots(
    plot_id INT NOT NULL PRIMARY KEY,
    district_id INT NOT NULL,
    identifier VARCHAR(30) NOT NULL,
    plot_number VARCHAR (30) NOT NULL,
    plot_area_ha DOUBLE NOT NULL,
    FOREIGN KEY (district_id) REFERENCES districts(district_id));

CREATE TABLE demographics (
    demographic_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    district_id INT NOT NULL,
    gender ENUM('f', 'm', 't') NOT NULL,
    age_from INT NOT NULL,
    age_to INT NOT NULL,
    count INT NOT NULL,
    FOREIGN KEY (district_id) REFERENCES districts(district_id));

CREATE TABLE age_pyramid(
    pyramid_id INT PRIMARY KEY AUTO_INCREMENT,
    district_id INT NOT NULL,
    f_0_2 INT,
    m_0_2 INT,
    f_3_6 INT,
    m_3_6 INT,
    f_7_14 INT,
    m_7_14 INT,
    f_15_18 INT,
    m_15_18 INT,
    f_19_24 INT,
    m_19_24 INT,
    f_25_34 INT,
    m_25_34 INT,
    f_35_44 INT,
    m_35_44 INT,
    f_45_59_64 INT,
    m_45_59_64 int,
    f_60_65_79 int, 
    m_60_65_79 int, 
    f_over_80 int, 
    m_over_80 int);

CREATE TABLE stops (
    stop_id INT PRIMARY KEY AUTO_INCREMENT,
    district_id INT NOT NULL,
    stop_name VARCHAR(100) NOT NULL,
    lines VARCHAR(150) NOT NULL,
    stop_type VARCHAR(50) NOT NULL,
    longitude DOUBLE NOT NULL,
    latitude DOUBLE NOT NULL,
    FOREIGN KEY (district_id) REFERENCES districts(district_id));

CREATE TABLE buildings (
    building_id INT PRIMARY KEY AUTO INCREMENT, 
    district_id INT NOT NULL, 
    plot_number VARCHAR(20)NOT NULL,
    index_type VARCHAR(20) NOT NULL,
    building_type VARCHAR(50) NOT NULL,
    building_area_ha DOUBLE NOT NULL, 
    FOREGIN KEY district_id REFERENCES districts(district_id));

CREATE TABLE greeen_areas (
    green_area_id INT PRIMARY KEY AUTO INCREMENT,
    district_id INT NOT NULL, 
    green_type VARCHAR(50) NOT NULL, 
    area_ha DOUBLE, 
    FOREGIN KEY district_id REFERENCES districts(district_id));

CREATE TABLE price_registry (
    price_registry_id INT AUTO_INCREMENT PRIMARY KEY,
    purchase_year INT NOT NULL,
    purchase_month INT NOT NULL,
    market_type VARCHAR(50) NOT NULL,
    avg_price DECIMAL(15, 2) NOT NULL,
    avg_area DECIMAL(10, 2) NOT NULL,
    avg_price_per_m2 DECIMAL(10, 2) NOT NULL,
    object_count INT NOT NULL,                   
    district_id INT NOT NULL,
    FOREIGN KEY (district_id) REFERENCES districts(district_id));

CREATE TABLE facility_access (
    facility_id INT AUTO_INCREMENT PRIMARY KEY,
    facility_name VARCHAR(255) NOT NULL,
    facility_type VARCHAR(255) NOT NULL,
    facility_code INT,
    street VARCHAR(255),
    longitude DECIMAL(20, 10) NOT NULL,
    latitude DECIMAL(20, 10) NOT NULL,
    district_id INT NOT NULL,
    FOREIGN KEY (district_id) REFERENCES districts(district_id));

