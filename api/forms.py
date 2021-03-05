from flask_wtf import Form, FlaskForm
from wtforms import TextField, PasswordField, StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

# Set your classes here.


def is_phone_number(FlaskForm, field):
        

        if str(field.data[:4]) != "+263":
                raise ValidationError('Please add The Zimabwean Country Code +263')

        if len(str(field.data)) != 13:
            raise ValidationError('Phone Number Should Have 13 Digits including The Country Code')

        if str(field.data)[4:6] != '71' and str(field.data)[4:6] != '73' and str(field.data)[4:6] != '78' and str(field.data)[4:6] != '77':
            raise ValidationError('Phone Number Should Include The Correct Zimbabwean Network Operator Codes')

def is_amount_valid(FlaskForm, field):
    if field.data < 5:
        raise ValidationError('Amount Should be Above 5')
    
    if not str(field.data).isdigit():
            raise ValidationError('The Amount should be a Number')

def is_security_code_valid(FlaskForm, field):
    if len(str(field.data)) < 3 :
        raise ValidationError('Security Code should have 3 or 4 digits')
    
    if not str(field.data).isdigit():
            raise ValidationError('Security Code should be a Number') 

def is_expiry_date_valid(FlaskForm, field):
    ex = list(field.data)
    if not ex[0].isdigit() and not ex[1].isdigit() and  ex[2] !='/' and not ex[3].isdigit() and not ex[4].isdigit() :
        raise ValidationError('Please Use The Format in The Example')

def is_card_number_valid(FlaskForm, field):
   
    if not str(field.data).isdigit():
        raise ValidationError('Card Number should be a Number') 
    if len(str(field.data)) != 16 :
        raise ValidationError('Card Number should have 16 digits')
    
    
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
