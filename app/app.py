import os
from flask import Flask, render_template, send_from_directory, abort
from pathlib import Path
from werkzeug.utils import secure_filename

app = Flask(__name__)


MOVIE_DIR = Path("~/Videos/Medias")
VIDEO_EXTENSIONS = [".mp4"]
SUBTITLE_EXTENSIONS = [".vtt"]


if lanflix_dir := os.getenv("LANFLIX_DIR"):
    MOVIE_DIR = Path(lanflix_dir)


def get_movies():
    return [d.name for d in MOVIE_DIR.iterdir() if d.is_dir()]


def get_media(media_id):
    media_dir = MOVIE_DIR / media_id
    if not media_dir.exists() or not media_dir.is_dir():
        abort(404)

    media_file = None
    subtitles = []

    for file in media_dir.iterdir():
        if file.suffix in VIDEO_EXTENSIONS:
            media_file = file.name
        elif file.suffix in SUBTITLE_EXTENSIONS:
            subtitles.append(file.name)

    if not media_file:
        abort(404)

    return media_dir, media_file, subtitles


@app.route('/')
def index():
    return render_template("index.html", movies=get_movies())


@app.route("/play/<media_id>")
def play(media_id):
    path, file, subtitles = get_media(media_id)
    return render_template(
        "player.html",
        media_id=media_id,
        media_filename=file,
        subtitles=subtitles
    )


@app.route("/media/<media_id>")
def media(media_id):
    path, file, _ = get_media(media_id)
    return send_from_directory(path, file)


@app.route("/media/<media_id>/subtitle/<subtitle>")
def subtitle(media_id, subtitle):
    path, _, subtitles = get_media(media_id)
    subtitle = secure_filename(subtitle)

    if subtitle not in subtitles:
        abort(404)

    return send_from_directory(path, subtitle)


@app.route("/media/<media_id>/poster")
def poster(media_id):
    media_path = f"{MOVIE_DIR}/{media_id}"
    poster_path = f"{media_path}/poster.jpg"

    if not os.path.exists(poster_path):
        return send_from_directory("static", "missing-poster.jpg")

    return send_from_directory(media_path, "poster.jpg")