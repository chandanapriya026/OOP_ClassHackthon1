# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 19:22:36 2021

@author: karth
"""

class Bloodbank:
  def init(self,name):
    self.hospitalname=name
  def donars(self):
    donar=["ravi AB-","raju A-","krishna O","swetha O-","akhil AB+"]
    for i in range(len(donar)) :
      print(donar[i])
  def availablebloodgroups(self):
    dngroups=["AB-","A-","O","O-","AB+"]
    for i in range(len(dngroups)):
      print(dngroups[i])

  def notifications(self):
    receivers=["ramu","bharghav","charan","nithin"]
    bdgroups=["AB-","O-","AB+","A-"]
    print("these are the blood requests ")
    for i in range(len(receivers)):
      print("{} wants {} blood ".format(receivers[i],bdgroups[i]))
hsp=Bloodbank()
bloodgroups=["A","A-","B","B-","O","O-","AB","AB-"]
print("Welcome to blood bank !")
print("Are you an admin or user? ")
x=input()
if x=='admin':
  print("enter your username :")
  y=input()
  print("succefully logged in as admin")
  print("enter the name of hospital having blood bank")
  hsp.hospitalname=input()
  k="enter when will be blood donation camp conducts in {} hospital"
  print(k.format(hsp.hospitalname))
  donationcamp=input()
  hsp=Bloodbank()
  print("these are the details of donars")
  hsp.donars()
  print("Notifications !")
  hsp.notifications()



if x=='user':
  print("Are you a donor or receiver?")
  z=input()
  if z=='donor':
    print("you got a notification !")
    print("emergency blood neded would you like to donate....accept/ignore ")
    w=input()
    if w=="accept":
      print("enter which bloodgroup do you want to donate")
      d=input()
      print("thanks for donating blood !")
    else :
      print("Exiting....")
    
    if d not in bloodgroups:
      print("you have entered wrong blood group ! please enter again ")

    
  if z=='receiver':
    print("these are the blood groups present now in our blood bank")
    hsp.availablebloodgroups()
    print("enter the blood group you want :")
    r=str(input())
    dngroups=["A-","O","O-","AB+","AB-"]
    if r in dngroups :
      print("your requested blood gruop is available ")
      print("sending notification....")
    else :
      print("your requested blood group is not available ")