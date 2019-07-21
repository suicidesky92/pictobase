#!/bin/python3

import os
import sqlite3

def testisdir():
 if not os.path.isdir('pics'):
  os.mkdir('pics')

try:
 with open("mypicturedatabase.db", 'r') as file:
  newdb = False
except FileNotFoundError:
 newdb = True 

connecting = sqlite3.connect("mypicturedatabase.db")
cursor = connecting.cursor()


def create_db():
 cursor.execute('''CREATE TABLE picture ( name TEXT NOT NULL, data BLOB NOT NULL )''')



def scanandwrite():
 dirpic = "./pics/"
 listpic = os.listdir(dirpic)
 for namepic in listpic:
  with open(dirpic + namepic, 'rb') as file:
   fileblob = file.read()
   data = (namepic, fileblob)
   cursor.execute('INSERT INTO picture VALUES (?,?)', data)
   connecting.commit()

def find(filename = 'photo.jpg'):
 filename = (filename,)
 for row in cursor.execute("SELECT data FROM picture WHERE name LIKE ?", filename):
  with open('test.jpg', 'wb') as file:
   file.write(row[0])

def tests(newdb):
 if newdb == True:
  create_db()
  scanandwrite()

testisdir()
tests(newdb)

find("lock.jpg")
