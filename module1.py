import pymysql as ps
import sys
import string
import os
from prettytable import PrettyTable
con=ps.connect("localhost","root","","IIT")
cur=con.cursor()
Admin_name='twinkle'
Admin_password='abcd'
def check_admin():
	n=input("ENTER ADMIN NAME : ")
	p = input("ENTER ADMIN PASSWORD : ")
	if n==Admin_name and p==Admin_password:
		return 1
	else:
		return 0

def user_menu():
	"""
				+--------------------------------------------------+
							.WELCOME.
				+--------------------------------------------------+
								
							1. NEW USER
							2. CURRENT USER
							3. EXIT

				+--------------------------------------------------+

							ENTER YOUR CHOICE :
	"""
def first():
	""" 
					------------------------------------------------------------------------------------------------------------
					------------------------------------------------------------------------------------------------------------

									   	WELCOME    TO    ' ASHIYANA '


   										(India's No.1 Property Dealers )

					--------------------------------------------------------------------------------------------------------------
					--------------------------------------------------------------------------------------------------------------
	"""
def c_user_menu():
	"""
					+------------------------------------------------------------------------------+
									GREETINGS OF THE DAY !
					+------------------------------------------------------------------------------+
						
										_MENU_

									1.VIEW YOUR DETAIL
									2.UPDATE YOUR DETAIL
									3.VIEW PROPERTIES
									4.BOOK APPOINTMENT
									5.SELL PROPERTY
									6.EXIT

									ENTER YOUR CHOICE ::::

					+------------------------------------------------------------------------------+
	"""
def sell_property():
	os.system('clear')
	UserId = input("ENTER YOUR UserId ")
	q="select * from users where UserId = '%s'"%(UserId)
	cur.execute(q)
	if cur.rowcount>0:
		os.system('clear')
		q="select max(Sn) from vtable"
		cur.execute(q)
		n=cur.fetchone()
		num=n[0] + 601
		print("     ENTER DETIALS OF YOUR PROPERTY: ")
		Property_Id = 'HH' + str(num)
		Price = input("ENTER Price of your property excluding Tax: ")
		BHK= input("ENTER BHK: ")
		Sqft = input("ENTER Sqft: ")
		Property_Type= input("ENTER Property_Type: ")
		Exterior_Wall= input("ENTER Exterior_Wall: ")
		Location= input("ENTER Location: ")
		q="insert into vtable values(%d,'%s','%s','%s','%s','%s','%s','%s','%s')"%(num,UserId,Property_Id,Price,BHK,Sqft,Property_Type,Exterior_Wall,Location)
		os.system('clear')
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tTHANKU FOR YOUR SUBMISSION ! \n\t\t\t\t\t\t\t\tWE WILL REVIEW YOUR PROPERTY SOON AND HENCE WILL INFORM YOU THE SAME !")
		u=input()
		cur.execute(q)
		con.commit()
	else:
		print("WRONG UserId !!!!! ")
def display_all_property():
	os.system('clear')
	q="select * from property "
	cur.execute(q)
	row=cur.fetchall()
	os.system('clear')
	print("\n\n\n\n\t\t\t\tDETAILS of ALL PROPERTIES:\n\n\n\n\n\n\n")
	t = PrettyTable(['Price','BHK','Sqft','Property_Type','Exterior_Wall','Location','PropertyId','STATUS' ])
	for i in range(0,len(row)):
		x = row[i]
		t.add_row(x)
	t.align['Title'] = 'l'
	print(t)
	u=input()
def buy_property():
	os.system('clear')
	m=True
	while m!=False:
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tMenu\n\n")
		print("\t\t\t\t\t\t\t\t1.VIEW ALL PROPERTIES")
		print("\t\t\t\t\t\t\t\t2.VIEW PROPERTIES WRT LOCATION")
		print("\t\t\t\t\t\t\t\t3.VIEW PROPERTIES WRT PROPERTY TYPE")
		print("\t\t\t\t\t\t\t\t4.VIEW PROPERTIES WRT BHK")
		print("\t\t\t\t\t\t\t\t5.VIEW PROPERTIES WRT STATUS-ON")
		print("\t\t\t\t\t\t\t\t6.EXIT")
		c=input("ENTER YOUR CHOICE: ")
		if c=='1':
			os.system('clear')
			q="select * from property "
			cur.execute(q)
			row=cur.fetchall()
			os.system('clear')
			print("\n\n\n\n\t\t\t\tDETAILS of ALL PROPERTIES:\n\n\n\n\n\n\n")
			t = PrettyTable(['Price','BHK','Sqft','Property_Type','Exterior_Wall','Location','PropertyId','STATUS' ])
			for i in range(0,len(row)):
				x = row[i]
				t.add_row(x)
			t.align['Title'] = 'l'
			print(t)
			u=input()
			
		if c=='2':
			os.system('clear')
			print("\n\n\nOUR PROPERTIES ARE IN LOCATIONS :\n\n Kanpur,Delhi,Patna,Varanasi \n\n Lucknow,Mumbai,Mathura,Amritsar \n\n Kolkata,Chennai,Aligarh,Indore\n\n")
			l=input("ENTER YOUR PREFERRED LOCATION : ")
			q="select * from property where Location = '%s'"%(l)
			cur.execute(q)
			row=cur.fetchall()
			os.system('clear')
			print("\n\n\n\n\t\t\t\tDETAILS of ALL PROPERTIES:\n\n\n\n\n\n\n")
			t = PrettyTable(['Price','BHK','Sqft','Property_Type','Exterior_Wall','Location','PropertyId','STATUS' ])
			for i in range(0,len(row)):
				x = row[i]
				t.add_row(x)
			t.align['Title'] = 'l'
			print(t)
			u=input()
		if c=='3':
			os.system('clear')
			print("\n\n\nOUR PROPERTIES TYPES INCLUDE:\n\n Apartment,Villa,Office Space ,Plot ,Bungalow")
			l=input("ENTER YOUR PREFERRED PROPERTY TYPE : ")
			q="select * from property where Property_Type = '%s' "%(l)
			cur.execute(q)
			row=cur.fetchall()
			os.system('clear')
			print("\n\n\n\n\t\t\t\tDETAILS of ALL PROPERTIES:\n\n\n\n\n\n\n")
			t = PrettyTable(['Price','BHK','Sqft','Property_Type','Exterior_Wall','Location','PropertyId','STATUS' ])
			for i in range(0,len(row)):
				x = row[i]
				t.add_row(x)
			t.align['Title'] = 'l'
			print(t)
			u=input()
		if c=='4':
			os.system('clear')
			print("\n\n\nOUR BHK INCLUDE:\n\n 1,2,3,4,5")
			l=int(input("ENTER YOUR PREFERRED BHK : "))
			q="select * from property where BHK = %d "%(l)
			cur.execute(q)
			row=cur.fetchall()
			os.system('clear')
			print("\n\n\n\n\t\t\t\tDETAILS of ALL PROPERTIES:\n\n\n\n\n\n\n")
			t = PrettyTable(['Price','BHK','Sqft','Property_Type','Exterior_Wall','Location','PropertyId','STATUS' ])
			for i in range(0,len(row)):
				x = row[i]
				t.add_row(x)
			t.align['Title'] = 'l'
			print(t)
			u=input()
		if c=='5':
			os.system('clear')
			q="select * from property where Status = 'ON' "
			cur.execute(q)
			row=cur.fetchall()
			os.system('clear')
			print("\n\n\n\n\t\t\t\tDETAILS of ALL PROPERTIES:\n\n\n\n\n\n\n")
			t = PrettyTable(['Price','BHK','Sqft','Property_Type','Exterior_Wall','Location','PropertyId','STATUS' ])
			for i in range(0,len(row)):
				x = row[i]
				t.add_row(x)
			t.align['Title'] = 'l'
			print(t)
			u=input()
		if c=='6':
			m=False
def dis_review():
	os.system('clear')
	q="select * from rtable "
	cur.execute(q)
	row=cur.fetchall()
	os.system('clear')
	print("\n\n\n\n\t\t\t\t\t\t\t\t\t\tPUBLIC'S RESPONSE :::::::\n\n\n\n\n\n\n")
	t = PrettyTable(['SERIAL NO','OUR USERS','THEIR REVIEWS', 'RATINGS(STARS)' ])
	for i in range(0,len(row)):
		x = row[i]
		t.add_row(x)

	t.align['Title'] = 'l'
	print(t)
	u=input()

def give_review():
	os.system('clear')
	print("\n\n                 FEEDBACK FORM ::  \n\n")
	q="select max(Sn) from rtable"
	cur.execute(q)
	n=cur.fetchone()
	num=n[0] + 1
	UserId=input("ENTER YOUR UserId: ")
	q="select * from users where UserId = '%s'"%(UserId)
	cur.execute(q)
	if cur.rowcount>0:
		q="select * from rtable where UserId = '%s'"%(UserId)
		cur.execute(q)
		if cur.rowcount>0:
			print("FEEDBACK EXISTS !!!!! ")
		else:
			f = input("PLEASE ! ENETR YOUR REVIEW : ")
			s = input("ENTER STAR-RATING OUT OF 5")
			if int(s) <6 and int(s)>0:
				q="insert into rtable values(%d,'%s','%s','%s')"%(num,UserId,f,s)
				cur.execute(q)
				con.commit()
			else:
				print("Enter a valid rating 1 to 5")
	else:
		print("Check your UserId!!!!")
def Admin_menu():
	"""
+--------------------------------------------------------------------------------------------+
								ADMIN MENU
+---------------------------------------------------------------------------------------------+
							1.VIEW ALL USERS
							2.VIEW SPECIFIC USER
							3.DELETE A USER
							4.VIEW PROPERTIES
							5.ADD PROPERTIES
							6.VIEW APPOINTMENTS
							7.VIEW SELLERS TO BE VERIFIED 
							8.VIEW PROPERTIES SOLD
							9.EXIT
+---------------------------------------------------------------------------------------------+
						ENTER YOUR CHOICE ::
+----------------------------------------------------------------------------------------------+
	"""
def appointment_table():
	os.system('clear')
	q="select * from atable "
	cur.execute(q)
	row=cur.fetchall()
	os.system('clear')
	print("\n\n\n\n\t\t\t\tDETAILS of ALL APPOINTMENTS:\n\n\n\n\n\n\n")
	t = PrettyTable(['Sn','UserId','PropertyId','Appointment_date','Appointment_time','Status' ])
	for i in range(0,len(row)):
		x = row[i]
		t.add_row(x)
	t.align['Title'] = 'l'
	print(t)
	u=input()
def set_appointment():
	os.system('clear')
	q="select max(Sn) from atable"
	cur.execute(q)
	n=cur.fetchone()
	num=n[0] + 1
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t A VERY HEARTY WELCOME !!! ")
	print("\t\t\t\t\t\t\t\t WE ARE VERY GLAD TO SEE YOU FOUND YOUR DREAM 'ASHIYANA'!")	
	print("\t\t\t\t\t\t\t\t Please,\t\t\t\t\t\t\t\t ENTER YOUR UserId :")
	u=input()
	print("\t\t\t\t\t\t\t\t ENTER YOUR Property_Id :")
	h=input()
	print("\t\t\t\t\t\t\t\t ENTER YOUR Preffered DATE :")
	d=input()
	print("\t\t\t\t\t\t\t\t ENTER YOUR Preffered TIME :")
	t=input()
	print(u,h,t,d)
	q="insert into atable values(%d,'%s','%s','%s','%s')"%(num,u,h,d,t)
	cur.execute(q)
	con.commit()

def verification_table():
	os.system('clear')
	q="select * from vtable "
	cur.execute(q)
	row=cur.fetchall()
	os.system('clear')
	print("\n\n\n\n\t\t\t\tDETAILS of ALL USERS WHO WANT TO SELL THEIR PROPERTY :\n\n\n\n\n\n\n")
	t = PrettyTable(['sn','UserId','PropertyId','Price','BHK','Sqft','Property_Type','Exterior_Wall','Location' ])
	for i in range(0,len(row)):
		x = row[i]
		t.add_row(x)
	t.align['Title'] = 'l'
	print(t)
	u=input()	
def psold_table():
	os.system('clear')
	q="select * from psold "
	cur.execute(q)
	row=cur.fetchall()
	os.system('clear')
	print("\n\n\n\n\t\t\t\tDETAILS of ALL PROPERTIES SOLD :\n\n\n\n\n\n\n")
	t = PrettyTable(['sn','UserId','PropertyId'  ])
	for i in range(0,len(row)):
		x = row[i]
		t.add_row(x)
	t.align['Title'] = 'l'
	print(t)
	u=input()	
def display_me():
	os.system('clear')
	UserId = input("ENTER  UserId: ")
	Password=input("ENTER  PASSWORD: ")
	q="select * from users where UserId = '%s'and Password = '%s'"%(UserId,Password)
	cur.execute(q)
	if(cur.rowcount>0):
		row= cur.fetchall()
		os.system('clear')
		print("\n\n\n\n\t\t\t\tYOUR DETAILS:\n\n\n\n\n\n\n")
		t = PrettyTable(['Sn','Name','UserId','Password','Age','MobNo','AdharNo' ])
		for i in range(0,len(row)):
			x = row[i]
			t.add_row(x)
		t.align['Title'] = 'l'
		print(t)
		u=input()
	else:
		os.system('clear')
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tWRONG UserId OR Password !!!!!!!!! ")
		u=input()
def display_all_users():
	os.system('clear')
	q="select * from users "
	cur.execute(q)
	row=cur.fetchall()
	os.system('clear')
	print("\n\n\n\n\t\t\t\tDETAILS of ALL USERS:\n\n\n\n\n\n\n")
	t = PrettyTable(['Sn','Name','UserId','Password','Age','MobNo','AdharNo' ])
	for i in range(0,len(row)):
		x = row[i]
		t.add_row(x)
	t.align['Title'] = 'l'
	print(t)
	u=input()
class myexp ( Exception ):
	def __init__(self,msg):
		self.message = msg

def new_user_menu():
	"""
					+-------------------------------------------------------------------------+
							HEY-YA ! LET'S START BY KNOWING YOU A BIT
					+-------------------------------------------------------------------------+

								SO, DO YOU WANT TO .


								1. BUY A PROPERTY ?
								2. SELL  A PROPERTY ?

					+-------------------------------------------------------------------------+

								ENTER YOUR CHOICE:
	"""
def new_user_insert():
	os.system('clear')
	print("\n\n                 REGISTRATION ::  \n\n")
	q="select max(Sn) from users"
	cur.execute(q)
	n=cur.fetchone()
	num=n[0] + 1
	Name = input("ENTER YOUR Name: ")
	UserId = Name +"_" + str(num)
	Password = input("ENTER A SECURE PASSWORD: ")
	Age = input("ENTER YOUR AGE: ")
	try:
		if int(Age)<=18 :
			raise myexp("INVALID AGE !!! ")
	except myexp as m:
		print(m.message)
		sys.exit()
	MobNo = input("ENTER YOUR MobNo: ")
	try:
		if len(MobNo)!=10 or MobNo.isdigit()==False:
			raise myexp("INVALID MobNo !!! ")
	except myexp as m:
		print(m.message)
		sys.exit()
	AdharNo = input("ENTER YOUR AdharNo: ")
	try:
		if len(AdharNo)!=12 or AdharNo.isdigit()==False:
			raise myexp("INVALID AdharNo !!! ")
	except myexp as m:
		print(m.message)
		sys.exit()
	q="insert into users values(%d,'%s','%s','%s','%s','%s','%s')"%(num,Name,UserId,Password,Age,MobNo,AdharNo)
	os.system('clear')
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tWELCOME ! ",Name,"\n\n\t\t\t\t\t\t\t\tGreetings Of the Day !!")
	print("\t\t\t\t\t\t\t\tYour USER ID is  ",UserId)
	print("\t\t\t\t\t\t\t\tAND  PASSWORD is",Password)
	print("\n\n\t\t\t\t\t\t\t\tKindly remember the Same for Future Use !!!\n\n")
	u=input()
	cur.execute(q)
	con.commit()

def delete_user():
	os.system('clear')
	UserId= input("ENTER  UserId: ")
	q="select * from users where UserId = '%s'"%(UserId)
	cur.execute(q)
	if(cur.rowcount>0):
		row= cur.fetchall()
		os.system('clear')
		print("\n\n\n\n\t\t\t\tUSER'S DETAILS:\n\n\n\n\n\n\n")
		t = PrettyTable(['Sn','Name','UserId','Password','Age','MobNo','AdharNo' ])
		for i in range(0,len(row)):
			x = row[i]
			t.add_row(x)
		t.align['Title'] = 'l'
		print(t)
		print("ARE U SURE YOU WANT TO DELETE THE ABOVE DATA ??? (Y/N)")
		c=input()
		if c=='y' or c=='Y':
			q="delete from users where UserId = '%s'"%(UserId)
			cur.execute(q)
			os.system('clear')
			print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tDELETED !!!")
			con.commit()
			c=input()
	else:
		os.system('clear')
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tWRONG UserId OR Password !!!!!!!!! ")
		u=input()

def update_me():
	os.system('clear')
	y=True
	UserId = input("ENTER YOUR UserId: ")
	Password=input("ENTER YOUR PASSWORD: ")
	q="select * from users where UserId = '%s'and Password = '%s'"%(UserId,Password)
	cur.execute(q)
	if(cur.rowcount>0):
		os.system('clear')
		while y!=False:
			print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tMENU ")
			print("\n\n\t\t\t\t\t\t\t\t1.UPDATE PASSWORD ")
			print("\t\t\t\t\t\t\t\t2.UPDATE AGE ")
			print("\t\t\t\t\t\t\t\t3.UPDATE MobNo ")
			print("\t\t\t\t\t\t\t\t4.UPDATE AdharNo ")
			print("\t\t\t\t\t\t\t\t5.EXIT ")
			print("\n\n\t\t\t\t\t\t\t\tENTER YOUR CHOICE:  ")
			c=input()
			if c=='1':
				os.system('clear')
				p=input("ENTER YOUR NEW PASSWORD: ")
				q="update users set Password = '%s' where UserId = '%s'"%(p,UserId)
				cur.execute(q)
				con.commit()
			if c=='2':
				os.system('clear')
				p=input("ENTER YOUR NEW AGE: ")
				try:
					if int(p)<=18 :
						raise myexp("INVALID AGE !!! ")
					else:
						q="update users set AGE = '%s' where UserId = '%s'"%(p,UserId)
						cur.execute(q)
						con.commit()
				except myexp as m:
					print(m.message)

			if c=='3':
				os.system('clear')
				p=input("ENTER YOUR NEW MobNo: ")
				try:
					if len(p)!=10 or p.isdigit()==False:
						raise myexp("INVALID MobNo !!! ")
					else:
						q="update users set MobNo= '%s' where UserId = '%s'"%(p,UserId)
						cur.execute(q)
						con.commit()
				except myexp as m:
					print(m.message)
					q="update users set MobNo= '%s' where UserId = '%s'"%(p,UserId)
			if c=='4':
				os.system('clear')
				p=input("ENTER YOUR NEW AdharNo: ")
				try:
					if len(p)!=12 or p.isdigit()==False:
						raise myexp("INVALID AdharNo !!! ")
					else:
						q="update users set AdharNo = '%s' where UserId = '%s'"%(p,UserId)
						cur.execute(q)
						con.commit()
				except myexp as m:
					print(m.message)
			if c=='5':
				y=False

def add_property():
	os.system('clear')
	
	q="select max(Sn) from vtable"
	cur.execute(q)
	n=cur.fetchone()
	num=n[0] + 10001
	print("     ENTER DETIALS OF YOUR PROPERTY: ")
	Property_id = 'HH' + str(num)
	Price = int(input("ENTER Price of your property excluding Tax: "))
	BHK= int(input("ENTER BHK: "))
	Sqft = int(input("ENTER Sqft: "))
	Property_Type= input("ENTER Property_Type: ")
	Exterior_Wall= input("ENTER Exterior_Wall: ")
	Location= input("ENTER Location: ")
	Status='ON'
	q="insert into property values(%d,%d,%d,'%s','%s','%s','%s','%s')"%(Price,BHK,Sqft,Property_Type,Exterior_Wall,Location,Property_id,Status)
	os.system('clear')
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tTHANKU FOR YOUR SUBMISSION !")
	u=input()
	cur.execute(q)
	con.commit()
