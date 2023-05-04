from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='htmlFiles', static_folder='staticFiles')


# --------------------Tools-------------------- :

class import_file:
    image_extensions = ['jpg', 'png']
    static_path = os.path.join('static')

    def __init__(self, file_name, *args, **kargs):
        self.extension = file_name.split('.')[-1]
        self.args = args
        self.kargs = kargs

        temp_dir_args = file_name.split('/') # 'resources/image.png' --> ['resources', 'image.png']
        self.file_name = os.path.join(*temp_dir_args) # os.path.join('resources', 'image.png')

        self.link = self.render_output()

    def render_output(self):
        if self.extension == 'html':
            return render_template(self.file_name, *self.args, **self.kargs)

        if self.extension in self.image_extensions:
            return os.path.join(self.static_path, self.file_name)

# -------------------Routing------------------- :

@app.route('/')
def home_page():
    return import_file('front_page.html').link