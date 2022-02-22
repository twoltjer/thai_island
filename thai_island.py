from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def splash():
    return render_template('splash.html')

@app.route("/menu")
def menu():
    return render_template('menu.html', nav_links=get_nav_links())


@app.route("/gallery")
def gallery():
    return render_template('gallery.html', nav_links=get_nav_links())

@app.route("/form")
def form():
    return render_template('form.html', title="User form!",
                           nav_links=get_nav_links())


@app.route("/process", methods=['POST', 'GET'])
def process_form():
    if request.method == 'GET':
        return render_template('bootstrap.html', title='Invalid form access',
                               content='You attempted to access the form URL directly. Try visiting /form and submitting!',
                               nav_links=get_nav_links())
    if request.method == 'POST':
        form_data = request.form
        user = ""
        passwd = ""
        for key, value in form_data.items():
            if key == "user":
                user = value
            if key == "passwd":
                passwd = value
        return render_template('bootstrap.html', title='Form submitted',
                               content=("Hello %s. Your password is %s." % (user, passwd)), nav_links=get_nav_links())


def get_nav_links():
    return {
        "Menu": "/menu",
        "Gallery": "/gallery"
        # "Menu": "/menu",
        # "Now!": "/now",
        # "Form": "/form"
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
