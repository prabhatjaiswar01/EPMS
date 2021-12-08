from tkinter import *
def regestation():
    screen1=Toplevel(screen)
    screen.geometry("300x250")
    screen.title("Notes 1.0")
def login():
    pass

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text="Notes 1.0",bg="grey",width="300",height="2",font=("Calibri",13)).pack()
    Button(text="Login",width="30",height="2",command=login).pack()
    Label(text="").pack()
    Button(text="Rigestation",width="30",height="2",command=regestation).pack()
    screen.mainloop()
if __name__ == '__main__':
    main_screen()
