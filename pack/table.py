import mysql.connector 


def tables (self,host,user, passw,database):
   
    mydb=mysql.connector.connect(host=(host),user=(user),password=(passw), database=(database))
    
    mycursor = mydb.cursor()
    
    mycursor.execute("show tables")
    
    
    Tables=[]
       
    for tb in mycursor:
        Tables.insert(len(Tables),tb[0])
    return Tables 
    
    myresult= mycursor.fetchall()
    
    return myresult



