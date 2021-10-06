import csv 
import os

grades = {}               
roll_names = {}
subjects_master = {}


roll_file = open("names-roll.csv", 'r')                # opening the files in read view
subjectm_file = open("subjects_master.csv", 'r')

reader1 = csv.DictReader(roll_file)                    #  read data with reader.
for row in reader1:
  roll_names[row['Roll']] = row['Name']

reader2 = csv.DictReader(subjectm_file)                   #  read data with reader.
for row in reader2:
  subjects_master[row['subno']] = [row['subname'],row['ltp'],row['crd']]

grades_file = open("grades.csv", 'r')
csvreader3 = csv.DictReader(grades_file)
for row in csvreader3:
  if not row['Roll'] in grades.keys():
    grades[row['Roll']] = {}
    if row['Sem'] not in grades[row['Roll']].keys():
      grades[row['Roll']][row['Sem']] = [[ row['SubCode'],
                                    subjects_master[row['SubCode']][0],
                                    subjects_master[row['SubCode']][1],
                                    subjects_master[row['SubCode']][2],
                                    row['Sub_Type'],
                                    row['Grade']]]
    else:
       grades[row['Roll']][row['Sem']].append([ row['SubCode'],
                                    subjects_master[row['SubCode']][0],
                                    subjects_master[row['SubCode']][1],
                                    subjects_master[row['SubCode']][2],
                                    row['Sub_Type'],
                                    row['Grade']])
  else:
    if row['Sem'] not in grades[row['Roll']].keys():
      grades[row['Roll']][row['Sem']] = [[ row['SubCode'],
                                    subjects_master[row['SubCode']][0],
                                    subjects_master[row['SubCode']][1],
                                    subjects_master[row['SubCode']][2],
                                    row['Sub_Type'],
                                    row['Grade']]]
    else:
       grades[row['Roll']][row['Sem']].append([ row['SubCode'],
                                    subjects_master[row['SubCode']][0],
                                    subjects_master[row['SubCode']][1],
                                    subjects_master[row['SubCode']][2],
                                    row['Sub_Type'],
                                    row['Grade']])


from openpyxl.workbook import Workbook


grade_rating = {'BB': 8, 'BC': 7, 'AB' : 9, 'CC' : 6, 'AA' : 10, 'CD' : 5, 'DD' : 4, 'F' : 0, 'F*' : 0, 'DD*' : 4, ' BB' : 8}
for roll in grades.keys():
  all_total = []
  all_total.append(['Roll No.', roll])
  all_total.append(['Name of the Student',roll_names[roll]])
  all_total.append(['Discipline',roll[4:6]])
  sem_no = ['Semester No.']
  per_sem_credit = ['Semester wise Credit Taken']
  spi = ['SPI']
  total_credits = ['Total Credits Taken']
  cpi = ['CPI']

  fpth = 'output/' + roll + '.xlsx'
  dir = os.path.dirname(fpth)

  if not os.path.exists(dir):
    os.makedirs(dir)

  
  wbook = Workbook()
  
  for sem in grades[roll].keys():
    sem_no.append(sem)
    no = 1 
    credit_no = 0
    spi_no = 0 
    wsheet = wbook.create_sheet()
    wsheet.title = 'Sem' + sem
    wsheet.append(['Sl No.','Subject Name','L-T-P','Credit','Subject Type','Grade'])
    
    
    for data in grades[roll][sem]:
      spi_no += int(data[3]) * grade_rating[data[5]]
      credit_no += int(data[3]) 
      data.insert(0,no)
      wsheet.append(data)
      no += 1

      
      
    per_sem_credit.append(credit_no)
    spi.append(round(spi_no/credit_no,2))

    if type(total_credits[-1]) == str:
      total_credits.append(credit_no)
    else:
      a = credit_no
      a += total_credits[-1] + credit_no
      total_credits.append(a)
    

  all_total.append(sem_no)
  all_total.append(per_sem_credit)
  all_total.append(spi)
  all_total.append(total_credits)
  wsheet = wbook['Sheet']
  for row in all_total:
    wsheet.append(row)
  wbook.save(filename=fpth)
