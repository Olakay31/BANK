import sys
import os
import time
import mysql.connector as sql
from select import select
import random

CBT_db = sql.connect(host="127.0.0.1", user="root", password ='', database="CBT_DATABASE")
cursor = CBT_db.cursor()
# cursor.execute("CREATE DATABASE CBT_DATABASE")
# cursor.execute("CREATE TABLE STUDENT_REG (STUDENT_ID INT(50) PRIMARY KEY AUTO_INCREMENT, STUDENT_FULLNAME VARCHAR(30), PASSWORD_ INT(11))")
# cursor.execute("CREATE TABLE STUDENT_(MARKS IN SUBJECT  INT(10) UNIQUE")
#DELETE FROM `USER_LOG` WHERE `USER_LOG`.`USER_ID` = 2;

class CBT_dbClass:
    def __init__(self):
        self.connection()
        self.option()
        
    def connection(self):
        self.CBT_db = sql.connect(host="localhost", user="root", passwd="", database="CBT_database")
        self.cursor = self.CBT_db.cursor()
  
    def option(self):
        print("""CBT EXAMINATION
              1. Register
              2. Question
              3. Quit""")
        self.userInput = input("Enter your option to countinue: ")
        if self.userInput == "1":
            self.register()
        elif self.userInput == "2":
            self.question()
        elif self.userInput == "3":
            self.quit()
        else:
            print("Invalid input")
            self.option() 
            
            
    def register(self):
           # global student_name
        self.connection()
        detail = ["fName", "gender","phone", "password"]
        request = ["Full Name", "Gender","Phone Number", " Password"]
       # student_name = (detail[0])
        for i in range(4):
            detail[i] = input("Enter your "+request[i]+"  ")
            reg_id = "02"+"reg"+str(random.randint(10000000, 90000000))
        myquery = """INSERT INTO student_reg (Full_Name, Gender, Phone_Number, Password, Reg_Id) VALUE(%s, %s, %s, %s, %s)"""
        val = (detail[0], detail[1], detail[2], detail[3], reg_id)
        self.cursor = self.CBT_db.cursor()
        self.cursor.execute(myquery, val)
        self.CBT_db.commit()
        print ("Please wait your Transaction is being processing")
        time.sleep(5)
        print(self.cursor.rowcount, """registration is successful 
              Your account number is """+reg_id)
        self.CBT_db.close()
        self.option()         
        
# Question_db = ["1. what is a noun?\n", "2. what is a verb?\n", "3. what is a pronoun?\n", "4. what is an adverb?\n", "5. what is the capital of oyo?\n"]
# answers_db = [["name", "person", "animal", "place", "things"], ["action", "word"], ["use", "noun"], ["qualifies", "verb"],["ibadan"]]
# x = 0
# #correct = 0
# # score = 0
# studentscore = []

# student_list = []
# no_student = int(input("Enter the number of student: "))
# for k in range(0, no_student):
#      m= input()
#      student_list.append(m)
# print(student_list)

# for y in student_list:
#     print("Your Exam Start Now\n", str(y))
#     x = 0
#     score = 0
#     for j in Question_db:
#         correct = 0
#         print(j)
#         userinput = input("Enter the correct Answer\n")
#         answer = answers_db[x]
#         for option in answer:
#             if option in userinput:
#                 correct +=1
#         if len(answer) == correct:
#             print("you are correct")
#             score +=5
#         else:
#             print("you are wrong")
#         x +=1
#     studentscore.append(score)
#     print("hello" " " +str(y)+ ", your total score is" " " +str(score)) 
# print(studentscore)
# studentscoreMax = max(studentscore)
# maxIndex = studentscore.index(studentscoreMax) 
# print("Congratulation" " " +str(student_list[maxIndex])+ " " "you have a maximum score of" " " +str(studentscore[maxIndex]))

# score = [24, 30]
# student = [ ' ', ' ']
# x = 0
# hightestScore = []
# for na in score:
#     if na == max(score):
#         hightestScore.append(student[x])
#     x +=1
# print(", " .join(hightestScore)) 
      
    # def question(self):
    #     transact = ["1. Withdraw", "2. Deposit", "3. Transfer", "4. Check Balance", "5. Quickairtime", "6. loan", "7. Customer Details", "8. close Account", "9. cancel"]
    #     self.acct_no = input("Enter your account number: ")
    #     self.acct_pin = input("Enter your account pin: ")
    #     query = "SELECT * FROM user_details WHERE Account_no=%s AND Account_Pin=%s"
    #     val = (self.acct_no, self.acct_pin)
    #     self.cursor.execute(query, val)
    #     self.record = self.cursor.fetchall()
    #     if self.record:
    #         print("You are welcome dear "+self.record[0][1]+" "+self.record[0][2])
    #         for val in transact:
    #             print(val)
    #         self.userInput = input("Enter an option to continue: ")
    #         if self.userInput == "1":
    #             self.withdraw()
    #         elif self.userInput == "2":
    #             self.deposit()
    #         elif self.userInput == "3":
    #             self.transfer()
    #         elif self.userInput == "4":
    #             self.checkBalance()
    #         elif self.userInput == "5":
    #             self.quickairtime() 
    #         elif self.userInput == "6":
    #             self.loan() 
    #         elif self.userInput == "7":
    #             self.customerDetails() 
    #         elif self.userInput == "82":
    #             self.closeAccount()             
    #         elif self.userInput == "9":
    #             self.option()
    #         else:
    #             print("Invalid input")
    #             self.option() 
    #     else:
    #         print("Invalid account details. please go and register first to continue")
    #         self.option()      
            
    def quit(self):
        self.CBT_db.close()
        sys.exit()

CBT = CBT_dbClass()            
            
