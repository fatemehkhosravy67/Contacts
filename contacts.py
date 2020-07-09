# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:15:47 2020

@author: fatemeh
"""


import sqlite3
class CONTACTS():
    firstname = input("please input first name:")
    lastname = input("please input last name:")
    cellnum = int(input("please input cell number:"))
    
    def __init__(self,firstname,lastname,cellnum):
        self.first_name = firstname
        self.last_name = lastname
        self.cell_num = cellnum
    def Contacts(self):
        db = sqlite3.connect("contacts.db")
        db.execute("DROP TABLE IF EXISTS contacts")
        db.execute("CREATE TABLE contacts(first_name text,last_name text,cell_num int)")
        db.execute("INSERT INTO contacts(first_name,last_name,cell_num) VALUES (?,?,?),(first_name,last_name,cell_num)")
        db.commit()
        cursor = db.execute("SELECT * FROM contacts ORDER BY first_name")
        for row in cursor: print(row)

        
        
        
