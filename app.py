import flask
from nyt import get_article_data
import os

app = flask.Flask(__name__)

@app.route("/")
def main():
    topic = "election"
    data = get_article_data(topic)
    return flask.render_template(
        "index.html",
        topic=topic,
        length=len(data["headlines"]),
        headlines=data["headlines"],
        snippets=data["snippets"],
        dates=data["dates"],
        links=data["links"],
    )
    # pass that data to an HTML template

app.run(
    host='0.0.0.0',
    port=int(os.getenv("PORT", 8080))
)