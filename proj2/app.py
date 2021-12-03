import os
from flask import Flask, render_template, request, send_file
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
from form import DataInputForm
import transcript_creator
from PIL import Image

# App config
app = Flask(__name__, template_folder='template')
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = '325245hkhf486axcv5719bf9397cbn69xv'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max-limit.


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DataInputForm(
        CombinedMultiDict((request.files, request.form)))
    alert_msg = ''
    colour = 'black'
    if request.method == 'POST' and form.validate():
        grades_file = form.grades.data
        name_roll_file = form.name_roll.data
        subjects_master_file = form.subjects_master.data
        seal_file = form.seal.data
        sign_file = form.sign.data
        g_filename = secure_filename(grades_file.filename)
        nr_filename = secure_filename(name_roll_file.filename)
        sm_filename = secure_filename(subjects_master_file.filename)
        g_file_path = os.path.join(os.getcwd(),
                                   'assets', 'input', g_filename)
        nr_file_path = os.path.join(os.getcwd(),
                                    'assets', 'input', nr_filename)
        sm_file_path = os.path.join(os.getcwd(),
                                    'assets', 'input', sm_filename)
        seal_file_path = None
        sign_file_path = None
        grades_file.save(g_file_path)
        name_roll_file.save(nr_file_path)
        subjects_master_file.save(sm_file_path)
        # Seal and Sign arrangement (Optional).
        if seal_file:
            seal_filename = secure_filename(seal_file.filename)
            seal_file_path = os.path.join(
                os.getcwd(), 'assets', 'input', seal_filename)
            seal_file.save(seal_file_path)
            seal_image_object = Image.open(seal_file_path)
            seal_image_object = seal_image_object.transpose(
                Image.FLIP_LEFT_RIGHT)
            seal_image_object = seal_image_object.transpose(Image.ROTATE_180)
            seal_image_object.save(seal_file_path)
        if sign_file:
            sign_filename = secure_filename(sign_file.filename)
            sign_file_path = os.path.join(
                os.getcwd(), 'assets', 'input', sign_filename)
            sign_file.save(sign_file_path)
            sign_image_object = Image.open(sign_file_path)
            sign_image_object = sign_image_object.transpose(
                Image.FLIP_LEFT_RIGHT)
            sign_image_object = sign_image_object.transpose(Image.ROTATE_180)
            sign_image_object.save(sign_file_path)
        rollno_range = form.rollno_range.data
        rollno_arr = rollno_range.split('-')
        rollno_arr.sort()
        rollno_arr = [roll.upper() for roll in rollno_arr]
        rollno_arr = [roll.strip() for roll in rollno_arr]
        alert_msg, colour = transcript_creator.create_transcript_data(
            rollno_arr, g_file_path, nr_file_path, sm_file_path, seal_file_path, sign_file_path)
        print(alert_msg)
    return render_template('index.html', title='Transcript Generator - Create transcripts', form=form, msg=alert_msg, colour=colour)


if __name__ == '__main__':
    app.run(debug=True)
