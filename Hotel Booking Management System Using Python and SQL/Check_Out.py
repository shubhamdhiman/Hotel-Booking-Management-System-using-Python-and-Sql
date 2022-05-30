import mysql.connector
# from time import sleep
from datetime import datetime


def check_out():
    try:
        con = mysql.connector.connect(user='root', password="mysql", database='OHBMS', host='localhost', port=3306)
        if con.is_connected():
            # print("Con connected")
            print()
    except:
        print("Unable to Connect")

    con = mysql.connector.connect(user='root', password='mysql', database='OHBMS', host='localhost', port=3306)
    myc = con.cursor()
    sql = "select * from customer_details where customer_id = (%s)"
    # person = int(input("Enter total number of person:"))
    dat = datetime.now()
    datf = dat.strftime("%d %B %Y")

    # def u_id():
    # print()

    def details():
        def det():
            try:
                aadhaar_no = int(input(" Enter your Aadhar Number: "))
                aadhaar = str(aadhaar_no)
                if len(aadhaar) != 12:
                    print("*** Aadhaar Number should have to be of 12 Digits ***")
                    det()
                customer_id = int(input("Enter you Unique ID Number:"))
                if type(customer_id) != int:
                    print("*** Unique ID Number should have to be in Digits ***")
                    det()
                param = (customer_id,)
                # print(param)
                try:
                    myc.execute(sql, param)
                    row = myc.fetchone()
                    # print(row)
                    if row[0] == customer_id and row[2] == aadhaar_no:
                        conco = mysql.connector.connect(user='root', password='mysql', database='OHBMS',
                                                        host='localhost', port=3306)
                        if conco.is_connected():
                            # print("Conco Connected")
                            print()
                        sqlco = 'INSERT INTO check_out (c_id, aadhaar_no, check_out_time) value (%s,%s,%s)'
                        myco = conco.cursor()
                        paramco = (customer_id, aadhaar_no, datf)
                        try:
                            myco.execute(sqlco, paramco)
                            conco.commit()
                            conco.close()
                            # print("Check Out Data Inserted Successful")
                            if conco.is_closed():
                                # print("Conco closed")
                                print()
                            con.close()
                            if con.is_closed():
                                # print("Con closed")
                                print()
                            print("!!!Thankyou for Visiting!!!\n!!!Please Visit Again!!!")
                        except:
                            print("Check Out Data Not Inserted")
                            conco.close()
                            if conco.is_closed():
                                # print("conco close")
                                print()
                            det()
                    else:
                        print("*** Please Enter Correct ID and Aadhaar Number ***")
                        con.close()
                        if con.is_closed():
                            # print("Con Closed")
                            print()
                        val()

                except:
                    print("*** Please Enter Aadhaar and Unique ID in Digits ***")
                    print("Data Didn't Retrieved")
                    con.close()
                    if con.is_closed():
                        # print("con close")
                        print()
                    val()
            except:
                print("*** Aadhaar Number and UID should have to be in Digits ***")
                det()

        def val():
            try:
                tak = int(input("To check U_ID, Press (1)\nTo Check_Out, Press (2)\nOtherwise, Press (3): "))
                if tak == 1:
                    def ud():
                        conu = mysql.connector.connect(user='root', password="mysql", database='OHBMS',
                                                       host='localhost', port=3306)
                        if conu.is_connected():
                            # print("Conu Connected")
                            print()

                        myu = conu.cursor()
                        a_no = int(input("Enter your aadhaar number: "))
                        ad_no = str(a_no)
                        if len(ad_no) != 12:
                            print("Aadhaar Number should have to be of 12 Digits")
                            ud()
                        sqlu = 'select * from customer_details where adhaar_no = (%s)'
                        paramu = (a_no,)
                        try:
                            myc.execute(sqlu, paramu)
                            row = myc.fetchone()
                            uid = row[0]
                            print(f"Your Unique Id Number is {row[0]}")
                            conu.close()
                            if conu.is_closed():
                                # print("Conu Closed")
                                print()
                            con.close()
                            if con.is_closed():
                                # print("Con closed")
                                print()
                            val()
                        except:
                            conu.close()
                            if conu.is_closed():
                                # print("Conu Close")
                                print()
                            print("Unable to find UID")
                            val()
                    ud()
                elif tak == 2:
                    det()
                elif tak == 3:
                    print("Thankyou")
                else:
                    print("*** Please Choose (1) or (2) or (3) ***")
                    val()
            except ValueError:
                print("***Please Choose (1) or (2) or (3) ***")
                val()
        val()

    details()
