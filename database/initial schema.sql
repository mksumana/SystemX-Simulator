CREATE DATABASE IF NOT EXISTS systemx;
USE systemx;

CREATE TABLE os_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    algorithm VARCHAR(50),
    avg_wait_time FLOAT,
    avg_turnaround FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cache_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    policy VARCHAR(20),
    hit_rate FLOAT,
    miss_rate FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE network_routes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    src VARCHAR(20),
    dest VARCHAR(20),
    path TEXT,
    algorithm VARCHAR(30),
    cost FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
