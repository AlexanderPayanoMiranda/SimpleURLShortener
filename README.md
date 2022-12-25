# **Simple URL Shortener project with Flask and SQLite.**
___
## Steps to execute the project:
1. Make sure to have Poetry installed.
2. Execute `poetry update` to update dependencies to their latest versions (Optional - Could cause unexpected behaviour).
3. Execute `poetry install` to install dependencies.
4. Execute `python init_db.py` to create the SQLite database.
5. Set Flask environment variables: `set FLASK_APP=app` and `SET FLASK_ENV=development`
6. Run the project with: `flask run`
7. Enjoy.
___
## The routes available are the following:
1. `"/"`: Index route, where you can get the shortened URL.
2. `"/stats"`: Route with URLs stats.