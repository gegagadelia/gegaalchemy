from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField
from wtforms.fields import EmailField, StringField, PasswordField, SubmitField, IntegerField, SelectMultipleField
from wtforms.validators import data_required, email, ValidationError, InputRequired


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[email(), data_required()],
                       render_kw={'class': 'form-control', 'placeholder': 'Enter Email'})
    password = PasswordField('Password', validators=[data_required()],
                             render_kw={'class': 'form-control', 'placeholder': 'Enter Password'})
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[email(), data_required()],
                       render_kw={'class': 'form-control', 'placeholder': 'Enter Email'})
    password = PasswordField('Password', validators=[data_required()],
                             render_kw={'class': 'form-control', 'placeholder': 'Enter Password'})
    first_name = StringField('First Name', validators=[data_required()],
                             render_kw={'class': 'form-control', 'placeholder': 'Enter First Name'})
    last_name = StringField('Last Name', validators=[data_required()],
                            render_kw={'class': 'form-control', 'placeholder': 'Enter Last Name'})
    age = IntegerField('Age', validators=[data_required()],
                       render_kw={'class': 'form-control', 'placeholder': 'Enter Age'})
    address = StringField('Address',
                          render_kw={'class': 'form-control', 'placeholder': 'Enter Address'})
    submit = SubmitField('Sign In', render_kw={'class': 'btn btn-primary'})