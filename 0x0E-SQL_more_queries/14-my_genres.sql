-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT name FROM tv_genres
INNER JOIN tv_show_genres
ON id = genre_id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;
