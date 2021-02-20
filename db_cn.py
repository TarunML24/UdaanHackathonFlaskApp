
import sqlite3
from sqlite3 import Error
 
 


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except :
        print("Database connection error")
 
    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e,"table creation error")

def main():
    database = "C:/Users/ankth/OneDrive/Desktop/TarunHouseKeeping.db"
 
    sql_create_AssetDB = """ CREATE TABLE IF NOT EXISTS AssetsDsc (
                                        AssetID integer PRIMARY KEY,
                                        AssetName text NOT NULL,
                                        COST integer
                                    ); """
 
    sql_create_TaskDdB = """CREATE TABLE IF NOT EXISTS Tasks (
                                    TaskDID integer PRIMARY KEY,
                                    TaskFreq integer,
                                    TDESC text
                                );"""
    sql_create_WorkerDB = """CREATE TABLE IF NOT EXISTS Worker (
                                    WorkID integer PRIMARY KEY,
                                    Wname text NOT NULL,
                                    priority integer,
                                    Phno integer,
                                    Addr text
                                );"""
    sql_create_AllTaskDB = """CREATE TABLE IF NOT EXISTS TaskAll (
                                    start_date text NOT NULL,
                                    allocated_time text NOT NULL,
                                    alt_id integer REFERENCES Tasks (TaskDID),
                                    alw_id integer REFERENCES Worker (WorkID),
                                    ala_id integer REFERENCES AssestsDsc (AssetID)
                                );"""
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_AssetDB)
        # create tasks table
        create_table(conn, sql_create_TaskDdB)
        create_table(conn, sql_create_TaskDdB)
        create_table(conn, sql_create_WorkerDB)
        create_table(conn, sql_create_AllTaskDB)
    else:
        print("Error! cannot create the database connection.")
    c = conn.cursor()
    ins_quer="""INSERT INTO AssetsDsc VALUES(1234,'car',100);"""
    c.execute(ins_quer)
    conn.commit()
        
if __name__ == '__main__':
    main()