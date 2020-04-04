import mysql.connector 


def champs (self,host,user, passw,database):
    
    mydb=mysql.connector.connect(host=(host),user=(user),password=(passw), database=(database))
        
    mycursor = mydb.cursor()
        
    mycursor.execute("SELECT * FROM personne")
        
    myresult= mycursor.fetchall()
    return myresult
    




