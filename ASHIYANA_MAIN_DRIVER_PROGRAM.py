import os
import module1 as mm
x=True
os.system('clear')
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(mm.first.__doc__)
l=input()
while(x != False):
	os.system('clear')
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tMENU\n\t\t\t\t\t\t\t\t1.ABOUT US \n\t\t\t\t\t\t\t\t2.LOGIN/REGISTER \n\t\t\t\t\t\t\t\t3.FEEDBACK \n\t\t\t\t\t\t\t\t4.FAQ \n\t\t\t\t\t\t\t\t5.VIEW REVIEWS \n\t\t\t\t\t\t\t\t6.EXIT")
	c= input("ENTER YOUR CHOICE: ")
	if c=='1':
		os.system('clear')
		fo=open("About_us.txt","r")
		ch=fo.read()
		print(ch)
		fo.close()
		input()
	elif c=='2':
		y=True
		while(y!=False):
			os.system('clear')
			print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tMENU\n\t\t\t\t\t\t\t\t1.ADMIN\n\t\t\t\t\t\t\t\t2.USER\n\t\t\t\t\t\t\t\t3.EXIT")
			c=input("ENTER YOUR CHOICE: ")
			if c=='1':
				if mm.check_admin():
					x=True
					while x!=False:
						os.system('clear')
						print(mm.Admin_menu.__doc__)
						t=input()
						if t=='1':
							mm.display_all_users()
						elif t=='2':
							mm.display_me()
						elif t=='3':
							mm.delete_user()
						elif t=='4':
							mm.buy_property()
						elif t=='5':
							mm.add_property()                                        
						elif t=='6':
							mm.appointment_table()
						elif t=='7':
							mm.verification_table()
						elif t=='8':
							mm.psold_table()
						elif t=='9':
							x=False
						else:
							print("ENTER VALID CHOICE!!! ")
				else:
					print("CHECK NAME AND PASSWORD !!!!!")

			elif c=='2':
				y1 = True
				while(y1 != False):
					os.system('clear')
					print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t",mm.user_menu.__doc__)                                    
					c=input("ENTER YOUR CHOICE: ")
					if c=='1':
						mm.new_user_insert()
						os.system('clear')
						print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t",mm.new_user_menu.__doc__)  
						ch=input()                          
						if ch=='1':
							os.system('clear')
							mm.buy_property()
						if ch=='2':
							mm.sell_property()
						else:
							print("ENTER CORRECT CHOICE !!!!! ")
					elif c=='2':
						m1=True
						while m1!=False:
							os.system('clear')
							print(mm.c_user_menu.__doc__)
							ch=input()
							if ch=='1':
								mm.display_me()
							if ch=='2':
								mm.update_me()
							if ch=='3':
								mm.buy_property()
							if ch=='4':
								mm.set_appointment()                         
							if ch=='5':
								mm.sell_property()
							if ch=='6':
								m1=False


					elif c=='3':
						y1 = False
					else:
						print("ENTER CORRECT CHOICE !! ")

			elif c=='3':
				y=False
			else:
				print("ENTER CORRECT CHOICE !!!!")

	elif c=='3':
		mm.give_review()
	elif c=='4':
		os.system('clear')
		fo=open("FAQ_ASHIYANA.TXT","r")
		ch=fo.read()
		print(ch)
		fo.close()
		input()                
	elif c=='5':
		mm.dis_review()
	elif c=='6':
		x=False
	else:
		print("ENTER CORRECT CHOICE !!!!!!")


