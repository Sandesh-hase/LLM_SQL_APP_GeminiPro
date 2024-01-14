import sqlite3

## Connection to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert recored, create table and retreieve the info
cursor = connection.cursor()

## create table
table_info = """

Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

## Insert some more records
cursor.execute("""Insert Into STUDENT values('Roy','Data Science','A',90)""")
cursor.execute("""Insert Into STUDENT values('Joy','Data Science','B',100)""")
cursor.execute("""Insert Into STUDENT values('Shiv','Data Science','A',86)""")
cursor.execute("""Insert Into STUDENT values('Vikash','DEVOPS','A',50)""")
cursor.execute("""Insert Into STUDENT values('Dipesh','DEVOPS','A',35)""")

print("The inserted records are")

data = cursor.execute("""select * from STUDENT""")

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()
