Db_cn file :

This file creates a database of the name : TarunHouseKeeping.db
at the location mentioned at line 36 in database variable.

Ex : database = "C:/Users/ankth/OneDrive/Desktop/TarunHouseKeeping.db"
Change this database location according to your pc.

This will create a database and the tables inside the database. It also inserts a value into AssetsDsc for easy verification of the print
all assets function.


server.py file:

This uses flask to create the required api's it uses modeling as required.
Each Api is divided into seperate classes. 

1)the Asset class takes input details of the assets and insert into databse.
2) The task class takes input TaskiD,Frequency and Description and stores it in database
3) The worker class inputs and store WorkerID,Name,Phno and Address.
4) The PrAsser is for printing the assets
5) And the AllocateTAsk is the Admin class as required to Assign Task

Running Instructions :

Before running this file change the db_connect variable in line 8 
change the Path after the sqlite:/// to wherever you have saved the database.

The line in original file is : db_connect = create_engine('sqlite:///C:/Users/ankth/OneDrive/Desktop/TarunHouseKeeping.db')

Sample Database db is also attached in zip we can use that or use db_cn to create a fresh database.

Requiremnts :
1) sqlite3 pip install sqlitee3
2) pip install Flask-SQLAlchemy
3) pip install Flask
4) pip install flask-restful
5) pip install jsonlib

NOTE (IMP) :
The path of database and .py files are different the database is kept one step above the .py file in the original code though it is together in zip the path mentioned in variables are different.
Databse is on dektop and .py files are in a folder UdaanMY on desktop.
