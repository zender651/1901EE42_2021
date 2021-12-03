import os
import csv
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, TableStyle, Table
from reportlab.lib.pagesizes import landscape, A3, A4
from reportlab.lib import colors

current_directory = os.getcwd()
input_dir = os.path.join(
    current_directory, 'assets', 'input')
if not os.path.exists(input_dir):
    os.makedirs(input_dir)
ouptut_dir = os.path.join(
    current_directory, 'assets', 'output', 'transcriptsIITP')
if not os.path.exists(ouptut_dir):
    os.makedirs(ouptut_dir)
for f in os.listdir(input_dir):
    os.remove(os.path.join(input_dir, f))
for f in os.listdir(ouptut_dir):
    os.remove(os.path.join(ouptut_dir, f))

# Output generation function.


def pdf_creator(stud_data, seal_loc, sign_loc):
    now = datetime.datetime.now()
    for data in stud_data:
        student_info_data = [['Programme:', format(data[1]['Programme']),
                              'Course:', format(data[1]['Course']), '', ''],
                             ['RollNo.:', format(data[1]['Roll No.']),  'Name:', format(
                                 data[1]['Name']),  'Year of Admission:', format(data[1]['Year of Admission'])],
                             ]
        if data[1]['Code'] == '01':
            # A3 Page ,i.e, with semester more than 4.
            pdf = canvas.Canvas('./assets/output/transcriptsIITP/{}.pdf'.format(
                data[1]['Roll No.']), bottomup=0, pagesize=landscape(A3))
            styles = getSampleStyleSheet()
            pdf.rect(15, 18, width=1165, height=800, stroke=1, fill=0)
            pdf.rect(280, 18, width=650, height=120, stroke=1, fill=0)
            pdf.rect(15, 138, width=1165, height=295, stroke=1, fill=0)
            pdf.rect(15, 433, width=1165, height=235, stroke=1, fill=0)
            pdf.drawImage('./logo.png', 80, 10, 140, 140,
                          mask='auto', preserveAspectRatio=True)
            pdf.drawImage('./logo.png', 1000, 10, 140, 140,
                          mask='auto', preserveAspectRatio=True)
            pdf.drawImage('./banner.png', 310, 18, 600,
                          120, preserveAspectRatio=True)
            # Student Info Block
            t = Table(student_info_data)
            t.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 1,
                                    colors.black), ('FONTSIZE', (0, 0), (-1, -1), 12), ('FONTNAME', (2, 0), (2, -1), 'Times-Bold'),  ('FONTNAME', (4, 0), (4, -1), 'Times-Bold'),  ('FONTNAME', (0, 0), (0, -1), 'Times-Bold'), ('BOTTOMPADDING', (0, 0), (-1, -1), 14), ('TOPPADDING', (0, 0), (-1, -1), 0)]))
            t.wrapOn(pdf, 680, 70)
            t.drawOn(pdf, 285, 148)
            # Marksheet Table
            x1 = 25
            x2 = 25
            y = 0
            for i, sem_data in enumerate(data[0].values()):
                if x1 <= 1000:
                    text = "<u>Semester {}</u>".format(
                        data[1]['Semester No.'][i])
                    para = Paragraph(text, style=styles["Heading4"])
                    para.wrapOn(pdf, 100, 0)
                    para.drawOn(pdf, x1, 224+y)
                    sem_data.reverse()
                    sem_t = Table(sem_data)
                    sem_t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                               ('FONTSIZE', (0, 0), (-1, -1), 5.6), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'), ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0), ('LEFTPADDING', (0, 0), (-1, -1), 2), ('RIGHTPADDING', (0, 0), (-1, -1), 2)]))
                    sem_t.wrapOn(pdf, 0, 0)
                    sem_t.drawOn(pdf, x1, 230+y)
                    summ_data = [['Credits Taken:', data[1]['Credits Taken'][i], 'Credits Cleared:',
                                  data[1]['Credits Taken'][i], 'SPI:', data[1]['SPI'][i], 'CPI:', data[1]['CPI'][i]]]
                    summ_table = Table(summ_data)
                    summ_table.setStyle(
                        [('BOX', (0, 0), (-1, 0), 1, colors.black), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 6.5), ('BOTTOMPADDING', (0, 0), (-1, 0), 6), ('TOPPADDING', (0, 0), (-1, 0), 0)])
                    summ_table.wrapOn(pdf, 0, 0)
                    summ_table.drawOn(pdf, x1, 380+y)
                    x1 = x1+295
                else:
                    y = 230
                    text = "<u>Semester {}</u>".format(
                        data[1]['Semester No.'][i])
                    para = Paragraph(text, style=styles["Heading4"])
                    para.wrapOn(pdf, 100, 0)
                    para.drawOn(pdf, x2, 224+y)
                    sem_data.reverse()
                    sem_t = Table(sem_data)
                    sem_t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                               ('FONTSIZE', (0, 0), (-1, -1), 4.6), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'), ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0), ('LEFTPADDING', (0, 0), (-1, -1), 2), ('RIGHTPADDING', (0, 0), (-1, -1), 2)]))
                    sem_t.wrapOn(pdf, 0, 0)
                    sem_t.drawOn(pdf, x2, 230+y)
                    summ_data = [['Credits Taken:', data[1]['Credits Taken'][i], 'Credits Cleared:',
                                  data[1]['Credits Taken'][i], 'SPI:', data[1]['SPI'][i], 'CPI:', data[1]['CPI'][i]]]
                    summ_table = Table(summ_data)
                    summ_table.setStyle(
                        [('BOX', (0, 0), (-1, 0), 1, colors.black), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 6.5), ('BOTTOMPADDING', (0, 0), (-1, 0), 6), ('TOPPADDING', (0, 0), (-1, 0), 0)])
                    summ_table.wrapOn(pdf, 0, 0)
                    summ_table.drawOn(pdf, x2, 380+y)
                    x2 = x2+290
            pdf.setFont('Helvetica', 16)
            pdf.drawString(100, 750, 'Date Generated:')
            pdf.drawString(240, 750, now.strftime("%d %b %Y %H:%M"))
            pdf.line(230, 755, 400, 755)
            pdf.drawImage(seal_loc, 560, 680, 120,
                          120, mask='auto', preserveAspectRatio=True)
            pdf.drawImage(sign_loc, 920, 670, 120,
                          120, mask='auto', preserveAspectRatio=True)
            pdf.line(900, 755, 1110, 755)
            pdf.drawString(900, 775, 'Assistant Registrar(Academic)')
        else:
            # A4 Page ,i.e, with semester less than 4.
            pdf = canvas.Canvas('./assets/output/transcriptsIITP/{}.pdf'.format(
                data[1]['Roll No.']), bottomup=0, pagesize=landscape(A4))
            styles = getSampleStyleSheet()
            pdf.rect(10, 15, width=820, height=570, stroke=1, fill=0)
            pdf.rect(190, 15, width=460, height=100, stroke=1, fill=0)
            pdf.rect(10, 115, width=820, height=205, stroke=1, fill=0)
            pdf.rect(10, 320, width=820, height=165, stroke=1, fill=0)
            pdf.drawImage('logo.png', 50, 10, 100, 100,
                          mask='auto', preserveAspectRatio=True)
            pdf.drawImage('logo.png', 700, 10, 100, 100,
                          mask='auto', preserveAspectRatio=True)
            pdf.drawImage('banner.png', 210, 10, 400,
                          120, preserveAspectRatio=True)
            t = Table(student_info_data)
            t.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 1,
                                    colors.black), ('FONTSIZE', (0, 0), (-1, -1), 8), ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),  ('FONTNAME', (4, 0), (4, -1), 'Helvetica-Bold'),  ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'), ('BOTTOMPADDING', (0, 0), (-1, -1), 8), ('TOPPADDING', (0, 0), (-1, -1), 0)]))
            t.wrapOn(pdf, 680, 70)
            t.drawOn(pdf, 195, 120)
            # Marksheet Table
            x1 = 30
            x2 = 30
            y = 0
            for i, sem_data in enumerate(data[0].values()):
                if x1 <= 890:
                    text = "<u>Semester {}</u>".format(
                        data[1]['Semester No.'][i])
                    para = Paragraph(text, style=styles["Heading4"])
                    para.wrapOn(pdf, 100, 0)
                    para.drawOn(pdf, x1, 175+y)
                    sem_data.reverse()
                    sem_t = Table(sem_data)
                    sem_t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                               ('FONTSIZE', (0, 0), (-1, -1), 7), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'), ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 0), (-1, -1), 1), ('TOPPADDING', (0, 0), (-1, -1), 0)]))
                    sem_t.wrapOn(pdf, 0, 0)
                    sem_t.drawOn(pdf, x1, 180+y)
                    summ_data = [['Credits Taken:', data[1]['Credits Taken'][i], 'Credits Cleared:',
                                  data[1]['Credits Taken'][i], 'SPI:', data[1]['SPI'][i], 'CPI:', data[1]['CPI'][i]]]
                    summ_table = Table(summ_data)
                    summ_table.setStyle(
                        [('BOX', (0, 0), (-1, 0), 1, colors.black), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 5), ('BOTTOMPADDING', (0, 0), (-1, 0), 2), ('TOPPADDING', (0, 0), (-1, 0), 0)])
                    summ_table.wrapOn(pdf, 0, 0)
                    summ_table.drawOn(pdf, x1, 300+y)
                    x1 = x1+410
                else:
                    y = 160
                    text = "<u>Semester {}</u>".format(
                        data[1]['Semester No.'][i])
                    para = Paragraph(text, style=styles["Heading4"])
                    para.wrapOn(pdf, 100, 0)
                    para.drawOn(pdf, x2, 175+y)
                    sem_data.reverse()
                    sem_t = Table(sem_data)
                    sem_t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                               ('FONTSIZE', (0, 0), (-1, -1), 7), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'), ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 0), (-1, -1), 1), ('TOPPADDING', (0, 0), (-1, -1), 0)]))
                    sem_t.wrapOn(pdf, 0, 0)
                    sem_t.drawOn(pdf, x2, 180+y)
                    summ_data = [['Credits Taken:', data[1]['Credits Taken'][i], 'Credits Cleared:',
                                  data[1]['Credits Taken'][i], 'SPI:', data[1]['SPI'][i], 'CPI:', data[1]['CPI'][i]]]
                    summ_table = Table(summ_data)
                    summ_table.setStyle(
                        [('BOX', (0, 0), (-1, 0), 1, colors.black), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 5), ('BOTTOMPADDING', (0, 0), (-1, 0), 2), ('TOPPADDING', (0, 0), (-1, 0), 0)])
                    summ_table.wrapOn(pdf, 0, 0)
                    summ_table.drawOn(pdf, x2, 300+y)
                    x2 = x2+410
            pdf.setFont('Helvetica', 12)
            pdf.drawString(100, 540, 'Date Generated:')
            pdf.drawString(205, 540, now.strftime("%d %b %Y %H:%M"))
            pdf.line(200, 545, 320, 545)
            pdf.drawImage(seal_loc, 380, 500, 80,
                          80, mask='auto', preserveAspectRatio=True)
            pdf.drawImage(sign_loc, 610, 490, 80,
                          80, mask='auto', preserveAspectRatio=True)
            pdf.drawString(600, 555, 'Assistant Registrar(Academic)')
            pdf.line(580, 540, 770, 540)
        # offset time of 1 minute.
        offset_time = datetime.timedelta(minutes=1)
        now += offset_time
        pdf.save()


    # Labels and initials.
marksheet_label = ['Sl No.', 'Subject No.', 'Subject Name',
                   'L-T-P', 'Credit', 'Subject Type', 'Grade']
roll_done = []
grade_vs_crd = {
    'AA': 10, 'AB': 9, 'BB': 8, 'BC': 7, 'CC': 6, 'CD': 5, 'DD': 4, 'F': 0, 'I': 0, 'AA*': 10, 'AB*': 9, 'BB*': 8, 'BC*': 7, 'CC*': 6, 'CD*': 5, 'DD*': 4, 'F*': 0, 'I*': 0
}
code_vs_programme = {'01': 'Bachelor of Technology',
                     '11': 'Masters in Technology', '12': 'Master of Science', '21': 'Doctor of Philosophy'}
code_vs_course = {
    'CS': 'Computer Science and Engineering',
    'EE': 'Electrical Engineering',
    'ME': 'Mechanical Engineering'
}


# Main logic


def create_transcript_data(rollno_arr, grade_loc, name_roll_loc, subjects_master_loc, seal_loc=None, sign_loc=None):
    try:
        with open(grade_loc, 'r') as f1, open(name_roll_loc, 'r') as f2, open(subjects_master_loc, 'r') as f3:
            # Data from files and marksheet genration in list form.
            grades_data = list(csv.reader(f1))[1:]
            names_roll_data = list(csv.reader(f2))[1:]
            subjects_master_data = list(csv.reader(f3))[1:]
            req_rollno = [[el[0], el[1]] for el in names_roll_data if el[0]
                          >= rollno_arr[0] and el[0] <= rollno_arr[1]]
            no_req_rollno = []
            no_req_rollno_str = ''
            if len(req_rollno):
                studs_data = []
                for names_roll_data_list in req_rollno:
                    stud_data = []
                    rollno = names_roll_data_list[0]
                    spi = []
                    data = {}
                    filtered_data = list(
                        filter(lambda x: rollno in x, grades_data))
                    no_of_sem = list({int(el[1]) for el in filtered_data})
                    for i in no_of_sem:
                        k = str(i)
                        data[k] = []
                        data[k].append(marksheet_label)
                        sem_filtered_data = list(
                            filter(lambda x: k == x[1], filtered_data))
                        sub_filtered_data = []
                        for el in sem_filtered_data:
                            sub_filtered_data.extend(
                                list(filter(lambda x: el[2] == x[0], subjects_master_data)))
                        for i in range(len(sub_filtered_data)):
                            temp = []
                            temp.append(str(i+1))
                            temp.extend(sub_filtered_data[i][0:])
                            temp.append(sem_filtered_data[i][-1])
                            temp.append(sem_filtered_data[i][-2])
                            data[k].append(temp)
                    for el in data.values():
                        d = el[1:]
                        sum = 0
                        for i in d:
                            sum += int(i[4]) * grade_vs_crd[i[6].strip()]
                        spi.append(sum)
                    stud_data.append(data)
                    data = {}
                    data['Roll No.'] = rollno
                    data['Name'] = names_roll_data_list[1]
                    data['Year of Admission'] = '20{}'.format(rollno[0: 2])
                    data['Programme'] = code_vs_programme[rollno[2: 4]]
                    data['Code'] = rollno[2: 4]
                    data['Course'] = code_vs_course[rollno[4: 6]]
                    data['Semester No.'] = no_of_sem.copy()
                    data['Credits Taken'] = [0]*len(no_of_sem)
                    data['SPI'] = [0]*len(no_of_sem)
                    data['Total Credits Taken'] = [0]*len(no_of_sem)
                    data['CPI'] = [0]*len(no_of_sem)
                    for el in filtered_data:
                        idx = data['Semester No.'].index(int(el[1]))
                        data['Credits Taken'][idx] += int(el[3])
                    for el in spi:
                        data['SPI'][spi.index(el)] = float('{0:.2f}'.format(
                            el / data['Credits Taken'][spi.index(el)]))
                    for i in range(len(data['Credits Taken'])):
                        if i == 0:
                            data['Total Credits Taken'][i] = data['Credits Taken'][i]
                        else:
                            data['Total Credits Taken'][i] = data['Total Credits Taken'][i -
                                                                                         1] + data['Credits Taken'][i]
                    for i in range(len(data['SPI'])):
                        sum = 0
                        for j in range(i+1):
                            sum += data['SPI'][j] * \
                                float(data['Credits Taken'][j])
                        data['CPI'][i] = float('{:.2f}'.format(
                            sum/data['Total Credits Taken'][i]))
                    stud_data.append(data)
                    studs_data.append(stud_data)
                # Calling function to generate pdf from data in list form
                pdf_creator(studs_data, seal_loc, sign_loc)
                diff = int(rollno_arr[-1][6:])-int(req_rollno[-1][0][6:])
                for i in range(diff):
                    r = int(req_rollno[-1][0][6:]) + i + 1
                    if r % 10 == r:
                        no_req_rollno.append(
                            req_rollno[-1][0][:6]+'0'+'{}'.format(r))
                    else:
                        no_req_rollno.append(
                            req_rollno[-1][0][:6]+'{}'.format(r))
                no_req_rollno_str = ', '.join(no_req_rollno)
                return 'Transcript generated successfully! ' + no_req_rollno_str, 'green'
            else:
                diff = int(rollno_arr[-1][6:])-int(rollno_arr[0][6:])
                for i in range(diff+1):
                    r = int(rollno_arr[0][6:]) + i
                    if r % 10 == r:
                        no_req_rollno.append(
                            rollno_arr[0][:6]+'0'+'{}'.format(r))
                    else:
                        no_req_rollno.append(
                            rollno_arr[0][:6]+'{}'.format(r))
                no_req_rollno_str = ', '.join(no_req_rollno)
                return 'No data found!! ' + no_req_rollno_str, 'red'
    except:
        return 'Something went wrong! Please try again.', 'red'


# rollno_range = '0401CS30-0401CS50'
# rollno_arr = rollno_range.split('-')
# rollno_arr.sort()
# rollno_arr = [roll.upper() for roll in rollno_arr]
# rollno_arr = [roll.strip() for roll in rollno_arr]
# print(create_transcript_data(rollno_arr, './files_for_testing/grades.csv',
#                              './files_for_testing/names-roll.csv', './files_for_testing/subjects_master.csv'))
