from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class AccessForm(FlaskForm):
    id = StringField('ID астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('ID капитана', validators=[DataRequired()])
    password_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')