from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField, TextAreaField, RadioField
from wtforms.validators import DataRequired, ValidationError, length, equal_to, Email

from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(max=20, min=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), equal_to('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exits, please choose a different username!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exits, please choose a different email!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(" There's no account with this email. Please register.")


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), length(min=5, max=20)])
    confirm_password = PasswordField('confirm Password', validators=[DataRequired(), equal_to('password')])
    submit = SubmitField('Reset Password')


class ContactForm(FlaskForm):
    name = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    contact_email = StringField('', validators=[DataRequired(), Email()])
    contact_phone = StringField('', validators=[DataRequired()])
    brand_name = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    message = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('Send Mail')


class ContactusForm(FlaskForm):
    brand_name = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    contactemail = StringField('', validators=[DataRequired(), Email()])
    phonenumber = StringField('', validators=[DataRequired()])
    management = BooleanField('')
    searchengine = BooleanField('')
    branding = BooleanField('')
    website = BooleanField('')
    digital = BooleanField('')
    graphic = BooleanField('')
    logocreation = BooleanField('')
    videocreation = BooleanField('')
    submit = SubmitField('Send Mail')
    
class ClientinfoForm(FlaskForm):
    name = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    email = StringField('', validators=[DataRequired(), Email()])
    phone = StringField('', validators=[DataRequired()])
    
    companyname = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    companyaddress = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    addressline = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    city = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    products = TextAreaField('', validators=[DataRequired()])
    target = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    describe = TextAreaField('', validators=[DataRequired()])
    achieve = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    brandcolor = StringField('', validators=[DataRequired(), length(min=2, max=2000)])
    
    slogan = RadioField('', validators=[DataRequired()], choices=[('Yes'), ('No')])
    cos_contact = RadioField('', validators=[DataRequired()], choices=[('Call'), ('Email'), ('WhatsApp'), ('Website')])
    socialmedia = RadioField('', validators=[DataRequired()], choices=[('Instagram'), ('Facebook'), ('Twitter'), ('Linkedin'), ('TikTok')])
    submit = SubmitField('SUBMIT')