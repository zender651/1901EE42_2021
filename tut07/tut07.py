import os
os.system("cls")
import pandas as pd
import re

def check_rlno(rno):
	return re.match(r"\d{4}\w{2}\d{2}",rno)
 
 
def gt_lec(string_ltp):
	ltp = string_ltp.split('-')
	return ltp

def get_flist(crse_taken):
	list_sn = set()
	for ind, row in crse_taken.iterrows():
		course = row["subno"]
		if check_rlno(row["rollno"]):
			if course not in course_ltp:
				print("Not found...")
			if course_ltp[course][0] != "0":
				list_sn.add((row["rollno"],row["subno"],"1"))
			if course_ltp[course][1] != "0":
				list_sn.add((row["rollno"],row["subno"],"2"))
			if course_ltp[course][2] != "0":
				list_sn.add((row["rollno"],row["subno"],"3"))

	return list_sn


def gt_list_com (fd_info):
	list_sn = set()
	for ind, row in fd_info.iterrows():
		if check_rlno(row["stud_roll"]):
			list_sn.add((row["stud_roll"],row["course_code"],str(row["feedback_type"])))
	return list_sn


fd_info = pd.read_csv("course_feedback_submitted_by_students.csv")
course_master = pd.read_csv("course_master_dont_open_in_excel.csv")
student_info = pd.read_csv("studentinfo.csv")
crse_taken = pd.read_csv("course_registered_by_all_students.csv")
output_file = pd.DataFrame(columns = ["Roll Number","Registered Sem","Scheduled Sem","Course Code","Name","Email","AEmail","Contact"])

sch_sem = {}

for ind,row in crse_taken.iterrows():
	if check_rlno(row["rollno"]):
		#sch_sem[row["rollno"]] = {}
		#print(row)
		if row["rollno"] not in sch_sem:
			sch_sem[row["rollno"]] = {}

		sch_sem[row["rollno"]][row["subno"]] = (row["register_sem"],row["schedule_sem"])
		#sch_sem[row["rollno"][row["subno"]]] = 5

course_ltp = {}

for ind, row in course_master.iterrows():
	course_ltp[row["subno"]] = gt_lec(row["ltp"])

fl_list = get_flist(crse_taken)


stud_info = {}

for ind,row in student_info.iterrows():
	stud_info[row["Roll No"]] = {}
	stud_info[row["Roll No"]] = row

compl_list = gt_list_com(fd_info)


fl_list = fl_list | compl_list
rem_list = compl_list ^ fl_list

for rcrd in rem_list:
	rno = rcrd[0]
	course = rcrd[1]
	feed_type = rcrd[2]
	reg_sem = sch_sem[rno][course][0]
	sched_sem = sch_sem[rno][course][1]
	if rno in stud_info:
		name = stud_info[rno]["Name"]
		mail = stud_info[rno]["email"]
		amail = stud_info[rno]["aemail"]
		contact = stud_info[rno]["contact"]
		new_row = {"Roll Number":rno, "Registered Sem":reg_sem,"Scheduled Sem":sched_sem,"Course Code":course,"Email":mail,"AEmail":amail,"Contact":contact,"Name":name};
		output_file = output_file.append(new_row,ignore_index=True)


output_file.to_excel("course_feedback_remaining.xlsx",index=False)