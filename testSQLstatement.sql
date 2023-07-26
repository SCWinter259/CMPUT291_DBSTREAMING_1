-- SELECT mid, title FROM movies WHERE title LIKE "%Captain%" COLLATE NOCASE;

/* INSERT INTO sessions VALUES (session_id, 'c100', start_time, NULL); */

/* I guess our only way is to check using python, because sqlite does not allow variables */

SELECT SUM(duration) FROM watch WHERE cid = 'c300' AND mid = 80;