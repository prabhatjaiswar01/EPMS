import os
from tkinter import *
from tkinter import ttk #this is for the combo box
import random,pymysql
from tkinter import messagebox as tmsg
import smtplib




class Regestation:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x750+0+0")
        self.root.title("This is regestation window")
        self.root.config(bg="white")
        bg1="white"     #All the lable ackground color this will provide
        self.root.resizable(True, True)
        title = Label(self.root, text="Registration Form", font=("times new roman", 30, "bold"),
                      bg="Black", fg="white", padx=10)
        title.pack(fill=X)

        title2 = Label(self.root, text=" Create your account here", font=("times new roman", 20, "bold"),
                       bg="yellow",bd=2, fg="red", anchor="w", padx=10).place(x=0, y=51, relwidth=1)
        #+++++++++++++++++++++++++ALl variables++++++++++++++++++++++++++++++++++++++++++++++++++
        self.var_email_id=StringVar()
        self.var_DOB=StringVar()
        self.var_contact=StringVar()
        self.clicked = StringVar()
        self.fav_question_answer=StringVar()
        # gander variable
        self.gender_var = StringVar()
        self.gender_var.set(1)  # without setting the variable as 1 we will getting the all the radio button selected
                                   # so to avoide this we have to set the variable as 1
        self.company_code=StringVar()  #this currently i am taking string after that i will convert thatself.var_email_id=StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()


        # ================ROW 0============================
        lbl_email = Label(self.root, text="Email ID :", font=("times new roman", 20),
                         bg=bg1, fg="black").place(x=15, y=100)
        self.txt_email = Entry(self.root, font=("times new roman", 15),
                              bg="light yellow",text=self.var_email_id, fg="black")
        self.txt_email.place(x=200, y=105, width=250)


        # # =========ROW1=====================================
        lbl_DOB = Label(self.root, text="DOB :", font=("times new roman", 20),
                                bg=bg1, fg="black").place(x=15, y=150)
        txt_DOB = Entry(self.root, font=("times new roman", 15),
                                bg="light yellow", fg="black",text= self.var_DOB).place(x=200, y=155, width=250)
        # # =========ROW2=====================================
        lbl_contact = Label(self.root, text="Contact no :", font=("times new roman", 20),
                        bg=bg1, fg="black").place(x=15, y=200)
        txt_contact = Entry(self.root, font=("times new roman", 15),
                        bg="light yellow", fg="black",text=self.var_contact).place(x=200, y=208, width=250)
        # # =========ROW3=================================
        option=["select your favrouite question","Your favourite Question",'Your Pet name',"Favourite Cricketer","Your Favourit place","Your Best friend","Your favourite Game"]

        self.clicked.set(option[0])  #clicked variable is initilied in upper variables
        # def selected(event):
            # l1=Label(self.root,text=self.clicked.get(),width=200).place(x=15,y=250)
            #  self.fav_question_answer.set(self.clicked.get())
        com_fav_question=OptionMenu(self.root,self.clicked,*option)  #,command=selected  to test above function use this command
        com_fav_question.place(x=15, y=250)
        self.txt_fav_question_answer = Entry(self.root, font=("times new roman", 15),
                         bg="light yellow", fg="black",text=self.fav_question_answer)
        self.txt_fav_question_answer.place(x=230, y=250, width=220)

        # # =========ROW4=====================================
          #here we are mainking the gender
        lbl_gender = Label(self.root, text="Gender :", font=("times new roman", 20),
                        bg=bg1, fg="black").place(x=15, y=300, width=100)


        # # =========ROW6=====================================
        # now we want option
        radio = Radiobutton(root, text="Male", variable=self.gender_var, value="Male",bg=bg1).place(x=200,y=300)
        radio = Radiobutton(root, text="Female", variable=self.gender_var, value="Female",bg=bg1).place(x=300,y=300)

        # # =========ROW7=====================================
        security_key_button = Button(self.root, text="Click here for security Code", bg="orange", fg="black", font=("times new roman", 20, "bold"),
                    command=self.securit_code,width=27).place(x=15, y=350)

        # # =========ROW8=====================================
        lbl_company_code = Label(self.root, text="Company Security Code:", font=("times new roman", 18),
                        bg=bg1, fg="black").place(x=13, y=420)


        txt_company_code = Entry(self.root, font=("times new roman", 15), textvariable=self.company_code,
                        bg="light yellow", fg="black").place(x=260, y=422, width=191)

        # # =========ROW9=====================================

        lbl_password = Label(self.root, text="Password:", font=("times new roman", 19),
                               bg=bg1, fg="black").place(x=15, y=470, width=115)
        txt_password = Entry(self.root, font=("times new roman", 15), textvariable=self.var_password,
                               bg="light yellow", fg="black").place(x=200, y=473, width=250)
        # # =========ROW10=====================================
        lbl_confirm_password = Label(self.root, text="Confirm Password:", font=("times new roman", 17),
                             bg=bg1, fg="black",width=250).place(x=9, y=520, width=200)
        txt_confirm_password = Entry(self.root, font=("times new roman", 15), textvariable=self.var_confirm_password,
                             bg="light yellow", fg="black",width=250).place(x=200, y=520, width=250)
        # # =========ROW1  submit button=====================================
        self.B1_registation=Button(self.root,text="Register",bg="light green",fg="black",font=("times new roman",20,"bold"),command=self.register,width=12).place(x=15,y=575)

        B1_reset=Button(self.root,text="Reset",bg="orange",fg="black",font=("times new roman",20,"bold"),command=self.reset,width=12).place(x=240,y=575)

        B1_Sign=Button(self.root,text="Sign IN",bg="cyan",fg="black",font=("times new roman",20,"bold"),command=self.sign_in,width=26).place(x=15,y=635)

        # making new frame here to get the image on the left hand side
        # left_frame = Frame(self.root, bg="ivory", bd=0, relief=GROOVE)  # white smoke
        # left_frame.place(x=4, y=165, width=870, height=528)

        self.check_connection()
     #====================================All function start here========================================================================
    def sign_in(self):

         self.root.destroy()
         os.system('login.py')

    def reset(self):

        self.var_email_id.set(""),
        self.var_DOB.set(""),
        self.var_contact.set(""),
        option=["select your favrouite question", "Your favourite Question", 'Your Pet name', "Favrouit Cricketer","Your Favourit place", "Your Best friend", "Your favourite Game"]
        self.clicked.set(option[0]),
        self.fav_question_answer.set(""),
        # gander variable
        self.gender_var.set(""),
        # self.gender_var.set(1)  # without setting the variable as 1 we will getting the all the radio button selected
        # so to avoide this we have to set the variable as 1
        self.company_code.set(""),  # this currently i am taking string after that i will convert thatself.var_email_id=StringVar()
        self.var_password.set(""),
        self.var_confirm_password.set("")

    def check_connection(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='',
                                  db='ems')  # here we making the connection with the database
            # here con is a variable and connect is the methoad and other are inside the bracket are argument
            cur = con.cursor()  # cusro is something which will help us to do the function for eg (add,update,delete,etc)
            cur.execute("select * from login")  # by the execute method you can execute the query of your choice
            rows = cur.fetchall()
            print(rows)

        except Exception as ex:
            tmsg.showerror("Error", f"Error due to : {str(ex)} ")

    def register(self):
        if self.var_email_id.get() == "" or self.var_DOB.get() == "" or self.var_contact.get() == "" or self.clicked.get() == "" or self.gender_var.get() == ""or self.company_code.get() == "" or self.var_password.get() == "" or self.var_confirm_password.get() == "":
            tmsg.showerror("Error", "Employee detials are must required")
        elif self.var_password.get()!=self.var_confirm_password.get():
            tmsg.showerror("Error","password and confirm password should be same")
            self.var_password.set("") or self.var_confirm_password.set("")
        elif self.clicked.get()=="select your favrouite question":
                tmsg.showerror("Error","Select your favourite Question")
        elif self.company_code.get()!=self.n:
            tmsg.showerror("Error","Invalid Company Code")
        else:

            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from login where email_id=%s", self.var_email_id.get())
                row = cur.fetchone()  # if the data is alredy present inside the data base then it will return the hole column
                # if the data is not present into the the data base then it will return None as the output
                # print(row)
                if row != None:
                    tmsg.showerror("Error",
                                   "This Employee Email is already has avilable in our record, try again with another ID",
                                   parent=self.root)
                else:
                    cur.execute(
                        "insert into login values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (

                            self.var_email_id.get(),
                            self.var_DOB.get(),
                            self.var_contact.get(),
                            self.clicked.get(),
                            self.fav_question_answer.get(),
                            self.gender_var.get(),
                            self.company_code.get(),
                            self.var_password.get(),
                            self.var_confirm_password.get(),

                        )
                        )  # execute is closing here
                    print(self.fav_question_answer.get())
                    con.commit()
                    con.close()

                    tmsg.showinfo("Success", "Your Registation is successfully Done",parent=self.root)
                    self.reset()

                    # self.btn_print.config(state=NORMAL)  # after add it will  print button will get normal
            except Exception as ex:
                tmsg.showerror("Error", f"Error due to : {str(ex)} ")

    def securit_code(self):

        self.n = str(random.randint(10000,
                               100000))  # this random module for giving the security code from the compand into the company this will work


        # billinarie's hired wife
        # only on pocet FM

        if self.txt_email.get()=="":
            tmsg.showerror("Error","Please enter your email Id for registation")


        else:





            try:
                    sender_email = "prabhatjaiswar01@gmail.com"
                    rec_email = f"{self.txt_email.get()}"
                    psd = "********"   #here my gmail password is there
                    message = f"Hey ,this is Yeduvantas technology and your Company Security code is {self.n}"
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender_email, psd)
                    # print("login successfully")
                    server.sendmail(sender_email, rec_email, message)
                    # self.B1_registation.config(state=NORMAL)
                    tmsg.showinfo("Sucess",f"Company Code is send to this email id :{self.txt_email.get()} ")


            except Exception as ex:
                tmsg.showerror("Error","Invalid Email ID,Code is send only valid Email ID")
                # tmsg.showerror("Error", f"Error due to : {str(ex)}")  #this line is for getting the erros to send the message


if __name__ == '__main__':
    root = Tk()
    obj = Regestation(root)
    root.mainloop()