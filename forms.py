from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, DateField, SelectField, EmailField



class registerForm(FlaskForm):
    username = StringField("Enter Username")
    password = PasswordField("Enter Password")
    email = EmailField("Enter Email")
    mobile = IntegerField("Enter Mobile Number")
    birthdate = DateField("Enter Birth Date")
    gender = SelectField("Enter Gender", choices=["Choose Gender","male", "female", "bulki", "lafsha", "shaurma", "karfuri", "jojo", "dr house"])
    country = SelectField(choices=["Choose Country", "Georgia", "USA", "Germany", "Canada"])