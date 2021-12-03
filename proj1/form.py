from wtforms import SubmitField, FloatField, Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired


class StudentResponseInputForm(Form):
    master_roll = FileField('Browse for file with all roll no. :', validators=[
                            FileRequired(), FileAllowed(['csv'], 'CSV files only!')])
    response = FileField('Browse for file with all google response:', validators=[
        FileRequired(), FileAllowed(['csv'], 'CSV files only!')])
    corr_marks = FloatField(
        'Enter marks for correct answers :', validators=[DataRequired()])
    wrng_marks = FloatField(
        'Enter marks for incorrect answers :', validators=[DataRequired()])
    generate_ms_btn = SubmitField('Generate roll no wise marksheet')
    con_ms_btn = SubmitField('Generate concise marksheet')
    send_email_btn = SubmitField('Send email')
