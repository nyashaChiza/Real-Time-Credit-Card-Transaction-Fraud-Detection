from flask_wtf import Form, FlaskForm
from wtforms import TextField, PasswordField, StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

# Set your classes here.

    
    
class SignIn(FlaskForm):
    """Sign In form."""
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    

class SignUp(FlaskForm):
    """SignUp form."""
    name = StringField('card Number', validators=[DataRequired()])
    surname = StringField('Card Holder Name', validators=[DataRequired()])
    password = StringField('Expiry Date', validators=[DataRequired()])
    email = IntegerField('Security Code', validators=[DataRequired()])
    

class RegisterForm(Form):
    name = TextField(
        'Name', validators=[DataRequired(), Length(min=6, max=25)]
    )
    surname = TextField(
        'Surname', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    ) 
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    address = TextField(
        'Address', validators=[DataRequired(), Length(min=6, max=65)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )


class LoginForm(Form):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
