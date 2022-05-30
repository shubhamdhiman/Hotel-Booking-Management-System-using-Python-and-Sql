import mysql.connector
from datetime import datetime, timedelta


def ava():
    def ava_a():
        try:
            days = int(input("Enter the Number of Days: "))
            r_type = input("Enter Room Type: ")
            if r_type == 'Executive' or r_type == 'Deluxe' or r_type == 'Simple':
                n = 0
                lst = []
                while n < days:
                    dat = datetime.now() + timedelta(days=n)
                    datf = dat.strftime("%d %B %Y")
                    # print(datf)

                    cona = mysql.connector.connect(user='root', password='mysql', database='ohbms',
                                                   host='localhost', port=3306)
                    if cona.is_connected():
                        # print("Inner Server Connected")
                        print()

                    sqla = "Select date, Room_type from timestamp where date=(%s)"
                    mya = cona.cursor()
                    param_a = (datf,)
                    # print(param_a)
                    try:
                        mya.execute(sqla, param_a)
                        row = mya.fetchone()
                        # print(row)
                        # print(type(row))
                        if isinstance(row, type(None)):
                            row = (0, 0)
                        if row[0] == datf and row[1] == r_type:
                            print(f"Sorry, {r_type} room is not available on {datf}")
                            cona.close()
                            if cona.is_closed():
                                # print("Inner Server Closed")
                                print()
                            break
                        else:
                            print(f"{r_type} room is available on {datf}")
                            lst.append(datf)

                    except:
                        # print("Something is wrong in availability")
                        print()
                    n += 1
                    cona.close()
                    if cona.is_closed():
                        # print("Inner Server Closed.")
                        print()
                    if len(lst) == days:
                        print("Rooms available")
            else:
                # print("*** Please Choose (Executive or Deluxe or Simple Room) ***")
                ava_a()
        except ValueError:
            # print("*** Please Enter Days in Digits ***")
            ava_a()

    def enter():

        take_i = input("Do you want to check availability? Press (Y) for Yes and (N) for No :")
        if take_i == "Y" or take_i == 'y' or take_i == 'n' or take_i == 'N':
            if take_i == "Y" or take_i == 'y':
                ava_a()
            else:
                print("Thankyou")
        else:
            enter()
    enter()
