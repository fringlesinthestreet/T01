from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
import env_variables
from flaskr.models import Posts, db, app
import datetime
import time


def create_app():

    db.init_app(app)

    return app


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    if request.method == "POST":
        try:
            text = request.form['text']
            ip = request.remote_addr
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            print(text, ip, date)
            #posts.append(text)
            post = Posts(text, ip, date)
            db.session.add(post)
            db.session.commit()
        except KeyError:
            errors.append(
                "Bad Request (400)"
            )
        except Exception as err:
            errors.append(
                "Ocurrió un error: {}".format(err)
            )

    posts = Posts.query.order_by(Posts.id).all()

    return render_template('index.html', errors=errors, posts=posts)


@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404

@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

@app.errorhandler(400)
def bad_request(e):
    return """
    Bad Request attempted <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run()
