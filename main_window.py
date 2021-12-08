"""=============================This is payroll managment system==================================================="""
from tkinter import *
from tkinter import messagebox as tmsg,ttk     #we are importing the ttk for the tree view
import pymysql
import  time
import os
import tempfile             #this function is for the temperory file
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Managment System | Developed By Prabhat Jaiswar")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.resizable(True,True)
        title=Label(self.root,text="Employee Payroll Managment System",font=("times new roman",30,"bold"),bg="#262625",fg="white",anchor="w",padx=10)
        title.place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root, text="All Employee's", command=self.employee_frame, font=("times new roman", 14),
                       bg="mediumorchid", fg="white", bd=1).place(x=1000, y=11, width=150)
        btn_sign_out=Button(self.root, text="Sign Out", command=self.sign_out, font=("times new roman", 14),
                       bg="cornflowerblue", fg="white", bd=1).place(x=1180, y=11, width=150)
        #==========================this is Frame1 for the employee detials==================================
        #==========================Variables=====================================================
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar()    #===========we are taking AADHAR CARD as a proof by default=============
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_experience=StringVar()



        Frame1=Frame(self.root,bd=3,bg="white",relief=RIDGE)
        Frame1.place(x=9,y=70,width=750,height=620)
        title2 = Label(Frame1, text="Employee Details",font=("times new roman", 20, "bold"),
                      bg="yellow", fg="red", anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        #================ROW 0============================
        lbl_code=Label(Frame1, text="Employee Code :", font=("times new roman", 20),
                      bg="white", fg="black").place(x=10,y=50)
        self.txt_code = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_emp_code,
                                bg="light yellow", fg="black")
        self.txt_code.place(x=220, y=57, width=200)
        btn_search =Button(Frame1,text="search",command=self.search,font=("times new roman", 14),
                                bg="white", fg="black",bd=1).place(x=450, y=51, width=120)

        #=========ROW1=====================================
        lbl_designation =Label(Frame1, text="Designation :", font=("times new roman", 20),
                         bg="white", fg="black").place(x=10, y=95)
        txt_designation = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_designation,
                                bg="light yellow", fg="black").place(x=172,y=103,width=200)

        lbl_doj = Label(Frame1, text="D.O.J :", font=("times new roman", 20),
                                bg="white", fg="black").place(x=390, y=97,width=100)
        txt_doj = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_doj,
                                bg="light yellow", fg="black").place(x=525, y=103,width=200)
        # =========ROW2=================================
        lbl_Name = Label(Frame1, text="Name :", font=("times new roman", 20),
                                bg="white", fg="black").place(x=10, y=140)
        txt_name = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_name,
                                bg="light yellow", fg="black").place(x=172, y=148, width=200)
        lbl_dob = Label(Frame1, text="D.O.B :", font=("times new roman", 20),
                        bg="white", fg="black").place(x=390, y=144, width=100)
        txt_dob = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_dob,
                        bg="light yellow", fg="black").place(x=525, y=150, width=200)

        # =========ROW3=================================
        lbl_age = Label(Frame1, text="Age :", font=("times new roman", 20),
                         bg="white", fg="black").place(x=10, y=185)
        txt_age = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_age,
                         bg="light yellow", fg="black").place(x=172, y=193, width=200)
        lbl_experience = Label(Frame1,text="Experience:", font=("times new roman", 19),
                        bg="white", fg="black").place(x=397, y=189, width=115)
        txt_experience = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_experience,
                        bg="light yellow", fg="black").place(x=525, y=195, width=200)

        # =========ROW4=================================
        lbl_gender = Label(Frame1, text="Gender :", font=("times new roman", 20),
                        bg="white", fg="black").place(x=10, y=230)
        txt_gender = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_gender,
                        bg="light yellow", fg="black").place(x=172, y=238, width=200)
        lbl_proof = Label(Frame1, text="Aadhar No:", font=("times new roman", 19),
                               bg="white", fg="black").place(x=395, y=234, width=115)
        txt_proof = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_proof_id,
                               bg="light yellow", fg="black").place(x=525, y=240, width=200)

        # =========ROW5=================================
        lbl_email = Label(Frame1, text="Email :", font=("times new roman", 20),
                           bg="white", fg="black").place(x=10, y=275)
        txt_email = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_email,
                           bg="light yellow", fg="black").place(x=172, y=283, width=200)
        lbl_contact = Label(Frame1, text="Contact :", font=("times new roman", 19),
                          bg="white", fg="black").place(x=385, y=279, width=115)
        txt_contact = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_contact,
                          bg="light yellow", fg="black").place(x=525, y=285, width=200)

        # =========ROW6=================================
        lbl_hired= Label(Frame1, text="Hired Location:", font=("times new roman", 18),
                          bg="white", fg="black").place(x=7, y=322)
        txt_hired = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_hr_location,
                          bg="light yellow", fg="black").place(x=172, y=328, width=200)
        lbl_status = Label(Frame1, text="Status :", font=("times new roman", 19),
                            bg="white", fg="black").place(x=377, y=324, width=115)
        txt_status = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_status,
                            bg="light yellow", fg="black").place(x=525, y=330, width=200)


        #============ROW6=================================
        lbl_address = Label(Frame1, text="Address :", font=("times new roman", 20),
                          bg="white", fg="black").place(x=7, y=367)
        self.txt_address =Text(Frame1, font=("times new roman", 15),bg="light yellow", fg="black")
        self.txt_address.place(x=172, y=373, width=550,height="200")  #we are converting the number as self due to get or access
                                                                      # the data later on


        #===========================Frame2===========================================
         #=========================Variables for the frame 2======================
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_t_salary = StringVar()
        self.var_t_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net_salary = StringVar()

        Frame2 = Frame(self.root, bd=3, bg="white", relief=RIDGE)
        Frame2.place(x=765, y=70, width=575, height=310)

        title3 = Label(Frame2, text="Employee Salary Details", font=("times new roman", 20, "bold"),
                      bg="yellow", fg="red", anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        # =========ROW0=================================
        lbl_month = Label(Frame2, text="Month:", font=("times new roman", 20),
                         bg="white", fg="black").place(x=10, y=50)
        txt_month = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_month,
                                bg="light yellow", fg="black").place(x=100, y=55, width=100)

        lbl_year = Label(Frame2, text="Year:", font=("times new roman", 20),
                          bg="white", fg="black").place(x=205, y=50)
        txt_year = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_year,
                          bg="light yellow", fg="black").place(x=270, y=55, width=100)

        lbl_salary = Label(Frame2, text="Salary:", font=("times new roman", 20),
                         bg="white", fg="black").place(x=375, y=50)
        txt_salary = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_t_salary,
                         bg="light yellow", fg="black").place(x=460, y=55, width=100)

        # =========ROW1=================================
        lbl_days = Label(Frame2, text="Total days:", font=("times new roman", 18),
                                bg="white", fg="black").place(x=10, y=95)
        txt_days = Entry(Frame2, font=("times new roman", 18),textvariable=self.var_t_days,
                                bg="light yellow", fg="black").place(x=140, y=100, width=150)

        lbl_absent = Label(Frame2,text="Absent :", font=("times new roman", 18),
                        bg="white", fg="black").place(x=304, y=97, width=100)
        txt_absent = Entry(Frame2, font=("times new roman", 18),textvariable=self.var_absent,
                        bg="light yellow", fg="black").place(x=405, y=100, width=150)

        # =========ROW2=================================
        lbl_medical = Label(Frame2, text="Medical:", font=("times new roman", 18),
                         bg="white", fg="black").place(x=10, y=145)
        txt_medical = Entry(Frame2, font=("times new roman", 18),textvariable=self.var_medical,
                         bg="light yellow", fg="black").place(x=140, y=145, width=150)

        lbl_pf = Label(Frame2, text="PF :", font=("times new roman", 18),
                           bg="white", fg="black").place(x=290, y=145, width=80)
        txt_pf = Entry(Frame2, font=("times new roman", 18),textvariable=self.var_pf,
                           bg="light yellow", fg="black").place(x=405, y=145, width=150)
        # ===============ROW3=================================
        lbl_convence = Label(Frame2, text="Convence:", font=("times new roman", 18),
                            bg="white", fg="black").place(x=10, y=190)
        txt_convence= Entry(Frame2, font=("times new roman", 18),textvariable=self.var_convence,
                            bg="light yellow", fg="black").place(x=140, y=190, width=150)

        lbl_netsalary = Label(Frame2, text="Net Salary:", font=("times new roman", 17),
                       bg="white", fg="black").place(x=288, y=190, width=130)
        txt_netsalary = Entry(Frame2, font=("times new roman", 18),textvariable=self.var_net_salary,
                       bg="light yellow", fg="black").place(x=405, y=190, width=150)

        #================Row4 for buttons============================
        btn_calculate = Button(Frame2, text="Calculate",command=self.calculate ,font=("times new roman", 14),
                            bg="gold", fg="black", bd=1).place(x=140, y=235, height=30,width=120)
        self.btn_save = Button(Frame2, text="Save",command=self.add, font=("times new roman", 14),
                               bg="springgreen", fg="black", bd=1)
        self.btn_save.place(x=285, y=235, height=30, width=120)
        btn_clear = Button(Frame2, text="Clear", font=("times new roman", 14),command=self.clear,
                               bg="cyan", fg="black", bd=1).place(x=430, y=235, height=30, width=120)
        self.btn_update = Button(Frame2, text="Update",state=DISABLED, command=self.update, font=("times new roman", 14),
                               bg="violet", fg="black", bd=1)
        self.btn_update.place(x=140, y=270, height=30, width=200)
        self.btn_delete = Button(Frame2, text="Delete",state=DISABLED, command=self.delete, font=("times new roman", 14),
                          bg="pink", fg="black", bd=1)
        self.btn_delete.place(x=350, y=270, height=30, width=200)

        # ===========================Frame3 ===========================================
        Frame3 = Frame(self.root, bd=3, bg="white", relief=RIDGE)
        Frame3.place(x=765, y=388, width=575, height=302)

        #==================calculator frame 1=============================================
        self.var_txt=StringVar()         #we are setting the data type for the variable as string
        self.var_operator=''
        #we are defing the function for the caluclator buttons
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)   #here we increment the variables
            self.var_txt.set(self.var_operator)            #here we are just assign the value to var_txt

        # #now we are making the function for getting the result of the calculation
        def result():
            res=str(eval(self.var_operator))# eval is an inbulid function which will automatically calculate the values with the
                                            # help of identifing the operator for eg 77+3 then it will   use split by
                                            # any opearetor(+,*,/,-) and then int(77)+ 'operator '+ 3= 80
            self.var_txt.set(res)          #we are setting the calculated value
            self.var_operator=''          #here we are deleting or clearing the screen of the result  of calcuator
        def clear():
            self.var_txt.set('')
            self.var_operator =''

        #======================Frame1 for the Calculator indise the salary frame===================================
        Cal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Cal_Frame.place(x=5,y=5,width=216,height=286)      #we are placing this field in below becz of the we want to do modifiaction into this frame
        #making the calculator result area here
        txt_Result=Entry(Cal_Frame,bg="light yellow",textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1,height=40)
        #in the upper line we use justify =right due to the text come to it from the right side to get the real effect of calculation
        #making the number button here
        #==============row 1 for the button 7,8,9 and divide===========================================
        btn_7=Button(Cal_Frame,text="7",font=("times new roman",15,"bold"),command=lambda:btn_click(7)).place(x=0,y=43,w=60,h=60)
        btn_8 = Button(Cal_Frame, text="8", font=("times new roman", 15, "bold"),command=lambda:btn_click(8)).place(x=51, y=43, w=60, h=60)
        btn_9 = Button(Cal_Frame, text="9", font=("times new roman", 15, "bold"),command=lambda:btn_click(9)).place(x=102, y=43, w=60, h=60)
        btn_div = Button(Cal_Frame, text="/", font=("times new roman", 15, "bold"),command=lambda:btn_click('/')).place(x=153, y=43, w=60, h=60)
        # ==============row 2 for the button 4,5,6 and the astric===========================================
        btn_4 = Button(Cal_Frame, text="4", font=("times new roman", 15, "bold"),command=lambda:btn_click(4)).place(x=0, y=103, w=60, h=60)
        btn_5 = Button(Cal_Frame, text="5", font=("times new roman", 15, "bold"),command=lambda:btn_click(5)).place(x=51, y=103, w=60, h=60)
        btn_6 = Button(Cal_Frame, text="6", font=("times new roman", 15, "bold"),command=lambda:btn_click(6)).place(x=102, y=103, w=60, h=60)
        btn_mul = Button(Cal_Frame, text="*", font=("times new roman", 15, "bold"),command=lambda:btn_click('*')).place(x=153, y=103, w=60, h=60)
        # ==============row 3 for the button 1,2,3,and sustract===========================================
        btn_1 = Button(Cal_Frame, text="1", font=("times new roman", 15, "bold"),command=lambda:btn_click(1)).place(x=0, y=163, w=60, h=60)
        btn_2 = Button(Cal_Frame, text="2", font=("times new roman", 15, "bold"),command=lambda:btn_click(2)).place(x=51, y=163, w=60, h=60)
        btn_3 = Button(Cal_Frame, text="3", font=("times new roman", 15, "bold"),command=lambda:btn_click(3)).place(x=102, y=163, w=60, h=60)
        btn_min = Button(Cal_Frame, text="-", font=("times new roman", 15, "bold"),command=lambda:btn_click('-')).place(x=153, y=163, w=60, h=60)#here min=substract
        # ==============row 4 for the button 0, (.) ,+ ,and equal===========================================
        btn_0 = Button(Cal_Frame, text="0", font=("times new roman", 15, "bold"),command=lambda:btn_click(0)).place(x=0, y=223, w=60, h=60)
        btn_dot = Button(Cal_Frame, text="C", font=("times new roman", 15, "bold"),command=clear).place(x=51, y=223, w=60, h=60)
        btn_sum = Button(Cal_Frame, text="+", font=("times new roman", 15, "bold"),command=lambda:btn_click('+')).place(x=102, y=223, w=60, h=60)
        btn_equal = Button(Cal_Frame, text="=", font=("times new roman", 15, "bold"),command=result).place(x=153, y=223, w=60, h=60)

        #========================Salary Frame 2============================================================
        #we are making another frame into the frame 3 called salary frame which is for the salary slip
        sal_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        sal_Frame.place(x=230, y=5, width=335, height=286)
        title_sal = Label(sal_Frame, text="Salary Reciept", font=("times new roman", 20, "bold"),
                       bg="yellow", fg="red", anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        #after giving the title we shoule making another frame for the textarea to generate the slip of the employee
           #we are making the another frame inside the paticular salary frame called salary frame 2 for the texta area
        sal_Frame2=Frame(sal_Frame,bg="white",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=37,relwidth=1,height=210)
        self.sample = f'''\tCompany Name,XYZ\n\tAddress : XYZ, Floor 4
---------------------------------------------------
 Employee ID\t\t:  
 Salary Of\t\t: MM-YYYY
 Generated On\t\t:  DD-MM-YYYY
---------------------------------------------------
 Total Days\t\t: DD
 Total Present\t\t: DD
 Total Absent\t\t: DD
 Convence\t\t: Rs.----
 Medical\t\t: Rs.----
 PF\t\t: Rs.----                               
 Gross Payment\t\t: Rs.-------
 Net Salary\t\t: Rs--------
---------------------------------------------------
 This is computer genrated slip, not
 required any signature'''

        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)   #making the scroll bar at Y or Vertical and fill y for fill totally into
        scroll_y.pack(fill=Y,side=RIGHT)       #the y and right is for getting the scroll bar into the right side of the frame

        self.txt_salary_recipt=Text(sal_Frame2,font=("times new roman",13),bg="light yellow",yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)    #here we are adding the scroll
        self.txt_salary_recipt.insert(END,self.sample)    #we are inseerting the sample variables here which are above in sample string variable

        self.btn_print= Button(sal_Frame,state=DISABLED,text="Print",command=self.print,font=("times new roman", 14),
                           bg="palegreen", fg="black", bd=1)
        self.btn_print.place(x=205, y=250, height=30, width=120)

        self.check_connection()     #we will first call this function due to check the connecvitry is with the database


    #++++++++++++++++++++++++++++++All the function are start from here+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def search(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='ems')
            cur = con.cursor()
            cur.execute("select * from emp_salary where e_id=%s", self.var_emp_code.get())
            row = cur.fetchone()  # if the data is alredy present inside the data base then it will return the hole column
            # if the data is not present into the the data base then it will return None as the output
            # print(rows)
            if row == None:
                tmsg.showerror("Error",
                               "Invalid Employee ID, please try with another ID",
                               parent=self.root)   #we are using the self.parent root for only if the user give the response ok then only
                                                   # it will allow to do the following things with the GUI
            else:
                self.var_emp_code.set(row[0])  #here we are setting the detials of the employee as per her/him Employee code or ID
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_experience.set(row[9])
                self.var_proof_id.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert(END,row[13])
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_t_salary.set(row[16])
                self.var_t_days.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_net_salary.set(row[22])
                file = open('salary_recipet/' + str(row[23]), "r")
                self.txt_salary_recipt.delete('1.0',END)
                for i in file:                         #here we are taking the value from inside the database and setting into the
                    self.txt_salary_recipt.insert(END,i)#salary recipt for loop is use for it will read data from file line by line
                file.close()
                self.btn_save.config(state=DISABLED) #after search you can only perform update and delete you cannot save
                self.btn_update.config(state=NORMAL) #bech it is already present in the the database
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state='readonly')#after search you cannot re-search without clearing the existing data
                self.btn_print.config(state=NORMAL)  #after search the print button get normal for the print the data
        except Exception as ex:
            tmsg.showerror("Error", f"Error due to : {str(ex)} ")
    def clear(self):
        #================here we are defining the state of the button=========================
        self.btn_save.config(state=NORMAL)#this normal the state of the save button becz user can save the new entry after clear
        self.btn_update.config(state=DISABLED) #this line will disable the update and delete function if user click on the clear btn
        self.btn_delete.config(state=DISABLED) #after clear without search user did not perfrom update and delete thats
                                              #why we disable this buttons
        self.btn_print.config(state=DISABLED)  #if user get clear then he will not able to print with searh or calculate
        self.txt_code.config(state=NORMAL)#after clear you can only you can enter the new emp id for search and all operation
        # =======================================================================================


        self.var_emp_code.set('')  # here we are setting the detials of the employee as per her/him Employee code or ID
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof_id.set('')
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0', END)
        self.var_month.set('')
        self.var_year.set('')
        self.var_t_salary.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')
        self.txt_salary_recipt.delete('1.0',END)
        self.txt_salary_recipt.insert(END,self.sample)

    def delete(self):
        if self.var_emp_code.get()=="":
            tmsg.showerror("Error","Employee ID must be required")
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", self.var_emp_code.get())
                row = cur.fetchone()  # if the data is alredy present inside the data base then it will return the hole column
                # if the data is not present into the the data base then it will return None as the output
                # print(rows)
                if row == None:
                    tmsg.showerror("Error",
                                   "Invalid Employee ID, please try with another ID",
                                   parent=self.root)   #we are using the self.parent root for only if the user give the response ok then only
                                                       # it will allow to do the following things with the GUI
                else:
                   op=tmsg.askyesno("Confirm","Do you really want to delete")
                   if op==True:
                      cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
                      con.commit()
                      con.close()
                      #I did no written else due to to if user click yes the it will delete otherwise not do any thing
                      tmsg.showinfo("Delete",f"Employee ID {self.var_emp_code.get()} is successfully deleted.",parent=self.root)
                      self.clear()#after the employee detial will be deleted from the database all the feild will be clear automatically
            except Exception as ex:
                tmsg.showerror("Error", f"Error due to : {str(ex)} ")

    def add(self):
          if self.var_emp_code.get()=="" or self.var_net_salary.get()=="" or self.var_name.get()=="":
              tmsg.showerror("Error","Employee detials are must required")
          else:

              try:
                con = pymysql.connect(host='localhost', user='root', password='',db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",self.var_emp_code.get())
                row = cur.fetchone()    #if the data is alredy present inside the data base then it will return the hole column
                                         #if the data is not present into the the data base then it will return None as the output
                # print(rows)
                if row!=None:
                    tmsg.showerror("Error","This Employee ID is already has avilable in our record, try again with another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (

                        self.var_emp_code.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0', END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_t_salary.get(),
                        self.var_t_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp_code.get()+".txt"  #this will be our file name for eg : 101.txt

                    )
                    ) #execute is closing here
                    con.commit()
                    con.close()
                    file=open('salary_recipet/'+str(self.var_emp_code.get())+".txt","w")
                    file.write(self.txt_salary_recipt.get('1.0',END))
                    file.close()
                    tmsg.showinfo("Success","Record is inserted successfully")
                    self.btn_print.config(state=NORMAL)    #after add it will  print button will get normal
              except Exception as ex:
                 tmsg.showerror("Error", f"Error due to : {str(ex)} ")


    def update(self):
          if self.var_emp_code.get()=="" or self.var_net_salary.get()=="" or self.var_name.get()=="":
              tmsg.showerror("Error","Employee detials are must required")
          else:

              try:
                con = pymysql.connect(host='localhost', user='root', password='',db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",self.var_emp_code.get())
                row = cur.fetchone()    #if the data is alredy present inside the data base then it will return the hole column
                                         #if the data is not present into the the data base then it will return None as the output
                # print(rows)
                if row==None:
                    tmsg.showerror("Error","This Employee ID is invalid, try again with valid Employee ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`t_days`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE `e_id`=%s",
                    (

                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0', END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_t_salary.get(),
                        self.var_t_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp_code.get()+".txt",  #this will be our file name for eg : 101.txt
                        self.var_emp_code.get()     #here we are putting the employee code last due to which id we have to update
                    )              #for eg update student_table s_name="new name" where std_rollno=1;
                    ) #execute is closing here
                    con.commit()
                    con.close()
                    file=open('salary_recipet/'+str(self.var_emp_code.get())+".txt","w")#here it is on write mode means it will
                                                                                        # over write the existing file with same name
                    file.write(self.txt_salary_recipt.get('1.0',END))
                    file.close()
                    tmsg.showinfo("Success","Record updated successfully")
              except Exception as ex:
                 tmsg.showerror("Error", f"Error due to : {str(ex)} ")
    def calculate(self):
        if self.var_month.get()=="" or self.var_year.get()=="" or self.var_t_salary=="" or self.var_t_days.get()=="" or self.var_absent.get()=="" or self.var_medical.get()=="" or self.var_pf.get()=="" or self.var_convence.get()=="":
               tmsg.showerror("Error","All fields are required")
        else:
            self.var_net_salary.set("RESULT")
            #35000/31=1752
            #31-10=21*1775
            per_day=int(self.var_t_salary.get())/int(self.var_t_days.get())
            work_day=int(self.var_t_days.get())-int(self.var_absent.get())
            sal_=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal_ - (deduct+addition)
            self.var_net_salary.set(str(round(net_sal,2)))
            #=========================Update the recipt============================================
                                                             #this is we are updating the slip detials
            new_sample = f'''\tCompany Name,XYZ\n\tAddress : XYZ, Floor 4   
---------------------------------------------------
Employee ID\t\t: {self.var_emp_code.get()}
Salary Of\t\t: {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}  
---------------------------------------------------
Total Days\t\t: {self.var_t_days.get()}
Total Present\t\t: {str(int(self.var_t_days.get())-int(self.var_absent.get()))}
Total Absent\t\t: {self.var_absent.get()}
Convence\t\t: Rs.{self.var_convence.get()}
Medical\t\t: Rs.{self.var_medical.get()}
PF\t\t: Rs.{self.var_pf.get()}                               
Gross Payment\t\t: Rs.{self.var_t_salary.get()}
Net Salary\t\t: Rs.{self.var_net_salary.get()}
---------------------------------------------------
This is computer genrated slip, not
required any signature'''
            self.txt_salary_recipt.delete('1.0',END)         #here we are deleting the total contain of the of the slip
            self.txt_salary_recipt.insert(END,new_sample)    #here we are adding the new slip into the slip area which is filled by detials

    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')#here we making the connection with the database
                                 #here con is a variable and connect is the methoad and other are inside the bracket are argument
            cur=con.cursor()    #cusro is something which will help us to do the function for eg (add,update,delete,etc)
            cur.execute("select * from emp_salary") #by the execute method you can execute the query of your choice
            rows=cur.fetchall()
            # print(rows)

        except Exception as ex:
            tmsg.showerror("Error",f"Error due to : {str(ex) } ")
    #++++++++++++++++++++++++++++++this is a new screen for the employee detials with new root++++++++++++++++++++++++++++++++++=
    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')#here we making the connection with the database
                                 #here con is a variable and connect is the method and other are inside the bracket are argument
            cur=con.cursor()    #cusro is something which will help us to do the function for eg (add,update,delete,etc)
            cur.execute("select * from emp_salary") #by the execute method you can execute the query of your choice
            rows=cur.fetchall()
            # print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())  #By the * we are defing its child elements
            for i in rows:
                self.employee_tree.insert('',END,values=i)
            con.close()
        except Exception as ex:
            tmsg.showerror("Error",f"Error due to : {str(ex) } ")
    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Employee Payroll Managment System | Developed By Prabhat Jaiswar")
        self.root2.geometry("1000x500+120+100")
        self.root2.config(bg="white")
        self.root2.resizable(True, True)
        title = Label(self.root2, text="All Employee Detials", font=("times new roman", 30, "bold"),
                      bg="#262625", fg="white", anchor="w", padx=10)
        title.pack(side=TOP,fill=X)
        self.root2.focus_force()  #this function is use for new window will get the more highlited on the screen

        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)   #we set the horizontal scroll bar
        scrolly.pack(side=RIGHT,fill=Y)    #we set the vertical scroll bar
        self.employee_tree = ttk.Treeview(self.root2, columns=('e_id', 'designation', 'name', 'age', 'gender', 'email',
                                                               'hr_location', 'doj', 'dob', 'experience', 'proof_id','contact',
                                                               'status', 'address', 'month', 'year', 'basic_salary','t_days',
                                                               'absent_days', 'medical', 'pf', 'convence', 'net_salary',
                                                               'salary_receipt'),
                                                                yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                                                #in upper line we simply attching our scrollbar at x and y axis on the new window

        self.employee_tree.heading('e_id', text='EID')  #here we are givig the heading name to our table
        self.employee_tree.heading('designation', text='Designation')
        self.employee_tree.heading('name', text='Name')
        self.employee_tree.heading('age', text='Age')
        self.employee_tree.heading('gender', text='Gender')
        self.employee_tree.heading('email', text='Email')
        self.employee_tree.heading('hr_location', text='Hr_Loc')
        self.employee_tree.heading('doj', text='D.O.J')
        self.employee_tree.heading('dob', text='D.O.B')
        self.employee_tree.heading('experience', text='Experience')
        self.employee_tree.heading('proof_id', text='Proof_id')
        self.employee_tree.heading('contact', text='Contact')
        self.employee_tree.heading('status', text='Status')
        self.employee_tree.heading('address', text='Address')
        self.employee_tree.heading('month', text='Month')
        self.employee_tree.heading('year', text='Year')
        self.employee_tree.heading('basic_salary', text='Basic_salary')
        self.employee_tree.heading('t_days', text='T_Days')
        self.employee_tree.heading('absent_days', text='Absent_days')
        self.employee_tree.heading('medical', text='Medical')
        self.employee_tree.heading('pf', text='PF')
        self.employee_tree.heading('convence', text='Convence')
        self.employee_tree.heading('net_salary', text='Net_salary')
        self.employee_tree.heading('salary_receipt', text='Salary_Receipt')

        self.employee_tree['show'] = 'headings'

        self.employee_tree.column('e_id', width=100)
        self.employee_tree.column('designation', width=100)
        self.employee_tree.column('name', width=100)
        self.employee_tree.column('age', width=100)
        self.employee_tree.column('gender', width=100)
        self.employee_tree.column('email', width=100)
        self.employee_tree.column('hr_location', width=100)
        self.employee_tree.column('doj', width=100)
        self.employee_tree.column('dob', width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id', width=100)
        self.employee_tree.column('contact', width=100)
        self.employee_tree.column('status', width=100)
        self.employee_tree.column('address', width=500)
        self.employee_tree.column('month', width=100)
        self.employee_tree.column('year', width=100)
        self.employee_tree.column('basic_salary', width=100)
        self.employee_tree.column('t_days', width=100)
        self.employee_tree.column('absent_days', width=100)
        self.employee_tree.column('medical', width=100)
        self.employee_tree.column('pf', width=100)
        self.employee_tree.column('convence', width=100)  # 500 but i did not put
        self.employee_tree.column('net_salary', width=100)
        self.employee_tree.column('salary_receipt', width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
        self.root2.mainloop()
        #++++++++++++++++++++++++++++++new window work is over++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #===============================now we are working on the print function========================================
    def print(self):
        file_=tempfile.mktemp(".txt")                                 #making one temporaty file with the extension .txt
        open(file_,"w").write(self.txt_salary_recipt.get('1.0',END))#we are opening this temperory file and writing
                                                                        # bill data on this temperory file
        os.startfile(file_,'print')    #we are opening this file with this file_ and using this print method

    def sign_out(self):
          # if self.var_emp_code.get()=="" or self.var_designation.get()=="" and self.var_name.get()=="" and self.var_age.get()=="" and self.var_gender.get()=="" and self.var_email.get()=="" and self.var_hr_location.get()=="" and self.var_doj.get()=="" and self.var_dob.get()=="" and self.var_experience.get()=="" and self.var_proof_id.get()=="" and self.var_contact.get()=="" and self.var_status.get()=="" and self.txt_address.get('1.0', END)=="":
          #    self.root.destroy()
          #    os.system('login.py')
          # # elif self.var_month.get()=="" and self.var_year.get()=="" and self.var_t_salary.get()=="" and self.var_t_days.get()=="" and self.var_absent.get()=="" and self.var_medical.get()=="" and self.var_pf.get()=="" and self.var_convence.get()==""and self.var_net_salary.get()=="":
          # #     tmsg.showerror("Error", "Without Clearing Data you cannot 'Sign Out' ")
          # else:
          #     tmsg.showerror("Error", "Without Clearing Data you cannot 'Sign Out' ")

         self.root.destroy()
         os.system('login.py')













if __name__ == '__main__':
    root=Tk()
    obj=EmployeeSystem(root)
    root.mainloop()