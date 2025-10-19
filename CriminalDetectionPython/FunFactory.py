import base64
from DBConnect import *  
def convertToBase64(imagePath) :
    #message_bytes = message.encode('ascii')
    base64_message="NA"
    with open(imagePath, "rb") as imageFile:
        base64_message = base64.b64encode(imageFile.read())
    #print(base64_message)
    message = base64_message.decode('ascii')
    return message

def convertFromBase64(base64_message='NA',fileName="NA") :
    imgdata = base64.b64decode(base64_message)
    filename = fileName  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)

def getMaxId():
    conn = connect()
    #integrated security 
    cursor = conn.cursor() 
    cursor.execute('select (ifnull(max(appid),1000)+1) as mxid from apps;')
    mxid=0
    for row in cursor: 
        mxid=row[0]
        print(int(mxid)+1)
    conn.close()
    return mxid
def getMaxIdPhotos():
    conn = connect()
    #integrated security 
    cursor = conn.cursor() 
    cursor.execute('select (ifnull(max(photo_id),1000)+1) as mxid from criminal_photos;')
    mxid=0
    for row in cursor: 
        mxid=row[0]
        print(int(mxid)+1)
    conn.close()
    return mxid
def insertPhotos(photo_id=0,criminal_id=0,criminal_name="NA",path="NA") : 
    conn = connect()    
    cursor = conn.cursor()
    args = [photo_id,criminal_id,criminal_name,path]
    args1=cursor.callproc('insertPhotos', args)
    print("Return value:", args1)
    #for result in cursor.stored_results():
     #       print(result.fetchall())
    cnt=cursor.rowcount 
    conn.commit()
    conn.close()
def insertLables(criminal_id="NA",criminal_name="NA") : 
    conn = connect()    
    cursor = conn.cursor()
    args = [criminal_id,criminal_name]
    args1=cursor.callproc('insertLables', args)
    print("Return value:", args1)
    #for result in cursor.stored_results():
     #       print(result.fetchall())
    cnt=cursor.rowcount 
    conn.commit()
    conn.close()
    #args = [userid,title,docPath,docDesc,dt,tm,key]
    #args1=cursor.callproc('insertDoc', args)
    #print("Return value:", args1)
    #for result in cursor.stored_results():
    #        print(result.fetchall())
    #cnt=cursor.rowcount
   
    #return cnt
def getSrno(cate='NA'):
    conn = connect()
    #integrated security 
    cursor = conn.cursor() 
    cursor.execute("select srNo as mxid from labels where title='"+cate+"';")
    mxid=0
    for row in cursor: 
        mxid=row[0]
        print(int(mxid)+1)
    conn.close()
    return mxid 
def getDictionary() :  
    conn = connect()    
    cursor = conn.cursor() 
    cursor.execute("select srNo as key1,title as val from labels")
    out = cursor.fetchall()
    variable = {key:val for key,val in out}
    print(variable)
    conn.commit()
    return variable
def getLabelCount() :  
    conn = connect()    
    cursor = conn.cursor() 
    cursor.execute("select count(*) as cnt from labels")
    out = cursor.fetchall() 
    print(out[0][0])
    conn.commit()
    return int(str(out[0][0]).strip())