import MySQLdb
import time
import sys
import os
sys.path.append(os.path.abspath("SO_site-packages"))

import pyperclip
from Tkinter import Tk

loggedin = False
if (os.path.isfile("login.txt")) :
  
if loggedin==False:	
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
    print userdata[0]
    if user == userdata[0]:
      loggedin = True
 
  except:
   conn2.rollback()
  
  
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
  