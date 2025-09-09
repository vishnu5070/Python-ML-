CREATE TABLE product_details (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(10),
    category VARCHAR(10),
);
CREATE TABLE time_period (
    time_id DATA PRIMARY KEY,
    year INT,
    month INT,
    day INT,
);
CREATE TABLE store_info (
    store_id INT KEY,
    store_name VARCHAR(10),
    location VARCHAR(20),\
);
CREATE TABLE sales_data (
    sales_id INT PRIMARY KEY,
    time_id DATE,
    product_id INT,
    store_id INT,
    FOREIGN KEY (time_id) REFERENCES time_period(time_id),
    FOREIGN KEY (product_id) REFERENCES time_period(product_id),
    FOREIGN KEY (store_id) REFERENCES time_period(store_id),
);