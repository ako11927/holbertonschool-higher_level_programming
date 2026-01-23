-- Count shows per genre (no genre_id in output, only name + count)
SELECT tv_genres.name, COUNT(*) AS number_of_shows FROM tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
