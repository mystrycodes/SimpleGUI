# starter code
import os
from csv import DictWriter
import tkinter as tk
from tkinter import W, ttk
win=tk.Tk()
win.title("GUI")

#creating labels
# widgets buttons,labels,-- tk,ttk
name_label=ttk.Label(win, text="Enter your name: ")#creates a label
name_label.grid(row=0,column=0,sticky=tk.W)#positioning the label pack(places in exact top center),grid

email_label=ttk.Label(win,text="Enter your email: ")
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text="Enter your age: ")
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text="Select your gender: ")
gender_label.grid(row=3,column=0,sticky=tk.W)

#creating entrybox
name_var=tk.StringVar()
name_entrybox = ttk.Entry(win, width=18 ,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var=tk.StringVar()
email_entrybox= ttk.Entry(win, width=18, textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=18,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

#Creating combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=15,textvariable=gender_var,state='readonly')
gender_combobox['values']=("Male",'Female',"Other")
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

#Creating radio buttons
usertype= tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text="Student",value="Student",variable=usertype)
radiobtn1.grid(row=4,column=0,sticky=tk.W)
radiobtn2=ttk.Radiobutton(win,text="Teacher",value="Teacher",variable=usertype)
radiobtn2.grid(row=4,column=1,sticky=tk.W)

#creating checkbutton
check_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text="check if you want to subscribe to our newsletter",variable=check_var)
checkbtn.grid(row=5,columnspan=2)


#creating buttons
# def action():
#     user_name=name_var.get()
#     user_email=email_var.get()
#     user_age=age_var.get()
#     user_gender=gender_var.get()
#     user_type=usertype.get()
#     subscribed= 'Yes' if check_var.get() else "NO"
#     with open('file.txt','a') as f:
#         f.write(f"{user_name},{user_email},{user_age},{user_gender},{user_type},{subscribed}\n")
#     name_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)
#     email_entrybox.delete(0,tk.END)
#     name_label.configure(foreground='#232343')
    # submit_button.configure(background="Blue")

# write to csv file
def action():
    user_name=name_var.get()
    user_email=email_var.get()
    user_age=age_var.get()
    user_gender=gender_var.get()
    user_type=usertype.get()
    subscribed= 'Yes' if check_var.get() else "NO"
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='#232343')

    # writing to csv file
    with open('file.csv','a',newline="") as f:
        writer=DictWriter(f,fieldnames=['Name','Email','Age','Gender','Type','Subscribed'])
        if os.stat('file.csv').st_size==0:
            writer.writeheader()
        writer.writerow({
            "Name":user_name,
            'Email':user_email,
            'Age':user_age,
            'Gender':user_gender,
            'Type':user_type,
            'Subscribed':subscribed
        })
submit_button = ttk.Button(win, width=16,text="Submit",command=action)
submit_button.grid(row=6,column=0)

win.mainloop()