import sqlite3

# connect to sqlite
connection=sqlite3.connect("student.db")

#create a cursor object to insert record, create table, retrieve 
cursor=connection.cursor()

#create table
table_info="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

##insert some more records

cursor.execute('''Insert into STUDENT values('Krish', 'Data Science','A', 90)''')
cursor.execute('''Insert into STUDENT values('Randy', 'Data Science','B', 100)''')
cursor.execute('''Insert into STUDENT values('Dhamo', 'Data Science','A', 95)''')
cursor.execute('''Insert into STUDENT values('keviri', 'DEVOPS','A', 60)''')
cursor.execute('''Insert into STUDENT values('sam', 'DEVOPS','A', 45)''')


## Display all the records

print("The inserted records are")

data=cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)
    
    
## close the connection

connection.commit()
connection.close()      