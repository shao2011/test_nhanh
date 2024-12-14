DROP KEYSPACE IF EXISTS default;

-- Create keyspace
CREATE KEYSPACE IF NOT EXISTS default
WITH replication = {'class':'SimpleStrategy', 'replication_factor':3};

-- Use keyspace
USE newshub;

-- Create table for articles
CREATE TABLE IF NOT EXISTS user_data (
    id INT PRIMARY KEY,
    user_memay TEXT,
    age INT
);

-- Insert sample data
INSERT INTO article (id, author, title, url, source, topic)
VALUES (0, 'authorr', 10);
