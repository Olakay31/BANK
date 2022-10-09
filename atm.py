#BANK APP
from sqlite3 import Cursor
import sys
import os
import time
import mysql.connector as sql
bank_database = sql.connect(host="127.0.0.1", user="root", password ='', database="_ACCOUNT_DATABASE")
cursor = bank_database.cursor()
# cursor.execute("CREATE DATABASE _ACCOUNT_DATABASE")
#cursor.execute("CREATE TABLE USER_LOG (USER_ID INT(255) PRIMARY KEY AUTO_INCREMENT, USER_NAME VARCHAR(30) UNIQUE, USER_PASSWORD INT(11))")
# cursor.execute("CREATE TABLE USER_ACCOUNT(ACCOUNT_NUMBER INT(10) UNIQUE, ACCOUNT_NAME VARCHAR(20), ACCOUNT_BALANCE INT(20))")
#DELETE FROM `USER_LOG` WHERE `USER_LOG`.`USER_ID` = 2;
# cursor.execute("DELETE FROM _ACCOUNT_DATABASE TABLE USE_LOG")
# cursor.execute("DELETE FROM USER_LOG")
# sql = "DROP TABLE USER_LOG"
# cursor.execute(sql)
class Bankapp:
    def __init__(self):
        pass
    def landing_page(self):
        print("""
            FIRST BANK PLC
        """)
        print("Type R to create account of L to log in")
        try:
            user_ = input("TYPE OPTION :")
            if user_ == "L":
                self.login()
            elif user_ == "R":
                self.registration()
        except:
            print(".....Loading Page")
            time.sleep(2)
            self.landing_page() 
    def registration(self):
        print("""
                    FIRST BANK PLC
                       Sign Up
        """)

        self.user_ = input("Enter Username")
        self.password = input("Enter Password of Atleat 5 digit ")
        verify = input("Confirm password")
        if self.password == verify:
            bankquery = "INSERT INTO USER_LOG(USER_NAME,USER_PASSWORD) VALUES(%s,%s)"
            reg_values = (self.user_,self.password)
            cursor.execute(bankquery,reg_values)
            bank_database.commit()
        else:
            print("Password does not match")
            self.registration()
        
    def login(self):
        print("""
                    FIRST BANK PLC
                       login
        """)
        self.user_ = input("Enter Username")
        self.pin = input ("Enter password")
        if self.pin == self.password:
            print("welcome")
        else:
            print("incorrect password")

firstbank = Bankapp()     
firstbank.landing_page()   

      