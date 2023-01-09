print("Welcome to Mario's Pizzaria!!\n")


def display_main_menu(): 
    user_selection()


def display_pizza_menu():
    print ("")
    for i in menuItems:
        table = dict.fromkeys(map(ord, ")(',"), None)
        i.name = str(i.name).translate(table)
        print(i.name)
        print(i.description)
        print("")
def user_order_menu():
  print("")
  for i in menuItems:
        table = dict.fromkeys(map(ord, ")(',"), None)
        i.name = str(i.name).translate(table)
        print(i.name)
        print(i.description)
        print("")

def reservation():
  print("\n++Reservation++\n")
  print("To make a reservation please enter a date less than a week in advance and between the times 8am - 11pm (We are closed on sundays). You cannot make more than one reservation. Any previous reservation will be erased when making a new one.")
  reservation_date = input("\nWhat date would you like to set for your reservation? (mm/dd/yyyy format or month day year format)\n")
  reservation_time = input("\nWhat time would you like to set for your reservation?(tt:tt am/pm \n")

  number_of_reservations =+ 1

  if number_of_reservations <= 1:
   print(f"\nYour reservation is now set for {reservation_date} at {reservation_time}.\n")
def end_screen():
  print("\nThank you for ordering from Mario's pizzaria")
def user_selection():
  
  user_interaction = True
  while user_interaction == True:
    print("\n ** Mario's Pizzaria **")
    print('')
    print("1. View Menu")
    print("2. Place An Order ")
    print("3. Make A Reservation")
    print("4. Exit")
    user_choice = int(
    input("\nPlease enter 1, 2, 3, or 4 to make a selection.\n"))
    if user_choice == 1:
        print("\n~~Pizza Menu~~")
        display_pizza_menu()  #print('show inventory')
    elif user_choice == 2:  #Initiate New Product Process.
        small_pizza = 0
        medium_pizza = 0
        large_pizza = 0
        user_order_menu()
        print("Pizza's come in small($10) medium($15) and large($20) sizes.")
        ordering = True
        while ordering == True:
          
          pizza_order = int(
            input('\nWhich pizza do you want? (Enter the number).\n'))
          pizza_size = input('\nWhat size pizza do want? (Enter s(small) or m(medium) or l(large)).\n')
          if pizza_size == "s":
            small_pizza =+ 1
          elif pizza_size == "m":
            medium_pizza =+ 1
          elif pizza_size == "l":
            large_pizza =+ 1
          else:
            pizza_size = input('Enter a valid pizza size.')
          if input('\nWill that be all?(yes or no)\n') == "yes":
            ordering = False
          else:
            ordering = True
        charity_donation = input("\nWould you like to donate a dollar to a charitable cause? (yes or no)\n")
        if charity_donation == "yes":
            print("\nThank you for your donation!")
            charity = 1
        else:
            print("\nOkay. :(")
            charity = 0
        total = small_pizza*10 + medium_pizza*15 + large_pizza*20 + charity
        total_with_tax = total*1.0625
        print(f"\nYour total is {total} before tax")
        print(f"\nYour total after tax is {total_with_tax}")
        print("\nThank you for ordering Mario's Pizza. \nEnjoy.")
    elif user_choice == 3:  #Initiate Buying a New Product.
        reservation()
    elif user_choice == 4:  #placeholder
        end_screen()
        user_interaction = False
    else:
        print("\nSorry, Not a Valid Choice. Please try again!")


class menuItem:
    def __init__(self, name, specialData, description):
        self.name = name,
        self.specialData = specialData,
        self.description = description


menuItems = [
    menuItem('1. Hawaiian', False,
             'Pineapple & ham on mozzarella & tomato sauce.'),
    menuItem(
        '2. Champagne Ham & Cheese', False,
        'Ham & two-cheese blend on mozzarella & tomato sauce, sprinkled with assorted greens.'
    ),
    menuItem('3. Beef & Onion', False,
             'Ground beef & caramelized onions on mozzarella & tomato sauce.'),
    menuItem('4. Pepperoni', False, 'Simple pepperoni & mozzarella pizza with mozzarella & tomato sauce.'),
    menuItem('5. Simply Cheese', False, 'Two-cheese blend on tomato sauce.'),
    menuItem('6. Bacon & Mushroom', False, 'Bacon & mushrooms with white cheddar cheese & tomato sauce.'),
    menuItem('7. Italiano', False, 'A traditional Italian pizza with fresh basil leaves & white Mozarella di Bufala cheese & tomato sauce.'),
    menuItem('8. The Deluxe', False, 'Mozzarella cheese, dry cured pepperoni, crumbled Italian sausage, green& red peppers with diced onions & tomato sauce.'),
    menuItem('9. Ham, Egg & Hollandaise', False, 'Sunny side up eggs with ham & Hollandaise sauce.'),
    menuItem('10. Americano', False, 'Pepperoni and mushrooms & tomato sauce.'),
    menuItem('11. Mr Wedge', False, 'Five cheese blend & tomato sauce.'),
    menuItem('12. BBQ Meatlovers', False, 'Brisket and rib meat with cheese & barbecue sauce.'),
    menuItem('13. Buffalo Chicken', True, 'Buffalo chicken peices with pepper jack cheese & buffalo sauce.'),
    menuItem('14. Steak & Blue Cheese', True, 'Steak with Blue Cheese & tomato sauce.'),
    menuItem('15. Shrimp & Crab', True, 'Shrimp & crab with cheese & tomato sauce.'),
    menuItem('16. Lebanese', True, "Olive oil, za'atar, pickles, green peppers, pepperoni with cheese & tomato sauce."),
    menuItem('17. Chinese Pizza', True, 'Onions, pea pods, water chestnuts, teriyaki chicken, ginger & thickened soy sauce.'),
]

display_main_menu()
