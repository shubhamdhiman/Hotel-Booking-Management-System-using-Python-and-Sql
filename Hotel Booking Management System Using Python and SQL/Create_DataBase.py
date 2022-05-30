import mysql.connector as msc
con = msc.connect(user='root', password='mysql', host='localhost')

# Creating Cursor class object so that we can call execute() mehtod.
co = con.cursor()
# Checking whether the connection with the server established or not.
if con.is_connected():
    # print("Server Connected")
    print()

# First sql command to create a database
sql1 = 'CREATE DATABASE OHBMS'
co.execute(sql1)        # Executing sql query using the con() class object.
print("Data base created")

# Using the database
sql2 = 'USE OHBMS'
co.execute(sql2)
print('Using database')

# This sql3 will be our Parent Table as we will use Foreign Key in rest of the tables.
sql3 = 'CREATE TABLE customer_details (Customer_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ' \
       'Full_Name VARCHAR (30) NOT NULL, Adhaar_No bigint NOT NULL, Contact_No bigint NOT NULL, ' \
        'Address VARCHAR (100), Pincode int NOT NULL)'
co.execute(sql3)
print("Customer_details table created")

# Creating table to store customer's friends or family details
sql4 = 'CREATE TABLE customer_famorfrdet (U_ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,' \
        'C_ID int NOT NULL,' \
        'Name VARCHAR (30) NOT NULL,' \
        'Aadhaar_No bigint NOT NULL,' \
        'Address VARCHAR (50),' \
        'Pincode int NOT NULL,' \
        'FOREIGN KEY (C_ID) REFERENCES customer_details (Customer_ID)' \
        'ON DELETE CASCADE)'
co.execute(sql4)
print("Customer_famorfrdet table created")

# Creating table for payment details
sql5 = 'CREATE TABLE Payment (U_ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,' \
       'C_ID int NOT NULL,' \
       'Total_Person int NOT NULL,' \
       'Room_Type VARCHAR (20) NOT NULL,' \
       'Days int NOT NULL,' \
       'Total_Amount int NOT NULL,' \
       'Paid VARCHAR (20),' \
       'FOREIGN KEY (C_ID) REFERENCES customer_details (Customer_ID)' \
       'ON DELETE CASCADE) '
co.execute(sql5)
print("payment table created")

# Creating table to record the timings.
sql6 = 'CREATE TABLE timestamp (U_ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,' \
       'C_ID int NOT NULL,' \
       'date VARCHAR (20),' \
       'time VARCHAR (20),' \
       'Total_Person int NOT NULL,' \
       'Days int NOT NULL,' \
       'Room_Type VARCHAR (30) NOT NULL,' \
       'FOREIGN KEY (C_ID) REFERENCES customer_details(customer_id)' \
       'ON DELETE CASCADE) '
co.execute(sql6)
print("timestamp table created")

# Here not using ON CASCADE DELETE as not required to delete the records of customer.
# Creating table to store check_out details.
sql7 = 'CREATE TABLE check_out (U_ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,' \
       'C_ID int NOT NULL,' \
       'Aadhaar_No bigint NOT NULL,' \
       'Check_Out_time VARCHAR (20) NOT NULL,' \
       'FOREIGN KEY (C_ID) REFERENCES customer_details (customer_ID))'
co.execute(sql7)
print('check_out table created')

# Here not using foreign key as not required while checking the availability of rooms.
# Creating table to check availability.
sql8 = 'CREATE TABLE availability (Date VARCHAR (20) NOT NULL PRIMARY KEY,' \
       'Room_Type VARCHAR (20),' \
       'id int)  '
print("availability table created")
co.execute(sql8)

# Using commit() method, to save the changes. ( In our case, changes are the tables we are creating )
con.commit()

# Closing the server
con.close()

