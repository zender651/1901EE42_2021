import os

cur_dir = os.getcwd()                       # for folders
final_roll_dir = os.path.join(
    cur_dir, 'output_individual_roll')
final_dir_subno = os.path.join(
    cur_dir, 'output_by_subject')
if not os.path.exists(final_roll_dir):
    os.makedirs(final_roll_dir)
if not os.path.exists(final_dir_subno):
    os.makedirs(final_dir_subno)
    
fl_data = open("regtable_old.csv", "r")           # opening the file

directory = './output_by_subject'             # linking to the directory by subject
for k in os.listdir(directory):
    os.remove(os.path.join(directory, k))


directory = './output_individual_roll'        # linking to the directory by individual roll
for k in os.listdir(directory):
    os.remove(os.path.join(directory, k))

f_read = fl_data.readlines()

for i in f_read[1:]:
    element = i.split(',')
    if not os.path.isfile('./output_individual_roll/{}.csv'.format(element[0])):
        a = open('./output_individual_roll/{}.csv'.format(element[0]), 'a')          
        a.write("rollno,register_sem,subno,sub_type\n")                           

    a = open('./output_individual_roll/{}.csv'.format(element[0]), 'a')
    a.write("{},{},{},{}".format(element[0], element[1], element[3], element[8]))


fl_data = open("regtable_old.csv", "r")                   # opening the file

f_read = fl_data.readlines()

for j in f_read[1:]:
    element = j.split(',')
    if not os.path.isfile('./output_by_subject/{}.csv'.format(element[3])):
        a = open('./output_by_subject/{}.csv'.format(element[3]), 'a')
        a.write("rollno,register_sem,subno,sub_type\n")

    a = open('./output_by_subject/{}.csv'.format(element[3]), 'a')
    a.write("{},{},{},{}".format(element[0], element[1], element[3], element[8]))


fl_data.close()    #closing the file operation