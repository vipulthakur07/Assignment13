from sqlite3 import *
#Question-1
print("Thakur")
print()
try:
    conn = connect('Studnets.db')
    print("Students Database has been created")
#Question-2
    print("Question 2")
    print()    
    mylist=[]
    for i in range(1,11):
        name=input("Enter your name :")
        while(1):
            marks=int(input("Enter your marks :"))
            if 0<=marks<=100:
                break;
            else:
                print("Please enter your marks between the range(0-100)")
        my=(name,marks)
        mylist.append(my)
    print("Hello")
    print()
    cur=conn.cursor()
    query='create table students(Name varchar(50),Marks double(3,1));'
    cur.execute(query)
    print("Students table has been created.")
    print()
    query = 'Insert into students(Name,Marks) values (?,?);'
    cur.executemany(query,mylist)
    query = 'select Name from students where Marks >80;'
    cur.execute(query)
    data = cur.fetchall()
    print("Values has been added to the table.")
    print()
    print("Vipul")
    print()
    print("Studnets with marks more than 80 are:")
    if len(data) is 0:
        print("There are no Student with marks grater than 80")
    else:
        for i in data:
            print(i[0])
    

finally:
    conn.close()
    print('DONE!!')
