#from IPython.display import clear_output
# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
current_cart = []


def shopping_cart():
    print("Welcome to Yasir's Shopping Program.")

    while True:
        x = input(
            "Yasir's Shopping Program Main Menu\nOptions:\n[1] Show Current Cart\n[2] Add Item To Cart\n[3] Remove Item From Cart\n[4] Quit\nChoose An Option By Simply Typing The Number Below.\n")
        # clear_output()
        if x == '1':
            if current_cart == []:
                print('Your Shopping Cart Is Empty.\nChoose Another Option.')
            else:
                print(f'This Is Your Current Cart.\n{current_cart}')
        elif x == '2':
            while True:
                if current_cart == []:
                    print('Your Shopping Cart Is Empty.')
                else:
                    print(f'This Is Your Current Cart.\n{current_cart}')
                z = input('What Would You Like To Add To Your Cart?\n').title()
                if z == "":
                    print(f'Invalid Input, Please Try Again.')
                elif z in current_cart:
                    print(
                        f'"{z}" Is Already In Your Cart.\nChoose Another Item Or Type "Return" To Return To The Main Menu.')
                elif z == "Return":
                    break
                else:
                    current_cart.append(z)
                    break
                # clear_output()
        elif x == '3':
            while True:
                if current_cart == []:
                    print(
                        'Your Shopping Cart Is Empty.')
                else:
                    print(f'This Is Your Current Cart.\n{current_cart}')
                y = input(
                    'What Would You Like To Remove? \nIf Here By Mistake Type "Return" To Return To The Main Menu.\n').title()
                if y in current_cart:
                    current_cart.remove(y)
                    print(f'{y} Has Been Removed From Your Cart')
                    break
                elif y == 'Return':
                    break
                elif y == '':
                    print(f'Invalid Input, Please Try Again.')
                else:
                    print(
                        'Sorry, That Item Is Not In Your Cart.\nChoose An Item In Your Cart To Remove.')

        elif x == '4':
            return ('Have  a nice day, see you next time.')
        else:
            print('Invalid Input, Please Try Again.')


shopping_cart()
