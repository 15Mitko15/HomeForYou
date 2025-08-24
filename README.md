Project set up:

You will need to have a pgAdmin4 and posgresql17. Create a server in the pgAdmin and set up the env variables.
After instaling the requirements.txt a migration should be ran. The command is - alembic upgrade head.
Then you can start the server with - uvicorn main:app --reload.




