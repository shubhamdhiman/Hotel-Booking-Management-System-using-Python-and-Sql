import mysql.connector
from time import sleep
import Rooms_and_Facilities
import Availability
import Check_In
import Check_Out
import UID_Check
# from datetime import datetime
try:
    con = mysql.connector.connect(user='root', password='mysql', host='localhost', database='ohbms', port=3306)
    if con.is_connected():
        # print("Connected Successfully.")
        print()

except:
    print("Unable to Connect.")

con = mysql.connector.connect(user='root', password='mysql', host='localhost', database='ohbms', port=3306)


def anonymous_hotel():
    def menu():
        print("!!! Hello !!!\n!!! Welcome to ANONYMOUS HOTEL !!! ")
        print("!! How May I Help YOU? !!")
        print("!! *** For Rooms & Facilities ***  Press (1) !!")
        print("!! *** For Availability Check ***  Press (2) !!")
        print("!! *** For Check In ***  Press (3) !!")
        print("!! *** For Check Out ***  Press (4) !!")
        print("!! *** For UID Check *** Press (5) !! ")
        cust_input = int(input("Enter Number :"))

        if cust_input == 1:
            Rooms_and_Facilities.rooms()
            sleep(10)
            men_u()

        elif cust_input == 2:
            Availability.ava()
            sleep(3)
            men_u()

        elif cust_input == 3:
            Check_In.check_in()
            men_u()
        elif cust_input == 4:
            Check_Out.check_out()
            men_u()
        elif cust_input == 5:
            UID_Check.ud()
            men_u()
        else:
            print("!!!Thankyou!!!")

    def men_u():
        men_u = input("Do you want to check the menu? If Yes, Press (Y). Else press any key.")
        if men_u == "Y" or men_u == "y":
            menu()
        else:
            print("Thankyou")
    men_u()


anonymous_hotel()


con.close()
