import mysql.connector

def connect (self,host,user, passw,database):
    
    conn = mysql.connector.connect(host=(host),user=(user),password=(passw), database=(database))
    
    conn.close()
   
       
