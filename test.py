from tkinter import *
from PIL import Image,ImageTk
import pymysql
from  tkinter import messagebox as tmsg,ttk
import os,re

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Screen")
        self.root.geometry("1350x900+0+0")
        self.root.config(bg="white")


        Logo_label = Label(root, text="WELCOME TO ADMIN SCREEN  ", font=("times new roman", 50, "bold"), bd=5, relief=SUNKEN, fg="black",
                           bg="springgreen").place(x=0, y=0, width=1350)  # (x=96,y=300)

        Logo_label = Label(root, text="Data Area", font=("times new roman", 50, "bold"), bd=5,
                           relief=SUNKEN, fg="black",
                           bg="cyan").place(x=800, y=90, width=550)

        # B1=Button(text="Check login details")

        self.Information()


     #++++++++++++++++++++++++++++++++ALL FUNCTION START HERE++++++++++++++++++++++++++++++++++++++++++++++++++
    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')#here we making the connection with the database
                                 #here con is a variable and connect is the method and other are inside the bracket are argument
            cur=con.cursor()    #cusro is something which will help us to do the function for eg (add,update,delete,etc)
            cur.execute("select * from login") #by the execute method you can execute the query of your choice
            rows=cur.fetchall()
            # print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())  #By the * we are defing its child elements
            for i in rows:
                self.employee_tree.insert('',END,values=i)
            con.close()
        except Exception as ex:
            tmsg.showerror("Error",f"Error due to : {str(ex) } ")


    def Information(self):
        login_frame = Frame(self.root, bg="ivory", bd=3, relief=GROOVE)  # white smoke
        # login_frame.place(x=460,y=70,width=465,height=400)
        login_frame.place(x=800, y=178, width=550, height=517)
        scrolly = Scrollbar(login_frame, orient=VERTICAL)
        scrollx = Scrollbar(login_frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)  # we set the horizontal scroll bar
        scrolly.pack(side=RIGHT, fill=Y)  # we set the vertical scroll bar

        self.employee_tree = ttk.Treeview(login_frame, columns=('email_id', 'dob', 'contact', 'favourite_question',
                                                               'favourite_answer', 'gender','security_code', 'password', 'confirm_password'),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        # in upper line we simply attching our scrollbar at x and y axis on the new window

        self.employee_tree.heading('email_id', text='EID')  # here we are givig the heading name to our table
        self.employee_tree.heading('dob', text='DOB')
        self.employee_tree.heading('contact', text='CONTACT')
        self.employee_tree.heading('favourite_question', text='FAVOURITE_QUESTION')
        self.employee_tree.heading('favourite_answer', text='FAVOURITE_ANSWER')
        self.employee_tree.heading('gender', text='GENDER')
        self.employee_tree.heading('security_code', text='SECURITY_CODE')
        self.employee_tree.heading('password', text='PASSWORD')
        self.employee_tree.heading('confirm_password', text='CONFIRM_PASSWORD')


        self.employee_tree['show'] = 'headings'

        self.employee_tree.column('email_id', width=200)
        self.employee_tree.column('dob', width=100)
        self.employee_tree.column('contact', width=100)
        self.employee_tree.column('favourite_question', width=130)
        self.employee_tree.column('favourite_answer', width=100)
        self.employee_tree.column('gender', width=100)
        self.employee_tree.column('security_code', width=100)
        self.employee_tree.column('password', width=100)
        self.employee_tree.column('confirm_password', width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH, expand=1)
        self.show()




if __name__ == '__main__':
   root=Tk()
   obj=Login(root)
   root.mainloop()