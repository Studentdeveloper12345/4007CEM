import random
import time
import datetime
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image  # pip install pillow
import tkinter.filedialog
import pandas as pd
import numpy as np
import sqlite3 as sql
import matplotlib.pyplot as plt
from tkcalendar import Calendar
import sqlite3
import string
from tkinter import Tk, Label, Entry, Button, END
import requests
import datetime
from tkcalendar import DateEntry

def main():
    root = Tk()
    app = LoginForm(root)
    root.mainloop()

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        root_height = 750
        root_width = 1350
        
          # Maximizing the page
        self.root.resizable(0, 0)  # Delete the restore button
        root_height = 750
        root_width = 1500

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))
        # ==================== For Login ================
        self.inputusername = StringVar()
        self.inputpassword = StringVar()
              
        # ================= Background Image =================
        self.bg_frame = Image.open('Save.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # ================= Login Frame =================
        self.lgn_frame = Frame(self.root, bg='#040405', width='700', height=600)  # Color and the size of the frame
        self.lgn_frame.place(x=450, y=130)  # Placement of the frame

        self.txt = 'WELCOME'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=20, y=30, width=300, height=30)        
      # ================= Left Side Image =================
        self.side_image = Image.open('download.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=25, y=100)

        # ================= Username Icon =================
        self.username_icon = Image.open('username.jpg')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=300, y=125)
        
        # ================= Username =================
        self.username_label = Label(self.lgn_frame, text='Username', bg='#040405',font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
        self.username_label.place(x=300, y=100)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'),textvariable= self.inputusername)
        self.username_entry.place(x=325, y=125, width=170)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=300, y=150)
            
        
        # ================= Password Icon =================
        self.password_icon = Image.open('password.jpg')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=300, y=225)
        
        # ================= Password =================
        self.password_label = Label(self.lgn_frame, text='Password', bg='#040405', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
        self.password_label.place(x=300, y=200)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'), textvariable=self.inputpassword,show='*')
        self.password_entry.place(x=325, y=225, width=270)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=300, y=250)
                     

        # ================= Login Button =================
        self.lgn_button = Image.open('login.jpg')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=30, y=500)

        self.login = Button(self.lgn_button_label, text='LOGIN', font=('yu gothic ui', 13, 'bold'), width=25, bd=0,
                            bg='#0080b3', cursor='hand2', activebackground='#0080b3', fg='white',command=self.login_system)
        self.login.place(x=20, y=10)
            
       # ================= Register Button ================
        self.re_button = Image.open('register.jpg')
        photo = ImageTk.PhotoImage(self.re_button)
        self.re_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.re_button_label.image = photo
        self.re_button_label.place(x=350, y=500)

        self.register = Button(self.re_button_label, text='REGISTER', font=('yu gothic ui', 13, 'bold'), width=25, bd=0,
                            bg='#0080b3', cursor='hand2', activebackground='#0080b3', fg='white',command=self.register) 
        self.register.place(x=20, y=10)
        
        # ================= Show/Hide Password in login form=================
        self.show_image = Image.open('show.jpg')
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=575, y=225)

        self.hide_image = Image.open('hide.jpg')
        self.photo = ImageTk.PhotoImage(self.hide_image)
        
   
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.photo, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.hide)
        self.hide_button.image = self.photo
        self.hide_button.place(x=575, y=225)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=575, y=225)
        self.password_entry.config(show='*')
        
# ================= Going to the register window =================
    def register(self):
        self.newWindow = Toplevel(self.root)
        self.app=RegisterForm(self.newWindow)
   #For creating login system
    def login_system(self):
        user = self.inputusername.get()
        pswd = self.inputpassword.get()
        conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')   
        with conn:
            cursor=conn.cursor()
        cursor.execute('SELECT * FROM Login_user where username=? AND password=?',(user,pswd)) #Copy the file name e.g.C:/Users/User/OneDrive/Desktop/money.db
        row=cursor.fetchall()
        if row:
            messagebox.showinfo('Info', 'Proceed to captcha for successful login')
            #=================Captcha============
            list1=[]
            for i in range(65,91):
                word=chr(i)
                list1.append(word)
            for m in range(97,123):
                word=chr(m)
                list1.append(word)
            for j in range(0,10):
                list1.append(j)
            window=tkinter.Tk()
            window.title("Captcha generator.")
            frame=tkinter.LabelFrame(window,text="CAPTCHA",background="sky blue")
            frame.pack()
            ans=random.choices(list1, k=6)
            l=tkinter.Label(frame,text=ans,foreground="Black",background="sky blue", font=("Comic Sans MS",40))
            l.grid(row=0,column=0)
            e=tkinter.StringVar(value='')
            e1=tkinter.Entry(frame,width=12,textvariable=e,foreground="Indigo",background="white",font=("Consolas",15))
            e1.grid(row=2,column=0)
            e1.focus()
            l=tkinter.Label(frame,text="Please answer this captcha.", foreground="Black",background="Sky blue",font=("Consolas",15))
            l.grid(row=1,column=0)
            main=""
            for i in ans:
                main=main+str(i)
            def ans_check():
                if main == str(e1.get()):
                    messagebox.showinfo("Success", "Login success.")
                    window.destroy()
                    self.newWindow = Toplevel(self.root)
                    self.app=UserHome(self.newWindow)
                else:
                    messagebox.showinfo("Error","Wrong!")
                    window.destroy()                   
                
            btn=tkinter.Button(frame,text="Go",foreground="black",background="#B66DFF",command=ans_check,font=("Consolas",15))
            btn.grid(row=2,column=2)

        elif self.inputusername.get()=="" or self.inputpassword.get()=="":
            messagebox.showinfo('Info', 'Both must be required to fill up.')            
        else:
            messagebox.showinfo('Sorry', 'Wrong username or password')
        conn.commit()       

        
class RegisterForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        root_height = 750
        root_width = 1350
        
          # Maximizing the page
        self.root.resizable(0, 0)  # Delete the restore button
        root_height = 750
        root_width = 1500

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))
            # ==================== For Register==========
        self.regusername = StringVar()
        self.regpassword = StringVar()
        self.regtrypassword = StringVar()

   
        # ================= Background Image =================
        self.bg_frame = Image.open('Save.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        
         # ================= Register Frame =================
        self.re_frame = Frame(self.root, bg='#040405', width='500', height=600)  # Color and the size of the frame
        self.re_frame.place(x=525, y=130)  # Placement of the frame

        self.retxt = 'REGISTER'
        self.reheading = Label(self.re_frame, text=self.retxt, font=('yu gothic ui', 25, 'bold'), bg='#040405', fg='white')
        self.reheading.place(x=20, y=30, width=300, height=45)

        # ================= Username Icon For Register =========
        self.reusername_icon = Image.open('username.jpg')
        photo = ImageTk.PhotoImage(self.reusername_icon)
        self.reusername_icon_label = Label(self.re_frame, image=photo, bg='#040405')
        self.reusername_icon_label.image = photo
        self.reusername_icon_label.place(x=100, y=125)
        
         # =================== UserName Register ===========
        self.reusername_label = Label(self.re_frame, text='Username', bg='#040405',font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
        self.reusername_label.place(x=100, y=100)

        self.reusername_entry = Entry(self.re_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'),textvariable= self.regusername)
        self.reusername_entry.place(x=125, y=125, width=170)

        self.reusername_line = Canvas(self.re_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.reusername_line.place(x=100, y=150)
        
         # ================= Password Icon For Register=================
        self.repassword_icon = Image.open('password.jpg')
        photo = ImageTk.PhotoImage(self.repassword_icon)
        self.repassword_icon_label = Label(self.re_frame, image=photo, bg='#040405')
        self.repassword_icon_label.image = photo
        self.repassword_icon_label.place(x=100, y=225)
        
        # ================= Password Register=================
        self.repassword_label = Label(self.re_frame, text='Password', bg='#040405', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
        self.repassword_label.place(x=100, y=200)

        self.repassword_entry = Entry(self.re_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'), textvariable=self.regpassword,show='*')
        self.repassword_entry.place(x=125, y=225, width=270)

        self.repassword_line = Canvas(self.re_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.repassword_line.place(x=100, y=250)    
        
        # ================= Retry Password Icon For Register=================
        self.retrypassword_icon = Image.open('password.jpg')
        photo = ImageTk.PhotoImage(self.retrypassword_icon)
        self.retrypassword_icon_label = Label(self.re_frame, image=photo, bg='#040405')
        self.retrypassword_icon_label.image = photo
        self.retrypassword_icon_label.place(x=100, y=325)
        
        # ================= Retry Password Register=================
        self.retrypassword_label = Label(self.re_frame, text='Re-try Password', bg='#040405', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
        self.retrypassword_label.place(x=100, y=300)

        self.retrypassword_entry = Entry(self.re_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'), textvariable=self.regtrypassword,show='*')
        self.retrypassword_entry.place(x=125, y=325, width=270)

        self.retrypassword_line = Canvas(self.re_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.retrypassword_line.place(x=100, y=350) 
        
        
        # ================= Register Button in register frame================
        self.reg_button = Image.open('register.jpg')
        photo = ImageTk.PhotoImage(self.reg_button)
        self.reg_button_label = Label(self.re_frame, image=photo, bg='#040405')
        self.reg_button_label.image = photo
        self.reg_button_label.place(x=150, y=500)

        self.register = Button(self.reg_button_label, text='REGISTER', font=('yu gothic ui', 13, 'bold'), width=25, bd=0,
                            bg='#0080b3', cursor='hand2', activebackground='#0080b3', fg='white',command=self.database)
        self.register.place(x=20, y=10)

         # ================= Show/Hide Password in register form=================
        self.show_image = Image.open('show.jpg')
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(self.re_frame, image=self.photo1, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=400, y=225)

        self.hide_image = Image.open('hide.jpg')
        self.photo = ImageTk.PhotoImage(self.hide_image)

        
   
    def show(self):
        self.hide_button = Button(self.re_frame, image=self.photo, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.hide)
        self.hide_button.image = self.photo
        self.hide_button.place(x=400, y=225)
        self.repassword_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.re_frame, image=self.photo1, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=400, y=225)
        self.repassword_entry.config(show='*')
                 
    def database(self):
        #=========Register=====
       name1=self.regusername.get()
       repassword=self.regpassword.get()
       retrypassword=self.regtrypassword.get()
       conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#Copy the file name e.g.C:/Users/User/OneDrive/Desktop/money.db
       ##C:/Users/Dell/Desktop/Money/money.db
       if self.regusername.get()=="":
           messagebox.showinfo('Info', 'Please fill the username')
       elif self.regpassword.get()=="":
           messagebox.showinfo('Info', 'Please fill your new password')           
       elif self.regpassword.get()==self.regtrypassword.get():
           messagebox.showinfo('Info', 'Register success')
           with conn:
               cursor=conn.cursor()
           cursor.execute('CREATE TABLE IF NOT EXISTS Register_user (username TEXT,password TEXT,reenter_password TEXT)') 
           cursor.execute('INSERT INTO Register_user (username,password,reenter_password) VALUES(?,?,?)',(name1,repassword,retrypassword))
           cursor.execute('CREATE TABLE IF NOT EXISTS Login_user(username INT, password INT)')
           cursor.execute('INSERT INTO Login_user(username,password) VALUES(?,?)', (name1,repassword))
           self.newWindow = Toplevel(self.root)
           self.app=LoginForm(self.newWindow)
           self.root.destroy()
       else:
            messagebox.showinfo('Info', 'Register failed, please check your new password')
       conn.commit()
                            
class UserHome:
    def __init__(self,root):
        self.root = root
        self.root.title("User Home")
        root_height = 750
        root_width = 1350

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))
       
        self.root.configure(background = "light blue")
       
        self.LabelTitle = Label(self.root,text = "Welcome User!", font=("arial",35,"bold"), bd=10,relief="sunken")
        self.LabelTitle.place(x=510,y=40)
        #Homepage button Frame
        
        self.Homeframe2 = Frame(self.root,width=500,height=30,bd=10,relief="groove")
        self.Homeframe2.place(x=500,y=135)
        
        self.Homeframe3 = Frame(self.root,width=500,height=40,bd=10,relief="groove")
        self.Homeframe3.place(x=500,y=225)
        
        self.Homeframe4 = Frame(self.root,width=500,height=40,bd=10,relief="groove")
        self.Homeframe4.place(x=500,y=315)

        self.Homeframe5 = Frame(self.root,width=500,height=40,bd=10,relief="groove")
        self.Homeframe5.place(x=500,y=405)

        self.Homeframe6 = Frame(self.root,width=500,height=40,bd=10,relief="groove")
        self.Homeframe6.place(x=500,y=495)    

        self.Homeframe7 = Frame(self.root,width=500,height=40,bd=10,relief="groove")
        self.Homeframe7.place(x=1260,y=100)
        
        self.Homeframe8 = Frame(self.root,width=500,height=40,bd=10,relief="groove")
        self.Homeframe8.place(x=500,y=585)
 
        def signout():
            self.root.destroy()#Destroy window
                
        SignOut = Button(self.Homeframe7,width=5,padx= 5,bd=5, font=("arail",8, "bold"), bg = "blue",  text = "Sign Out", command =signout)#button detail
        SignOut.pack()#place button
        
        def UserExpenses():
            self.newWindow = Toplevel(self.root)
            self.app=Expenses_window(self.newWindow)
        
        Expense = Button(self.Homeframe2, bd=5, font=("arail",8, "bold"), bg = "blue", width=50,height=4, text = "Expenses", command =UserExpenses)
        Expense.pack()
        def currencycoverter():
            class Converter():
                def __init__(self, url):
                    self.data = requests.get(url).json()
                    self.currencies = self.data['rates']

                def convert(self, fcurrency, tcurrency, amount):
                    initial_amount = amount
                    if fcurrency != 'USD':
                        amount = amount / self.currencies[fcurrency]

                    amount = round(amount * self.currencies[tcurrency], 4)
                    return amount
            class App(tk.Tk):
                def __init__(self, converter):
                    tk.Tk.__init__(self)
                    self.title = 'Currency Converter'
                    self.currency_converter = converter

                    # self.configure(background = 'red')
                    self.geometry("500x200")

                     # ========Label==========
                    self.intro_label = Label(self, text ='   Welcome to the Currency Convertor   ', fg='red', relief=tk.RAISED, borderwidth=3)
                    self.intro_label.config(font=('Courier', 15, 'bold'))

                    self.date_label = Label(self, text=f"Date : {self.currency_converter.data['date']}", relief=tk.GROOVE, borderwidth=5)

                    self.intro_label.place(x=10, y=5)
                    self.date_label.place(x=160, y=50)
                    
    
                     # ===========Entry box==========
                    valid = (self.register(self.restrictNumberOnly), '%d', '%P')
                    self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER,validatecommand=valid)
                    self.converted_amount_field_label = Label(self, text='', fg='blue', bg='white', relief=tk.RIDGE, justify=tk.CENTER, width=17, borderwidth=3)

                                # =========dropdown========
                    self.from_currency_variable = StringVar(self)
                    self.from_currency_variable.set("INR")  # ==========default value=========
                    self.to_currency_variable = StringVar(self)
                    self.to_currency_variable.set("USD")  # =======default value========

                    font = ("Courier", 12, "bold")
                    self.option_add('*TCombobox*Listbox.font', font)
                    self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                                values=list(self.currency_converter.currencies.keys()), font=font,
                                                                state='readonly', width=12, justify=tk.CENTER)
                    self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                                values=list(self.currency_converter.currencies.keys()), font=font,
                                                                state='readonly', width=12, justify=tk.CENTER)

                                # ========placing=======
                    self.from_currency_dropdown.place(x=30, y=120)
                    self.amount_field.place(x=36, y=150)
                    self.to_currency_dropdown.place(x=340, y=120)
                    self.converted_amount_field_label.place(x=346, y=150)

                                # =======Convert button========
                    self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
                    self.convert_button.config(font=('Courier', 10, 'bold'))
                    self.convert_button.place(x=225, y=135)

                                #=======Exit button========
                    self.exit_button = Button(self, text="Exit",fg="black",command=self.exit)
                    self.exit_button.place(x=400,y=50)

                def exit(self):
                    self.destroy()

                def perform(self):
                    #=============Convert Function===============
                    try:
                        amount = float(self.amount_field.get())
                        from_curr = self.from_currency_variable.get()
                        to_curr = self.to_currency_variable.get()
                        converted = self.currency_converter.convert
                        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
                        converted_amount = round(converted_amount, 2)

                        self.converted_amount_field_label.config(text=str(converted_amount))

                        conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                        with conn:
                            cursor=conn.cursor()
                        cursor.execute('CREATE TABLE IF NOT EXISTS converter (OriginalAmount TEXT,OriginalCurrency TEXT, NewCurrency TEXT,NewAmount TEXT)')
                        cursor.execute('INSERT INTO converter (OriginalAmount,OriginalCurrency,NewCurrency,NewAmount) VALUES(?,?,?,?)',(amount,from_curr,to_curr,converted_amount))           
                        conn.commit()
                    except:
                        messagebox.showinfo('Info', 'Invalid, The entry must be filled with real numbers.')                   

                def restrictNumberOnly(self, action, string):
                    #=================Validation=====================
                    regex = regex.compile(r"[0-9,]*?(\.)?[0-9,]*$")
                    result = regex.match(string)
                    return (string == "" or (string.count('.') <= 1 and result is not None))
              
                        
            if __name__ == '__main__':
                url = 'https://api.exchangerate-api.com/v4/latest/USD'
                converter = Converter(url)
                App(converter)       
            
                        
        MultiCurrencyConverter = Button(self.Homeframe3, bd=5, font=("arail",8, "bold"), bg = "blue", width=50,height=5, text = "Multi-Currency Convertor", command=currencycoverter)
        MultiCurrencyConverter.pack()
        
        def PersonalGoals():
            self.newWindow = Toplevel(self.root)
            self.app=financialGoals_window(self.newWindow)
        
        PersonalGoals = Button(self.Homeframe4, bd=5, font=("arail",8, "bold"), bg = "blue", width=50,height=4, text = "Financial Goals", command =PersonalGoals)
        PersonalGoals.pack()

        def MoneyManagementTips():
            self.newWindow = Toplevel(self.root)
            self.app=MoneyManagementTips_window(self.newWindow)

        
        MoneyManagementTips = Button(self.Homeframe5, bd=5, font=("arail",8, "bold"), bg = "blue", width=50,height=4, text = "Money Management Tips", command =MoneyManagementTips)
        MoneyManagementTips.pack()

        def PersonalCustomerSupport():
            self.newWindow = Toplevel(self.root)
            self.app=PersonalCustomerSupport_window(self.newWindow)
        
        PersonalCustomerSupport = Button(self.Homeframe6, bd=5, font=("arail",8, "bold"), bg = "blue", width=50,height=4, text = "Personal Customer Support", command =PersonalCustomerSupport)
        PersonalCustomerSupport.pack() 
        
        def Analysis():
            self.newWindow = Toplevel(self.root)
            self.app=Analysis_window(self.newWindow)
        
        Analysis = Button(self.Homeframe8, bd=5, font=("arail",8, "bold"), bg = "blue", width=50,height=4, text = "Analysis", command =Analysis)
        Analysis.pack()                

class MoneyManagementTips_window:
    def __init__(self,root):
        self.root = root   
        self.root.geometry('520x620')
        self.root.title("Money Management System Tips")
        self.root.configure(background='cyan')
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        w = 630
        h = 650
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.update()
        canvas = Canvas(root, bg="cyan", width=root.winfo_width(), height=root.winfo_height())
        canvas.pack()

        def go_back():
            root.destroy()

        def chat_bot():
            root = Tk()
            root.title("Chatbot")
            
            BG_GRAY = "#ABB2B9"
            BG_COLOR = "#17202A"
            TEXT_COLOR = "#EAECEE"
            
            FONT = "Helvetica 14"
            FONT_BOLD = "Helvetica 13 bold"
            
            # Send function
            def send():
                send = "User -> " + e.get()
                txt.insert(END, "\n" + send)
            
                user = e.get().lower()
            
                if (user == 'hello' or user == 'hello?' or user == 'hello!' or user == 'hi!' or user == 'hi' or user == 'hi?' or user == 'is anyone here' or user == 'is anyone here?' or user == 'is anyone here!'):
                    txt.insert(END, "\n" + "Bot -> Hi,user.How can i assist you?\nSelection (Choose 1 and it will direct you to that point)\nExpenses\nCurrency Convertor\nFinancial goals\nTips\nCustomer support\nStatistics")
                elif (user == 'bye' or user == 'thank you'):
                    txt.insert(END,"\n" + "Bot -> Have a nice day")
                
                if (user == 'expenses'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> How do I display my expenses values in bill area?")
                    txt.insert(END,"\n" + "Bot -> You are required to fill up all the entry values first.Then use the generate bill button to generate your values in bill area.")
                    txt.insert(END,"\n" + "User -> How to total up all expenses?")
                    txt.insert(END,"\n" + "Bot -> You are required to fill up all the values first based on each category.Then use the total button to calculate each category amount.")
                    txt.insert(END,"\n" + "User -> How to use the savings calculator?")
                    txt.insert(END,"\n" + "Bot -> To use the calculator,please go to expenses page and click the calculator button. Further explanation on the usage of calculator can obtained from tips page.")   
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == 'no'):
                    txt.insert(END, "\n" + "Bot -> Hi,user.How can i assist you?\nSelection (Choose 1 and it will direct you to that point)\nExpenses\nCurrency Convertor\nFinancial goals\nTips\nCustomer support\nStatistics")
                elif (user=='yes'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                elif (user == 'financial goals'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> Where can I view my financial goals?")
                    txt.insert(END,"\n" + "Bot -> You can reach out to personal goals in the main menu.")
                    txt.insert(END,"\n" + "User -> How to calculate my financial goals?")
                    txt.insert(END,"\n" + "Bot -> To view all tips/customer support for financial goals,please go to tips/customer page for further explanation.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == 'statistics'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> I would to view expenses spend by category statistics?")
                    txt.insert(END,"\n" + "Bot -> To view this statistics graph,please go to the money analytics menu and select the expenses spend by category button. This will require you to choose monthly or yearly option and generate the graph based on the option.")
                    txt.insert(END,"\n" + "User -> I  would like to view my total necessities statistics based on monthly/yearly")
                    txt.insert(END,"\n" + "Bot -> To view this statistics graph,please go to the money analytics menu and select the sum of total necessities expenses button. This will require you to choose monthly or yearly option and generate the graph based on the option.")
                    txt.insert(END,"\n" + "Bot -> To view all tips/customer support for statistics,please go to tips/customer page for further explanation.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == 'currency convertor'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> How do I change my current and new currency in this system?")
                    txt.insert(END,"\n" + "Bot -> To change your current and new currency, simply choose a currency option from the option box.")
                    txt.insert(END,"\n" + "User -> How to convert my value based on currency?")
                    txt.insert(END,"\n" + "Bot -> To convert your value based on currency,please use the convert button in currency convertor page.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == 'customer support'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> I require assistance on  usage of calculator in expenses page. How do I get the monthly balance based on monthly salary and expenses?")
                    txt.insert(END,"\n" + "Bot -> Here are guidance I can provide for calculator. To get the monthly balance,you are required to fill in the values for monthly salary and all three expenses which is total necessities,total savings and total non-essential first.Then use the monthly balance button to calculate the amount.")
                    txt.insert(END,"\n" + "User -> How do I change my current and new currency in this system?")
                    txt.insert(END,"\n" + "Bot -> I want to clear all my values in the expenses page.")
                    txt.insert(END,"\n" + "User -> To clear values,please use the clear button in the expenses page. This will directly remove all previous unwanted values in the expenses page.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == 'tips'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> I would like to view all tips in the system.")
                    txt.insert(END,"\n" + "Bot -> Sure,the what kind of tips would you like to view? Please choose 1.(Selection)\n1) Expenses tips\n2) Financial goals tips\n3) Statistics tips")
                elif (user == '1'):
                    txt.insert(END,"\n" + "Bot -> Here are the tips that I obtained for expenses so far:\nOnce you know how much money you have coming in, the next step is to figure out where its going.\nTracking and categorizing your expenses can help you determine what you are spending the most money on and where it might be easiest to save.\nBeing aware of our spending habits is the best way of utilizing our money.\nWhen you know how much money you spend, it’s easy to balance your income with your spending and even save for the future. \nIf you operate a budget; (daily, monthly or even annual), the best way of ensuring that your spending is within the budget is by tracking your spending. \nWhen you track your spending, you know where your money goes and you can ensure that your money is used wisely. \nOur expenses page allow you to note down all the expenses you made easily.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == '2'):
                    txt.insert(END,"\n" + "Bot -> Here are the tips that I obtained for Financial goals so far:\nHaving a goal will change how you look at your money. \nYou’ll start to see how every decision you make matters to your greater financial health.\nFor example, if you don’t have financial goals, it’s no big deal to buy Starbucks every day.\n But let’s look at just how much those lattes are really costing you. \nYou’ll typically spend $25 for just one workweek of lattes—that’s $100 a month! What else could you do with that money? \nOur finanial goals for saving allow you to set the type of your goal either its for retirement or long term savings and also able to update it easily !")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == '3'):
                    txt.insert(END,"\n" + "Bot -> Here are the tips that I obtained for Statistics so far:\nEffective decision-making is crucial to the success of any future plans. \nUnfortunately, the opposite is also true: failure to establish a culture that fosters effective, evidence-based decision-making can be crippling. \nThis is why reading statistic is very important, one can able to tell which part needs to be strengthen and which part need to weaken by\n reading the statistic graph. \nOur statistic graph will able to let you see the graph of sum of your total necessities, total savings and total non-essential expenses that \nchanges over the month, and you can also see the final expenses breakdown graph.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")


                    

                e.delete(0,END)
            
            
            Label1= Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)
            
            txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=115)
            txt.grid(row=1, column=0, columnspan=2)
            
            scrollbar = Scrollbar(txt)
            scrollbar.place(relheight=1, relx=0.974)

            
            e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
            e.grid(row=2, column=0)
            
            send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                        command=send).grid(row=2, column=1)
            
            root.mainloop()

        for i in range(0, 21):
            if i ==0:
                Tips = """Tips for how to plan the budget"""
                ff =("times",20,"bold")
                y = 20
            if i == 1 : 
                Tips = """First, why you should save money and plan the budget"""
                ff = ("times",12,"bold")
                y = 80
            elif i == 2 :
                Tips = """The importance of saving money is simple: It allows you to enjoy greater security in your life. If you have cash set aside for emergencies, you have a fallback should something unexpected happen. And, if you have savings set aside for discretionary expenses, you may be able to take risks or try new things. This app will come in handy in every way, you will be able to plan your saving plan with this app easily!"""
                ff = ("times",10)
                y += 60
            elif i == 3:
                Tips ="""Next, track your spending"""
                ff = ("times",12,"bold")
                y += 80
            elif i == 4 :
                Tips ="""Once you know how much money you have coming in, the next step is to figure out where it’s going. Tracking and categorizing your expenses can help you determine what you are spending the most money on and where it might be easiest to save.Being aware of our spending habits is the best way of utilizing our money. When you know how much money you spend, it’s easy to balance your income with your spending and even save for the future. If you operate a budget; (daily, monthly or even annual), the best way of ensuring that your spending is within the budget is by tracking your spending. When you track your spending, you know where your money goes and you can ensure that your money is used wisely. Our expenses page allow you to note down all the expenses you made easily."""
                ff = ("times",10)
                y += 100
            elif i == 5:
                Tips ="""Separate Needs and Wants"""
                ff = ("times",12,"bold")
                y += 120
            elif i == 6 :
                Tips ="""Ask yourself: Do I want this or do I need it? Set clear priorities for yourself and the decisions become easier to make."""
                ff = ("times",10)
                y += 40
            elif i == 7:
                Tips = """Setting a realistic financial goals"""
                ff = ("times",12,"bold")
                y += 60
            elif i == 8:
                Tips = """Having a goal will change how you look at your money. You’ll start to see how every decision you make matters to your greater financial health.For example, if you don’t have financial goals, it’s no big deal to buy Starbucks every day. But let’s look at just how much those lattes are really costing you. You’ll typically spend $25 for just one workweek of lattes—that’s $100 a month! What else could you do with that money? Our finanial goals for saving allow you to set the type of your goal either its for retirement or long term savings and also able to update it easily !"""
                ff = ("times",10)
                y += 80
            elif i == 9:
                Tips = """Looking at a statistic graph"""
                ff = ("times",12,"bold")
                y += 100
            elif i == 10:
                Tips = """Effective decision-making is crucial to the success of any future plans. Unfortunately, the opposite is also true: failure to establish a culture that fosters effective, evidence-based decision-making can be crippling. This is why reading a statistic is very important, one can able to tell which part needs to be strengthen and which part need to weaken by reading the statistic graph. Our statistic graph will able to let you see the graph of sum of your total necessities, total savings and total non-essential expenses that changes over the month, and you can also see the final expenses breakdown graph."""
                ff = ("times",10)
                y += 90
            elif i == 11:
                Tips = """Adjust your spending to stay on budget"""
                ff = ("times",12,"bold")
                y += 100
            elif i == 12:
                Tips = """Now that you’ve documented your income and spending, you can make any necessary adjustments so that you don’t overspend and have money to put toward your goals. Look toward your “wants” as the first area for cuts. Can you skip movie night in favor of a movie at home? If you’ve already adjusted your spending on wants, take a closer look at your spending on monthly payments. On close inspection a “need” may just be a “hard to part with."""
                ff = ("times",10)
                y += 80
            elif i == 13:
                Tips = """Review your budget regularly"""
                ff = ("times",12,"bold")
                y += 80
            elif i == 14:
                Tips = """Once your budget is set, it’s important to review it and your spending on a regular basis to be sure you are staying on track. Few elements of your budget are set in stone: You may get a raise, your expenses may change or you may reach a goal and want to plan for a new one."""
                ff = ("times",10)
                y += 60
            elif i == 15:
                Tips = """Put Your Plan Into Action"""
                ff = ("times",12,"bold")
                y += 60
            elif i == 16:
                Tips = """Match your spending to when you receive your income. Decide ahead of time what you’ll use each pay cheque for. This will protect you from going into debt further because you won’t rely on credit to pay for your living expenses."""
                ff = ("times",10)
                y += 60

            label = Label(root, text=Tips,font=ff,justify=LEFT,bg='cyan', wraplength=450)
            canvas.create_window(70, y, window=label, anchor=W)

            scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
            scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
            canvas.config(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox("all"))

            # log out and go back buttons
            back_btn = Button(root, text='Go Back',command=go_back,width=15,font=("times",12,"bold"))
            back_btn.place(x=460,y=100)
            chat_btn = Button(root, text='Chat Bot',command=chat_bot,width=15,font=("times",12,"bold"))
            chat_btn.place(x=460,y=200)

class PersonalCustomerSupport_window:
    def __init__(self,root):
        self.root = root   
        self.root.geometry('520x620')
        self.root.title("Money Management System")
        self.root.configure(background='cyan')
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        w = 630
        h = 650
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.update()
        canvas = Canvas(root, bg="cyan", width=root.winfo_width(), height=root.winfo_height())
        canvas.pack()

        def go_back():
            root.destroy()

        def chat_bot():
            root = Tk()
            root.title("Chatbot")
            
            BG_GRAY = "#ABB2B9"
            BG_COLOR = "#17202A"
            TEXT_COLOR = "#EAECEE"
            
            FONT = "Helvetica 14"
            FONT_BOLD = "Helvetica 13 bold"
            
            # Send function
            def send():
                send = "User -> " + e.get()
                txt.insert(END, "\n" + send)
            
                user = e.get().lower()
            
                if (user == 'hello' or user == 'hello?' or user == 'hello!' or user == 'hi!' or user == 'hi' or user == 'hi?' or user == 'is anyone here' or user == 'is anyone here?' or user == 'is anyone here!'):
                    txt.insert(END, "\n" + "Bot -> Hi,user.How can i assist you?\nSelection (Choose 1 and it will direct you to that point)\nExpenses\nCurrency Convertor\nFinancial goals\nTips\nCustomer support\nStatistics")
                elif (user == 'bye' or user == 'thank you'):
                    txt.insert(END,"\n" + "Bot -> Have a nice day")
                
                if (user == 'expenses'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> How do I display my expenses values in bill area?")
                    txt.insert(END,"\n" + "Bot -> You are required to fill up all the entry values first.Then use the generate bill button to generate your values in bill area.")
                    txt.insert(END,"\n" + "User -> How to total up all expenses?")
                    txt.insert(END,"\n" + "Bot -> You are required to fill up all the values first based on each category.Then use the total button to calculate each category amount.")
                    txt.insert(END,"\n" + "User -> How to use the savings calculator?")
                    txt.insert(END,"\n" + "Bot -> To use the calculator,please go to expenses page and click the calculator button. Further explanation on the usage of calculator can obtained from tips page.")   
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == 'no'):
                    txt.insert(END, "\n" + "Bot -> Hi,user.How can i assist you?\nSelection (Choose 1 and it will direct you to that point)\nExpenses\nCurrency Convertor\nFinancial goals\nTips\nCustomer support\nStatistics")
                elif (user=='yes'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                elif (user == 'financial goals'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> Where can I view my financial goals?")
                    txt.insert(END,"\n" + "Bot -> You can reach out to personal goals in the main menu.")
                    txt.insert(END,"\n" + "User -> How to calculate my financial goals?")
                    txt.insert(END,"\n" + "Bot -> To view all tips/customer support for financial goals,please go to tips/customer page for further explanation.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == 'statistics'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> I would to view expenses spend by category statistics?")
                    txt.insert(END,"\n" + "Bot -> To view this statistics graph,please go to the money analytics menu and select the expenses spend by category button. This will require you to choose monthly or yearly option and generate the graph based on the option.")
                    txt.insert(END,"\n" + "User -> I  would like to view my total necessities statistics based on monthly/yearly")
                    txt.insert(END,"\n" + "Bot -> To view this statistics graph,please go to the money analytics menu and select the sum of total necessities expenses button. This will require you to choose monthly or yearly option and generate the graph based on the option.")
                    txt.insert(END,"\n" + "Bot -> To view all tips/customer support for statistics,please go to tips/customer page for further explanation.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == 'currency convertor'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> How do I change my current and new currency in this system?")
                    txt.insert(END,"\n" + "Bot -> To change your current and new currency, simply choose a currency option from the option box.")
                    txt.insert(END,"\n" + "User -> How to convert my value based on currency?")
                    txt.insert(END,"\n" + "Bot -> To convert your value based on currency,please use the convert button in currency convertor page.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == 'customer support'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> I require assistance on  usage of calculator in expenses page. How do I get the monthly balance based on monthly salary and expenses?")
                    txt.insert(END,"\n" + "Bot -> Here are guidance I can provide for calculator. To get the monthly balance,you are required to fill in the values for monthly salary and all three expenses which is total necessities,total savings and total non-essential first.Then use the monthly balance button to calculate the amount.")
                    txt.insert(END,"\n" + "User -> How do I change my current and new currency in this system?")
                    txt.insert(END,"\n" + "Bot -> I want to clear all my values in the expenses page.")
                    txt.insert(END,"\n" + "User -> To clear values,please use the clear button in the expenses page. This will directly remove all previous unwanted values in the expenses page.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == 'tips'):
                    txt.insert(END,"\n" + "Bot -> What can I do for you?")
                    txt.insert(END,"\n" + "User -> I would like to view all tips in the system.")
                    txt.insert(END,"\n" + "Bot -> Sure,the what kind of tips would you like to view? Please choose 1.(Selection)\n1) Expenses tips\n2) Financial goals tips\n3) Statistics tips")
                elif (user == '1'):
                    txt.insert(END,"\n" + "Bot -> Here are the tips that I obtained for expenses so far:\nOnce you know how much money you have coming in, the next step is to figure out where its going.\nTracking and categorizing your expenses can help you determine what you are spending the most money on and where it might be easiest to save.\nBeing aware of our spending habits is the best way of utilizing our money.\nWhen you know how much money you spend, it’s easy to balance your income with your spending and even save for the future. \nIf you operate a budget; (daily, monthly or even annual), the best way of ensuring that your spending is within the budget is by tracking your spending. \nWhen you track your spending, you know where your money goes and you can ensure that your money is used wisely. \nOur expenses page allow you to note down all the expenses you made easily.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == '2'):
                    txt.insert(END,"\n" + "Bot -> Here are the tips that I obtained for Financial goals so far:\nHaving a goal will change how you look at your money. \nYou’ll start to see how every decision you make matters to your greater financial health.\nFor example, if you don’t have financial goals, it’s no big deal to buy Starbucks every day.\n But let’s look at just how much those lattes are really costing you. \nYou’ll typically spend $25 for just one workweek of lattes—that’s $100 a month! What else could you do with that money? \nOur finanial goals for saving allow you to set the type of your goal either its for retirement or long term savings and also able to update it easily !")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")
                elif (user == '3'):
                    txt.insert(END,"\n" + "Bot -> Here are the tips that I obtained for Statistics so far:\nEffective decision-making is crucial to the success of any future plans. \nUnfortunately, the opposite is also true: failure to establish a culture that fosters effective, evidence-based decision-making can be crippling. \nThis is why reading statistic is very important, one can able to tell which part needs to be strengthen and which part need to weaken by\n reading the statistic graph. \nOur statistic graph will able to let you see the graph of sum of your total necessities, total savings and total non-essential expenses that \nchanges over the month, and you can also see the final expenses breakdown graph.")
                    txt.insert(END,"\n" + "Bot -> Is there anything else I can do for you?\nYes\nNo")



                    

                e.delete(0,END)
            
            
            Label1= Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)
            
            txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=115)
            txt.grid(row=1, column=0, columnspan=2)
            
            scrollbar = Scrollbar(txt)
            scrollbar.place(relheight=1, relx=0.974)
            
            e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
            e.grid(row=2, column=0)
            
            send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                        command=send).grid(row=2, column=1)
            
            root.mainloop()

        for i in range(0, 21):
            if i ==0:
                Tips = """Support for how to use the system"""
                ff =("times",20,"bold")
                y = 20
            if i == 1 : 
                Tips = """How to login and register"""
                ff = ("times",12,"bold")
                y = 80
            elif i == 2 :
                Tips = """In order to register, you must enter the username and password that you preferable and make sure the re-enter password is the same as the password you entered the first time. Then proceed to the login page and enter the username and password, type in the correct captcha and click the login button."""
                ff = ("times",10)
                y += 60
            elif i == 3:
                Tips ="""How to calculate the expenses"""
                ff = ("times",12,"bold")
                y += 60
            elif i == 4 :
                Tips ="""Simply fill in all the amount accordingly, such as monthly and yearly salary, neccesities and non neccesities. Theres a calculator function for user to calculate complicated bills as well."""
                ff = ("times",10)
                y += 40
            elif i == 5:
                Tips ="""How to create the financial goals for savings"""
                ff = ("times",12,"bold")
                y += 60
            elif i == 6 :
                Tips ="""First, you can set the title of the goals you wan in the description box, then fill in the necessary information in the required amount and collected amount box and choose the target date and created date of the goal. Finally choose type of the goal and click submit."""
                ff = ("times",10)
                y += 60
            elif i == 7:
                Tips = """How to view the statistic"""
                ff = ("times",12,"bold")
                y += 60
            elif i == 8:
                Tips = """First select the start date and end date of the statistic you wish to see, then choose the statistic you wish to see from the filter and click submit."""
                ff = ("times",10)
                y += 40
            elif i == 9:
                Tips = """How to use the chatbot"""
                ff = ("times",12,"bold")
                y += 60
            elif i == 10:
                Tips = """You can find the chatbot at the bottom of tips and customer support. Click the chatbot and you may choose the option related to your question."""
                ff = ("times",10)
                y += 40
            elif i == 11:
                Tips = """How to use the real-time currency convertor"""
                ff = ("times",12,"bold")
                y += 60
            elif i == 12:
                Tips = """Enter the amount you wish to convert, then choose a currency from the first currency option and choose the currency you wish to convert."""
                ff = ("times",10)
                y += 40

            label = Label(root, text=Tips,font=ff,justify=LEFT,bg='cyan', wraplength=450)
            canvas.create_window(70, y, window=label, anchor=W)

            scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
            scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
            canvas.config(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox("all"))

            # log out and go back buttons
            back_btn = Button(root, text='Go Back',command=go_back,width=15,font=("times",12,"bold"))
            back_btn.place(x=460,y=100)
            chat_btn = Button(root, text='Chat Bot',command=chat_bot,width=15,font=("times",12,"bold"))
            chat_btn.place(x=460,y=200)
            
class Expenses_window:
    def __init__(self,root):
        self.root = root
        self.root.title("User Expenses")
        root_height = 750
        root_width = 1350

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

        self.root.config(bg = "light blue")
        
        #Salaries
        MonthlySalary = IntVar()
        YearlySalary = IntVar()
        DateStart=StringVar()
        DateFinish=StringVar()
        #Necessities
        Groceries = IntVar()
        Housing = IntVar()
        Transportation = IntVar()
        Insurance = IntVar()
        #Savings 
        Retirement = IntVar()
        LongTermSavings = IntVar()
        #Non-essential 
        Electronics = IntVar()
        Vacation = IntVar()
        Luxuries = IntVar()
        Pets = IntVar()
        #Total expenses
        Total_necessities_expenses= IntVar()
        Total_savings_expenses= IntVar()
        Total_non_essential_expenses= IntVar()
        Monthly_balance= IntVar()
        Yearly_balance= IntVar()
        

#==============================FRAMES======================================
        self.options_frame = Frame(self.root, bg='#040405', width='950', height=600)  # Color and the size of the frame
        self.options_frame.place(x=5, y=5)  # Placement of the frame   
        self.SalariesFrame = Frame(self.root, bd=2, width=1340, height=50, padx=18, pady=10,bg = "#C8A2C8", relief = RIDGE)
        self.SalariesFrame.place(x=5,y=75)
        self.NeccesitiesFrame = Frame(self.root, bd=2, width=280, height=350, padx=18, pady=10,bg = "#C8A2C8", relief = RIDGE)
        self.NeccesitiesFrame.place(x=5,y=130)
        self.SavingsFrame = Frame(self.root, bd=2, width=280, height=350, padx=25, pady=10,bg = "#C8A2C8", relief = RIDGE)
        self.SavingsFrame.place(x=305,y=130)
        self.Non_essentialFrame = Frame(self.root, bd=2, width=280, height=350, padx=30, pady=10,bg = "#C8A2C8", relief = RIDGE)
        self.Non_essentialFrame.place(x=605,y=130)
        self.Total_expensesFrame = Frame(self.root, bd=2, width=1340, height=200, padx=18, pady=10,bg = "#C8A2C8", relief = RIDGE)
        self.Total_expensesFrame.place(x=5,y=500)
        
        #===========Functions==========================
        def homeButton():
            self.root.destroy()#Destroy window
        def text():
            MonthlySalary.get()
            YearlySalary.get()
            DateStart.get()
            DateFinish.get()
            Groceries.get()
            Housing.get()
            Transportation.get()
            Insurance.get()
            Retirement.get()
            LongTermSavings.get()
            Electronics.get()
            Vacation.get()
            Luxuries.get()
            Pets.get()
            Total_necessities_expenses.get()
            Total_savings_expenses.get()
            Total_non_essential_expenses.get()
            Monthly_balance.get()
            Yearly_balance.get()


            
#=================================Buttons================================
        #Add button
        self.homebutton = Button(self.options_frame, text="Home",font = ('arial', 20 , 'bold'),height=0,width=10, bd =4,command=homeButton)
        self.homebutton.grid(row=0,column=0)

#===============================Text and Labels============================
        self.month_label = Label(self.SalariesFrame, text='Monthly Salary',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.month_label.place(x=5, y=1)
        self.month_entry = Entry(self.SalariesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable= MonthlySalary)
        self.month_entry.place(x=140, y=1, width=150)        
        self.year_label = Label(self.SalariesFrame, text='Yearly Salary',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.year_label.place(x=315, y=1)
        self.year_entry = Entry(self.SalariesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable= YearlySalary)
        self.year_entry.place(x=440, y=1, width=150)
        self.date_start_label = Label(self.SalariesFrame, text='Date start spend',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.date_start_label.place(x=615, y=1)
        self.date_start_entry = DateEntry(self.SalariesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=DateStart)
        self.date_start_entry.place(x=750, y=1, width=150)
        self.date_finish_label = Label(self.SalariesFrame, text='Date finish spend',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.date_finish_label.place(x=915, y=1)
        self.date_finish_entry = DateEntry(self.SalariesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=DateFinish)
        self.date_finish_entry.place(x=1060, y=1, width=150)
        
        #==================Necessities=======================#
        self.necessities_title = Label(self.NeccesitiesFrame, text='Necessities',font=("times new roman",13,"bold"),fg='#FFD700')
        self.necessities_title.place(x=85, y=1)
        self.groceries_label = Label(self.NeccesitiesFrame, text='Groceries',font=("times new roman",13,"bold"),fg='#4f4e4d')
        self.groceries_label.place(x=3, y=40)
        self.groceries_entry = Entry(self.NeccesitiesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable= Groceries)
        self.groceries_entry.place(x=145, y=40, width=100)
        self.housing_label = Label(self.NeccesitiesFrame, text='Housing',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.housing_label.place(x=3, y=90)
        self.housing_entry = Entry(self.NeccesitiesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Housing)
        self.housing_entry.place(x=145, y=90, width=100)
        self.transportation_label = Label(self.NeccesitiesFrame, text='Transportation',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.transportation_label.place(x=3, y=140)
        self.transportation_entry = Entry(self.NeccesitiesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Transportation)
        self.transportation_entry.place(x=145, y=140, width=100)
        self.insurance_label = Label(self.NeccesitiesFrame, text='Insurance',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.insurance_label.place(x=3, y=190)
        self.insurance_entry = Entry(self.NeccesitiesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Insurance)
        self.insurance_entry.place(x=145, y=190, width=100)    
        
        #==================Savings=======================#
        self.savings_title = Label(self.SavingsFrame, text='Savings',font=("times new roman",13,"bold"),fg='#FFD700')
        self.savings_title.place(x=85, y=1)
        self.retirement_label = Label(self.SavingsFrame, text='Retirement',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.retirement_label.place(x=3, y=40)
        self.retirement_entry = Entry(self.SavingsFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Retirement)
        self.retirement_entry.place(x=145, y=40, width=100)
        self.longtermsaving_label = Label(self.SavingsFrame, text='Long term saving',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.longtermsaving_label.place(x=3, y=90)
        self.longtermsaving_entry = Entry(self.SavingsFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=LongTermSavings)
        self.longtermsaving_entry.place(x=145, y=90, width=100)

        #==================Non-essential=======================#
        self.non_essential_title = Label(self.Non_essentialFrame, text='Non-essential',font=("times new roman",13,"bold"),fg='#FFD700')
        self.non_essential_title.place(x=85, y=1)
        self.electronics_label = Label(self.Non_essentialFrame, text='Electronics',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.electronics_label.place(x=1, y=40)
        self.electronics_entry = Entry(self.Non_essentialFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Electronics)
        self.electronics_entry.place(x=145, y=40, width=100)
        self.vacation_label = Label(self.Non_essentialFrame, text='Vacation',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.vacation_label.place(x=1, y=90)
        self.vacation_entry = Entry(self.Non_essentialFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Vacation)
        self.vacation_entry.place(x=145, y=90, width=100)
        self.luxuries_label = Label(self.Non_essentialFrame, text='Luxuries',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.luxuries_label.place(x=1, y=140)
        self.luxuries_entry = Entry(self.Non_essentialFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Luxuries)
        self.luxuries_entry.place(x=145, y=140, width=100)
        self.pets_label = Label(self.Non_essentialFrame, text='Pets',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.pets_label.place(x=1, y=190)
        self.pets_entry = Entry(self.Non_essentialFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Pets)
        self.pets_entry.place(x=145, y=190, width=100)

        
        #===============Total Necessities expenses==============#
        def total():
            try:
                self.Total_necessities_expenses = (
                    (Groceries.get()+ Housing.get()+ Transportation.get()+ Insurance.get())
                )
                Total_necessities_expenses.set(str(self.Total_necessities_expenses))
                self.Total_savings_expenses = (
                    (Retirement.get()+ LongTermSavings.get())
                )
                Total_savings_expenses.set(str(self.Total_savings_expenses))
                self.Total_non_essential_expenses = (
                    (Electronics.get()+ Vacation.get()+ Luxuries.get()+ Pets.get())
                )
                Total_non_essential_expenses.set(str(self.Total_non_essential_expenses))
            except:
                messagebox.showinfo('Info', 'Warning, The entry must be filled with real numbers.')                   


        def balance1():
            try:
                self.balance1=(
                    ((MonthlySalary.get()-Total_necessities_expenses.get()-Total_savings_expenses.get()-Total_non_essential_expenses.get()))
                )
                Monthly_balance.set(str(self.balance1))
            except:
                messagebox.showinfo('Info', 'Warning, The entry must be filled with real numbers.')                   

        def balance2():
            try:
                self.balance2=(
                    ((YearlySalary.get()-Total_necessities_expenses.get()-Total_savings_expenses.get()-Total_non_essential_expenses.get()))
                )
                Yearly_balance.set(str(self.balance2))
            except:
                messagebox.showinfo('Info', 'Warning, The entry must be filled with real numbers.')                   



        self.totalexpenses_title = Label(self.Total_expensesFrame, text='Total expenses',font=('yu gothic ui', 13, 'bold'),fg='#FFD700')
        self.totalexpenses_title.place(x=85, y=1)
        self.total_necessities_label = Label(self.Total_expensesFrame, text='Total necessities',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.total_necessities_label.place(x=3, y=40)
        self.total_necessities_entry = Entry(self.Total_expensesFrame,highlightthickness=0,relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Total_necessities_expenses)
        self.total_necessities_entry.place(x=165, y=40, width=100)
        self.total_savings_label = Label(self.Total_expensesFrame, text='Total savings',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.total_savings_label.place(x=3, y=90)
        self.total_savings_entry = Entry(self.Total_expensesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Total_savings_expenses)
        self.total_savings_entry.place(x=165, y=90, width=100)
        self.total_non_essential_label = Label(self.Total_expensesFrame, text='Total non-essential',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.total_non_essential_label.place(x=3, y=140)
        self.total_non_essential_entry = Entry(self.Total_expensesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Total_non_essential_expenses)
        self.total_non_essential_entry.place(x=165, y=140, width=100)
        self.monthly_balance_label = Label(self.Total_expensesFrame, text='Monthly Balance',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.monthly_balance_label.place(x=300, y=40)
        self.monthly_balance_entry = Entry(self.Total_expensesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Monthly_balance)
        self.monthly_balance_entry.place(x=450, y=40, width=100)
        self.yearly_balance_label = Label(self.Total_expensesFrame, text='Yearly Balance',font=('yu gothic ui', 13, 'bold'),fg='#4f4e4d')
        self.yearly_balance_label.place(x=300, y=90)
        self.yearly_balance_entry = Entry(self.Total_expensesFrame,highlightthickness=0, relief=GROOVE, bg='white', fg='#000000',font=('yu gothic ui', 13, 'bold'),textvariable=Yearly_balance)
        self.yearly_balance_entry.place(x=450, y=90, width=100)
        self.totalbutton=Button(self.Total_expensesFrame,text='Total all',fg ='#4f4e4d',font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command=total)
        self.totalbutton.place(x=605, y=90)
        self.balance1button=Button(self.Total_expensesFrame,text='Monthly Balance',fg ='#4f4e4d',font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command=balance1)
        self.balance1button.place(x=605, y=40)
        self.balance2button=Button(self.Total_expensesFrame,text='Yearly Balance',fg ='#4f4e4d',font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command=balance2)
        self.balance2button.place(x=805, y=40)
        
            
        #===================Expenses Area================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 130,width = 375,height = 380)
        #===========
        expenses_title = Label(F3,text = "Expenses Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        expenses_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)
        
        #========================
        def check_expenses():
            try:
                if DateStart.get()=="" or DateFinish.get()=="":
                    messagebox.showinfo('Info', 'Warning, The bill needs all entries to be filled in order to generate. Also, all entries must have a real numbers except the date.')
                else:
                    self.txt.delete('1.0',END)
                    self.txt.insert(END,"Expenses\n")
                    self.txt.insert(END,f"\nDate start expenses : {str(DateStart.get())}")
                    self.txt.insert(END,f"\nDate finish expenses : {str(DateFinish.get())}")
                    self.txt.insert(END,f"\nMonthly expenses : {str(MonthlySalary.get())}")
                    self.txt.insert(END,f"\nYearly expenses : {str(YearlySalary.get())}")
                    self.txt.insert(END,"\n=========================================")
                    self.txt.insert(END,"\nNo    Type      Price     Category ")
                    self.txt.insert(END,"\n=========================================")
                    self.txt.insert(END,f"\n1   Groceries       {Groceries.get()}      Necessities")
                    self.txt.insert(END,f"\n2   Housing         {Housing.get()}        Necessities")
                    self.txt.insert(END,f"\n3   Transportation  {Transportation.get()} Necessities")
                    self.txt.insert(END,f"\n4   Insurance       {Insurance.get()}      Necessities")
                    self.txt.insert(END,f"\n5   Retirement      {Retirement.get()}      Savings")
                    self.txt.insert(END,f"\n6   LongTermSavings {LongTermSavings.get()} Savings")
                    self.txt.insert(END,f"\n7   Electronics     {Electronics.get()}    Non-essential")
                    self.txt.insert(END,f"\n8   Vacation        {Vacation.get()}       Non-essential")
                    self.txt.insert(END,f"\n9   Luxuries        {Luxuries.get()}       Non-essential")
                    self.txt.insert(END,f"\n10  Pets            {Pets.get()}           Non-essential")
                    self.txt.insert(END,"\n=========================================")
                    self.txt.insert(END,f"\nTotal necessities : {int(Total_necessities_expenses.get())}")
                    self.txt.insert(END,f"\nTotal savings : {int(Total_savings_expenses.get())}")
                    self.txt.insert(END,f"\nTotal non-essential : {int(Total_non_essential_expenses.get())}")
                    self.txt.insert(END,f"\nMonthly Balance : {int(Monthly_balance.get())}")
                    self.txt.insert(END,f"\nYearly Balance : {int(Yearly_balance.get())}")
            except:
                messagebox.showinfo('Info', 'Warning, The bill needs all entries to be filled in order to generate. Also, all entries must have a real numbers except the date.')                   

        
        
        #Function to clear the bill area
        def clear():
            self.txt.delete('1.0',END)
          
        def reset(): 
            self.month_entry.delete(0,END)
            self.year_entry.delete(0,END)
            self.date_start_entry.delete(0,END)
            self.date_finish_entry.delete(0,END)
            self.groceries_entry.delete(0,END)
            self.housing_entry.delete(0,END)
            self.transportation_entry.delete(0,END)
            self.insurance_entry.delete(0,END)
            self.retirement_entry.delete(0,END)
            self.longtermsaving_entry.delete(0,END)
            self.electronics_entry.delete(0,END)
            self.vacation_entry.delete(0,END)
            self.luxuries_entry.delete(0,END)
            self.pets_entry.delete(0,END)
            self.total_necessities_entry.delete(0,END)
            self.total_savings_entry.delete(0,END)
            self.total_non_essential_entry.delete(0,END)
            self.monthly_balance_entry.delete(0,END)
            self.yearly_balance_entry.delete(0,END)

        self.genexpensesbutton = Button(self.Total_expensesFrame,text = "Generate Bill",fg ='#4f4e4d',font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command=check_expenses)
        self.genexpensesbutton.place(x=1005,y=40)
        self.clearbutton =Button(self.Total_expensesFrame, text='Clear bill',fg ='#4f4e4d',font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command=clear)
        self.clearbutton.place(x=1205, y=40)
        self.resetbutton=Button(self.Total_expensesFrame, text='Reset field',fg ='#4f4e4d',font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command=reset)
        self.resetbutton.place(x=805, y=90)
        


        #Function To Clear All Field  
        
        #Function to open Calculator in another frame   
        def Transaction():
            self.newWindow = Toplevel(self.root)
            self.app=Transaction(self.newWindow)
        
        self.Transactionbutton=Button(self.Total_expensesFrame,text='Transaction',fg ='#4f4e4d',font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command=Transaction)
        self.Transactionbutton.place(x=605, y=140)
        

        class Transaction():
              def __init__(self,root):
                self.root = root
                self.root.title("Transaction")
                self.root.resizable(0, 0) # Delete the restore button
                root_height = 530
                root_width =  350

                screen_width = self.root.winfo_screenwidth()
                screen_height = self.root.winfo_screenheight()

                x_cordinate = int((screen_width/2) - (root_width/2))
                y_cordinate = int((screen_height/2) - (root_height/2))

                self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))
                self.root.config(bg = "coral")

                #Variables
                v1 = tk.StringVar()
                v2 = tk.StringVar()
                v3 = tk.StringVar()
                v4 = tk.StringVar()
                v5 = tk.StringVar()
                v6 = tk.StringVar()
                v7 = tk.StringVar()
                v8 = tk.StringVar()
                v9 = tk.StringVar()

                self.TransactionFrame = Frame(self.root, bd=2, width=335, height=515, padx=20, pady=9,bg = "#0ABAB5", relief = RIDGE)
                self.TransactionFrame.place(x=5,y=0)

                def exit():
                    self.root.destroy()
     
                def clear_all():
                    e1.delete(0,tk.END)
                    e2.delete(0,tk.END)
                    e3.delete(0,tk.END)
                    e4.delete(0,tk.END)
                    e5.delete(0,tk.END)
                    e6.delete(0,tk.END)
                    e7.delete(0,tk.END)
                    e8.delete(0,tk.END)
                    e8.config(state='normal')
                    e9.delete(0,tk.END)
                    e9.config(state='normal')
                     
                def cal_monthly_balance():
                    try:
                        if e1.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="":
                            messagebox.showinfo('Info', 'The month entries need all entries to be filled with real numbers in order to calculate the monthly balance except year. For the date entry, it must be filled with only month')                   
                        else:
                            e8.config(state='normal')
                            e8.delete(0,tk.END)
                            e8.config(state='disabled')
                            Monthly_salary = int(e1.get())
                            total_expenses = (int(e3.get())+int(e4.get())+int(e5.get())) 
                            Monthly_balance = Monthly_salary - total_expenses 
                            e8.config(state='normal')
                            e8.insert(0,Monthly_balance)
                            e8.config(state='disabled')
                                
                            conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                            with conn:
                                cursor=conn.cursor()
                            cursor.execute('CREATE TABLE IF NOT EXISTS CALCULATOR (MonthlySalaries INT,YearlySalaries INT, TotalNecessities INT,TotalSavings INT, TotalNonEssential INT,Month VARCHAR, Year VARCHAR,MonthlyExpenses INT,YearlyExpenses INT)')
                            cursor.execute('INSERT INTO CALCULATOR (MonthlySalaries, TotalNecessities,TotalSavings, TotalNonEssential,Month,MonthlyExpenses) VALUES(?,?,?,?,?,?)',(e1.get(), e3.get(),e4.get(),e5.get(),e6.get(),e8.get()))           
                            conn.commit()
                    except:
                        messagebox.showinfo('Info', 'Invalid, The calculator needs all entries to be filled with real numbers in order to calculate the monthly balance. For the month date entry, it must be filled with only month')                   

        
                def cal_yearly_balance():
                    try:
                        if e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e7.get()=="":
                            messagebox.showinfo('Info', 'Warning, The year entries all entries to be filled with real numbers in order to calculate the monthly balance. For the date entry, it must be filled with month and year together')                   
                        else:
                            e9.config(state='normal')
                            e9.delete(0,tk.END)
                            e9.config(state='disabled')
                            Yearly_salary= int(e2.get())
                            total_expenses = (int(e3.get())+int(e4.get())+int(e5.get())) 
                            Yearly_balance = Yearly_salary - total_expenses 
                            e9.config(state='normal')
                            e9.insert(0,Yearly_balance)
                            e9.config(state='disabled')
                                
                            conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                            with conn:
                                cursor=conn.cursor()
                            cursor.execute('CREATE TABLE IF NOT EXISTS CALCULATOR1 (MonthlySalaries INT,YearlySalaries INT, TotalNecessities INT,TotalSavings INT, TotalNonEssential INT,Month VARCHAR, Year VARCHAR, MonthlyExpenses INT,YearlyExpenses INT)')
                            cursor.execute('INSERT INTO CALCULATOR1(YearlySalaries, TotalNecessities,TotalSavings, TotalNonEssential,Year,YearlyExpenses) VALUES(?,?,?,?,?,?)',(e2.get(), e3.get(),e4.get(),e5.get(),e7.get(),e9.get()))           
                            conn.commit()
                    except:
                        messagebox.showinfo('Info', 'Invalid, The calculator needs all entries to be filled with real numbers in order to calculate the yearly balance. For the date entry, it must be filled with month and year together')  
                l1 = tk.Label(self.TransactionFrame,text="Enter the Amount",font=("Arial,bold",20),fg="Black",bg="White")

                l2 = tk.Label(self.TransactionFrame,text="Monthly Salary",font=("Arial",10),fg="Black",bg="White")
                e1 = tk.Entry(self.TransactionFrame,font=("Arial,bold,11"),relief=GROOVE,textvariable=v1)
 
                l3 = tk.Label(self.TransactionFrame,text="Yearly Salary:",font=("Arial",10),fg="Black",bg="White")
                e2 = tk.Entry(self.TransactionFrame,font=("Arial",11),textvariable=v2)
 
                l4 = tk.Label(self.TransactionFrame,text="Total necessities:",font=("Arial",10),fg="Black",bg="White")
                e3 = tk.Entry(self.TransactionFrame,font=("Arial",11),textvariable=v3)
 
                l5 = tk.Label(self.TransactionFrame,text="Total savings:",font=("Arial",10),fg="Black",bg="White")
                e4 = tk.Entry(self.TransactionFrame,font=("Arial",11),textvariable=v4)

                l6= tk.Label(self.TransactionFrame,text="Total non-essential:",font=("Arial",10),fg="Black",bg="White")
                e5 = tk.Entry(self.TransactionFrame,font=("Arial",11),textvariable=v5)

                l7= tk.Label(self.TransactionFrame,text="Month:",font=("Arial",10),fg="Black",bg="White")
                e6 = tk.Entry(self.TransactionFrame,font=("Arial",11),textvariable=v6)

                l8= tk.Label(self.TransactionFrame,text="Year:",font=("Arial",10),fg="Black",bg="White")
                e7 = tk.Entry(self.TransactionFrame,font=("Arial",11),textvariable=v7)
 
                b1 = tk.Button(self.TransactionFrame,text="Calculate Monthly Balance",font=("Arial",12),relief=GROOVE,command=cal_monthly_balance)
                b2 = tk.Button(self.TransactionFrame,text="Calculate Yearly Balance",font=("Arial",12),relief=GROOVE,command=cal_yearly_balance)
 
                l9 = tk.Label(self.TransactionFrame,text="Monthly Balance:",font=("Arial",10),fg="Black",bg="White")
                e8 = tk.Entry(self.TransactionFrame,font=("Arial",11),state='disabled',textvariable=v8)

                l10 = tk.Label(self.TransactionFrame,text="Yearly Balance:",font=("Arial",10),fg="Black",bg="White")
                e9 = tk.Entry(self.TransactionFrame,font=("Arial",11),state='disabled',textvariable=v9)

                b3 = tk.Button(self.TransactionFrame,text="Clear Values",font=("Arial",15),command=clear_all)
                b4 = tk.Button(self.TransactionFrame,text="Exit Application",font=("Arial",15),command=exit)
 
                l1.place(x=40,y=10)
                l2.place(x=3,y=70)
                e1.place(x=140,y=70,width=110)
                l3.place(x=3,y=100)
                e2.place(x=140,y=100,width=110)
                l4.place(x=3,y=130)
                e3.place(x=140,y=130,width=110)
                l5.place(x=3,y=160)
                e4.place(x=140,y=160,width=110)
                l6.place(x=3,y=190)
                e5.place(x=140,y=190,width=110)
                l7.place(x=3,y=220)
                e6.place(x=140,y=220,width=110)
                l8.place(x=3,y=250)
                e7.place(x=140,y=250,width=110)
                l9.place(x=3,y=350)
                e8.place(x=140,y=350,width=110)
                l10.place(x=3,y=380)
                e9.place(x=140,y=380,width=110)
                b1.place(x=40,y=275)
                b2.place(x=40,y=315)
                b3.place(x=70,y=405)
                b4.place(x=60,y=455)
 
#Function to open Calculator in another frame   
        def Calculator():
            self.newWindow = Toplevel(self.root)
            self.app=Calculator(self.newWindow)
        
        self.Calculatorbutton=Button(self.Total_expensesFrame,text='Calculator',fg ='#4f4e4d',font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command=Calculator)
        self.Calculatorbutton.place(x=805, y=140)
        

        class Calculator():
            def __init__(self,root):
                self.root = root
                self.root.title("Calculator")
                self.root.resizable(0, 0) # Delete the restore button
                root_height = 312
                root_width =  324

                screen_width = self.root.winfo_screenwidth()
                screen_height = self.root.winfo_screenheight()

                x_cordinate = int((screen_width/2) - (root_width/2))
                y_cordinate = int((screen_height/2) - (root_height/2))

                self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))
                self.root.config(bg = "coral")

                # 'StringVar()' :It is used to get the instance of input field
 
                input_text = StringVar()
                global expression
 
                # Let us creating a frame for the input field
 
                input_frame = Frame(self.root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
                input_frame.pack(side=TOP)
            
                def btn_click(item):
                    global expression
                    expression = expression + str(item)
                    input_text.set(expression)

                # 'bt_clear' function :This is used to clear 
                # the input field

                def bt_clear(): 
                    global expression 
                    expression = "" 
                    input_text.set("")
 
                # 'bt_equal':This method calculates the expression 
                # present in input field
 
                def bt_equal():
                    global expression 
                    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
                    input_text.set(result)
                    expression = ""
                    
                expression = ""
                        
                
 
         
                #Let us create a input field inside the 'Frame'
 
                input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
                input_field.grid(row=0, column=0)
                input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
                #Let us creating another 'Frame' for the button below the 'input_frame'
 
                btns_frame = Frame(self.root, width=312, height=272.5, bg="grey")
                btns_frame.pack()
 
                # first row
 
                self.clearbutton = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
                divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
                # second row
 
                seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
                eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
                nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
                multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
                # third row
 
                four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
                five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
                six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
                minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
                # fourth row
 
                one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
                two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
                three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
                plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
                # fifth row
 
                zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
                point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
                equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

            
class financialGoals_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x1000+200+130")
        self.root.title("Financial Goals")
        self.root.config(bg="white")
        self.root.resizable(0,0) #Delete the restore button
        #==============Variables=============
        self.number=IntVar()
        self.description=StringVar()
        self.requiredamount=IntVar()
        self.collectedamount=IntVar()
        self.targetdate=StringVar()
        self.datecreated=StringVar()
        self.goals=StringVar()
        self.var_searchtxt=StringVar()
    
        #==================Labels==============
        lbl_title=Label(self.root,text="Financial Goals",font=("Times New Roman",15,"bold"),bg="#0f4d7d",fg="white").place(x=15,y=10,width=800,height=20)
        lbl_view=Label(self.root,text="View By Number",bg="white",font=("Times New Roman",10)).place(x=420,y=80)
        lbl_Number=Label(self.root,text="Number",bg="white",font=("Times New Roman",15)).place(x=50,y=40)
        lbl_description=Label(self.root,text="Description",bg="white",font=("Times New Roman",15)).place(x=50,y=80)
        lbl_required=Label(self.root,text="Required Amount",bg="white",font=("Times New Roman",15)).place(x=50,y=120)        
        lbl_collected=Label(self.root,text="Collected Amount",bg="white",font=("Times New Roman",15)).place(x=50,y=160)
        lbl_target=Label(self.root,text="Target Date",bg="white",font=("Times New Roman",15)).place(x=50,y=200)
        lbl_created=Label(self.root,text="Date Created",bg="white",font=("Times New Roman",15)).place(x=50,y=240)
        lbl_goals=Label(self.root,text="Type Of Goals",bg="white",font=("Times New Roman",15)).place(x=50,y=280)

        #================Entries and Combobox=================
        txt_view = Entry(self.root, textvariable=self.var_searchtxt,font=("Times New Roman",15),bg='white').place(x=530,y=80,width=160)
        txt_Number= Entry(self.root, textvariable=self.number,font=("Times New Roman",15),bg='white').place(x=180,y=40,width=160)
        txt_description=Entry(self.root, textvariable=self.description,font=("Times New Roman",15),bg='white').place(x=180,y=80,width=180)
        txt_requiredamount=Entry(self.root, textvariable=self.requiredamount,font=("Times New Roman",15),bg='white').place(x=200,y=120,width=180)
        txt_collectedamount=Entry(self.root, textvariable=self.collectedamount,font=("Times New Roman",15),bg='white').place(x=200,y=160,width=180)
        txt_target=DateEntry(self.root, textvariable=self.targetdate,font=("Times New Roman",15),bg='white').place(x=180,y=200,width=180)
        txt_created=DateEntry(self.root, textvariable=self.datecreated,font=("Times New Roman",15),bg='white').place(x=180,y=240,width=180)
        txt_goals=ttk.Combobox(self.root, state='readonly', textvariable=self.goals,font=("Times New Roman",15),width=18)
        txt_goals['values']=('Retirement','Long-Term Savings')
        txt_goals.current(0)
        txt_goals.place(x=180,y=280,width=180)

        btn_search=Button(self.root,command=self.search,text="Search",font=("Times New Roman",15), bg="#4caf50",fg="white",cursor="hand2").place(x=730,y=70,width=100,height=40)
        btn_add=Button(self.root,command=self.Save,text="Add",font=("Times New Roman",15), bg="#4caf50",fg="white",cursor="hand2").place(x=50,y=350,width=110,height=40)
        btn_update=Button(self.root,command=self.update,text="Update",font=("Times New Roman",15), bg="#4caf50",fg="white",cursor="hand2").place(x=500,y=655,width=110,height=40)
        btn_delete=Button(self.root,command=self.delete,text="Delete",font=("Times New Roman",15), bg="#4caf50",fg="white",cursor="hand2").place(x=650,y=655,width=110,height=40)
        btn_read=Button(self.root,command=self.Read,text="Retrieve",font=("Times New Roman",15), bg="#4caf50",fg="white",cursor="hand2").place(x=800,y=655,width=110,height=40)
        btn_clear=Button(self.root,command=self.clear,text="Clear",font=("Times New Roman",15), bg="#4caf50",fg="white",cursor="hand2").place(x=170,y=350,width=110,height=40)
        btn_exit=Button(self.root,command=self.exit,text="Exit",font=("Times New Roman",15), bg="#4caf50",fg="white",cursor="hand2").place(x=50,y=600,width=110,height=40)
        #===============Frame
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=420,y=150,width=500,height=500)
        
        
        #==============Scrollbar
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        
        #=========Creatingtableview
        self.goalsTable=ttk.Treeview(emp_frame,columns=("Number","Description","RequiredAmount","CollectedAmount","TargetDate","DateCreated","Goals"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.goalsTable.xview)
        scrolly.config(command=self.goalsTable.yview)
        
        
        self.goalsTable.heading("Number",text="Number")
        self.goalsTable.heading("Description",text="Description")
        self.goalsTable.heading("RequiredAmount",text="Required Amount")
        self.goalsTable.heading("CollectedAmount",text="Collected Amount")
        self.goalsTable.heading("TargetDate",text="Target Date")
        self.goalsTable.heading("DateCreated",text="Date Created")
        self.goalsTable.heading("Goals",text="Goals")
        
        self.goalsTable["show"]="headings"
        self.goalsTable.column("Number",width=100)
        self.goalsTable.column("Description",width=300)
        self.goalsTable.column("RequiredAmount",width=150)
        self.goalsTable.column("CollectedAmount",width=150)
        self.goalsTable.column("TargetDate",width=100)
        self.goalsTable.column("DateCreated",width=100)
        self.goalsTable.column("Goals",width=200)
        
        self.goalsTable.pack(fill=BOTH,expand=1)
        self.goalsTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        
    def exit(self):
        self.root.destroy()
        
    def show(self):
        #Show the data from sqlite database onto the table
        con=sqlite3.connect(database=r'C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS financialgoals(Number TEXT, Description TEXT, RequiredAmount TEXT, CollectedAmount TEXT, TargetDate TEXT, DateCreated TEXT, Goals TEXT)")
        cur.execute("SELECT * FROM 'financialgoals' ORDER BY Number ASC")
        con.commit()
        rows=cur.fetchall()
        self.goalsTable.delete(*self.goalsTable.get_children())
        for row in rows:
            self.goalsTable.insert("",END,values=row)
        
    def get_data(self,ev):
        try:
            f=self.goalsTable.focus()
            content=(self.goalsTable.item(f))
            row=content['values']
            self.number.set(int(row[0])),
            self.description.set(row[1]),
            self.requiredamount.set(int(row[2])),
            self.collectedamount.set(int(row[3])),
            self.targetdate.set(row[4]),
            self.datecreated.set(row[5]),
            self.goals.set(row[6])
        except:
            messagebox.showerror("Info", "Choose the row.",parent=self.root)
        
        
    def search(self):
        #search the goal by number
        con=sqlite3.connect(database=r'C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS financialgoals(Number TEXT, Description TEXT, RequiredAmount TEXT, CollectedAmount TEXT, TargetDate TEXT, DateCreated TEXT, Goals TEXT)")
        cur.execute("SELECT * FROM 'financialgoals' ORDER BY Number ASC")
        con.commit()
        if self.var_searchtxt.get()=="":
            messagebox.showerror("Error","Required Number",parent=self.root)
        else:
            cur.execute("Select * from financialgoals where Number=?",(self.var_searchtxt.get(),))
            row=cur.fetchone()
            if row!=None:
                self.goalsTable.delete(*self.goalsTable.get_children())
                self.goalsTable.insert("",END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
                        
    def Read(self):
        #retrieve all data on the table after searching the specific number
        self.goalsTable.delete(*self.goalsTable.get_children())
        con=sqlite3.connect(database=r'C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS financialgoals(Number TEXT, Description TEXT, RequiredAmount TEXT, CollectedAmount TEXT, TargetDate TEXT, DateCreated TEXT, Goals TEXT)")
        con.commit()
        cur.execute("SELECT * FROM 'financialgoals' ORDER BY Number ASC")
        fetch = cur.fetchall()
        for data in fetch:
            self.goalsTable.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        cur.close()
        

    def Save(self):
        #create new data on all specific row
        con=sqlite3.connect(database=r'C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS financialgoals(Number TEXT, Description TEXT, RequiredAmount TEXT, CollectedAmount TEXT, TargetDate TEXT, DateCreated TEXT, Goals TEXT)")
        cur.execute("SELECT * FROM 'financialgoals' ORDER BY Number ASC")
        con.commit()
        try:
            cur.execute("Select * from financialgoals where Number=?",(self.number.get(),))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Number already exits, Try new", parent=self.root)
            elif self.description.get()=="" or self.targetdate.get()=="" or self.datecreated.get()=="" or self.goals.get()=="":
                messagebox.showinfo("Info","Please filled all entries. For 'Numbers', 'Required Amount', and 'Collected Amount', it must be typed in real numbers.",parent=self.root)
            else:
                cur.execute("Insert into financialgoals (Number, Description,RequiredAmount,CollectedAmount,TargetDate,DateCreated,Goals) values(?,?,?,?,?,?,?)",(
                self.number.get(),self.description.get(),self.requiredamount.get(),self.collectedamount.get(),self.targetdate.get(),self.datecreated.get(),self.goals.get(),))
                con.commit()
                messagebox.showinfo("Success","New goals has been added",parent=self.root)
                self.clear()
                self.show()
        except:
            messagebox.showinfo("Info","Please filled all entries. For 'Numbers', 'Required Amount', and 'Collected Amount', it must be typed in real numbers.",parent=self.root)

        
            
    def delete(self):
        #delete all data
        con=sqlite3.connect(database=r'C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS financialgoals(Number TEXT, Description TEXT, RequiredAmount TEXT, CollectedAmount TEXT, TargetDate TEXT, DateCreated TEXT, Goals TEXT)")
        cur.execute("SELECT * FROM 'financialgoals' ORDER BY Number ASC")
        con.commit()
        if self.number.get()=="":
            messagebox.showerror("Error","Number must be required",parent=self.root)
        else:
            cur.execute("Select * from financialgoals where Number=?",(self.number.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid", parent=self.root)
            else:
                cosM=messagebox.askyesno("Confirm","Delete?",parent=self.root)
                if cosM==True:
                    cur.execute("delete from financialgoals where Number=?",(self.number.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Delete Successfully",parent=self.root)
                    self.clear()
                    self.show()
       
            
    def update(self):
        #update new data from the current data on the table
        con=sqlite3.connect(database=r'C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS financialgoals(Number TEXT, Description TEXT, RequiredAmount TEXT, CollectedAmount TEXT, TargetDate TEXT, DateCreated TEXT, Goals TEXT)")
        cur.execute("SELECT * FROM 'financialgoals' ORDER BY Number ASC")
        con.commit()
        try:
            cur.execute("Select * from financialgoals where Number=?",(self.number.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Number already exists.", parent=self.root)
            elif self.description.get()=="" or self.targetdate.get()=="" or self.datecreated.get()=="" or self.goals.get()=="":
                messagebox.showinfo("Info","Please filled all entries. For 'Numbers', 'Required Amount', and 'Collected Amount', it must be typed in real numbers. So all entries are needed to update properly.",parent=self.root)
            else:
                cur.execute("Update financialgoals set Description=?,RequiredAmount=?,CollectedAmount=?,TargetDate=?,DateCreated=?,Goals=? where Number=?",(self.description.get(),self.requiredamount.get(),self.collectedamount.get(),self.targetdate.get(),self.datecreated.get(),self.goals.get(),self.number.get()))
                con.commit()
                messagebox.showinfo("Success","Updated Successfully",parent=self.root)
                self.clear()
                self.show()
        except:
            messagebox.showinfo("Info","Please filled all entries. For 'Numbers', 'Required Amount', and 'Collected Amount', it must be typed in real numbers. So all entries are needed to update properly.",parent=self.root)

     
    def clear(self):
        #clear the inputs of all entries 
        self.number.set("")
        self.description.set("")
        self.requiredamount.set("")
        self.collectedamount.set("")
        self.targetdate.set("")
        self.datecreated.set("")
        self.goals.set("")
        
        self.show()
    
class Analysis_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Money Analysis")
        root_height = 750
        root_width = 1350

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

        self.root.config(bg = "light blue")   
        
        self.gooutframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.gooutframe.place(x=1260,y=700)
 
        def goback():
            self.root.destroy()#Destroy window
                
        goback = Button(self.gooutframe,width=5,padx= 5,bd=5, font=("arail",8, "bold"), bg = "#ff9966",  text = "Go back", command =goback)#button detail
        goback.pack()#place button
    
    #Homepage button Frame        
        self.Analysispageframe1 = Frame(self.root,width=1000,height=50,bd=10,relief="groove")
        self.Analysispageframe1.place(x=500,y=175)
        
        self.Analysispageframe2 = Frame(self.root,width=1000,height=50,bd=10,relief="groove")
        self.Analysispageframe2.place(x=500,y=275)
        
        self.Analysispageframe3 = Frame(self.root,width=1000,height=50,bd=10,relief="groove")
        self.Analysispageframe3.place(x=500,y=375)

        self.Analysispageframe4 = Frame(self.root,width=1000,height=50,bd=10,relief="groove")
        self.Analysispageframe4.place(x=500,y=475)
        
        self.Analysispageframe5 = Frame(self.root,width=1000,height=50,bd=10,relief="groove")
        self.Analysispageframe5.place(x=500,y=575)

        self.Analysispageframe6 = Frame(self.root,width=1000,height=50,bd=10,relief="groove")
        self.Analysispageframe6.place(x=1260,y=100)
 
        def signout():
            self.root.destroy()#Destroy window
                
        SignOut = Button(self.Analysispageframe6,width=5,padx= 5,bd=5, font=("arail",8, "bold"), bg = "#ff9966",  text = "Sign Out", command =signout)#button detail
        SignOut.pack()#place button
        
        def NetWorth():
            self.newWindow = Toplevel(self.root)
            self.app=NetWorth_window(self.newWindow)
        
        NetWorth = Button(self.Analysispageframe1, bd=5, font=("arail",8, "bold"), bg = "#ff9966", width=75,height=2, text = "Amount of Net Worth Calculated over Time ", command =NetWorth)
        NetWorth.pack()
        def SumOfTotalNecessities():
            self.newWindow = Toplevel(self.root)
            self.app=SumOfTotalNecessities_window(self.newWindow)
        
        SumOfTotalNecessities = Button(self.Analysispageframe2, bd=5, font=("arail",8, "bold"), bg = "#ff9966", width=75,height=2, text = "Sum of total necessities expenses changes over month/year", command =SumOfTotalNecessities)
        SumOfTotalNecessities.pack()
        def SumOfTotalSavings():
            self.newWindow = Toplevel(self.root)
            self.app=SumOfTotalSavings_window(self.newWindow)
        
        SumOfTotalSavings = Button(self.Analysispageframe3, bd=5, font=("arail",8, "bold"), bg = "#ff9966", width=75,height=2, text = "Sum of total savings expenses changes over month/year", command =SumOfTotalSavings)
        SumOfTotalSavings.pack()

        def SumOfTotalNonEssentialExpenses():
            self.newWindow = Toplevel(self.root)
            self.app=SumOfTotalNonEssentialExpenses_window(self.newWindow)
        
        SumOfTotalNonEssentialExpenses = Button(self.Analysispageframe4, bd=5, font=("arail",8, "bold"), bg = "#ff9966", width=75,height=2, text = "Sum of total non-essential expenses changes over month/year",command =SumOfTotalNonEssentialExpenses)
        SumOfTotalNonEssentialExpenses.pack()

        def breakDown():
            self.newWindow = Toplevel(self.root)
            self.app=breakdown_window(self.newWindow)


        breakdown = Button(self.Analysispageframe5, bd=5, font=("arail",8, "bold"), bg = "#ff9966", width=75,height=2, text = "Expenses breakdown by category",command =breakDown)
        breakdown.pack()
        
class SumOfTotalNecessities_window:
    def __init__(self,root):
        self.root = root
        self.root.title("SumOfTotalNecessities")
        self.root.resizable(0, 0) 
        root_height = 750
        root_width = 750

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

        self.root.config(bg = "light blue")   
        #=============Frames============
        MainFrame = Frame(self.root, bg = "light blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2,  bg = "Ghost White", relief = RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font = ('arial', 30 , 'bold'), text="Sum Of Total Necessities", bg = "Ghost White")
        self.lblTitle.grid()
    
        self.gooutframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.gooutframe.place(x=250,y=700)
        
        self.showframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.showframe.place(x=100,y=500)

        self.shframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.shframe.place(x=400,y=500)

        self.resetframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.resetframe.place(x=250,y=600)

        self.graph=StringVar()
        self.option=StringVar()
               
        def show_frame(frame):
            frame.tkraise()
            
        def goback():
            self.root.destroy()#Destroy window

        def reset():
            showbutton.current(0)
            shbutton.current(0)
        #=====Buttons and Comboboxes=============      
        goback = Button(self.gooutframe,width=5,padx= 5,bd=5, font=("arail",8, "bold"),
                    bg = "#ff9966",  text = "Go back", command =goback)#button detail
        goback.pack()#place button

        showbutton= ttk.Combobox(self.showframe,font=("arail",8, "bold"),textvariable=self.graph)
        showbutton['values']=('','Bar Graph')#, #'Line Graph')
        showbutton.current(0)
        showbutton.pack()

        shbutton= ttk.Combobox(self.shframe,font=("arail",8, "bold"),textvariable=self.option)
        shbutton['values']=('','Monthly','Yearly')
        shbutton.current(0)
        shbutton.pack()

        resetbutton= Button(self.resetframe,font=("arail",8, "bold"),text="Reset", command=reset)
        resetbutton.pack()

        #==========Listbox with specific conditions======
        def graph(*args):
            for w in self.root.grid_slaves(1): # all elements 
                w.grid_remove()                # delete elements 
            if(self.graph.get()=='Bar Graph' and self.option.get()=='Monthly'):
                conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                with conn:
                    cursor=conn.cursor()
                cursor.execute('''SELECT cm.Month, SUM(cm.TotalNecessities) as 'Total Necessities' From CALCULATOR cm GROUP BY cm.Month''')
                member= cursor.fetchall()
                df = pd.DataFrame(member,columns=['Month','Total Necessities'])
                df.plot(kind='bar',x='Month', y='Total Necessities')
                plt.xticks(rotation=30, horizontalalignment="center")
                plt.title('Sum Of Total Necessities',fontsize=10)
                plt.xlabel('Month')
                plt.ylabel('Total Necessities')
                plt.show()
            elif(self.graph.get()=='Bar Graph' and self.option.get()=='Yearly'):
                conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                with conn:
                    cursor=conn.cursor()
                cursor.execute('''SELECT cm.Year, SUM(cm.TotalNecessities) as 'Total Necessities' From CALCULATOR1 cm GROUP BY cm.Year''')
                member= cursor.fetchall()
                df = pd.DataFrame(member,columns=['Year','Total Necessities'])
                df.plot(kind='bar',x='Year', y='Total Necessities')
                plt.xticks(rotation=30, horizontalalignment="center")
                plt.title('Sum Of Total Necessities',fontsize=10)
                plt.xlabel('Year')
                plt.ylabel('Total Necessities')
                plt.show()
        self.graph.trace('w',graph)
        self.option.trace('w',graph) # on change of string variable

class SumOfTotalNonEssentialExpenses_window:
    def __init__(self,root):
        self.root = root
        self.root.title("SumOfTotalNonEssentialExpenses")
        self.root.resizable(0, 0) 
        root_height = 750
        root_width = 750

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

        self.root.config(bg = "light blue")   
        #========Frames=============
        MainFrame = Frame(self.root, bg = "light blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2,  bg = "Ghost White", relief = RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font = ('arial', 30 , 'bold'), text="Sum Of Total Non-Essential Expenses", bg = "Ghost White")
        self.lblTitle.grid()
    
        self.gooutframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.gooutframe.place(x=250,y=700)
        
        self.showframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.showframe.place(x=100,y=500)

        self.shframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.shframe.place(x=400,y=500)

        self.resetframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.resetframe.place(x=250,y=600)

        self.graph=StringVar()
        self.option=StringVar()
               
        def show_frame(frame):
            frame.tkraise()
            
        def goback():
            self.root.destroy()#Destroy window

        def reset():
            showbutton.current(0)
            shbutton.current(0)
                
        goback = Button(self.gooutframe,width=5,padx= 5,bd=5, font=("arail",8, "bold"),
                    bg = "#ff9966",  text = "Go back", command =goback)#button detail
        goback.pack()#place button
        #=================Buttons and Comboboxes==========
        showbutton= ttk.Combobox(self.showframe,font=("arail",8, "bold"),textvariable=self.graph)
        showbutton['values']=('','Bar Graph')#, #'Line Graph')
        showbutton.current(0)
        showbutton.pack()

        shbutton= ttk.Combobox(self.shframe,font=("arail",8, "bold"),textvariable=self.option)
        shbutton['values']=('','Monthly','Yearly')
        shbutton.current(0)
        shbutton.pack()

        resetbutton= Button(self.resetframe,font=("arail",8, "bold"),text="Reset", command=reset)
        resetbutton.pack()

        #==========Listbox with specific conditions======
        def graph(*args):
            for w in self.root.grid_slaves(1): # all elements 
                w.grid_remove()                # delete elements 
            if(self.graph.get()=='Bar Graph' and self.option.get()=='Monthly'):
                conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                with conn:
                    cursor=conn.cursor()
                cursor.execute('''SELECT cm.Month, SUM(cm.TotalNonEssential) as 'Total Non-Essential' From CALCULATOR cm GROUP BY cm.Month''')
                member= cursor.fetchall()
                df = pd.DataFrame(member,columns=['Month','Total Non-Essential'])
                df.plot(kind='bar',x='Month', y='Total Non-Essential')
                plt.xticks(rotation=30, horizontalalignment="center")
                plt.title('Sum Of Total Non-Essential',fontsize=10)
                plt.xlabel('Month')
                plt.ylabel('Total Non-Essential')
                plt.show()
            elif(self.graph.get()=='Bar Graph' and self.option.get()=='Yearly'):
                conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                with conn:
                    cursor=conn.cursor()
                cursor.execute('''SELECT cm.Year, SUM(cm.TotalNonEssential) as 'Total Non-Essential' From CALCULATOR1 cm GROUP BY cm.Year''')
                member= cursor.fetchall()
                df = pd.DataFrame(member,columns=['Year','Total Non-Essential'])
                df.plot(kind='bar',x='Year', y='Total Non-Essential')
                plt.xticks(rotation=30, horizontalalignment="center")
                plt.title('Sum Of Total Non-Essential',fontsize=10)
                plt.xlabel('Year')
                plt.ylabel('Total Non-Essential')
                plt.show()
        

        self.graph.trace('w',graph)
        self.option.trace('w',graph) # on change of string variable

class SumOfTotalSavings_window:
    def __init__(self,root):
        self.root = root
        self.root.title("SumOfTotalSavings")
        self.root.resizable(0, 0) 
        root_height = 750
        root_width = 750

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

        self.root.config(bg = "light blue")   

        #===========Frames===========
        MainFrame = Frame(self.root, bg = "light blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2,  bg = "Ghost White", relief = RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font = ('arial', 30 , 'bold'), text="Sum Of Total Savings", bg = "Ghost White")
        self.lblTitle.grid()
    
        self.gooutframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.gooutframe.place(x=250,y=700)
        
        self.showframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.showframe.place(x=100,y=500)

        self.shframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.shframe.place(x=400,y=500)

        self.resetframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.resetframe.place(x=250,y=600)

        self.graph=StringVar()
        self.option=StringVar()
               
        def show_frame(frame):
            frame.tkraise()
            
        def goback():
            self.root.destroy()#Destroy window

        def reset():
            showbutton.current(0)
            shbutton.current(0)
                
        goback = Button(self.gooutframe,width=5,padx= 5,bd=5, font=("arail",8, "bold"),
                    bg = "#ff9966",  text = "Go back", command =goback)#button detail
        goback.pack()#place button

        #==========Buttons and Comboboxes======
        showbutton= ttk.Combobox(self.showframe,font=("arail",8, "bold"),textvariable=self.graph)
        showbutton['values']=('','Bar Graph')#, #'Line Graph')
        showbutton.current(0)
        showbutton.pack()

        shbutton= ttk.Combobox(self.shframe,font=("arail",8, "bold"),textvariable=self.option)
        shbutton['values']=('','Monthly','Yearly')
        shbutton.current(0)
        shbutton.pack()

        resetbutton= Button(self.resetframe,font=("arail",8, "bold"),text="Reset", command=reset)
        resetbutton.pack()
        
        #==========Listbox with specific conditions======
        def graph(*args):
            for w in self.root.grid_slaves(1): # all elements 
                w.grid_remove()                # delete elements 
            if(self.graph.get()=='Bar Graph' and self.option.get()=='Monthly'):
                conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                with conn:
                    cursor=conn.cursor()
                cursor.execute('''SELECT cm.Month, SUM(cm.TotalSavings) as 'Total Savings' From CALCULATOR cm GROUP BY cm.Month''')
                member= cursor.fetchall()
                df = pd.DataFrame(member,columns=['Month','Total Savings'])
                df.plot(kind='bar',x='Month', y='Total Savings')
                plt.xticks(rotation=30, horizontalalignment="center")
                plt.title('Sum Of Total Savings',fontsize=10)
                plt.xlabel('Month')
                plt.ylabel('Total Savings')
                plt.show()
            elif(self.graph.get()=='Bar Graph' and self.option.get()=='Yearly'):
                conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                with conn:
                    cursor=conn.cursor()
                cursor.execute('''SELECT cm.Year, SUM(cm.TotalSavings) as 'Total Savings' From CALCULATOR1 cm GROUP BY cm.Year''')
                member= cursor.fetchall()
                df = pd.DataFrame(member,columns=['Year','Total Savings'])
                df.plot(kind='bar',x='Year', y='Total Savings')
                plt.xticks(rotation=30, horizontalalignment="center")
                plt.title('Sum Of Total Savings',fontsize=10)
                plt.xlabel('Year')
                plt.ylabel('Total Savings')
                plt.show()
        self.graph.trace('w',graph)
        self.option.trace('w',graph) # on change of string variable

class NetWorth_window:
    def __init__(self,root):
        self.root = root
        self.root.title("NetWorth")
        self.root.resizable(0, 0) 
        root_height = 750
        root_width = 750

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

        self.root.config(bg = "light blue")   

        #==========Frames=========
        MainFrame = Frame(self.root, bg = "light blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2,  bg = "Ghost White", relief = RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font = ('arial', 30 , 'bold'), text="Net Worth", bg = "Ghost White")
        self.lblTitle.grid()
    
        self.gooutframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.gooutframe.place(x=250,y=700)
        
        self.showframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.showframe.place(x=100,y=500)

        self.shframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.shframe.place(x=400,y=500)

        self.resetframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.resetframe.place(x=250,y=600)

        self.graph=StringVar()
        self.option=StringVar()
               
        def show_frame(frame):
            frame.tkraise()
            
        def goback():
            self.root.destroy()#Destroy window

        def reset():
            showbutton.current(0)
            shbutton.current(0)
                
        goback = Button(self.gooutframe,width=5,padx= 5,bd=5, font=("arail",8, "bold"),
                    bg = "#ff9966",  text = "Go back", command =goback)#button detail
        goback.pack()#place button

        #==========Buttons and Comboboxes======
        showbutton= ttk.Combobox(self.showframe,font=("arail",8, "bold"),textvariable=self.graph)
        showbutton['values']=('','Bar Graph')#, #'Line Graph')
        showbutton.current(0)
        showbutton.pack()

        shbutton= ttk.Combobox(self.shframe,font=("arail",8, "bold"),textvariable=self.option)
        shbutton['values']=('','Monthly','Yearly')
        shbutton.current(0)
        shbutton.pack()

        resetbutton= Button(self.resetframe,font=("arail",8, "bold"),text="Reset", command=reset)
        resetbutton.pack()
        
        #==========Listbox with specific conditions======
        def graph(*args):
            for w in self.root.grid_slaves(1): # all elements 
                w.grid_remove()                # delete elements 
            if(self.graph.get()=='Bar Graph' and self.option.get()=='Monthly'):
                conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                with conn:
                    cursor=conn.cursor()
                cursor.execute('''SELECT cm.Month, cm.MonthlyExpenses as 'Total Networth' From CALCULATOR cm GROUP BY cm.Month''')
                member= cursor.fetchall()
                df = pd.DataFrame(member,columns=['Month','Total Networth'])
                df.plot(kind='bar',x='Month', y='Total Networth')
                plt.xticks(rotation=30, horizontalalignment="center")
                plt.title('Sum Of Total NetWorth',fontsize=10)
                plt.xlabel('Month')
                plt.ylabel('Total Networth')
                plt.show()
            elif(self.graph.get()=='Bar Graph' and self.option.get()=='Yearly'):
                conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                with conn:
                    cursor=conn.cursor()
                cursor.execute('''SELECT cm.Year, cm.YearlyExpenses as 'Total NetWorth' From CALCULATOR1 cm GROUP BY cm.Year''')
                member= cursor.fetchall()
                df = pd.DataFrame(member,columns=['Year','Total NetWorth'])
                df.plot(kind='bar',x='Year', y='Total NetWorth')
                plt.xticks(rotation=30, horizontalalignment="center")
                plt.title('Sum Of Total NetWorth',fontsize=10)
                plt.xlabel('Year')
                plt.ylabel('Total NetWorth')
                plt.show()
        self.graph.trace('w',graph)
        self.option.trace('w',graph) # on change of string variable


class breakdown_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Breakdown")
        self.root.resizable(0, 0) 
        root_height = 750
        root_width = 750

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

        self.root.config(bg = "light blue")   

        #================Frames=============
        MainFrame = Frame(self.root, bg = "light blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2,  bg = "Ghost White", relief = RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font = ('arial', 30 , 'bold'), text="Expenses Breakdown by Category", bg = "Ghost White")
        self.lblTitle.grid()
    
        self.gooutframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.gooutframe.place(x=250,y=700)
        
        self.showframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.showframe.place(x=100,y=500)

        self.shframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.shframe.place(x=400,y=500)

        self.resetframe = Frame(self.root,width=150,height=150,bd=10,relief="groove")
        self.resetframe.place(x=250,y=600)

        self.graph=StringVar()
        self.option=StringVar()
               
        def show_frame(frame):
            frame.tkraise()
            
        def goback():
            self.root.destroy()#Destroy window

        def reset():
            showbutton.current(0)
            shbutton.current(0)
                
        goback = Button(self.gooutframe,width=5,padx= 5,bd=5, font=("arail",8, "bold"),
                    bg = "#ff9966",  text = "Go back", command =goback)#button detail
        goback.pack()#place button

        #==========Buttons and Comboboxes======
        showbutton= ttk.Combobox(self.showframe,font=("arail",8, "bold"),textvariable=self.graph)
        showbutton['values']=('','Bar Graph')
        showbutton.current(0)
        showbutton.pack()

        shbutton= ttk.Combobox(self.shframe,font=("arail",8, "bold"),textvariable=self.option)
        shbutton['values']=('','Monthly','Yearly')
        shbutton.current(0)
        shbutton.pack()

        resetbutton= Button(self.resetframe,font=("arail",8, "bold"),text="Reset", command=reset)
        resetbutton.pack()

        #==========Listbox with specific conditions======
        def graph(*args):
            for w in self.root.grid_slaves(1): # all elements 
                w.grid_remove()                # delete elements 
            if(self.graph.get()=='Bar Graph' and self.option.get()=='Monthly'):
                conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                with conn:
                    cursor=conn.cursor()
                cursor.execute('''SELECT cm.Month, SUM(cm.TotalNecessities) as 'Total Necessities',SUM(cm.TotalSavings) as 'Total Savings',SUM(cm.TotalNonEssential) as 'Total Non-essential' From CALCULATOR cm GROUP BY cm.Month''')
                member= cursor.fetchall()
                df = pd.DataFrame(member,columns=['Month','Total Necessities','Total Savings','Total Non-essential'])
                df.plot(kind='bar',x='Month', y=['Total Necessities','Total Savings','Total Non-essential'])
                plt.xticks(rotation=30, horizontalalignment="center")
                plt.title('Expenses breakdown by category',fontsize=10)
                plt.xlabel('Month')
                plt.ylabel('Expenses category in Month')
                plt.show()
            elif(self.graph.get()=='Bar Graph' and self.option.get()=='Yearly'):
                conn = sqlite3.connect('C:/Users/User/OneDrive/Desktop/money.db')#C:/Users/Dell/Desktop/Money/money.db
                with conn:
                    cursor=conn.cursor()
                cursor.execute('''SELECT cm.Year, SUM(cm.TotalNecessities) as 'Total Necessities',SUM(cm.TotalSavings) as 'Total Savings',SUM(cm.TotalNonEssential) as 'Total Non-essential' From CALCULATOR1 cm GROUP BY cm.Year''')
                member= cursor.fetchall()
                df = pd.DataFrame(member,columns=['Year','Total Necessities','Total Savings','Total Non-essential'])
                df.plot(kind='bar',x='Year', y=['Total Necessities','Total Savings','Total Non-essential'])
                plt.xticks(rotation=30, horizontalalignment="center")
                plt.title('Expenses breakdown by category',fontsize=10)
                plt.xlabel('Month')
                plt.ylabel('Expenses category in Year')
                plt.show()
        self.graph.trace('w',graph)
        self.option.trace('w',graph) # on change of string variable 

    #define all our window
    def Login_window(self):
        self.newWindow = Toplevel(self.master)
        self.app=LoginForm(self.newWindow)  

    def Register_window(self):
        self.newWindow = Toplevel(self.master)
        self.app=RegisterForm(self.newWindow)
  
    def UserExpenses(self):
        self.newWindow = Toplevel(self.master)
        self.app=Expenses_window(self.newWindow)
    def financialGoals(self):
        self.newWindow = Toplevel(self.master)
        self.newWindoe = financialGoals_window(self.newWindow)
    def tips(self):
        self.newWindow = Toplevel(self.master)
        self.app=MoneyManagementTips_window(self.newWindow)   
    def Analysis_window(self):
        self.newWindow = Toplevel(self.master)
        self.app=Analysis_window(self.newWindow)
        
if __name__ == "__main__":
    main() 
    



