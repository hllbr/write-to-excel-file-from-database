from sqlite3.dbapi2 import Cursor, connect
import xlsxwriter
import sqlite3
w = xlsxwriter.Workbook("hllbr.xlsx")
s = w.add_worksheet("customers")

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("Select FirstName From Customers ")
for data,row in enumerate(cursor):
    s.write(data,0,row[0])
w.close()