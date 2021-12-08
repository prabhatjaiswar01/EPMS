from tkinter import *
from PIL import Image,ImageTk
import pymysql
from  tkinter import messagebox as tmsg
import os,re

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Screen")
        self.root.geometry("1350x900+0+0")
        self.root.config(bg="green")

        self.bg1=ImageTk.PhotoImage(file="frame_background.jpg") #here we just loading the image into the the background 1 image into variable
        bg1=Label(self.root,image=self.bg1).place(x=0,y=0,relwidth=1,relheight=1)

        title=Label(self.root,text="Welcome to YEDUVANTAS Technologys",font="Lucida 40 bold",bg="blue",fg="white") #,bg="#3776ab"
        title.pack(fill=X)
        Logo_label = Label(root, text="YEDUVANTAS LOGO", font=("times new roman",50,"bold"),bd=5,relief=SUNKEN,fg="black",bg="springgreen").place(x=0,y=73,width=874)#(x=96,y=300)
        self.employee()
        #====================Main login frame===========================
    def employee(self):           #if we dont want into in function then you have to only remove the def function no need to change indentation
        login_frame=Frame(self.root,bg="ivory",bd=3,relief=GROOVE)  #white smoke
        # login_frame.place(x=460,y=70,width=465,height=400)
        login_frame.place(x=880,y=70,width=467,height=625)
        # login_frame.pack()

        self.bg2 = ImageTk.PhotoImage(file="employee_logo.jpg")

        bg2 = Label(login_frame, image=self.bg2).place(x=0, y=0,width=460,height=120)

        #===========================All variables====================================================
        self.email=StringVar()
        self.password=StringVar()
        self.clicked = StringVar()     #this is for the favorite question click event data
        self.fav_question_answer = StringVar()
        self.txt_change_password=StringVar()
        self.txt_change_confirm_password=StringVar()


        #=======================login detials here========================================================================
        email_lbl=Label(login_frame,text="Email ID:",font=("timesnewroman 16 bold"),bg="ivory",fg="#581845").place(x=15,y=150)#x=15,y=150
        self.txt_email=Entry(login_frame,font=("timesnewroman 14 "),bg="light yellow",text=self.email)
        self.txt_email.place(x=15,y=190,width=260)#x=180,y=150,width=260

        password_lbl= Label(login_frame, text="Password:",font=("timesnewroman 16 bold"), bg="ivory",
                          fg="#581845").place(x=15, y=230) #x=15, y=190
        self.txt_password = Entry(login_frame,show="*", font=("timesnewroman 14 "), text=self.password,bg="light yellow")
        self.txt_password.place(x=15, y=270,width=260)#x=180, y=190,width=260

        btn_reg=Button(login_frame,text="Register New Account?",bg="ivory",font=("timesnewRoman",14 ,"bold"),bd=0,fg="black",cursor="hand2",command= self.register)
        btn_reg.place(x=15,y=320)#x=15,y=250

        btn_forget = Button(login_frame, text="Forget Password?",command=self.forget_password, bg="ivory",bd=0, font=("timesnewRoman", 14, "bold"),
                         fg="black", curso="hand2")
        btn_forget.place(x=250, y=320) #x=250, y=250
         #here we are taking the image and resizing it for to place into our login button
        self.btn_image=Image.open("login_button_img.png")
        # resized=self.btn_image.resize((200,100),Image.ANTIALIAS)
        resized=self.btn_image.resize((200,50),Image.ANTIALIAS)
        self.btn_image1=ImageTk.PhotoImage(resized)

        btn_login=Button(login_frame,image=self.btn_image1,command=self.login,bd=1,bg="CRIMSON",fg="white",cursor="hand2",width=200)
        btn_login.place(x=15,y=380)  #(x=15,y=310)



        btn_admin_login = Button(login_frame,text="Admin login", command=self.admin, bg="orange", bd=1,
                                 font=("timesnewRoman", 20, "bold"),
                                 fg="black", curso="hand2") # text="Admin login"
        btn_admin_login.place(x=15, y=460,width=205)   #x=234, y=310,width=220
        # note_label=Label(login_frame,text="Note:",font=("times new roman",20,"bold")
        note_label1=Label(login_frame,text="Note:It is very secure software so you have",font=("times new roman",18,"bold"))
        note_label2=Label(login_frame,text="enter same login detials as you have entered",font=("times new roman",17,"bold"))
        note_label3=Label(login_frame,text="at the time of registation ",font=("times new roman",18,"bold"))
        note_label1.place(x=15,y=520)
        note_label2.place(x=14,y=555)
        note_label3.place(x=15,y=585)

        #making new frame here to get the image on the left hand side
        left_frame = Frame(self.root, bg="ivory",bd=0, relief=GROOVE)  # white smoke
        left_frame.place(x=4, y=165, width=870, height=528)

        #here we are setting the image according to out needs to no need to worry
        self.btn_image = Image.open("left_design.jpg")
        resized = self.btn_image.resize((874, 582), Image.ANTIALIAS)   #874, 582  which size image you want
        self.left_frame = ImageTk.PhotoImage(resized)
        bg2 = Label(left_frame, image=self.left_frame).place(x=-7, y=-58)

        self.check_connection()

    #===================================DBMS connection==================================================================
    def register(self):
        self.root.destroy()
        os.system('regestation.py')

    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')#here we making the connection with the database
                                 #here con is a variable and connect is the methoad and other are inside the bracket are argument
            cur=con.cursor()    #cusro is something which will help us to do the function for eg (add,update,delete,etc)
            cur.execute("select * from emp_salary") #by the execute method you can execute the query of your choice
            rows=cur.fetchall()

        except Exception as ex:
            tmsg.showerror("Error",f"Error due to : Please start your SQL server ") #{str(ex) }

    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            tmsg.showerror("Error","login details must required")
        else:

            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from login where email_id=%s", self.txt_email.get())
                row = cur.fetchone()  # if the data is alredy present inside the data base then it will return the hole column
                # if the data is not present into the the data base then it will return None as the output
                # print(row)          #we are using the print to check the what the data fetching from the database
                if row == None:
                    tmsg.showerror("Error",
                                   "Invalid Email ID, please try with another Email ID",) # we are using the self.parent root for only if the user give the response ok then only
                                                      # it will allow to do the following things with the GUI
                    self.email.set(""),
                    self.password.set("")

                elif(self.txt_email.get()==row[0] and self.txt_password.get()!=row[8]):
                    tmsg.showerror("Error","You have entered wrong password")
                    self.password.set("")
                elif(self.txt_email.get()!=row[0] and self.txt_password.get()!=row[8]):
                     tmsg.showerror("Error","Invalid Email ID and Password")
                elif(self.txt_email.get()==row[0] and self.txt_password.get()==row[8]):
                       tmsg.showinfo("Sucess",f"You have sucessfully login, Welcome {self.txt_email.get()}")
                       self.root.destroy()  #this will destroy the current window
                       os.system('main_window.py')  #this will open a main window if user and password corret
                else:
                    tmsg.showerror("Error","Invalid Email id and password, please try again!")
                    # tmsg.showinfo("Sucess", f"You have sucessfully login, Welcome {self.txt_email.get()}")
                    # self.root.destroy()
                    # os.system('main_window.py')

            except Exception as ex:
                tmsg.showerror("Error", f"Error due to : {str(ex)} ")
    def forget_password(self):
        if self.txt_email.get()=="":
            tmsg.showerror("Error","Email id must required to forget the password")

        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select email_id from login where email_id=%s", self.txt_email.get())
                row = cur.fetchone()  # if the data is alredy present inside the data base then it will return the hole column
                # if the data is not present into the the data base then it will return None as the output
                # print(row)          #we are using the print to check the what the data fetching from the database
                if row == None :
                    tmsg.showerror("Error",
                                   "Invalid Email ID,You cannot forget",
                                   parent=self.root)  # we are using the self.parent root for only if the user give the response ok then only
                #                                       # it will allow to do the following things with the GUI
                    self.email.set(""),
                    self.password.set("")
                # elif self.email.get()!=row[0]:
                #     tmsg.showerror("Error","Invalid Email ID",)

                else:

                    self.root2 = Toplevel(self.root)
                    self.root2.title("Forget Password")
                    self.root2.geometry("450x500")
                    self.root2.config(bg="white")

                    self.root2.resizable(True, True)
                    # title = Label(self.root2, text="All Employee Detials", font=("times new roman", 30, "bold"),
                    #               bg="#262625", fg="white", anchor="w", padx=10)
                    # title.pack(side=TOP, fill=X)
                    self.root2.focus_force()  # this function is use for new window will get the more highlited on the

                     #==============for lobel=========================================
                    title_l1=Label(self.root2,text=f"Forget password",bg="gold",fg="black",font=("times new roman",20,"bold"),pady=20).pack(fill=X)
                    email_l2 = Label(self.root2, text=f"Email ID:", bg="white", fg="black", font=("times new roman", 20, "bold")).place(x=7,y=85)
                    title_l2 = Label(self.root2, text=f"{self.txt_email.get()}", bg="white", fg="black", font=("times new roman",18, "bold")).place(x=130,y=85)

                    # ==============for combobox=========================================
                    option = ["select your favrouite question", "Your favourite Question", 'Your Pet name', "Favrouit Cricketer",
                              "Your Favourit place", "Your Best friend", "Your favourite Game"]

                    self.clicked.set(option[0])  # clicked variable is initilied in upper variables
                    # def selected(event):
                    # l1=Label(self.root,text=self.clicked.get(),width=200).place(x=15,y=250)
                    #  self.fav_question_answer.set(self.clicked.get())
                    com_fav_question = OptionMenu(self.root2, self.clicked,
                                                  *option)  # ,command=selected  to test above function use this command
                    com_fav_question.place(x=0, y=140,relwidth=1,height=40)


                    email_l2 = Label(self.root2, text=f"Enter you favourite question answer:", bg="white", fg="black", font=("times new roman", 18, "bold")).place(x=10,y=195)


                    txt_fav_question_answer = Entry(self.root2, font=("times new roman", 15),
                                                    bg="light yellow", fg="black", text=self.fav_question_answer).place(x=15,
                                                                                                                        y=250,width=220)
                    #this is for the password
                    password_l1 = Label(self.root2, text="Enter New Password :", bg="white", fg="black",
                                     font=("times new roman", 18, "bold")).place(x=10, y=300)

                    txt_change_password = Entry(self.root2, font=("times new roman", 15),
                                                    bg="light yellow", fg="black", text=self.txt_change_password).place(x=246,
                                                                                                                        y=303,
                                                                                                                        width=195)
                    password_l2 = Label(self.root2, text="Confirm Password :", bg="white", fg="black",
                                        font=("times new roman", 18, "bold")).place(x=10, y=350)

                    txt_change_confirm_password = Entry(self.root2, font=("times new roman", 15),
                                                bg="light yellow", fg="black", text=self.txt_change_confirm_password).place(x=246,
                                                                                                                    y=350,
                                                                                                                    width=195)
                    btn_reset=Button(self.root2,text="reset password",bg="yellow",fg="black",font=("times new roman",18,"bold"),
                                                                        command=self.reset,width=20).place(x=80,y=410)
            except Exception as ex:
                tmsg.showerror("Error", f"Error due to : {str(ex)} ")

    def reset(self):
        if self.clicked.get()=="select your favrouite question":
            tmsg.showerror("Error","Select your favrouite question",parent=self.root2)
        elif self.fav_question_answer.get()=="" or self.txt_change_password=="" or self.txt_change_confirm_password=="":
            tmsg.showerror("Error","All fields are must required",parent=self.root2)
        elif self.txt_change_password.get()!=self.txt_change_confirm_password.get():
            tmsg.showerror("Error","Password and Confirm should me same",parent=self.root2)

        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from login where email_id=%s", self.txt_email.get())
                row = cur.fetchone()  # if the data is alredy present inside the data base then it will return the hole column
                # if the data is not present into the the data base then it will return None as the output
                # print(row[3])
                # print(row[4])
                if self.clicked.get()!=row[3] or self.fav_question_answer.get()!=row[4]:
                    tmsg.showerror("Error",
                                   "Your Selected Question and Answer is 'Not' same ",
                                   parent=self.root2)
                else:

                    cur.execute("UPDATE `login` SET `password`=%s,`confirm_password`=%s WHERE `email_id`=%s",(self.txt_change_password.get(),self.txt_change_confirm_password.get(),self.txt_email.get()))
      #error on that particule file
                                #          )
                                # # for eg update student_table s_name="new name" where std_rollno=1;
                                #          )  # execute is closing here

                    tmsg.showinfo("Success",f"{self.txt_email.get()} have successfully reset your password")
                    # print("Your password are reset succesfully")
                    con.commit()
                    con.close()
            except Exception as ex:
                tmsg.showerror("Error", f"Error due to : {str(ex)} ")
    def admin(self):
        login_frame1 = Frame(self.root, bg="ivory", bd=4, relief=GROOVE)  # white smoke
        # login_frame.place(x=460,y=70,width=465,height=400)
        login_frame1.place(x=880, y=70, width=467, height=625)

        #=================All variables are define here for the admin screen=============================
        self.admin_id=StringVar()
        self.admin_password=StringVar()
        self.cnf_admin_password=StringVar()
        self.admin_click = StringVar()
        self.admin_fav_question_answer = StringVar()
        self.admin_change_password = StringVar()
        self.admin_change_confirm_password = StringVar()

        # login_frame.pack()

        self.bg2 = ImageTk.PhotoImage(file="admin_logo.jpg")

        bg2 = Label(login_frame1, image=self.bg2,bd=1).place(x=-10, y=0, width=480, height=120)

        #=========================main admin login screen start here====================================

        email_lbl = Label(login_frame1, text="Email ID:", font=("timesnewroman 16 bold"), bg="ivory",
                          fg="#581845").place(x=15, y=150)  # x=15,y=150
        self.txt_email_admin = Entry(login_frame1, font=("timesnewroman 14 "), bg="light yellow", text=self.admin_id)
        self.txt_email_admin.place(x=15, y=190, width=260)  # x=180,y=150,width=260

        password_lbl = Label(login_frame1, text="Password:", font=("timesnewroman 16 bold"), bg="ivory",
                             fg="#581845").place(x=15, y=230)  # x=15, y=190
        self.txt_password_admin = Entry(login_frame1,show="*", font=("timesnewroman 14 "), text=self.admin_password, bg="light yellow")
        self.txt_password_admin.place(x=15, y=270, width=260)  # x=180, y=190,width=260

        btn_forget_admin = Button(login_frame1, text="Forget Password?", command=self.admin_forget_password, bg="ivory", bd=0,
                            font=("timesnewRoman", 14, "bold"),
                            fg="black", curso="hand2")
        btn_forget_admin.place(x=15, y=320)  # x=15,y=250

         # x=250, y=250
        # here we are taking the image and resizing it for to place into our login button
        self.btn_image = Image.open("Admin_login_btn.jpeg")
        # resized=self.btn_image.resize((200,100),Image.ANTIALIAS)
        resized = self.btn_image.resize((200, 50), Image.ANTIALIAS)
        self.btn_image1 = ImageTk.PhotoImage(resized)

        btn_login11= Button(login_frame1, image=self.btn_image1, command=self.admin_login_function, bd=1, bg="CRIMSON", fg="white",
                           cursor="hand2", width=200)
        btn_login11.place(x=15, y=380)  # (x=15,y=310)

        # btn_emloyee_delete = Button(login_frame1, text="Delete employee details", command=self.forget_password, bg="ivory", bd=0,
        #                     font=("timesnewRoman", 14, "bold"),
        #                     fg="black", curso="hand2")
        # btn_emloyee_delete.place(x=15, y=450)

        btn_back_page = Button(login_frame1, text="Back", command=self.back,
                                    bg="light green", bd=3,
                                    font=("timesnewRoman", 14, "bold"),
                                    fg="black", curso="hand2")
        btn_back_page.place(x=319, y=570,width=130)
    def back(self):
        self.employee()


    def admin_login_function(self):
        if self.txt_email_admin.get()=="" or self.txt_password_admin.get()=="":
            tmsg.showerror("Error","ADMIN login details must required")
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from admin where admin_id=%s", self.admin_id.get())
                row = cur.fetchone()  # if the data is alredy present inside the data base then it will return the hole column
                # if the data is not present into the the data base then it will return None as the output
                # print(row)          #we are using the print to check the what the data fetching from the database
                if row == None:
                    tmsg.showerror("Error",
                                   "Invalid Email ID, please try with another Email ID",) # we are using the self.parent root for only if the user give the response ok then only
                                                      # it will allow to do the following things with the GUI
                    self.admin_id.set(""),
                    self.admin_password.set("")

                elif(self.admin_id.get()==row[0] and self.admin_password.get()!=row[1]):
                    tmsg.showerror("Error","You have entered wrong password")
                    self.password.set("")
                elif(self.admin_id.get()!=row[0] and self.admin_password.get()!=row[1]):
                     tmsg.showerror("Error","Invalid Email ID and Password")
                elif(self.admin_id.get()==row[0] and self.admin_password.get()==row[1]):
                       tmsg.showinfo("Sucess",f"You have sucessfully login, Welcome {self.txt_email.get()}")
                       self.root.destroy()
                       os.system('main_window.py')
                else:
                    tmsg.showerror("Error","Invalid Email id and password, please try again!")
            except Exception as ex:
                tmsg.showerror("Error", f"Error due to : {str(ex)} ")
    def admin_forget_password(self):
        if self.admin_id.get()=="":
            tmsg.showerror("Error","Admin Email id must required to forget the password")

        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select admin_id from admin where admin_id=%s", self.admin_id.get())
                row = cur.fetchone()  # if the data is alredy present inside the data base then it will return the hole column
                # if the data is not present into the the data base then it will return None as the output
                # print(row)          #we are using the print to check the what the data fetching from the database
                if row == None :
                    tmsg.showerror("Error",
                                   "Invalid Admin Email ID,You cannot forget",
                                   parent=self.root)  # we are using the self.parent root for only if the user give the response ok then only
                #                                       # it will allow to do the following things with the GUI
                    self.admin_id.set(""),
                    self.admin_password.set("")
                # elif self.email.get()!=row[0]:
                #     tmsg.showerror("Error","Invalid Email ID",)

                else:

                    self.root2 = Toplevel(self.root)
                    self.root2.title("Forget Password")
                    self.root2.geometry("450x500")
                    self.root2.config(bg="white")

                    self.root2.resizable(True, True)
                    # title = Label(self.root2, text="All Employee Detials", font=("times new roman", 30, "bold"),
                    #               bg="#262625", fg="white", anchor="w", padx=10)
                    # title.pack(side=TOP, fill=X)
                    self.root2.focus_force()  # this function is use for new window will get the more highlited on the

                     #==============for lobel=========================================
                    title_l1=Label(self.root2,text=f"Forget Admin password",bg="gold",fg="black",font=("times new roman",20,"bold"),pady=20).pack(fill=X)
                    email_l2 = Label(self.root2, text=f"Admin ID:", bg="white", fg="black", font=("times new roman", 20, "bold")).place(x=7,y=85)
                    title_l2 = Label(self.root2, text=f"{self.txt_email_admin.get()}", bg="white", fg="black", font=("times new roman",18, "bold")).place(x=130,y=85)

                    # ==============for combobox=========================================
                    option = ["select your favrouite question", 'Your Pet name', "Favrouit Cricketer",
                              "Your Favourit place", "Your Best friend", "Your favourite Game"]

                    self.admin_click.set(option[0])  # clicked variable is initilied in upper variables
                    # def selected(event):
                    # l1=Label(self.root,text=self.clicked.get(),width=200).place(x=15,y=250)
                    #  self.fav_question_answer.set(self.clicked.get())
                    com_fav_question = OptionMenu(self.root2, self.admin_click,
                                                  *option)  # ,command=selected  to test above function use this command
                    com_fav_question.place(x=0, y=140,relwidth=1,height=40)


                    label_l2 = Label(self.root2, text=f"Enter you favourite question answer:", bg="white", fg="black", font=("times new roman", 18, "bold")).place(x=10,y=195)


                    txt_fav_question_answer = Entry(self.root2, font=("times new roman", 15),
                                                    bg="light yellow", fg="black", text=self.admin_fav_question_answer).place(x=15,
                                                                                                                        y=250,width=220)
                    #this is for the password
                    password_l1 = Label(self.root2, text="Enter New Password :", bg="white", fg="black",
                                     font=("times new roman", 18, "bold")).place(x=10, y=300)

                    admin1_change_password = Entry(self.root2, font=("times new roman", 15),
                                                    bg="light yellow", fg="black", text=self.admin_change_password).place(x=246,
                                                                                                                        y=303,
                                                                                                                        width=195)
                    password_l2 = Label(self.root2, text="Confirm Password :", bg="white", fg="black",
                                        font=("times new roman", 18, "bold")).place(x=10, y=350)

                    admin1_change_confirm_password = Entry(self.root2, font=("times new roman", 15),
                                                bg="light yellow", fg="black", text=self.admin_change_confirm_password).place(x=246,
                                                                                                                    y=350,
                                                                                                                    width=195)
                    btn_reset=Button(self.root2,text="reset password",bg="yellow",fg="black",font=("times new roman",18,"bold"),
                                                                        command=self.admin_reset,width=20).place(x=80,y=410)
            except Exception as ex:
                tmsg.showerror("Error", f"Error due to : {str(ex)} ")
    def admin_reset(self):
        if self.admin_click.get()=="select your favrouite question":
            tmsg.showerror("Error","Select your favrouite question",parent=self.root2)
        elif self.admin_fav_question_answer.get()=="" or self.admin_change_password=="" or self.admin_change_confirm_password=="":
            tmsg.showerror("Error","All fields are must required",parent=self.root2)
        elif self.admin_change_password.get()!=self.admin_change_confirm_password.get():
            tmsg.showerror("Error","Password and Confirm should me same",parent=self.root2)

        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from admin where admin_id=%s", self.admin_id.get())
                row = cur.fetchone()  # if the data is alredy present inside the data base then it will return the hole column
                # if the data is not present into the the data base then it will return None as the output
                # print(row[3])
                # print(row[4])
                if self.admin_click.get()!=row[3] or self.admin_fav_question_answer.get()!=row[4]:
                    tmsg.showerror("Error",
                                   "Your Selected Question and Answer is 'Not' same ",
                                   parent=self.root2)
                else:

                    cur.execute("UPDATE `admin` SET `admin_password`=%s,`cnf_admin_password`=%s WHERE `admin_id`=%s",(self.admin_change_password.get(),self.admin_change_confirm_password.get(),self.admin_id.get()))
      #error on that particule file
                                #          )
                                # # for eg update student_table s_name="new name" where std_rollno=1;
                                #          )  # execute is closing here

                    tmsg.showinfo("Success",f"{self.admin_id.get()} have successfully reset your password")
                    # print("Your password are reset succesfully")
                    con.commit()
                    con.close()
            except Exception as ex:
                tmsg.showerror("Error", f"Error due to : {str(ex)} ")
    # def valadation(self):
    #     if self.txt_email.get()!="":
    #         regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #         patt =re.compile(regex)
    #         matches= patt.finditer(self.txt_email.get())
    #         tmsg.showerror("Error","Invalid Email Id you have Entered")
    #
    #     else:
    #         pass
    def regular_expression(self):
        # Python program to validate an Email

        # import re module

        # re module provides support
        # for regular expressions
        import re

        # Make a regular expression
        # for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # Define a function for
        # for validating an Email

        def check(email):

            # pass the regular expression
            # and the string into the fullmatch() method
            if (re.fullmatch(regex, email)):
                pass

            else:
                tmsg.showerror("Error","Invalid Email")
                self.email.set("")
                self.password.set("")
        check(self.email.get())



if __name__ == '__main__':
   root=Tk()
   obj=Login(root)
   root.mainloop()