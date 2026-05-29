from expenses import *
import sqlite3
def get_int(integer):
    while True:
        try :
            return int(input(integer))
            
        except:
            print("please input a Integer Only")
            continue
choice=get_int("\nplease enter your choice \n1. Add expense \n2. View Expense\n3. Category\n4. total spent\n5. Exit\nchoice : ")

while True:
    if choice == 1:
        pass
    elif choice==2:
        pass
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        print("Thank you for using the program")
        break
