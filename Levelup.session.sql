SELECT * FROM levelupapi_gametype;

SELECT * FROM auth_user;

SELECT * FROM authtoken_token;

SELECT * FROM levelupapi_gamer;

SELECT * FROM levelupapi_event;

SELECT * FROM django_migrations;

DELETE FROM django_migrations WHERE app='levelupapi'


DELETE

DROP TABLE levelupapi_event;
DROP TABLE levelupapi_gamer;
DROP TABLE levelupapi_gametype;
DROP TABLE levelupapi_game;