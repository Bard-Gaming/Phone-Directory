from flask import (Flask, render_template)

app = Flask(__name__, template_folder='webpages')


def html_file(file_name: str):
    render_template(f'webpages/{file_name}.html')

# -------------------Routing------------------- :

@app.route('/')
def home_page():
    return html_file('front_page')