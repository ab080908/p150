#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:19:31 2024

@author: GB
"""

from tkinter import *
import random
root=Tk()
root.title("Luck Friend Wheel")
root.geometry("700x800")
enter_name= Entry(root)
enter_name.place(relx= 0.5, rely=0.2,anchor=CENTER)
friend_list= Label(root)
random_number_label= Label(root)
lucky_friend= Label(root)
list1=[]
def addcountry():
    friend_name= enter_name.get()
    list1.append(friend_name)
    friend_list["text"]= "Your country list : "+str(list1)
def random_number():   
    length= len(list1)
    random_no= random.randint(0,length-1)
    random_number_label["text"]= str(random_no)
    generated_random_number= list1[random_no]
    lucky_friend["text"]= "your random country is: "+ str(generated_random_number)
btn= Button(root, text="Add to the country list", command= addcountry)
btn.place(relx=0.5,rely=0.3, anchor= CENTER)
friend_list.place(relx=0.5,rely=0.4, anchor= CENTER)
btn1= Button(root, text= "What is your random country? ", command=random_number)
btn1.place(relx= 0.5, rely=0.5, anchor= CENTER)
random_number_label.place(relx=0.5 ,rely=0.6, anchor= CENTER)
lucky_friend.place(relx= 0.5, rely= 0.7, anchor= CENTER)

enter_name_capital= Entry(root)
enter_name_capital.place(relx= 0.5, rely=0.75,anchor=CENTER)
friend_list_c= Label(root)
random_number_label_c= Label(root)
lucky_friend_c= Label(root)
list2=[]
def addcapital():
    friend_name_c= enter_name_capital.get()
    list2.append(friend_name)
    friend_list_c["text"]= "Your capital list : "+str(list2)
def random_number_c():   
    length= len(list2)
    random_no_c= random.randint(0,length-1)
    random_number_label_c["text"]= str(random_no_c)
    generated_random_number_c= list2[random_no_c]
    lucky_friend_c["text"]= "your random capital is: "+ str(generated_random_number_c)
btn_c= Button(root, text="Add to the capital list", command= addcapital)
btn_c.place(relx=0.5,rely=0.8, anchor= CENTER)
friend_list_c.place(relx=0.5,rely=0.85, anchor= CENTER)
btn2= Button(root, text= "What is your random capital? ", command=random_number_c)
btn2.place(relx= 0.5, rely=0.9, anchor= CENTER)
random_number_label_c.place(relx=0.5 ,rely=0.95, anchor= CENTER)
lucky_friend_c.place(relx= 0.5, rely= 0.99, anchor= CENTER)
root.mainloop()
