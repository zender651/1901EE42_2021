import os
import csv
from flask import Flask, render_template, request, send_file
from flask_wtf.csrf import CSRFProtect
from flask_mail import *
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
from form import StudentResponseInputForm
import marksheet_creator

# App config
app = Flask(__name__, template_folder='template')
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = '325245hkhf486axcv5719bf9397cbn69xv'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB max-limit.

# Email config
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'gglrspnssender@gmail.com'
app.config['MAIL_PASSWORD'] = 'Pankaj@12345'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = StudentResponseInputForm(
        CombinedMultiDict((request.files, request.form)))
    alert_msg = ''
    colour = 'black'
    if request.method == 'POST' and form.validate():
        mr_file = form.master_roll.data
        r_file = form.response.data
        mr_filename = secure_filename(mr_file.filename)
        r_filename = secure_filename(r_file.filename)
        mr_file_path = os.path.join(os.getcwd(),
                                    'assets', 'input', mr_filename)
        r_file_path = os.path.join(os.getcwd(),
                                   'assets', 'input', r_filename)
        mr_file.save(mr_file_path)
        r_file.save(r_file_path)
        # Generate Roll no. wise Marksheet
        if form.generate_ms_btn.data:
            alert_msg, colour = marksheet_creator.marksheet_creator_run(mr_file_path, r_file_path,
                                                                        form.corr_marks.data, 0-form.wrng_marks.data, 1)
        # Create a concise marksheet.
        if form.con_ms_btn.data:
            alert_msg, colour = marksheet_creator.marksheet_creator_run(mr_file_path, r_file_path,
                                                                        form.corr_marks.data, 0-form.wrng_marks.data, 2)
            p = os.path.join(os.getcwd(), 'assets', 'output',
                             'marksheet', 'concise_marksheet.csv')
            return send_file(p, as_attachment=True)
        # Send Email.
        if form.send_email_btn.data:
            alert_msg, colour = marksheet_creator.send_email_marksheet(mr_file_path, r_file_path,
                                                                       form.corr_marks.data, 0-abs(form.wrng_marks.data))
            try:
                with open('./assets/output/marksheet/concise_marksheet.csv', 'r') as f:
                    c_m_data = list(csv.reader(f))[1:]
                    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    for row in c_m_data:
                        if re.fullmatch(email_regex, row[1]) and re.fullmatch(email_regex, row[4]):
                            mail_body = '''
Dear Student,
Quiz marks (+ve Marks): {}
Marking Scheme: +{} Correct, -{} for wrong.
Attached marksheet with -ve marks for reference.
        '''.format(row[2], form.corr_marks.data, abs(form.wrng_marks.data))
                            msg = Message(subject="Final Quiz Marksheet of Google Response - with Negative", body=mail_body,
                                          sender="gglrspnssender@gmail.com", recipients=[row[1], row[4]])
                            with app.open_resource("./assets/output/marksheet/{}.xlsx".format(row[7].upper())) as fx:
                                msg.attach("{}.xlsx".format(row[7].upper(
                                )), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", fx.read())
                                mail.send(msg)
            except:
                alert_msg, colour = 'Email not sent successfully! Please try again', 'red'
    return render_template('index.html', title='Marksheet - Create marksheet from Google Form Response', form=form, msg=alert_msg, colour=colour)


if __name__ == '__main__':
    app.run(debug=True)
