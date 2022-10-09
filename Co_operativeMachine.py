import sys
import time
import random
import re
import mysql.connector as sql
mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database='Kay_cooperative_database')
mycursor = mycon.cursor()

# mycursor.execute("CREATE TABLE chicago_branch (customer_id INT(4) PRIMARY KEY AUTO_INCREMENT, Full_Name VARCHAR(40), Contact VARCHAR(11), Username VARCHAR(20) UNIQUE KEY, Address VARCHAR(50), Occupation VARCHAR(20), Savings INT(10), unique_ID VARCHAR(4) UNIQUE KEY, Loan INT(10), Info VARCHAR(50))") 

class Co_operative:
    def __init__(self):
        self.name = "OLIVE LANE CO-OPERATIVE NETWORK"
        self.location = "Chicago, America"
        self.mainMenu()

    def mainMenu(self):
        print("Welcome to " + self.name + " " + self.location)
        self.menu = input(""" 
            1. First Timer
            2. Regular
        >>  """)
        if self.menu == "1":
            self.firstTimer()
        elif self.menu == "2":
            self.login()
        else:
            self.mainMenu()

    def firstTimer(self):
        self.user1 = input("As a first timer, you are expected to pay registration fee of #2000 (Type that in) \n>>  ")
        if self.user1 == "2000":  
                time.sleep(2)
                print("")
                print("we would like you to reply to this notification with 'OK' to know that you agree to all terms and conditions")
                self.notification()
                self.user2 = input(">> ")
                if self.user2.lower() == "ok":
                    time.sleep(2)
                    self.register()
                else:
                    print("Please type in 'OK' to be sure you agreed to the terms and conditions")
                    self.notification()
        else:
            print("You are expected to pay the sum of #2000 as your registration fee")
            self.firstTimer()

    def notification(self):
        print("""
                Here are the few notifications of OLIVE LANE Co_operative Network

                1. Every Friday at 4pm will be the time of the meeting

                2. your savings at every meeting is compulsory and which the minimum amount is #500

                3. You have to save continously for good six(6) month before you are licensed to get a loan
        """)


    def register(self):
        print("NOTE THAT YOU ARE EXPECTED TO BE ABOVE 18 BEFORE YOU CAN JOIN THIS CO_OPERATIVE NETWORK \nNow please provide your details")
        self.UserAge = input("Your AGE please > ")
        if self.UserAge >= "18":
            self.full_Name = input("FULL NAME > ")
            self.contact = input("PHONE NO. > ")
            if re.search(r'[a-zA-Z]', self.contact) and len(self.contact) < 11:
                print("Invalid phone number")
                self.register()
            else:
                pass
            self.userName = input("PREFFERD USERNAME > ")
            self.Address = input("ADDRESS > ")
            self.occupation = input("OCCUPATION > ")
            print("Ok, thanks for the details " + self.full_Name + "\n Please wait a bit for your unique id")
            time.sleep(4)
            self.uniqueId = "02"+str(random.randint(10000, 90000))
            print(" " + self.uniqueId, "\n This is your unique ID")
            Query = "INSERT INTO chicago_branch (Full_Name, Contact, Username, Address, Occupation,Age, unique_ID) VALUES(%s, %s, %s,%s, %s, %s, %s)"
            Val = (self.full_Name, self.contact, self.userName, self.Address, self.occupation, self.UserAge, self.uniqueId)
            mycursor.execute(Query, Val)
            mycon.commit() 
            mycon.close()
            time.sleep(4)
            print("")
            print("You are now a full member of " + self.name + ". You can now proceed to the main room \nPLEASE DO NOT FORGET YOUR UNIQUE ID")
            self.login()
        else:
            time.sleep(2)
            print("You are an underage so... bye")
            sys.exit()

    def login(self):
        print("")
        self.user_name = input("Username >> ")
        self.unique_Id = input("Unique ID >> ")
        time.sleep(2)
        sqlQuery = "SELECT Username, unique_ID, Full_Name FROM chicago_branch WHERE Username=%s AND unique_ID=%s"
        sqlVal = (self.user_name, self.unique_Id)
        mycursor.execute(sqlQuery, sqlVal)
        myreg = mycursor.fetchall()
        self.name = myreg[0][2]
        if myreg:
            self.regular()
        else:
            print("INVALID USERNAME/UNIQUE_ID")
            self.login()

    def regular(self):
        print(" ")
        self.user = input("Dear " + self.name + """
            Welcome to today's co_operative meeting
            What would you like to do,,,, TAKE NOTE!!! Your Savings first
        
                1. save                             2. Loan
                3. Check Savings Balance            4. Pay loan back
                5. Members                          6. Notification for the day 
                7. Check co_operative Info.         8. Quit
        >>   """)
        if self.user == "1":
            time.sleep(2)
            self.savings()
        elif self.user == "2":
            time.sleep(2)
            self.loan()
        elif self.user == "3":
            time.sleep(2)
            self.checkBalance()
        elif self.user == "4":
            time.sleep(2)
            self.payBack()
        elif self.user == "5":
            time.sleep(2)
            self.members()
        elif self.user == "6":
            time.sleep(2)
            self.notification4Today()
        elif self.user == "7":
            time.sleep(2)
            self.notification()
            time.sleep(3)
            self.regular()
        elif self.user == "8":
            time.sleep(2)
            sys.exit()
        else:
            print("Input the right string")
            self.regular()

    def savings(self):
        savingsQuery = "SELECT Savings FROM chicago_branch WHERE Username=%s AND unique_ID=%s"
        savingsVal = (self.user_name, self.unique_Id)
        mycursor.execute(savingsQuery, savingsVal)
        myreg1 = mycursor.fetchone()
        # amount = {"1":1000, "2":2000, "3":5000, "4":10000, "5":20000, "6":50000}
        # for key, val in amount.items():
        #     print(key, val)
        # self.userInput = input("Enter your deposit amount> ")
        # query = "SELECT Savings FROM chicago_branch WHERE unique_ID=%s"
        # account = (self.unique_Id,)
        # mycursor.execute(query, account)
        # self.balance = mycursor.fetchone()
        # newBalance = amount (int(self.userInput)) + self.balance (int(0))
        # query = "UPDATE chicago_branch SET Savings = %s WHERE unique_ID=%s"
        # account = (newBalance, self.unique_Id)
        # mycursor.execute(query, account)
        # mycon.commit()
        # print(amount [self.userInput], "deposit is successful") 
        # self.savings()
        
        for self.myBalance in myreg1:
            pass
        self.inputSavings = (input("How much would you like to save today \nNOTE!!! nothing less than #500 \n>> "))
        if self.inputSavings >= 500 :
            self.summation = self.inputSavings [0] + self.myBalance[0]
            balQuery = "UPDATE chicago_branch SET Savings=%s WHERE unique_ID=%s"
            valQuery = (self.summation, self.unique_Id)
            mycursor.execute(balQuery, valQuery)
            mycon.commit()
            print("Successfully saved " + [self.summation] + "\n THAT'S IT, now you can proceed to do any other thing")
            query = "UPDATE user_details SET Savings = %s WHERE Account_no=%s"
            account = (self.summation, self.unique_Id)
            mycursor.execute(query, account)
            mycon.commit()
            self.regular()
        else:
            print("You are supposed to input an amount equals to or greater than #500")
            self.savings()

    def checkBalance(self):
        print("")
        self.myUsername = input("Enter your Username >> ")
        balanceQuery = "SELECT Savings FROM chicago_branch WHERE Username=%s"
        balanceVal = (self.myUsername,)
        mycursor.execute(balanceQuery, balanceVal)
        myreg0 = mycursor.fetchone()
        for self.myBalance in myreg0:
            pass
        if myreg0:
            print("Dear Cusomer; \n  Your current Savings Balance is: #" +str(self.myBalance))
            time.sleep(3)
            self.regular()
        else:
            print("Invalid Username")
            self.checkBalance()

    def members(self):
        print("")
        print("This are list of our members, you can get to know more about yourselves here")
        memberQuery = "SELECT Full_Name FROM chicago_branch"
        mycursor.execute(memberQuery)
        myreg = mycursor.fetchall()
        for members in myreg:
            print(members)
        self.regular()

    def loan(self):
        loanQuery = "SELECT Loan FROM chicago_branch WHERE unique_ID=%s"
        loanVal = (self.unique_Id,)
        mycursor.execute(loanQuery, loanVal)
        myreg2 = mycursor.fetchone()
        for self.loanBalance in myreg2:
            pass
            print("")
        print("Dear " + self.name +"""
        ABOUT THE INTEREST
                
            - NOTE that on every pay back, there's an interest of 5%

            - NOTE that this loan has to be paid within 2 month of collecting the loan, which means you have to return the loans in 8 different times OR LESS, as you wish
        """)
        time.sleep(2)
        self.loanMoney = float(input("How much would you like to get as your loan; \n>> "))
        time.sleep(1)
        if self.loanBalance == 0:
            balanceQuery = "UPDATE chicago_branch SET Interest=%s WHERE unique_ID=%s"
            balanceVal = (self.newBal, self.unique_Id)
            mycursor.execute(balanceQuery, balanceVal)
            mycon.commit()
            print("Payment was Successful")
            time.sleep(2)        
            self.interestPay()
            self.confirmId = input("Unique ID >> ")
            time.sleep(1)
            loan_Query = "SELECT unique_ID FROM chicago_branch WHERE unique_ID=%s"
            loan_Val = (self.confirmId,)
            mycursor.execute(loan_Query, loan_Val)
            myreg3 = mycursor.fetchall()
            if myreg3:
                print("Your request is being processed...")
                time.sleep(3)
                balQuery1 = "UPDATE chicago_branch SET Loan=%s WHERE unique_ID=%s"
                valQuery1 = (self.loanMoney, self.confirmId)
                mycursor.execute(balQuery1, valQuery1)
                mycon.commit()
                print("PLEASE TAKE YOUR LOAN \n" + str(self.loanMoney))
                time.sleep(2)
                print("This is the breakdown of your Loan Pay back")
                self.breakdown = float(self.loanMoney / 8)
                self.interest = float((5 / 100) * self.loanMoney)
                self.total = float(self.breakdown + self.interest)
                time.sleep(2)
                balQuery2 = "UPDATE chicago_branch SET loanBreakdown=%s, DueInterest=%s WHERE unique_ID=%s"
                valQuery2 = (self.breakdown, self.interest, self.unique_Id)
                mycursor.execute(balQuery2, valQuery2)
                mycon.commit()
                print("AMOUNT COLLECTED; " + str(self.loanMoney))
                print("AMOUNT TO BE RETURNED AT EACH MEETING; " + str(self.breakdown))
                print("INTEREST OF 5%; " + str(self.interest))
                print("INTEREST plus AMOUNT TO BE RETURNED; " + str(self.total))
                print("SO YOUR PAYBACK HAS TO BE " + str(self.total) + " EIGHT DIFFERENT TIME OR LESS, AS YOU WISH")
                time.sleep(3)
                self.regular()
            else:
                print("Invalid Credentials")
                self.regular()
        else:
            print("You have an unpaid Loan of " + str(self.loanBalance))
            self.regular()

    def payBack(self):
        payBackQuery = "SELECT Loan FROM chicago_branch WHERE unique_ID=%s"
        payBackVal = (self.unique_Id,)
        mycursor.execute(payBackQuery, payBackVal)
        myreg4 = mycursor.fetchone()
        for self.payBackBalance in myreg4:
            pass
        self.userPay = float(input("WELCOME " + self.name +"; \n Input your payback.. NOTE - just the real money alone not with interest \n> "))
        payBackQuery2 = "SELECT loanBreakdown FROM chicago_branch WHERE unique_ID=%s"
        payBackVal2 = (self.unique_Id,)
        mycursor.execute(payBackQuery2, payBackVal2)
        myreg5 = mycursor.fetchone()
        for self.payBreakdown in myreg5:
            pass
        if self.userPay >= self.payBreakdown:
            print("Please wait while we proccess your request...")
            time.sleep(3)
            self.newBal = float(self.payBackBalance - self.userPay)
            balQuery = "UPDATE chicago_branch SET Loan=%s WHERE unique_ID=%s"
            valQuery = (self.newBal, self.unique_Id)
            mycursor.execute(balQuery, valQuery)
            mycon.commit()
            print("Payment was Successful")
            time.sleep(2)        
            self.interestPay()
        else:
            print("This is not up to your normal breakdown payment per week \n This is your breakdown payment " + str(self.payBreakdown))
            self.payBack()

    def interestPay(self):
        print("")
        self.userInterest = float(input("Now your interest > "))
        payBackQuery3 = "SELECT DueInterest FROM chicago_branch WHERE unique_ID=%s"
        payBackVal3 = (self.unique_Id,)
        mycursor.execute(payBackQuery3, payBackVal3)
        myreg6 = mycursor.fetchone()
        for self.dueInterest in myreg6:
            pass
        payBackQuery4 = "SELECT Interest FROM chicago_branch WHERE unique_ID=%s"
        payBackVal4 = (self.unique_Id,)
        mycursor.execute(payBackQuery4, payBackVal4)
        myreg7 = mycursor.fetchone()
        for self.companyInterest in myreg7:
            pass
        if self.userInterest == self.dueInterest:
            print("Please wait while we proccess your request...")
            time.sleep(3)
            self.payInterest = float(self.companyInterest + self.userInterest)
            interestQuery = "UPDATE chicago_branch SET DueInterest=%s WHERE unique_ID=%s"
            interestVal = (self.payInterest, self.unique_Id)
            mycursor.execute(interestQuery, interestVal)
            mycon.commit()
            print("Payment of interest was Successful")
            time.sleep(3)
            self.regular()
        else:
            print("That is not the right amount for the interest \n The normal interest that should be paid back is "+ str(self.dueInterest))
            self.interestPay()

       

    def notification4Today(self):
        print("""
        There's nothing much for today, Just make sure
            - You pay your savings
            - Return due loan &
            - Invite others
        """)   
        time.sleep(3)
        self.regular()

project = Co_operative()
 