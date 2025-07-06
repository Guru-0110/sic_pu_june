import pymysql

def connectDb():
    connection=None
    try:
        connection=pymysql.Connect(host="localhost",user="root",password="Guru232005",
                    database="guru_db",port=3306,charset="utf8")
        print("data base connected")
    except:
        print("data base not connected")
    return connection

def disconnectDb(connection):
    try:
        connection.close()
        print("Data base disconnected")
    except:
        print("Data base not disconnected")

def create_db():
    query = " create database if not exists guru_db"
    connection=connectDb()
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        print("Data base created")
        disconnectDb(connection)
    except:
        print("No database created")

def create_table():
 
        query="CREATE TABLE IF NOT EXISTS employees (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50) NOT NULL,designation VARCHAR(30),phone_number BIGINT UNIQUE,salary FLOAT,commission FLOAT DEFAULT 0, years_of_experience TINYINT,technology VARCHAR(30) NOT NULL)"
        connection = connectDb()
        try:
            cursor.execute(query)
            cursor = connection.cursor()
            print('Table created')
            cursor.close()
            disconnectDb(connection)
        except Exception as e:
           print('Table creation failed:', e)
# id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50) NOT NULL,designation VARCHAR(30),phone_number BIGINT UNIQUE,salary FLOAT,commission FLOAT DEFAULT 0, years_of_experience TINYINT,technology VARCHAR(30) NOT NULL)"

def read_all():
    query='select * from employee'
    connection=connectDb()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("All rows fetched")
        cursor.close()
        disconnectDb(connection)
    except:
        print("The tables are not retrived")

def read_employee_details():
    query = ''
    name=input("Enter the name of the employee :")
    designation=input("Enter the Designation :")
    phone_number=int(input("enter the phone number:"))
    salary = float(input("Enter the salary :"))
    commission = int(input("Enter the commission :"))
    years_of_experience = int(input("Enter the years of experience :"))
    return(name,designation,phone_number,salary,commission,years_of_experience)

    values=()

def update_employee():
    query='update employee set years_of_experience = %s,salary = %s where id = %s'


connection1=connectDb()
# print(connection1)
create_db()
create_table()
read_all()
disconnectDb(connection1)
