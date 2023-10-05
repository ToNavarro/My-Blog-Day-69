from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired("Required Field.")])
    subtitle = StringField("Subtitle", validators=[DataRequired("Required Field.")])
    img_url = StringField("Blog Image URL", validators=[DataRequired("Required Field."), URL("Not a valid URL.")])
    body = CKEditorField("Blog Content", validators=[DataRequired("Required Field.")])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Required Field."), Email(message="Not a valid email.")])
    password = PasswordField("Password", validators=[DataRequired("Required Field."), Length(min=8, message="Password must be at least 8 char long.")])
    name = StringField("Name", validators=[DataRequired("Required Field.")])
    submit = SubmitField("SIGN ME UP!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Required Field.")])
    password = PasswordField("Password", validators=[DataRequired("Required Field.")])
    submit = SubmitField("LET ME IN!")


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired("Required Field.")])
    submit = SubmitField("SUBMIT COMMENT")
