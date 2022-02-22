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

@app.route("/contact")
def contact():
    return render_template('contact.html', nav_links=get_nav_links())


@app.route("/process", methods=['POST', 'GET'])
def process_form():
    if request.method == 'GET':
        return render_template('invalid_access.html', nav_links=get_nav_links())
    if request.method == 'POST':
        form_data = request.form
        name = ""
        message = ""
        for key, value in form_data.items():
            if key == "name":
                name = value
            if key == "message":
                message = value
        return render_template('process.html', nav_links=get_nav_links())


def get_nav_links():
    return {
        "Menu": "/menu",
        "Gallery": "/gallery",
        "Contact Us": "/contact"
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
