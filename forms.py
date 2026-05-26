from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, DateField, SelectField, EmailField
from wtforms.validators import DataRequired, length, equal_to
from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed


class registerForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired()])
    password = PasswordField("Enter Password", validators=[DataRequired(), length(min=8, max=12)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), equal_to("password", message="Passwords must match")])
    email = EmailField("Enter Email", validators=[DataRequired()])
    mobile = IntegerField("Enter Mobile Number", validators=[DataRequired()])
    birthdate = DateField("Enter Birth Date", validators=[DataRequired()])
    gender = SelectField("Enter Gender", choices=["Choose Gender","male", "female", "bulki", "lafsha", "shaurma", "karfuri", "jojo", "dr house"])
    country = SelectField(choices=["Choose Country", "Georgia", "USA", "Germany", "Canada"], validators=[DataRequired()])
    image = FileField("Enter Image", validators=[FileRequired(message="Image must be uploaded",), FileSize(1024 * 1024 * 10), FileAllowed(["jpg", "png", "jpeg"])])


class HistoryForm(FlaskForm):
    history_title = StringField("Enter History Title")
    description = StringField("Enter History Description")
    image = FileField("Must Upload Image")
