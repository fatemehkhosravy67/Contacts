# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 18:33:41 2020

@author: fatemeh
"""

import sqlite3
class CONTACTS():
    def __init__(self,firstname,lastname,cellnum):
        self.first_name = firstname
        self.last_name = lastname
        self.cell_num = cellnum
        self.db=None        
    def CreateDBandTB(self,dbName,tbName):
        self.db = sqlite3.connect(dbName)
        self.db.execute(" CREATE TABLE IF NOT EXISTS {1}(fname varchar(50),lname varchar(50),cellNO int)".format(tbName,tbName))
        self.db.commit()
    def InsertData(self):
        mySTR="INSERT INTO contacts(fname,lname,cellNO) VALUES ('{0}','{1}',{2})".format(self.first_name,self.last_name,self.cell_num)
        self.db.execute(mySTR)
        self.db.commit()
    def GetData(self,tbName):
        cursor = self.db.execute("SELECT * FROM {0} ORDER BY fname".format(tbName))
        for row in cursor: print(row)
        


firstname = input("please input first name:")
lastname = input("please input last name:")
cellnum = int(input("please input cell number:"))
myContact=CONTACTS(firstname, lastname, cellnum)
myContact.CreateDBandTB('ContactDB', 'contacts')
myContact.InsertData()
myContact.GetData('contacts')
























