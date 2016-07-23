import MySQLdb
import time
import sys
import os
sys.path.append(os.path.abspath("SO_site-packages"))

#Imports
import pyperclip
from Tkinter import Tk


#login stuff
loggedin = False
loginSaved = False
if (os.path.isfile("login.txt")) :
	loginSaved = True
else:
	print False

if loginSaved:
	print "Logged in.\nUser:"
	with open("login.txt") as f:
		lines = f.readlines()
 		user =  lines[0].strip()
 		userid = lines[1]
  
if loggedin==False:	
	if loginSaved == False:
 		user = raw_input("Please enter username: ")
 		userid = raw_input("Please enter user id: ")

 	conn2 = MySQLdb.connect(host= "sql5.freesqldatabase.com",
			user="sql5128478",
			passwd="KmRD1fpZdL",
			db="sql5128478")
 	x1 = conn2.cursor()
 	
 	try:
		x1.execute("""SELECT user FROM user WHERE id = %s""", (userid))
		userdata = x1.fetchone()
		if user == userdata[0]:
 		   	print "Authentication successful!"
 		   	loggedin = True
 
	except:
		conn2.rollback()
  
#Listener for clipboard
recent_value = ""
while loggedin:
	tmp_value = pyperclip.paste()

	conn = MySQLdb.connect(host= "sql5.freesqldatabase.com",
			user="sql5128478",
			passwd="KmRD1fpZdL",
			db="sql5128478")
	x = conn.cursor()

	if tmp_value != recent_value:
		recent_value = tmp_value
		#print "Value changed: %s" % str(recent_value)[:20]

		try:
			#x.execute("""INSERT INTO  `cb`.`data` ( `id` , `data`) VALUES (%s,%s)""",(`2` , recent_value ))
			x.execute("""UPDATE data SET data = %s WHERE id = %s""", (recent_value,`1`))
			print "db updated"
			conn.commit()
		except:
			conn.rollback()

	#Listener for database change
	try:
		conn1 = MySQLdb.connect(host= "sql5.freesqldatabase.com",
			user="sql5128478",
			passwd="KmRD1fpZdL",
			db="sql5128478")
		x1 = conn1.cursor()
		print "checking db"
		x1.execute("""SELECT data FROM data where id = %s""",(`1`))
		data = x1.fetchone()
		newData = ""
			#print row[0],row[1]
		newData =  data[0]
		print newData
		print recent_value
		if newData != pyperclip.paste():
			print"DB Val different"
			pyperclip.copy(newData)

	except:
		conn1.rollback()
		conn1.close()
		conn.close()
	time.sleep(0.1)
  