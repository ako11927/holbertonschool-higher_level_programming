-- Number of records with same score in second_table, sorted by count DESC
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
