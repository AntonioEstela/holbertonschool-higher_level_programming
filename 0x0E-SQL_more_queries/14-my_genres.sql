-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT `tv_genres`.`name` as name
FROM `tv_show_genres`
INNER JOIN `tv_genres`
ON `genre_id`=`tv_genres`.`id`
WHERE `show_id`=8;