# required libraries:
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from csv import DictWriter
import os

window = tk.Tk()
window.title('Student\'s Information')


#labelframe part:
part0 = ttk.Labelframe(window)
part0.grid(row=0, columnspan=5, padx=10, pady=10)

part1 = ttk.LabelFrame(window, text='Student\'s Basic Information')
part1.grid(row=2, column=0, padx=50, pady=10)

part2 = ttk.LabelFrame(window, text='More Information')
part2.grid(row=2, column=1, padx=50, pady=10)

part3 = ttk.LabelFrame(window)
part3.grid(row=3, column=0, padx=50, pady=10, sticky=tk.W)


# Load the image
logo_image = tk.PhotoImage(file="C:/Users/tohid/Desktop/Python Project/Hohai.png")


#heading part:
logo_label = ttk.Label(part0, image=logo_image)
logo_label.grid(row=0, column=1, padx=140)

heading1 = ttk.Label(part0, text='河海大学', font=('helvetica',25,'bold'))
heading1.grid(row=1, column=1, padx=45, pady=10)
heading1.configure(foreground='Blue')

heading = ttk.Label(part0, text='Welcome to the International College', font=('helvetica',20))
heading.grid(row=2, column=1, padx=45, pady=10)
heading.configure(foreground='Blue')


#label part (labelframe 1):
name_label = ttk.Label(part1, text='Name: ', font=('helvetica',14))
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

nationality_label = ttk.Label(part1, text='Country: ', font=('helvetica',14))
nationality_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

age_label = ttk.Label(part1, text='Age: ', font=('helvetica',14))
age_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

gender_label = ttk.Label(part1, text='Select Gender : ', font=('helvetica',14))
gender_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
 
passport_label = ttk.Label(part1, text='Give your passport no : ', font=('helvetica',14))
passport_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)


#Entrybox part(labelframe1):
name_var = tk.StringVar()
name_box = ttk.Entry(part1, width=50, textvariable=name_var)
name_box.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
name_box.focus()

nationality_var = tk.StringVar()
nationality_box = ttk.Entry(part1, width=50, textvariable=nationality_var)
nationality_box.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

age_var = tk.StringVar()
age_box = ttk.Entry(part1, width=10, textvariable=age_var)
age_box.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

#gender radiobutton(labelframe1):
gender_var = tk.StringVar()
male_rbtn = ttk.Radiobutton(part1, text='Male', value='Male', variable=gender_var)
male_rbtn.grid(row=3, column=1, padx=10, pady=20, sticky=tk.W)

female_rbtn = ttk.Radiobutton(part1, text='Female', value='Female', variable=gender_var)
female_rbtn.grid(row=3, column=1, padx=10, pady=20)

others_rbtn = ttk.Radiobutton(part1, text='Others', value='Others', variable=gender_var)
others_rbtn.grid(row=3, column=1, padx=10, pady=20, sticky=tk.E)

passport_var = tk.StringVar()
passport_box = ttk.Entry(part1, width=25,textvariable=passport_var)
passport_box.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

year_label = ttk.Label(part1, text='Year', font=('helvetica',12))
year_label.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

month_label = ttk.Label(part1, text='Month', font=('helvetica',12))
month_label.grid(row=5, column=1, padx=10, pady=5)

day_label = ttk.Label(part1, text='Day', font=('helvetica',12))
day_label.grid(row=5, column=1, padx=10, pady=5, sticky=tk.E)

birth_label = ttk.Label(part1, text='Date of Birth: ', font=('helvetica',14))
birth_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)


#Year,Month,Day combobox create:
year_var = tk.StringVar()
year_combobox = ttk.Combobox(part1, width=7, textvariable=year_var, state='readonly')
year_combobox['values'] = tuple(range(1980,2010))
year_combobox.current(0)
year_combobox.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

month_var = tk.StringVar()
month_combobox = ttk.Combobox(part1, width=10, textvariable=month_var, state='readonly')
month_combobox['values'] = ('January','February','March','April','May','June','July','August','September','October','November','December')
month_combobox.current(0)
month_combobox.grid(row=6,column=1,padx=10,pady=5)

day_var = tk.StringVar()
day_combobox = ttk.Combobox(part1, width=3, textvariable=day_var, state='readonly')
day_combobox['values'] = tuple(range(1,32))
day_combobox.current(0)
day_combobox.grid(row=6, column=1, padx=10, pady=5, sticky=tk.E)


#Entrybox part(labelframe2):
father_var = tk.StringVar()
father_box = ttk.Entry(part2, width=50, textvariable=father_var)
father_box.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

mother_var = tk.StringVar()
mother_box = ttk.Entry(part2, width=50, textvariable=mother_var)
mother_box.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

degree_var = tk.StringVar()
degree_combobox = ttk.Combobox(part2, width=20, textvariable=degree_var, state='readonly')
degree_combobox['values'] = ('Bachelor', 'Master', 'PhD', 'Non-Degree Program')
degree_combobox.current(0)
degree_combobox.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

major_var = tk.StringVar()
major_box = ttk.Entry(part2, width=50, textvariable=major_var)
major_box.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

room_var = tk.StringVar()
room_box = ttk.Entry(part2, width=10, textvariable=room_var)
room_box.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

counselor_var = tk.StringVar()
counselor_combobox = ttk.Combobox(part2, width=20, textvariable=counselor_var, state='readonly')
counselor_combobox['values'] = ('Ms. Catherine YANG', 'Ms. Joyce XU', 'Mr. David YING', 'Ms. Lea LI')
counselor_combobox.current(0)
counselor_combobox.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)


#more info part(labelframe2):
father_label = ttk.Label(part2, text='Father\'s Name: ', font=('helvetica',14))
father_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

mother_label = ttk.Label(part2, text='Mother\'s Name: ', font=('helvetica',14))
mother_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

degree_label = ttk.Label(part2, text='Degree : ', font=('helvetica',14))
degree_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

major_label = ttk.Label(part2, text='Study Major: ', font=('helvetica',14))
major_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

roomnumber_label = ttk.Label(part2, text='Room Number: ', font=('helvetica',14))
roomnumber_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

counselor_label = ttk.Label(part2,text='Counselor\'s Name: ', font=('helvetica',14))
counselor_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)


#checkbtn create:
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(part3, text='I have checked all of my information carefully', variable=checkbtn_var)
checkbtn.grid(row=0, column=0)


#function define and csv file create:
def action():
    name = name_var.get()
    country = nationality_var.get()
    age = age_var.get()
    father_name = father_var.get()
    mother_name = mother_var.get()
    gender = gender_var.get()
    passport_no = passport_var.get()
    degree = degree_var.get()
    major = major_var.get()
    B_Year = year_var.get()
    B_Month = month_var.get()
    B_Day = day_var.get()
    room = room_var.get()
    counselor = counselor_var.get()
    if checkbtn_var.get() == 0:
        condition = 'No'
    else:
        condition = 'Yes'
    

    #messagebox:
    if name == '' or country == '' or age =='' or father_name == '' or mother_name == '' or passport_no == '' or room == '':
        m_box.showerror('Input Warning','Please fill all the information!!!')
   
    else:
        try:
            age = int(age)
            room = int(room)
        except ValueError:
            m_box.showerror('Value error','Please fill age and room numbers as number!!!')
        else:
            m_box.showinfo('Message','You have successfully submitted!!!')

        #csv file create:
        with open ('student_data.csv','a',newline='') as f:
            dict_writer = DictWriter(f, fieldnames=['Stud_Name','Stud_Age','Stud_Country','Father\'s_Name','Mothers\'s_Name','Stud_Gender','Stud_Passport','Degree','Stud_Major','Stud_DOB','Room_No','Counselor','Checked'])
            if os.stat('student_data.csv').st_size == 0:
                dict_writer.writeheader()
            dict_writer.writerow({
                'Stud_Name' : name,
                'Stud_Country' : country,
                'Stud_Age' : age, 
                'Father\'s_Name' : father_name,
                'Mothers\'s_Name' : mother_name,
                'Stud_Gender' : gender,
                'Stud_Passport' : passport_no,
                'Degree' : degree,
                'Stud_Major' : major,
                'Stud_DOB' : [B_Year, B_Month, B_Day],
                'Room_No' : room,
                'Counselor' : counselor,
                'Checked' : condition
            })

    #pop part:
    name_box.delete(0,tk.END)
    nationality_box.delete(0,tk.END)
    age_box.delete(0,tk.END)
    father_box.delete(0,tk.END)
    mother_box.delete(0,tk.END)
    passport_box.delete(0,tk.END)
    room_box.delete(0,tk.END)
    major_box.delete(0,tk.END)
    

#submit button:
submit_btn = ttk.Button(window,text='Submit',command=action)
submit_btn.grid(row=3,column=1,padx=70,sticky=tk.E)

window.mainloop()