import re
import os
import shutil 

os.system('cls')

def regex_renamer():     # defining the function for renaming

   
    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    seies_ind = int(input("Enter the number of the web ss that you wish to rename. 1/2/3: "))
    ss_padd = int(input("Enter the Season Number Padding: "))
    ep_padd = int(input("Enter the Episode Number Padding: "))
    series_name = ""
    if seies_ind==1:
        series_name = "Breaking Bad"
    elif seies_ind ==2:
        series_name="Game of Thrones"
    else:
        series_name ="Lucifer"
       
    if series_name=='Breaking Bad':
        ss_files= os.listdir(os.getcwd()+"\\wrong_srt\\"+series_name)
        for ss in ss_files:
            ss_sub= re.split(' ',ss)
            ss_info=re.split('[se]',ss_sub[2])
            newpath=os.getcwd()
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+series_name+"\\"+ss,newpath+"\\corrected_srt\\Breaking Bad\\Breaking Bad - Season "+str('{:' + '0' + '>' + str(ss_padd) + '}').format(ss_info[1])+" Episode "+str('{:' + '0' + '>' + str(ep_padd) + '}').format(ss_info[2])+"."+re.split('\.',ss_sub[3])[3]) 
    
    elif series_name=='Game of Thrones':
        ss_files= os.listdir(os.getcwd()+"\\wrong_srt\\"+series_name)
        for ss in ss_files:
            ss_mains= re.split('.WEB',ss)
            ss_sub=re.split("-",ss_mains[0])
            ss_info=re.split('[x]',ss_sub[1])
            newpath=os.getcwd()
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+series_name+"\\"+ss,newpath+"\\corrected_srt\\Game of Thrones\\Game of Thrones - Season "+str('{:' + '0' + '>' + str(ss_padd) + '}').format(ss_info[0].strip())+" Episode "+str('{:' + '0' + '>' + str(ep_padd) + '}').format(ss_info[1])+"-"+ss_sub[2]+"."+re.split('\.',ss_mains[1])[4])          
    
    elif series_name=='Lucifer':
        ss_files= os.listdir(os.getcwd()+"\\wrong_srt\\"+series_name)
        for ss in ss_files:
            ss_mains= re.split('.HDTV',ss)
            ss_sub=re.split("-",ss_mains[0])
            ss_info=re.split('[x]',ss_sub[1])
            newpath=os.getcwd()+"\\corrected_srt\\Lucifer\\Lucifer - Season "
            shutil.copyfile(os.getcwd()+"\\wrong_srt\\"+series_name+"\\"+ss,newpath+str('{:' + '0' + '>' + str(ss_padd) + '}').format(ss_info[0].strip())+" Episode "+str('{:' + '0' + '>' + str(ep_padd) + '}').format(ss_info[1])+"-"+ss_sub[2]+"."+re.split('\.',ss_mains[1])[3])          

if os.path.isdir("corrected_srt") == 0:
    os.mkdir("corrected_srt")
if os.path.isdir("corrected_srt\Breaking Bad") == 0:
	os.mkdir("corrected_srt\Breaking Bad")	    
if os.path.isdir("corrected_srt\Game of Thrones") == 0:
    os.mkdir("corrected_srt\Game of Thrones")
if os.path.isdir("corrected_srt\Lucifer") == 0:
	os.mkdir("corrected_srt\Lucifer")

            

regex_renamer()