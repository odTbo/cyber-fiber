from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, URL, Email


class RegisterForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    # date_of_birth = DateField("Date of Birth", format='%m/%d/%Y')
    age = StringField("Age", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class CreatePostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    body = TextAreaField("Content", validators=[DataRequired()], id="FormPostBody")
    submit = SubmitField("Submit")
