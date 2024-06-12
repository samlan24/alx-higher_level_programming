--creates a table
-- sets 1 as the default value
-- name is VARCHAR

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
