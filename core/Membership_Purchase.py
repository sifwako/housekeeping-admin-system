# Class to represent a membership level
class Membership_Level:
    '''Class to represent a membership level purchased by users'''
    # Constructor
    def __init__(self):
        self.memID = ''
        self.memName = ''
        self.memYear = 0
        self.price = 0.0
        self.description = ''
    def setmemID(self,Id=''):
        self.memID = Id
    def getmemID(self):
        return self.memID
    def setmemName(self,name=''):
        self.memName = name
    def getmemName(self):
        return self.memName
    def setmemYear(self,year=0):
        self.memYear = year
    def getmemYear(self):
        return self.memYear
    def setmemPrice(self,price=0.0):
        self.price = price
    def getmemPrice(self):
        return self.price
    def setdescription(self, desc=''):
        self.description = desc
    def getdescription(self):
        return self.description

# Beginner Membership Level
class Beginner(Membership_Level):
    '''Class to represent a beginner membership level'''
    # Constructor
    def __init__(self):
        Membership_Level.__init__(self)

# Active Membership Level class
class Active(Membership_Level):
    '''Class to represent an active membership level'''
    #Constructor
    def __init__(self):
        Membership_Level.__init__(self)

# Superfit Membership Level class
class Superfit(Membership_Level):
    '''Class to represent a superfit membership level'''
    #Constructor
    def __init__(self):
        Membership_Level.__init__(self)

# A fitness class
class Fitness_Class:
    '''Class to represent a fitness class'''
    # Constructor
    def __init__(self):
        self.fitID = ''
        self.fitName = ''
        self.fitPrice = 0.0
        self.description =''
    def setfitID(self,id=''):
        self.fitID =id
    def getfitID(self):
        return self.fitID
    def setfitName(self,name=''):
        self.fitName = name
    def getfitName(self):
        return self.fitName
    def setfitPrice(self,price=0.0):
        self.fitPrice= price
    def getfitPrice(self):
        return self.fitPrice
    def setdescription(self, desc=''):
        self.description = desc
    def getdescription(self):
        return self.description

# Class to represent a Yoga fitness type
class Yoga(Fitness_Class):
    '''Class to represent a Yoga fitness class'''
    # Constructor
    def __init__(self):
        Fitness_Class.__init__(self)
        self.courseType =''
    def setcourseType(self, crs=''):
        self.courseType = crs
    def getcourseType(self):
        return self.courseType

# Zumba fitness class
class Zumba(Fitness_Class):
    '''Class to represent a Crossfit fitness class'''
    # Constructor
    def __init__(self):
        Fitness_Class.__init__(self)
        self.classType = ''
    def setclassType(self,type=''):
        self.classType=type
    def getclassType(self):
        return self.classType

# Pilates fitness  class
class Pilates(Fitness_Class):
    '''Class to represent a Cycling fitness class'''
    # Constructor
    def __init__(self):
        Fitness_Class.__init__(self)
        self.classType = ''
    def setclassType(self,clss=''):
        self.classType = clss
    def getclassType(self):
        return self.classType


# Payment class
class Payment:
    '''Class to represent a credit card payment'''
    # Constructor
    def __init__(self):
        self.cardName = ""
        self.cardNo = ""
        self.amount = 0.0
        self.cvv = ''
    def setcardName(self, name=''):
        self.cardName = name
    def getcardName(self):
        return self.cardName
    def setcardNo(self, no = ""):
        self.cardNo =no
    def getcardNo(self):
        return self.cardNo
    def setamount(self, amount=0.0):
        self.amount=amount
    def getamount(self):
        return self.amount
    def setcvv(self,cvv=''):
        self.cvv = cvv
    def getcvv(self):
        return self.cvv