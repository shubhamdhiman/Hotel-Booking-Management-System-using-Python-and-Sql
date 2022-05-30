Created a project using Python and Mysql. 

Description:

	1. The project name is Offline Hotel Booking Management System.
	2. Here, a customer can check the availability of the room in the hotel based on the Room Type(3 Room Types).
	   The availability will be checked through the database which we will create.
	3. Customers can check the room type and facilities inside the hotel.
	4. Customers can enter their details if the room is available and will have to add the details of all the members with him/her.
	   All the details will get stored in the database.
	5. If the payment is not done, all the data in the database will get removed from the database automatically.
	   If the payment is done then all the details of the customer with the check_in timing and room type will be stored in database tables.
	   Also, after payment, a UID will be provided to the customer, which will help them during check_out.
	6. During the check_out if the customer forgets his/her UID then they can find their UID with the help of their entered Aadhaar Number.
	   After check_out the checkout timing will also be stored in the database.
	


1. How to Use?
   1. 7 (.py) files are there.
      One is the main file i.e. OHBMS and 5 files will work as module in this project.
      The remaining 1 file is to create a database with tables.
   2. First, use the file name Create_DataBase.py and create the database.
      Then we have to run the main file that is OHBMS.py
   3. Some lines are commented in the code which you can use according to your need.

2. Prerequisites--
   1. Python IDLE ( PyCharm Recommended as I created this project in PyCharm )
   2. Mysql Installed with Python to Mysql Connector.
   3. Then you are good to go.

>>> print("Thankyou")
