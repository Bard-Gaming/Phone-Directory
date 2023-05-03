from flask import Flask, render_template

app = Flask(__name__, template_folder='web_pages')


def html_file(file_name: str):
    return render_template(f'{file_name}.html')

# -------------------Routing------------------- :

@app.route('/')
def home_page():
    return html_file('front_page')