# **Simple URL Shortener project with Flask and SQLite.**
___
## Steps to execute the project:
1. Make sure to have Poetry installed.
2. Execute `poetry update` to install dependencies.
3. Execute `python init_db.py` to create the SQLite database.
4. Set Flask environment variables: `set FLASK_APP=app` and `SET FLASK_ENV=development`
5. Run the project with: `flask run`
6. Enjoy.
___
## The routes available are the following:
1. `"/"`: Index route, where you can get the shortened URL.
2. `"/stats"`: Route with URLs stats.