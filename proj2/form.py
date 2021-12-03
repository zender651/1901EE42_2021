from wtforms import SubmitField, Form, StringField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired


class DataInputForm(Form):
    rollno_range = StringField('Enter range of Roll No. (separate roll with "-"):',
                               validators=[DataRequired()])
    grades = FileField('Browse for file with grades:', validators=[
        FileRequired(), FileAllowed(['csv'], 'CSV files only!')])
    name_roll = FileField('Browse for file with name and roll no.:', validators=[
        FileRequired(), FileAllowed(['csv'], 'CSV files only!')])
    subjects_master = FileField('Browse for file with subjects data:', validators=[
        FileRequired(), FileAllowed(['csv'], 'CSV files only!')])
    seal = FileField('Browse for seal image:', validators=[
        FileAllowed(['png', 'jpg', 'jpeg'], 'Image files only!')])
    sign = FileField('Browse for signature image:', validators=[
        FileAllowed(['png', 'jpg', 'jpeg'], 'Image files only!')])
    generate_trans = SubmitField('Generate transcript')
