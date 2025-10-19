#!C:\Users\Megha\AppData\Local\Programs\Python\Python310\python
import mysql.connector as mycon

def connect() : 
    try:
        con=mycon.connect(host='brnb4dk6d13j8edq1cnj-mysql.services.clever-cloud.com',user='uoi9dfyxj5a28d8v',password='Ij07Dw39ZRpAV9X2Gt1z',database='brnb4dk6d13j8edq1cnj')
    except Exception as e:
        print('max connections')
    return con