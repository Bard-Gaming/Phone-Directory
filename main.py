from flask import Flask, render_template, request #Flask
from flask_wtf import FlaskForm #WTForms integration
from wtforms import StringField, SubmitField #WTForms
from wtforms.validators import DataRequired, Length #WTForms validators
import os

app = Flask(__name__, template_folder='htmlFiles', static_folder='staticFiles')
app.config['SECRET_KEY'] = '5e97ff184fd17570d846cb2ace1d4992' # clé secrète (requis pour sécurité)

# --------------------Tools-------------------- :
def read_data(file_name='userdata.txt'):
    with open(file_name, 'rt', encoding='utf-8') as file:
        return [data_element.rstrip('\n') for data_element in file.readlines()]

# Outil pour enregistrer données:
class save_data:
    def __init__(self, data, file_name='userdata.txt'):
        self.data = str(data)
        self.file_name = file_name

    def appendDuplicate(self):
        with open(self.file_name, 'at', encoding='utf-8') as file:
            try:
                file.write(f'{self.data}\n')
            except Exception as err:
                print(err)

    def append(self):
        if self.exists(): # Si données existent déjà -> pas enregistrer
            print(f' * [{self.__class__}] Failed to save data: Data already saved')
        else:
            self.appendDuplicate()


    def exists(self, data=None):
        data = data if data != None else self.data
        return True if data in read_data(self.file_name) else False

# Outil pour importer les fichiers plus facilement:

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


# -------------Forms (User input)-------------- :

class contactForm(FlaskForm):
    username = StringField('Nom: ',
                           validators=[DataRequired(), Length(min=3, max=30)])
    phone_number = StringField('Numéro de Téléphone: ',
                               validators=[DataRequired(), Length(min=8, max=20)])
    submit = SubmitField('Ajouter')

# -------------------Routing------------------- :

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        username = request.form.get('username')
        phone_number = request.form.get('phone_number')

        save_data((username, phone_number)).append()

    contact_form = contactForm()
    return import_file('front_page.html', form=contact_form).link

@app.route('/directory/')
def directory_page():
    data_list = [eval(data_element) for data_element in read_data()]
    return import_file('directory_page.html', data_list = data_list).link

@app.route('/about/')
def about_page():
    return import_file('about_page.html').link

if __name__ == '__main__':
    # app.debug = 1
    app.run()