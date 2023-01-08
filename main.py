import random
import datetime
import time
from datetime import date


class menuItem:
	def __init__(self,name,specialData,description):
		self.name = name,
		self.specialData = specialData,
		self.description = description


menuItems = [
	menuItem('Hawaiian',False,'example'),
  menuItem('Champagne Ham & Cheese',False,'example'),
  menuItem('Beef & Onion',False,'example'),
  menuItem('Pepperoni',False,'example'),
  menuItem('Simply Cheese',False,'example'),
  menuItem('Bacon & Mushroom',False,'example'),
  menuItem('Italiano',False,'example'),
  menuItem('The Deluxe',False,'example'),
  menuItem('Ham, Egg & Hollandaise',False,'example'),
  menuItem('Americano',False,'example'),
  menuItem('Mr Wedge',False,'example'),
  menuItem('BBQ Meatlovers',False,'example'),
	menuItem('Buffalo Chicken',True,'example'),
  menuItem('Steak & Blue Cheese',True,'example'),
  menuItem('Shrimp & Crab',True,'example'),
  menuItem('Lebanese',True,'example'),
  menuItem('Chinese Pizza',True,'example'),
  
]

for i in menuItems:
	print(i.name)
	print(i.specialData)  
	print(i.description)

def display_main_menu():
  print("\n **Mario's Pizzaria**")  
  print("1. View Menu") 
  print("2. Place An Order ")  
  print("3. Make A Reservation") 
        

def user_selection():
  
    #global isUsed
    user_choice = int(input("Please 1,2, or 3 to make a selection"))
    if user_choice == 1:  #Go to Store Inventory.
        display_pizza_menu() #print('show inventory')
    elif user_choice == 2:  #Initiate New Product Process.
        print('add a new product')
    elif user_choice == 3:  #Initiate Buying a New Product.
        print("buying a product")
    elif user_choice == 4:  #Initiate Removing a Product.
         print('remove a product')
    elif user_choice == 5:  #Exit the program
        print("Thank you for using the program!"
         )  # adds thank you message before exiting the program
        isUsed = False  #print("program ends.")  # changes the value of isUsed to False
    else:
        print("\nSorry, Not a Valid Choice. Please try again!") 