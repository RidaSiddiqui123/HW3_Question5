# -------------------------------------------------------------------------
# AUTHOR: Rida Siddiqui
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #2
# TIME SPENT: 2 hrs
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with
# standard arrays

# importing some Python libraries
# --> add your Python code here
from pymongo import MongoClient
#from parser import *

def connectDataBase():
    # Create a database connection object using pymongo
    # --> add your Python code here

    DB_HOST = 'localhost:27017'

    try:
        client = MongoClient(host=[DB_HOST])
        db = client.CSParser
        return db

    except:
        print("Database not connected")


def insertPage(col, url, html):
    col.insert_one({"url": url, "html": html})



#def getPageURL(col, page):
    #pageToParse = col.find({"url": page}, {"html": 1})
   # parsePage(pageToParse)


def insertFaculty(col, list, list1):
    print()
