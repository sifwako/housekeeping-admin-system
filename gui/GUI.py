import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox
from UserAccount import User



class logintodb:

    """A class to represent the login page"""
    # Constructor
    def __init__(self, user = User()):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.configure(bg= '#152b3a')
        self.root.title("Gold Gym Login Page")
        self.root.resizable(0, 0)
        self.wn_user = user

        # Defining the labels and their placement.
        self.heading = tk.Label(self.root, text=" Welcome to Gold Fitness House", font='time 22 bold italic',
                              bg="#0A87AE", fg="white")
        self.heading.place(x=70, y=50, width=450, height=65)
        self.username_lable = tk.Label(self.root, text="Username: ", font='sans 16 bold', bg = "#0A87AE", fg = "white")
        self.username_lable.place(x=100, y=200, width = 110)

        self.username = tk.Entry(self.root, width=35, bd = 0)
        self.username.place(x=220, y=203, width=300)

        self.password_lable = tk.Label(self.root, text="Password: ", font='sans 16 bold', bg = "#0A87AE", fg = "white")
        self.password_lable.place(x=100, y=250, width=110)

        self.password = tk.Entry(self.root, width=35, bd=0)
        self.password.place(x=220, y=253, width=300)

        self.submitbtn = tk.Button(self.root, text="Login", font='sans 16 bold',
                              highlightbackground='green', highlightthickness=0, fg="white", command=self.gotohomepage)
        self.submitbtn.place(x=210, y=350, width=80, height=30)

        self.singupbtn = tk.Button(self.root, text="Register", font='sans 16 bold',
                              highlightbackground='green', highlightthickness=0, fg="white", command=self.gotosignuppage)
        self.singupbtn.place(x=410, y=350, width=80, height=30)

        self.root.mainloop()


    # Function that leads to the registration page
    def gotosignuppage(self):
        self.root2 = Toplevel(self.root)
        self.wn_singup = SignUp(self.root2, self.root)
        self.root.withdraw()

    # This is going to be used to
    # 1. go to the home page after login in
    # 2. check if the password and user name entered are correct
    # 3. displays a message window based on the checking
    def gotohomepage(self):
        if self.username.get() and self.password.get():
            if self.paswordcheck():
                self.wn_user.login(self.username.get(), self.password.get())
                self.username.delete(0, 'end')
                self.password.delete(0, 'end')
                messagebox.showerror("Welcom", f"Welcome Home {self.logininfo['username']}")
                self.root2 = Toplevel(self.root)
                global uname
                uname = f"{self.logininfo['username']}"
                self.wn_homepage = Homepage(self.root2, self.root, self.wn_user)
                self.root.withdraw()
            else:
                messagebox.showerror("Error", "Login Information Is Incorrect")
        else:
             messagebox.showerror("Error", "Please fill the login info")

    # This function checks the password and user name entered in the login page.

    def paswordcheck(self):
        with open("webuser.txt", 'r') as openfile:
            self.loginintro = openfile.readlines()
            for i in self.loginintro:
                self.logininfo = eval(i)
                if self.logininfo['username'] == str(self.username.get()) and self.logininfo["userpassword"] == str(
                    self.password.get()):
                    return True
                    break
            else:
                return False

class SignUp:

    """A class to represent a sign up page"""

    # Constructor
    def __init__(self, parent, log=logintodb, user=User()):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg='#152b3a')
        self.root.title("Gold Fitness House Home Page")
        self.root.resizable(0, 0)
        self.wn_login = log
        self.webuser = user

        # Defining the labels and their placement.
        self.lable = tk.Label(self.root, text=" Sign Up For Gold Fitness House", font='time 22 bold italic', bg="#0A87AE", fg="white")
        self.lable.place(x=70, y=50, width=450, height= 65)

        self.fname_lable = tk.Label(self.root, text="Full Name: ", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.fname_lable.place(x=80, y=150, width=120, height = 30)

        self.fname = tk.Entry(self.root, width=35, bd=0)
        self.fname.place(x=200, y=150, width=300, height= 30)

        self.uname_lable = tk.Label(self.root, text="Username: ", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.uname_lable.place(x=80, y=200, width=120, height = 30)

        self.uname = tk.Entry(self.root, width=35, bd=0)
        self.uname.place(x=200, y=200, width=300, height = 30)

        self.pass_lable = tk.Label(self.root, text="Password:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.pass_lable.place(x=80, y=250, width=120, height = 30)

        self.passw = tk.Entry(self.root, width=35, bd=0)
        self.passw.place(x=200, y=250, width=300, height = 30)

        self.cpass_lable = tk.Label(self.root, text="Confirm Password:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.cpass_lable.place(x=80, y=300, width=120, height = 30)

        self.cpassw = tk.Entry(self.root, width=35, bd=0)
        self.cpassw.place(x=200, y=300, width=300, height = 30)

        self.addi_lable = tk.Label(self.root, text="Address:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.addi_lable.place(x=80, y=350, width=120, height=30)

        self.addi = tk.Entry(self.root, width=35, bd=0)
        self.addi.place(x=200, y=350, width=300, height=30)

        self.number_lable = tk.Label(self.root, text="Number:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.number_lable.place(x=80, y=400, width=120, height=30)

        self.number = tk.Entry(self.root, width=35, bd=0)
        self.number.place(x=200, y=400, width=300, height=30)


        self.donebtn = tk.Button(self.root, text="Done", font='sans 16 bold',
                              highlightbackground='green', highlightthickness= 0, fg = "black", command = self.signupdone)

        self.donebtn.place(x=285, y=480, width=90, height = 40)

    # Checks Existence of user name
    def unamexist(self):
        with open("webuser.txt") as user:
            self.userdict = user.readlines()
            for i in self.userdict:
                self.finduser = eval(i)
                if self.finduser['username'] == self.uname.get() and self.webuser.getUserName() != self.uname.get():
                    return True


    # This function checks if
    # 1. the fields are filled
    # 2. the username exists
    # 3. password is retyped correctly
    # Then finally the registration information given is going to be stored on both the Recods and webuser txt.
    def signupdone(self):
        if self.fname.get() and self.uname.get() and self.addi.get() and self.number.get() and self.passw.get():
            if self.passw.get() != self.cpassw.get():
                messagebox.showerror("error", "Password should be similar!!Please Try Again")
            else:
                if self.unamexist():
                    messagebox.showerror("error", "An account with that user name already exist!!! Please try another")
                else:
                    self.webuser.registerrecods(self.fname.get(), self.uname.get(), self.passw.get(), self.addi.get(),
                                            self.number.get(), "R")
                    messagebox.showinfo("show info", "Welcome To Gold Fitness House")
                    self.wn_login.deiconify()
                    self.root.destroy()
        else:
            messagebox.showerror("error", "All Field should be filled!!!Please Try Again")

class Homepage:

    '''Class to represent the Homepage'''

    # Constructor
    def __init__(self, parent, log=logintodb, user=User):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg='#152b3a')
        self.root.title("Gold Fitness House Home Page")
        self.root.resizable(0, 0)
        self.wn_login = log
        self.wn_cart = Cart
        self.wn_user = user

        # Defining the labels and their placement.

        self.homelable = tk.Label(self.root, text=f"Welcome {uname} ", font='time 22 bold', bg="#0A87AE", fg="white")
        self.homelable.place(x=70, y=50, width=449, height=65)

        self.infobtn = tk.Button(self.root, text="Profile", font='sans 16 bold',
                                 highlightbackground='#0A87AE', highlightthickness=0, fg="black", command = self.gotoprofile)
        self.infobtn.place(x=70, y=115, width=89.8, height=40)

        self.topbtn = tk.Button(self.root, text="Top Up", font='sans 16 bold',
                                highlightbackground='#0A87AE', highlightthickness=0, fg="black", command = self.gototopup)
        self.topbtn.place(x=159.8, y=115, width=89.8, height=40)

        self.cartbtn = tk.Button(self.root, text="Cart", font='sans 16 bold',
                                 highlightbackground='#0A87AE', highlightthickness=0, fg="black", command = self.gototocart)
        self.cartbtn.place(x=249.6, y=115, width=89.8, height=40)

        self.logbtn = tk.Button(self.root, text="Log Out", font='sans 16 bold',
                                highlightbackground='#0A87AE', highlightthickness=0, fg="black", command = self.logout)
        self.logbtn.place(x=339.4, y=115, width=89.8, height=40)

        self.privilagebtn = tk.Button(self.root, text="View", font='sans 16 bold', state = self.btnstate(),
                                highlightbackground='#0A87AE', highlightthickness=0, fg="black", command=self.gotoview)
        self.privilagebtn.place(x=429.2, y=115, width=89.8, height=40)

        self.infolable = tk.Label(self.root, text="Membership Year", font='time 18 bold', bg="#0A87AE", fg="black")
        self.infolable.place(x=70, y=220, width=160, height=35)

        self.servicelable = tk.Label(self.root, text="You should perform your purchase with membership year", font='time 12 bold', bg="#152b3a", fg="white")
        self.servicelable.place(x=110, y=170, width=400, height=35)

        self.pricelable = tk.Label(self.root, text="Prices", font='time 18 bold', bg="#0A87AE", fg="black")
        self.pricelable.place(x=405.5, y=220, width=112.5, height=35)

        # services
        self.var1 = tk.IntVar()
        self.service_1 = tk.Checkbutton(self.root, text="1-year membership", variable = self.var1, font='time 16 bold',
                                        onvalue=1, offvalue=0, bg="#152b3a", fg="white")
        self.service_1.place(x=70, y=260, height=20)

        self.var2 = tk.IntVar()
        self.service_2 = tk.Checkbutton(self.root, text="6-months membership", font='time 16 bold', variable = self.var2,
                                        onvalue=1, offvalue=0, bg="#152b3a", fg="white")
        self.service_2.place(x=70, y=290, height=20)

        self.var3 = tk.IntVar()
        self.service_3 = tk.Checkbutton(self.root, text="3-months membership ", font='time 16 bold', variable = self.var3,
                                        onvalue=1,offvalue=0, bg="#152b3a", fg="white")
        self.service_3.place(x=70, y=320, height=20)

        self.var4 = tk.IntVar()
        self.servicelable = tk.Label(self.root, text="Fitness Class", font='time 18 bold', bg="#0A87AE", fg="black")
        self.servicelable.place(x=70, y=350, width=150, height=35)


        self.pricelable = tk.Label(self.root, text="Membership Level", font='time 18 bold', bg="#0A87AE", fg="black")
        self.pricelable.place(x=405.5, y=350, width=160, height=35)

        self.var5 = tk.IntVar()
        self.service_5 = tk.Checkbutton(self.root, text="Yoga", font='time 16 bold', variable = self.var5,
                                        onvalue=1,offvalue=0, bg="#152b3a", fg="white")
        self.service_5.place(x=70, y=390, height=20)

        self.var6 = tk.IntVar()
        self.service_6 = tk.Checkbutton(self.root, text="Zumba", font='time 16 bold', onvalue = 1, variable = self.var6,
                                offvalue=0, bg="#152b3a", fg="white")
        self.service_6.place(x=70, y=420, height=20)

        self.var7 = tk.IntVar()
        self.service_7 = tk.Checkbutton(self.root, text="Pilates", font='time 16 bold', variable = self.var7,
                                        onvalue=1,offvalue=0, bg="#152b3a", fg="white")
        self.service_7.place(x=70, y=450, height=20)

        self.var8 = tk.IntVar()
        self.service_8 = tk.Checkbutton(self.root, text="Beginner", font='time 16 bold', variable = self.var8,
                                        onvalue=1,offvalue=0, bg="#152b3a", fg="white")
        self.service_8.place(x=405.5, y=390, height=20)

        self.var9 = tk.IntVar()
        self.service_9 = tk.Checkbutton(self.root, text="Active", font='time 16 bold', variable = self.var9,
                                        onvalue=1,offvalue=0, bg="#152b3a", fg="white")
        self.service_9.place(x=405.5, y=420, height=20)

        self.var10 = tk.IntVar()
        self.service_10 = tk.Checkbutton(self.root, text="Active", font='time 16 bold', variable = self.var10,
                                        onvalue=1,offvalue=0, bg="#152b3a", fg="white")
        self.service_10.place(x=405.5, y=450, height=20)

        self.price_1 = tk.Label(self.root, text="10980 AED", font='time 16 bold', bg="#152b3a", fg="white")
        self.price_1.place(x=405.5, y=260, height=20)

        self.price_2 = tk.Label(self.root, text="7500 AED", font='time 16 bold', bg="#152b3a", fg="white")
        self.price_2.place(x=405.5, y=290, height=20)

        self.price_3 = tk.Label(self.root, text="450 AED", font='time 16 bold', bg="#152b3a", fg="white")
        self.price_3.place(x=405.5, y=320, height=20)


        self.cartbtn = tk.Button(self.root, text="Add to Cart", font='sans 16 bold',
                                 highlightbackground='green', highlightthickness=0, fg="black", command = self.cart)
        self.cartbtn.place(x=220, y=490, width=150.5, height=40)

    # Logout from account
    def logout(self):
        self.wn_login.deiconify()
        self.root.destroy()

    # Directs to the user's profile
    def gotoprofile(self):
        self.root2 = Toplevel(self.root)
        self.wn_homepage = Profile(self.root2, self.root, self.wn_user)
        self.root.withdraw()

    # Directs to the user's top up page
    def gototopup(self):
        self.root2 = Toplevel(self.root)
        self.wn_homepage = Topup(self.root2, self.root)
        self.root.withdraw()

    # Directs  to the user's cart page
    def gototocart(self):
        true = self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 \
        and self.var5.get() == 0 and self.var6.get() == 0 and self.var7.get() == 0 and self.var8.get() == 0 \
        and self.var9.get() == 0 and self.var10.get() == 0
        if true:
            messagebox.showerror("error", 'Your cart is empty')
        else:
            self.root2 = Toplevel(self.root)
            self.wn_cart = Cart(self.root2, self.root)
            self.root.withdraw()

    # Directs us to the user's privilege view page
    def gotoview(self):
        self.root2 = Toplevel(self.root)
        self.wn_homepage = View(self.root2, self.root)
        self.root.withdraw()

    # This function will
    # 1. define the user's privilege view button  either us normal or disabled
    # this will happen based on the account type

    def btnstate(self):
        if self.wn_user.manager() or self.wn_user.staff():
            return 'normal'
        elif self.wn_user.regular():
            return 'disabled'

    # Direct us to the user's cart.
    def cart(self):
        true = self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 \
               and self.var5.get() == 0 and self.var6.get() == 0 and self.var7.get() == 0 and self.var8.get() == 0 \
               and self.var9.get() == 0 and self.var10.get() == 0
        if true:
            messagebox.showerror("error", 'Make sure you are purchasing atleast one membership')
        else:
            # defining the price of the services.
            cartdict = {}
            if self.var1.get(): cartdict["1-year membership"] = 10980
            if self.var2.get(): cartdict["6-months membership"] = 7500
            if self.var3.get(): cartdict["3-months membership"] = 450
            messagebox.showinfo("info", "Proceed to your cart to retreive your purchases")
            global purchase_list
            purchase_list = cartdict

class Profile:

    '''Class to represent the Profile page'''

    # constructor

    def __init__(self, parent, wn_home=Homepage, user=User()):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg='#152b3a')
        self.root.title("User Profile Page")
        self.root.resizable(0, 0)
        self.wn_home = wn_home
        self.wn_user = user
        self.wn_user.updatingtobalance()


        # defining the widgets

        self.lable = tk.Label(self.root, text=f"Hello {uname}", font='time 22 bold italic', bg="#0A87AE", fg="white")
        self.lable.place(x=70, y=50, width=450, height=65)

        self.fname_lable = tk.Label(self.root, text="Full Name:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.fname_lable.place(x=80, y=150, width=110, height = 30)

        self.fname = tk.Entry(self.root, width=35, bd=0)
        self.fname.place(x=200, y=150, width=300, height = 30)
        self.fname.insert(0, self.wn_user.getFullname())

        self.uname_lable = tk.Label(self.root, text="Username:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.uname_lable.place(x=80, y=200, width=110, height = 30)

        self.uname = tk.Entry(self.root, width=35, bd=0)
        self.uname.place(x=200, y=200, width=300, height = 30)
        self.uname.insert(0, f"{self.wn_user.getUserName()}")

        self.pass_lable = tk.Label(self.root, text="Password:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.pass_lable.place(x=80, y=250, width=110, height = 30)

        self.passw = tk.Entry(self.root, width=35, bd=0)
        self.passw.place(x=200, y=250, width=300, height = 30)
        self.passw.insert(0, self.wn_user.getPassword())

        self.cpass_lable = tk.Label(self.root, text="Confirm Password:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.cpass_lable.place(x=80, y=300, width=110, height = 30)

        self.cpassw = tk.Entry(self.root, width=35, bd=0)
        self.cpassw.place(x=200, y=300, width=300, height = 30)

        self.addi_lable = tk.Label(self.root, text="Address:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.addi_lable.place(x=80, y=350, width=110, height=30)

        self.addi = tk.Entry(self.root, width=35, bd=0)
        self.addi.place(x=200, y=350, width=300, height=30)
        self.addi.insert(0, self.wn_user.getaddress())

        self.number_lable = tk.Label(self.root, text="Number:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.number_lable.place(x=80, y=400, width=110, height=30)

        self.number = tk.Entry(self.root, width=35, bd=0)
        self.number.place(x=200, y=400, width=300, height=30)
        self.number.insert(0, self.wn_user.getPhoneNum())

        self.balance_lable = tk.Label(self.root, text="Balance:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.balance_lable.place(x=80, y=450, width=110, height=30)

        self.balance = tk.Label(self.root, text= self.wn_user.getbalance(), width=35, bd=0, bg = "white")
        self.balance.place(x=200, y=450, width=300, height=30)

        self.backbtn = tk.Button(self.root, text="Back", font='sans 16 bold',
                              highlightbackground='green', highlightthickness = 0, fg = "black", command = self.goback)
        self.backbtn.place(x=70, y=550, width=90, height = 40)

        self.updatebtn = tk.Button(self.root, text="Update", font='sans 16 bold',
                                 highlightbackground='green', highlightthickness=0, fg="black", command = self.update)

        self.updatebtn.place(x=430, y=550, width=90, height=40)


    # defining the name existance,
    # it will return true if the name already exist.

    def unamexist(self):
        with open("webuser.txt") as user:
            self.userdict = user.readlines()
            for i in self.userdict:
                self.finduser = eval(i)
                if self.finduser['username'] == self.uname.get() and self.wn_user.getUserName() != self.uname.get():
                    return True

    # when we run this function it will update our account
    # it will check if all the fields are filled
    # it will check the exitance of the user name provided
    #finally it will update all the files that are required. the Recods.txt file and webuser.txt file

    def update(self):
        if self.fname.get() and self.uname.get() and self.addi.get() and self.number.get() and self.passw.get():
            if self.passw.get() != self.cpassw.get():
                messagebox.showerror("Confirm password", "Password should be similar")
            else:
                if self.unamexist():
                    messagebox.showerror("Username Exist", "Username already exist, Please try another")
                else:
                    self.wn_user.updateinfo(self.fname.get(), self.uname.get(), self.passw.get(), self.addi.get(),
                                            self.number.get())
                    messagebox.showerror("error", "Successfully Updated")
                    self.goback()
        else:
            messagebox.showerror("error", "All fields must be full")

    # this function will direct us back to the home page.

    def goback(self):
        self.wn_home.deiconify()
        self.root.withdraw()


class Topup:

    '''Class to represent the Topup page'''

    # Constructor
    def __init__(self, parent, home=Homepage,):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg='#152b3a')
        self.root.title("Customer Account Top Up Page")
        self.root.resizable(0, 0)
        self.wn_home = home
        self.user = User()
        self.user.updatingtobalance()

        # defining the widgets for the  the top up page

        self.lable = tk.Label(self.root, text="Top up from card", font='time 22 bold italic', bg="#0A87AE", fg="white")
        self.lable.place(x=70, y=50, width=450, height = 65)

        self.fname_lable = tk.Label(self.root, text="Name on card:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.fname_lable.place(x=80, y=150, width=110, height = 30)

        self.fname = tk.Entry(self.root, width=35, bd=0)
        self.fname.place(x=200, y=150, width=300, height = 30)

        self.cardnum_lable = tk.Label(self.root, text="Card Number:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.cardnum_lable.place(x=80, y=200, width=110, height = 30)

        self.cardnum = tk.Entry(self.root, width=35, bd=0)
        self.cardnum.place(x=200, y=200, width=300, height = 30)

        self.edate_lable = tk.Label(self.root, text="Exp Date:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.edate_lable.place(x=80, y=250, width=110, height = 30)

        self.edate = tk.Entry(self.root, width=35, bd=0)
        self.edate.place(x=200, y=250, width=300, height = 30)

        self.cvv_lable = tk.Label(self.root, text="CVV:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.cvv_lable.place(x=80, y=300, width=110, height = 30)

        self.cvv = tk.Entry(self.root, width=35, bd=0)
        self.cvv.place(x=200, y=300, width=300, height = 30)

        self.amount_lable = tk.Label(self.root, text="Amount:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.amount_lable.place(x=80, y=350, width=110, height=30)

        self.amount = tk.Entry(self.root, width=35, bd=0)
        self.amount.place(x=200, y=350, width=300, height=30)

        self.balance_lable = tk.Label(self.root, text="Balance:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.balance_lable.place(x=80, y=400, width=110, height=30)

        self.balance = tk.Label(self.root, text= self.user.getbalance(), width=35, bd=0, bg="white")
        self.balance.place(x=200, y=400, width=300, height=30)

        self.backbtn = tk.Button(self.root, text="Back", font='sans 16 bold',
                              highlightbackground='green', highlightthickness=0, fg="black", command=self.donetopup)

        self.backbtn.place(x=80, y=480, width=90, height=40)

        self.topupbtn = tk.Button(self.root, text="Done", font='sans 16 bold',
                                  highlightbackground='green', highlightthickness=0, fg="black", command=self.topup)

        self.topupbtn.place(x=420, y=480, width=90, height=40)


    # this function will redirect us to the home page

    def donetopup(self):

        self.wn_home.deiconify()
        self.root.destroy()

    # this function will help use topup
    # it will check all the field if they are filled first.

    def topup(self):

        if self.fname.get() and self.cardnum.get() and self.edate.get() and self.cvv.get() and self.amount.get():

            # it will ma make sure if the amount paid first should be a float
            # the amount toped up should be more than 100 or equal to 100
            # we are using exception handling method to achieve that.
            try:
                amount = float(self.amount.get())
                if amount >= 100:
                    self.user.topupmoney(amount)
                    messagebox.showinfo("info", f"You have Topped up:  AED {amount}")
                    self.wn_home.deiconify()
                    self.root.withdraw()
                else:
                    raise ValueError
            except ValueError:
                messagebox.showerror("error", "A minimum amount to top up is 100 AED!! Please Try Again!!!")
        else:
            messagebox.showerror("error", "All fields must be field!!Please Try Again")

class Cart:

    '''Class to represent the Cart'''
    # Constructor
    def __init__(self, parent, home=Homepage, top=Topup):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg= '#152b3a')
        self.root.title("Your Cart")
        self.root.resizable(0, 0)
        self.wn_home = home
        self.user = User()
        self.carttopup = top
        self.user.updatingtobalance()

        # defining all the lables for the cart page.

        self.lable = tk.Label(self.root, text="Here is Your Cart", font='time 22 bold italic', bg="#0A87AE", fg="white")
        self.lable.place(x=70, y=50, width=450, height=65)

        self.order_lable = tk.Label(self.root, text="Your Order:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.order_lable.place(x=80, y=150, width=110, height=30)

        self.order = tk.Label(self.root, text=purchase_list, font='sans 12 bold', bg="white", fg="black")
        self.order.place(x=200, y=150, width=300, height=30)

        self.price_lable = tk.Label(self.root, text="Total Price:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.price_lable.place(x=80, y=200, width=110, height=30)


        self.price = tk.Label(self.root, text=f"AED {self.totalprice()}", font='sans 12 bold', bg="white", fg="black")
        self.price.place(x=200, y=200, width=300, height=30)

        self.rate_lable = tk.Label(self.root, text="Discount Rate:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.rate_lable.place(x=80, y=250, width=110, height=30)

        self.rate = tk.Label(self.root, text=f"{self.user.rate()}%", font='sans 12 bold', bg="white", fg="black")
        self.rate.place(x=200, y=250, width=300, height=30)

        self.Discounted_lable = tk.Label(self.root, text="Discount Price:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.Discounted_lable.place(x=80, y=300, width=110, height=30)

        self.Discounted = tk.Label(self.root, text=f"AED {self.user.discount(self.totalprice())}", font='sans 12 bold', bg="white", fg="black")
        self.Discounted.place(x=200, y=300, width=300, height=30)

        self.balance_lable = tk.Label(self.root, text="Balance:", font='sans 12 bold', bg="#0A87AE", fg="white")
        self.balance_lable.place(x=80, y=350, width=110, height=30)

        self.balance = tk.Label(self.root, text=self.user.getbalance(), width=35, bd=0, bg="white")
        self.balance.place(x=200, y=350, width=300, height=30)

        self.back = tk.Button(self.root, text = "Back",font='sans 16 bold',
                              highlightbackground='green', highlightthickness = 0, fg = "black", command = self.goback)
        self.back.place(x=70, y=450, width=90, height=40)


        self.paybtn = tk.Button(self.root, text="Pay", font='sans 16 bold',
                              highlightbackground='green', highlightthickness = 0, fg = "black", command = self.cartpay)

        self.paybtn.place(x=430, y=450, width=90, height = 40)

    # this function will direct us back to the homepage

    def goback(self):
        self.wn_home.deiconify()
        self.root.withdraw()

    #  Getting the overall price, of the listed items.

    def totalprice(self):
        sum = 0
        for i in purchase_list.values():
            sum = sum + i
        return sum

    # This function will be used to pay for the listed  items in the cart.

    def cartpay(self):

        if self.user.balancecheck(self.totalprice()):
            messagebox.showerror("Paying System", "Your Payment Was Successful")
            self.user.servicedetail(purchase_list, self.totalprice())
            self.wn_home.deiconify()
            self.root.destroy()
        else:
            messagebox.showerror("error", "Insufficient balance\n "
                                                  "Please To Top Up")


class View:
    '''Class to represent the View page'''

    # This page is only going to be viewed if you are either an employee or a manager.
    # regular users can't access it.
    # constructor

    def __init__(self, parent, home=Homepage):
        self.root = parent
        self.root.geometry("600x600")
        self.root.configure(bg='#152b3a')
        self.root.title("Top Up Page")
        self.root.resizable(0, 0)
        self.wn_home = home
        self.user=User()

        # defining the labels of teh View page

        self.lable = tk.Label(self.root, text="All The Users Info", font='time 22 bold italic', bg="#0A87AE", fg="white")
        self.lable.place(x=70, y=50, width=450, height=65)

        self.txtbox = tk.Text(self.root, font='time 12 bold italic')
        self.txtbox.place(x=70, y=150, width=450, height=320)
        self.txtbox.insert(tk.END, self.viewallaccounts())

        self.back = tk.Button(self.root, text="Back", font='sans 16 bold',
                              highlightbackground='green', highlightthickness=0, fg="black", command=self.goback)
        self.back.place(x=60, y=490, width=190, height=40)
        self.delete = tk.Button(self.root, text="Delete all Accounts", font='sans 16 bold', state='normal',
                              highlightbackground='green', highlightthickness=0, fg="black", command=self.deleteall)
        self.delete.place(x=340, y=490, width=190, height=40)

        self.root.mainloop()

    def viewallaccounts(self):
        return self.user.list()

    def deleteall(self):
        self.deleteme()

    def deleteme(self):
        result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
        if result == 'yes':
            self.user.deleteaccounts()
            self.goback()
        else:
            return


    # invoking this function will direct us to the home page

    def goback(self):
        self.wn_home.deiconify()
        self.root.destroy()

    # this function will determine the state of the delete accounts button
    # first it will check if the user is a manager
    # if it is a manager it will enable the button
    # if it is an staff or trainer it will disable the button

    def state(self):
        if self.user.manager():
            return "normal"
        if self.user.staff():
            return 'disabled'


gui = logintodb()






