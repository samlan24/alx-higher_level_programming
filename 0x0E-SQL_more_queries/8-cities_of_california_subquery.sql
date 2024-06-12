--script that all cities of California 
--results sorted in ascending order by cities.id

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id;
