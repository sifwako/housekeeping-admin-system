import random

class User:
    """class to represent the user"""
    # Constructor
    def __init__(self, uname="sifan", fname="", password="", address="", pnumber="", acctype="R", balance=0):
        self.user_name = uname
        self.full_name = fname
        self.password = password
        self.address = address
        self.phone_number = pnumber
        self.account_type = acctype
        self.balance = balance
        self.purchases = []
        self.usercode = ''

    # setters and getters functions

    def setUserName(self, userName):
        self.user_name = userName
    def getUserName(self):
        return self.user_name

    def setPassword(self, password):
        self.password = password
    def getPassword(self):
        return self.password

    def setFullname(self, fullname):
        self.full_name = fullname
    def getFullname(self):
        return self.full_name

    def setAddress(self, address):
        self.address = address
    def getaddress(self):
        return self.address

    def setPhoneNum(self, phone):
        self.phone_number = phone
    def getPhoneNum(self):
        return self.phone_number

    def setAccountType(self, accountType):
        self.account_type = accountType
    def getAccountType(self):
        return self.account_type

    def setbalance(self, bal):
        self.balance = bal
    def getbalance(self):
        return self.balance

    def setPurchasedService(self, ser):
        self.purchasedSerivces = ser
    def getPurchasedService(self):
        return self.purchasedSerivces

    # this function will be used by the GUI to configure the sign up page
    # once all infomation are given it is going to be recorded on the Records.txt file and webuser.txt file
    def registerrecods(self, fname, uname, password, addi, pnumber, acctype):
        self.setFullname(fname)
        self.setUserName(uname)
        self.setPassword(password)
        self.setAddress(addi)
        self.setPhoneNum(pnumber)
        self.setAccountType(acctype)
        self.usercode = f"{self.getUserName()[0:3]}{random.randint(100, 999)}"

        # this dictionary variable is what is going to be recoded on the Records.txt file
        self.userrecord = {
            'code': self.usercode,
            'fname': self.getFullname(),
            'uname': self.getUserName(),
            'passw': self.getPassword(),
            'addi': self.getaddress(),
            'pnum': self.getPhoneNum(),
            'balance': self.getbalance(),
            'acctype': self.getAccountType()
        }

        with open("webuser.txt", 'a+') as user:
            # this dictionary variable is what is going to be recoded on the webuser.txt file
            self.webuser = {
                "usercode": self.userrecord['code'],
                "username": self.userrecord["uname"],
                "userpassword": self.userrecord['passw']
            }
            user.write('\n')
            user.write(str(self.webuser))

        # here we will append all the users in to the files created.
        with open("Records.txt", "a+") as allrecords:
            allrecords.write('\n')
            allrecords.write(str(self.userrecord))

    # this function will define the login page for the users.
    # it will take two parameters. a username and password.
    def login(self, username, password):
        self.setUserName(username)
        self.setPassword(password)
        with open("webuser.txt", 'r') as openfile:
            self.loginintro = openfile.readlines()
            for i in self.loginintro:
                self.logininfo = eval(i)
                if self.logininfo['username'] == str(self.getUserName()) and self.logininfo["userpassword"] == \
                        str(self.getPassword()):
                    self.usercode = self.logininfo['usercode']
                    global usercode
                    usercode = self.usercode

        with open('Records.txt', 'r') as fileopen:
            readfile = fileopen.readlines()
            for i in readfile:
                readline = eval(i)
                if readline["code"] == str(self.usercode):
                    self.setFullname(readline['fname'])
                    self.setUserName(readline['uname'])
                    self.setPassword(readline['passw'])
                    self.setAddress(readline['addi'])
                    self.setPhoneNum(readline['pnum'])
                    self.setAccountType(readline['acctype'])

    # this function is used when the user access his profile
    # the function will updated all the users if they run this function
    # it will rewrite it if it gets updated
    def updateinfo(self, name, uname, passw, addi, num):
        file = open('Records.txt', 'r+')
        readfile = file.readlines()
        for i in readfile:
            readline = eval(i)
            if readline["code"] == self.usercode:
                readline['fname'] = name
                self.setFullname(name)
                readline['uname'] = uname
                self.setUserName(uname)
                readline['passw'] = passw
                self.setPassword(passw)
                readline['addi'] = addi
                self.setAddress(addi)
                readline['pnum'] = num
                self.setPhoneNum(num)
        list1 = {
            'code': self.usercode,
            'fname': self.getFullname(),
            'uname': self.getUserName(),
            'passw': self.getPassword(),
            'addi': self.getaddress(),
            'pnum': self.getPhoneNum(),
            "balance": self.getbalance(),
            'acctype': self.getAccountType()
        }

        # before updating we need to check in the filesystem if we have selected the correct user
        # this way we will only update the loged in user.

        with open("Records.txt", "r+") as writefile:
            self.loginintro = writefile.readlines()
            global logintro
            logintro = self.loginintro
            for i in self.loginintro:
                self.logininfo = eval(i)
                if self.logininfo["code"] == self.usercode:
                    self.loginintro[self.loginintro.index(i)] = str(list1)

            # Here will rewrite the files of the specific user.
            with open("Records.txt", 'w') as rewritefile:
                for j in logintro:
                    self.loginintroeval = eval(j)
                    if self.loginintroeval['code'] == self.usercode:
                        rewritefile.write(j)
                        rewritefile.write('\n')
                    else:
                        rewritefile.write(j)

        # in this file manipulation we will try to read the file Records.txt
        # then we will update it into the webuser in case we have changed the username or password
        with open("Records.txt", "r+") as writefile:
            self.loginintro = writefile.readlines()
            with open("webuser.txt", 'w') as rewritefile:
                for i in self.loginintro:
                    self.userlogin = eval(i)
                    list2 = {
                        "usercode": self.userlogin["code"],
                        "username": self.userlogin["uname"],
                        "userpassword": self.userlogin["passw"]
                    }
                    rewritefile.write(str(list2))
                    rewritefile.write("\n")

    # we will use this function in the top up file,
    # when we topup it will update the balance of the user in the database and the profile tap

    def topupmoney(self, amount):
        with open("Records.txt", "r+") as writefile:
            self.loginintro = writefile.readlines()
            global topintro
            topintro = self.loginintro
            for i in self.loginintro:
                self.logininfo = eval(i)
                if self.logininfo["code"] == usercode:
                    totalbalance = float(self.logininfo['balance']) + amount
                    self.setbalance(totalbalance)
                    self.logininfo["balance"] = self.getbalance()
                    self.loginintro[self.loginintro.index(i)] = self.logininfo
            with open('Records.txt', 'w') as rewrite:
                for j in self.loginintro:
                    self.logininfo = eval(str(j))
                    if self.logininfo["code"] == usercode:
                        rewrite.write(str(j))
                        rewrite.write('\n')
                    else:
                        rewrite.write(str(j))

    # this function is going to be used to update the balance of the user.
    def updatingtobalance(self):
        with open('Records.txt', 'r+') as read:
            self.loginintro = read.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    self.setbalance(self.logininfo["balance"])


    # this function is going to used to check the balance
    def balancecheck(self, totalprice):
        with open('Records.txt', 'r+') as read:
            self.loginintro = read.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo["balance"] >= totalprice:
                        return True
                        break

    # this function is going to used to calculate the user's discounts if he/she has any.
    def discount(self, totalprice):
        if self.manager():
            return totalprice - (totalprice * 0.4)
        if self.staff():
            return totalprice - (totalprice * 0.25)
        if self.trainer():
            return totalprice - (totalprice * 0.4)
        else:
            return totalprice



    # checking for the user if he/she is a only regular user
    def regular(self):
        with open('Records.txt', 'r') as rewrite:
            for j in self.loginintro:
                self.logininfo = eval(str(j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo['acctype'] == "R":
                        return True


    # checking for the user if he/she is a manager user
    def manager(self):
        with open('Records.txt', 'r') as rewrite:
            self.loginintro = rewrite.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo["acctype"] == "M":
                        return True

    # checking for the user if he/she is a staff user
    def staff(self):

        with open('Records.txt', 'r') as rewrite:
            self.loginintro = rewrite.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo["acctype"] == "S":
                        return True
    # checking for the user if he/she is a trainer user
    def trainer(self):
        with open('Records.txt', 'r') as rewrite:
            self.loginintro = rewrite.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    if self.logininfo["acctype"] == "T":
                        return True

    # recording the rate of  users based on their acctype
    def rate(self):
        if self.manager():
            return 0.4
        if self.trainer():
            return 0.4
        if self.staff():
            return 0.25
        else:
            return 0

    # this function will be used to record the services that has been purchased by the specific user.
    # it will create a Product-Pruchased.txt file
    # finally it will record the purchases made by the logged in user.

    def servicedetail(self, services, price):
        details = {
            "usercode": "",
            "services": services,
            "totalPrice": price
        }

        with open('Records.txt', 'r+') as read:
            self.loginintro = read.readlines()
            for j in self.loginintro:
                self.logininfo = eval((j))
                if self.logininfo["code"] == usercode:
                    details["usercode"] = usercode
                    with open("Product-Purchased.txt", "a") as appendservice:
                        appendservice.write(str(details))
                        appendservice.write('\n')


    # this will return a list of users so that either the manager or the staff only can view it

    def list(self):

        with open('Records.txt', 'r+') as read:
            list1 = []
            self.loginintro = read.readlines()
            for i in self.loginintro:
                list1.append(i)
                list1.append("\n")
        return (list1)

    # this function is only going to be used by the manager who is authorized to delete all the accounts.

    def deleteaccounts(self):

        with open('Records.txt', 'w') as read:
            read.write("")

        with open("webuser.txt", 'w') as overwrite:
            overwrite.write("")


class RegularUser(User):
    """class to represent the reqular user"""
    def __init__(self, uname="", fname="", password="", address="", pnumber="", acctype={}):
        User.__init__(self, uname, fname, password, address, pnumber, acctype)


class Employee(User):
    """class to represent the Employee"""
    # Constructor
    def __init__(self, uname="", fname="", password="", address="", pnumber="", acctype={}):
        User.__init__(self, uname, fname, password, address, pnumber, acctype)


class Staff(Employee):
    """class to represent the Staff"""
    # Constructor
    def __init__(self, uname="", fname="", password="", address="", pnumber="", acctype={}):
        Employee.__init__(self, uname, fname, password, address, pnumber, acctype)


class Manager(Employee):
    """class to represent the manager"""
    # Constructor
    def __init__(self, uname="", fname="", password="", address="", pnumber="", acctype={}):
        Employee.__init__(self, uname, fname, password, address, pnumber, acctype)


class Trainer(Employee):
    """Class to represent a trainer user"""
    # Constructor
    def __init__(self, uname="", fname="", password="", address="", pnumber="", acctype={}):
        Employee.__init__(self, uname, fname, password, address, pnumber, acctype)



class PayingSystem:
    """A class to represent the paying system"""
    # Constructor
    def __init__(self, cname="", cnumber='', camount=0):
        self.card_name = cname
        self.card_number = cnumber
        self.card_amount = camount


    # Setters and Getters functions

    def setcname(self, name):
        self.card_name = name
    def getcname(self):
        return self.card_name

    def setcnumber(self, num):
        self.card_number = num
    def getcnumber(self):
        return self.card_number

    def setcamount(self, amount):
        self.card_amount = amount
    def getcamount(self):
        self.card_amount

