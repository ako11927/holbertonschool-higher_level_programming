-- Records from second_table where name is not NULL/empty, score DESC
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
