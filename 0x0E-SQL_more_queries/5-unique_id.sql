--creates a table unique_id
-- id has 1 as the default value
-- if the table exists the script should not fail

CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
