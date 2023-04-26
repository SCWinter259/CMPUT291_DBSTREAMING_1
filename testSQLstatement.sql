SELECT MAX(sid)+1 AS session_id FROM sessions;
SELECT datetime('now') AS start_time;

/* INSERT INTO sessions VALUES (session_id, 'c100', start_time, NULL); */

/* I guess our only way is to check using python, because sqlite does not allow variables */