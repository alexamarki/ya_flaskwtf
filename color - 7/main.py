from flask import Flask, render_template, redirect
from accessform import AccessForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    prof_list = ['инженер', 'пилот', 'биотехнолог', 'строитель', 'врач', 'метеоролог', 'климатолог', 'киберинженер',
                 'штурман', 'астрогеолог', 'пилот дронов']
    return render_template('list.html', list=list, prof_list=prof_list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data_dict = {'title': "Анкета", 'surname': "Lee", 'name': "Mason", 'education': "высшее",
                 'profession': "биотехнолог",
                 'sex': "male", 'motivation': "нету", 'ready': False}
    return render_template('auto_answer.html', data_dict=data_dict, title=data_dict['title'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = AccessForm()
    return render_template('auth.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def distribution():
    crew = ['Jane Sully', 'Jake Chow', 'Christopher Soot']
    return render_template('distribution.html', title='Размещение по каютам', crew=crew)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    return render_template('table.html', title='Оформление каюты', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
