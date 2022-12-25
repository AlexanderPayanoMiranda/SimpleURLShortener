import sqlite3
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for


def get_db_connection() -> sqlite3.connect:
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_RANDOM_STRING"

hashids = Hashids(min_length=4, salt=app.config["SECRET_KEY"])


@app.route("/", methods=("GET", "POST"))
def index() -> render_template or redirect:
    connection = get_db_connection()

    if request.method == "POST":
        url = request.form["url"]

        if not url:
            flash("The URL is required!")
            return redirect(url_for("index"))

        url_data = connection.execute(
            "INSERT INTO urls (original_url) VALUES (?)",
            (url, )
        )

        connection.commit()
        connection.close()

        url_id = url_data.lastrowid
        hashid = hashids.encode(url_id)
        short_url = request.host_url + hashid

        return render_template("index.html", short_url=short_url)
    return render_template("index.html")


@app.route("/<url_id>")
def url_redirect(url_id: hashids.encode) -> redirect:
    connection = get_db_connection()

    original_id = hashids.decode(url_id)
    if original_id[0]:
        url_data = connection.execute(
            "SELECT original_url, clicks FROM urls WHERE id = (?)",
            (original_id[0], )
        ).fetchone()
        original_url = url_data["original_url"]
        clicks = url_data["clicks"]

        connection.execute(
            "UPDATE urls SET clicks = ? WHERE id = ?",
            (clicks+1, original_id[0])
        )
        connection.commit()
        connection.close()

        return redirect(original_url)
    else:
        flash("Invalid URL")
        return redirect(url_for("index"))


@app.route("/stats")
def stats() -> render_template:
    connection = get_db_connection()
    db_urls = connection.execute(
        "SELECT id, created, original_url, clicks FROM urls"
    ).fetchall()
    connection.close()

    urls = []
    for url in db_urls:
        url = dict(url)
        url["short_url"] = request.host_url + hashids.encode(url["id"])
        urls.append(url)

    return render_template("stats.html", urls=urls)
