import os
import csv
from openpyxl import Workbook

curr_dir = os.getcwd()
f_dir = os.path.join(
    curr_dir, 'output_individual_roll')
f_dir_subno = os.path.join(
    curr_dir, 'output_by_subject')
if not os.path.exists(f_dir):
    os.makedirs(f_dir)
if not os.path.exists(f_dir_subno):
    os.makedirs(f_dir_subno)
# For creating a fresh output of .csv file on each run.
for b in os.listdir('./output_by_subject/'):
    os.remove(os.path.join('./output_by_subject/', b))
for b in os.listdir('./output_individual_roll/'):
    os.remove(os.path.join('./output_individual_roll/', b))


def output_by_subject(name, data_list):   # defining function output by subject
    wkbook = Workbook()
    st = wkbook.active
    for k in data_list:
        st.append(k)
    wkbook.save('./output_by_subject/{}.xlsx'.format(name))


def output_individual_roll(name, data_list):        # defining function output by individual roll no
    wkbook = Workbook()
    st = wkbook.active
    for k in data_list:
        st.append(k)
    wkbook.save('./output_individual_roll/{}.xlsx'.format(name))


rll_done = []
subno_done = []

with open('regtable_old.csv', 'r') as b:
    file_data = list(csv.reader(b))[1:]
    a_ = 0
    for data_list in file_data:
        rollno = data_list[0]
        subno = data_list[3]
        if not rollno in rll_done:
            filtered_data = list(
                filter(lambda x: rollno in x, file_data))
            filtered_data.insert(
                0, ['rollno', 'register_sem', 'schedule_sem', 'subno', 'grade1', 'date_of_entry1', 'grade2', 'date_of_entry2', 'sub_type'])
            data_roll = []
            for p in filtered_data:
                data_roll.append(
                    [p[0], p[1], p[3], p[8]])
            output_individual_roll(rollno, data_roll)
            rll_done.append(rollno)
        if not subno in subno_done:
            filtered_data = list(filter(lambda x: subno in x, file_data))
            filtered_data.insert(
                0, ['rollno', 'register_sem', 'schedule_sem', 'subno', 'grade1', 'date_of_entry1', 'grade2', 'date_of_entry2', 'sub_type'])
            data_sub = []
            for p in filtered_data:
                data_sub.append(
                    [p[0], p[1], p[3], p[8]])
            output_by_subject(subno, data_sub)
            subno_done.append(subno)