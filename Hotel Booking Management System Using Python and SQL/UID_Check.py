import mysql.connector


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
        myu.execute(sqlu, paramu)
        row = myu.fetchone()
        uid = row[0]
        print(f"Your Unique Id Number is {row[0]}")
        conu.close()
        if conu.is_closed():
            # print("Conu Closed")
            print()


    except:
        conu.close()
        if conu.is_closed():
            # print("Conu Close")
            print()
        print("Unable to find UID")

