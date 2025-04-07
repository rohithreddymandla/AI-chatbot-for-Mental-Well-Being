from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from Application.models import User, Emergency


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[InputRequired(), Email()])
    emergency_contact_email = StringField('Emergency Email',
                        validators=[InputRequired(), Email()])
    emergency_contact_phone = StringField('Emergency Phone Number',
                           validators=[InputRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another username.')
        
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('That email is already exists. Please Log in.')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
