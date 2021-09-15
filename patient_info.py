# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:33:03 2021

@author: karth
"""

# Create class "Patient"   
class Patient:
	# Constructor
	def __init__(self, name, bloodgrp, address, branch):
		self.name = name
		self.bloodgrp = bloodgrp
		self.address = address
		self.branch = branch
		
	# Function to create and append new Patient
	def accept(self, Name, bloodgrp, address, branch ):
		# use ' int(input()) ' method to take input from user
		ob = Patient(Name, bloodgrp, address, branch )
		ls.append(ob)

	# Function to display Patient details	
	def display(self, ob):
			print("Name : ", ob.name)
			print("bloodgrp : ", ob.bloodgrp)
			print("address : ", ob.address)
			print("branch : ", ob.branch)
			print("\n")	
		
	# Search Function	
	def search(self, bloodgrp):
		for i in range(ls.__len__()):
			if(ls[i].bloodgrp == bloodgrp):
				return i	

	# Delete Function								
	def delete(self, bloodgrp):
		i = obj.search(bloodgrp)
		del ls[i]

	
		
# Create a list to add Patients   
ls =[]
# an object of Patient class
obj = Patient('D', "A_n", "147_2_2", "XYZ")

print("\nOperations used, ")
print("\n1.Accept Patient details\n2.Display Patient Details\n" "3.Search Details of a Patient\n4.Delete Details of Patient"  "\n6.Exit")

# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept("A", "A_p", "159_f", "XYZ_A")
obj.accept("B", "O_p", "189_1_4", "XYZ_B")
obj.accept("C", "AB_n", "145_8", "XYZ_C")
		
# elif(ch == 2):
print("\n")
print("\nList of Patients\n")
for i in range(ls.__len__()):	
	obj.display(ls[i])
			
# elif(ch == 3):
print("\n Patient Found, ")
s = obj.search("A_p")
obj.display(ls[s])
		
# elif(ch == 4):
obj.delete("AB_n")
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):	
	obj.display(ls[i])
			

			
# else:
print("Thank You !")
	
