import mysql.connector
from datetime import datetime, timedelta
from time import sleep


def check_in():
    try:
        conf = mysql.connector.connect(user='root', password='mysql', database='OHBMS', host='localhost', port=3306)
        # if conf.is_connected():
        # print("Outer Server Connected")
    except:
        print("Outer Server Not Connected")
        print()

    conf = mysql.connector.connect(user='root', password='mysql', database='OHBMS', host='localhost', port=3306)
    myc = conf.cursor()
    sqlf = "INSERT INTO customer_details (Full_Name,Adhaar_No, " \
           "Contact_No, Address, Pincode) values (%s,%s,%s,%s,%s)"
    try:
        print("\n*** Please Enter Person and Days in Digits ***")
        person = int(input("Enter the total number of person: "))
        days = int(input("Enter the number of days you want to stay: "))
        print("*** Please Choose and Type One\n\t Executive\n\t Deluxe\n\t Simple\t\t:")
        r_type = input("Enter the type of room: ")
        if r_type == "Executive" or r_type == "Deluxe" or r_type == "Simple":
            pass
        else:
            check_in()

    except ValueError:
        check_in()

    def details():
        try:
            print("***Enter your Details***")
            full_name = input("Enter your Name: ")
            if full_name == '':
                print("*** Don't Leave Name Empty ***")
                details()

            aadhaar_no = int(input("Enter your Aadhaar number: "))
            aadhaar_n = str(aadhaar_no)
            if len(aadhaar_n) != 12:
                print("*** Aadhaar Number should have to be of 12 Digits ***")
                details()

            contact_no = int(input("Enter your Contact_no: "))
            contact_n = str(contact_no)
            if len(contact_n) != 10:
                print("*** Contact Number should have to be of 10 Digits ***")
                details()

            address = input("Enter your Address: ")
            if address == '':
                print("*** Don't Leave Address Empty ***")
                details()

            pincode = int(input("Enter your Pincode: "))
            pincod = str(pincode)
            if len(pincod) != 6:
                print("*** Pincode should have to be of 6 Digits ***")
                details()
            param = (full_name, aadhaar_no, contact_no, address, pincode)
            print(param)
            try:
                myc.execute(sqlf, param)
                conf.commit()
                rowid = myc.lastrowid
                # print(rowid)
                # print(type(rowid))
                print("Data Inserted Successfully.")
                # **************** Entering Time Stamp *******************
                cont = mysql.connector.connect(user='root', password='mysql', host='localhost',
                                               database='OHBMS', port=3306)
                myt = cont.cursor()

                def time_in():
                    n = 0
                    while n < days:

                        sqlt = 'insert into timestamp (C_ID,Date,Time,Total_Person, Days, Room_Type) ' \
                               'values (%s,%s,%s,%s,%s,%s)'
                        cdt = datetime.now() + timedelta(days=n)
                        f_cdt = cdt.strftime("%d %B %Y")
                        f_cdt2 = cdt.strftime("%I:%M:%S")
                        # print(cdt)

                        param_t = (rowid, f_cdt, f_cdt2, person, days, r_type)
                        # print(param_t)
                        try:
                            myt.execute(sqlt, param_t)
                            cont.commit()
                            print("Time Data Inserted Successfully.")
                        except:
                            print("Unable to Insert Time Data.")
                        n += 1

                time_in()
                # ********** Entering Time End *******************

                if person > 1:
                    def frd():
                        try:
                            for i in range(person - 1):
                                sql2 = "INSERT INTO customer_famorfrdet (C_ID,Name," \
                                    "Aadhaar_No, Address, Pincode) " \
                                    "values (%s,%s,%s,%s,%s)"
                                f_full_name = input("Enter Name: ")
                                f_aadhaar_no = int(input("Enter Adhaar number: "))
                                f_address = input("Enter Address: ")
                                f_pincode = int(input("Enter Pincode: "))
                                param_f = (rowid, f_full_name, f_aadhaar_no,
                                           f_address, f_pincode)
                                # print(param_f)
                                try:
                                    myc.execute(sql2, param_f)
                                    conf.commit()
                                    # print("Multiple Data Inserted Successfully.")
                                except:
                                    # con.rollback()
                                    # print("Unable to Insert Multiple Data")
                                    conf.close()
                                    if conf.is_closed():
                                        print("Conf Disconnected Successfully.")
                        except ValueError:
                            print("*** Aadhaar Number and Pincode should be in Digits ***")
                            frd()
                    frd()
                else:
                    print()

                # ******************* Payment *************************
                conp = mysql.connector.connect(user="root", password="mysql", host="localhost", database="ohbms",
                                               port=3306)
                myp = conp.cursor()
                sqlp = 'INSERT INTO payment (C_ID, Total_person, Room_Type, Days, Total_Amount, Paid) ' \
                       'values (%s,%s,%s,%s,%s,%s)'
                # r_type = input("ROom type: ")
                # person = int(input("person: "))
                # days = int(input("Days: "))
                # rowid = int(input("row_id"))
                # paid = input("Paid?")
                if r_type == "Executive":
                    room_rent = 5000
                elif r_type == "Deluxe":
                    room_rent = 3000
                else:
                    room_rent = 1500
                amount = person * days * room_rent

                def try_ag():

                    def ped():
                        paid = input("If payment is done, Press (Y). If not, Press any key.")
                        if paid == "y" or paid == 'Y':
                            paramp = (rowid, person, r_type, days, amount, paid)
                            # print(paramp)
                            try:
                                myp.execute(sqlp, paramp)
                                conp.commit()
                                print("Payment Details Inserted Successfully")
                                print(f"Congratulations!!! You have allocated {r_type} room. ")
                                print(f"Your Unique ID Number is {rowid}.")
                                print("*** Please Don't Forget your Unique ID ***")

                            except:
                                print("Payment Details Insertion Unsuccessful")
                            # print(paramp)

                        else:
                            try_ag()
                    # ********** Payment deletion starts here *************

                    def deleting():
                        cond = mysql.connector.connect(user='root', password='mysql', host='localhost',
                                                       database='ohbms', port=3306)
                        sqld1 = 'delete from customer_details where customer_id = (%s)'
                        sqld2 = 'delete from timestamp where C_ID = (%s)'
                        sqld3 = 'delete from customer_famorfrdet where C_ID = (%s)'
                        mydel = cond.cursor()
                        param_del = (rowid,)
                        try:
                            mydel.execute(sqld1, param_del)
                            cond.commit()
                            mydel.execute(sqld2, param_del)
                            cond.commit()
                            mydel.execute(sqld3, param_del)
                            cond.commit()
                            # print("Data Deleted Successfully")
                        except:
                            print("Data Didn't Deleted Successfully")

                    def chec():

                        pay = input("Do you want to do the payment? Press( Y (for yes) and N (for no) )")
                        if pay == "y" or pay == "Y":
                            ped()
                        else:
                            print("Thankyou")
                            deleting()
                    chec()

                try_ag()
                # ************* Payment Ends Here ***************

            except:
                # con.rollback()
                print("Unable to Insert Single Data")
                conf.close()
                if conf.is_closed():
                    print("Conf Disconnected Successfully.")
        except:
            print("Please Enter Aadhaar_No, Contact_No and Pincode in digits.")
            sleep(2)
            details()

    def ava():
        n = 0
        lst = []
        while n < days:
            dat = datetime.now() + timedelta(days=n)
            datf = dat.strftime("%d %B %Y")
            print(datf)

            cona = mysql.connector.connect(user='root', password='mysql', database='ohbms', host='localhost', port=3306)
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
                    break
                else:
                    print(f"{r_type} room is available on {datf}")
                    lst.append(datf)
            except:
                print("Something is wrong in availability")
            n += 1
            cona.close()
            if cona.is_closed():
                # print("Inner Server Closed.")
                print()
            if len(lst) == days:
                print("rooms available")
                details()

    ava()
    conf.close()
    if conf.is_closed():
        # print("Outer Server Closed")
        print()



