from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flasktest.models import User


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        # 17:01 https://www.youtube.com/watch?v=CSHx6eCkmv0&t=875s
        # https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog
        if user:
            raise ValidationError('That username is taken. Please choose a different one')
    def validate_email(self, email):
        user = User.query.filter_by(username=email.data).first()
        # 17:01 https://www.youtube.com/watch?v=CSHx6eCkmv0&t=875s
        # https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog
        if user:
            raise ValidationError('That email is taken. Please choose a different one') 

