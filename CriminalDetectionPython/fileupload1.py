#!C:\Users\Prajwal\AppData\Local\Programs\Python\Python311\python
# Import Basic OS functions
import os
# Import modules for CGI handling
import cgi, cgitb
import urllib.request
#from HaarWavelet import *
from FunFactory import *  
import shutil
from ConvertToSketch import *
from ImageAugmentation import *
import glob
#from HOG import *


# enable debugging
cgitb.enable()
# print content type
print("Content-type:text/html\r\n\r\n")
print("path="+os.getcwd()) 
#print() 
#form=cgi.FieldStorage()

# HTML INPUT FORM
HTML = """
<html>
<head>
<title></title>
</head>
<body>

  <h1>Upload File</h1>
  <form action="http://localhost:64203/Default.aspx" method="POST">
    File: <input name="file" type="file">
    <input name="submit" type="submit">
</form>

{% if filedata %}

<blockquote>

{{filedata}}

</blockquote>

{% endif %}  

</body>
</html>
"""
filename=""
ext=""
uploaded_file_path=""
inFileData = None
form = cgi.FieldStorage()  
criminal_id=form.getvalue("criminal_id")
#criminal_id_b=format(int(criminal_id), 'b')

criminal_name=form.getvalue("criminal_name")
criminal_id_b=criminal_name
try: 
   insertLables(criminal_id,criminal_name)
except Exception as e:
   print("entry already exists")
    
UPLOAD_DIR=os.getcwd()+"\\DataSet\\" +criminal_id_b+"/"
UPLOAD_DIR_Test=os.getcwd()+"\\test\\" +criminal_id_b+"/"
UPLOAD_DIR1=os.getcwd()+"\\images\\" 
UPLOAD_DIR2=os.getcwd()+"\\temp\\" 
UPLOAD_DIR3=os.getcwd()+"\\criminal_photos\\" 
try:
   
   for file in glob.glob(UPLOAD_DIR2+"*.*"): 
      os.remove(file)
    
   for file in glob.glob(UPLOAD_DIR1+"/0/"+"*.*"):
      os.remove(file)  
   for file in glob.glob(UPLOAD_DIR1+"*.*"):
      os.remove(file)  
    
except Exception as e:
   print("error in delete")
   print(e) 
try: 
   os.mkdir(UPLOAD_DIR)
   os.mkdir(UPLOAD_DIR_Test)
except Exception as e:
   print("error in delete")
   print(e)
#print("value="+form.getvalue("uid"))
# IF A FILE WAS UPLOADED (name=file) we can find it here.
#fid=form.getvalue("fid")
#print(form)
fileitem = form['file']

if 'file' in form:

   filefield = form['file']
   if not isinstance(filefield, list):
      filefield = [filefield]
    
   for fileitem in filefield:
      print("f"+fileitem.filename)
       #if fileitem.filename:
          #fn = os.path.basename(fileitem.filename)
      docid=getMaxIdPhotos()
      print("id="+str(docid))
      nm,ext=os.path.basename(fileitem.filename).split('.')
      fn=str(criminal_id)+"_"+str(docid)+"."+ext
      print("file")
      print(fn)
      filename=os.path.basename(fileitem.filename)
      print(filename)
      print("file")
          # save file
      with open(UPLOAD_DIR2 + fn, 'wb') as f:
         print("saved")
         shutil.copyfileobj(fileitem.file, f)
      shutil.copy(UPLOAD_DIR2 + fn, UPLOAD_DIR3 + fn)
      convert(UPLOAD_DIR2+fn,UPLOAD_DIR+fn)
      augmentation(UPLOAD_DIR2+fn,UPLOAD_DIR+str(criminal_id)+"_"+str(docid),"."+ext)
      augmentation1(UPLOAD_DIR2+fn,UPLOAD_DIR+str(criminal_id)+"_"+str(docid),"."+ext)
      augmentation2(UPLOAD_DIR2+fn,UPLOAD_DIR+str(criminal_id)+"_"+str(docid),"."+ext)
      augmentation3(UPLOAD_DIR2+fn,UPLOAD_DIR+str(criminal_id)+"_"+str(docid),"."+ext)
      augmentation4(UPLOAD_DIR2+fn,UPLOAD_DIR+str(criminal_id)+"_"+str(docid),"."+ext)
      convert_to_sketchify(UPLOAD_DIR2+fn,UPLOAD_DIR,str(criminal_id)+"_"+str(docid)+"_sketchify"+"."+ext)
      #convert_to_sketch2(UPLOAD_DIR2+fn,UPLOAD_DIR,str(criminal_id)+"_"+str(docid)+"_sketch2"+"."+ext)
      convert_to_sketch2(UPLOAD_DIR2+fn,UPLOAD_DIR+str(criminal_id)+"_"+str(docid)+"_sketch2","."+ext,UPLOAD_DIR_Test+str(criminal_id)+"_"+str(docid)+"_sketch2")
      # flip the image by horizontally
      img = cv2.imread(UPLOAD_DIR2+fn)
      img_h = cv2.flip(img, 1)
      try: 
         os.remove(UPLOAD_DIR2+fn) 
      except Exception as e:
         print("error in delete")
         print(e) 
      cv2.imwrite(UPLOAD_DIR2+fn,img_h)
      convert(UPLOAD_DIR2+fn,UPLOAD_DIR+fn)
      augmentation(UPLOAD_DIR2+fn,UPLOAD_DIR+str(criminal_id)+"_"+str(docid)+"_fliped","."+ext)
      augmentation1(UPLOAD_DIR2+fn,UPLOAD_DIR+str(criminal_id)+"_"+str(docid)+"_fliped","."+ext)
      augmentation2(UPLOAD_DIR2+fn,UPLOAD_DIR+str(criminal_id)+"_"+str(docid)+"_fliped","."+ext)
      convert_to_sketchify(UPLOAD_DIR2+fn,UPLOAD_DIR,str(criminal_id)+"_"+str(docid)+"_sketchify"+"_fliped"+"."+ext)
       
      #convert_to_sketch2(UPLOAD_DIR2+fn,UPLOAD_DIR,str(criminal_id)+"_"+str(docid)+"_sketch2"+"_fliped"+"."+ext)
      convert_to_sketch2(UPLOAD_DIR2+fn,UPLOAD_DIR+str(criminal_id)+"_"+str(docid)+"_sketch2"+"_fliped","."+ext)
     
      insertPhotos(docid,criminal_id,criminal_name,fn)
      #img_preprocessing1(fn,category,docid1)
    
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#print(jinja2.Environment().from_string(HTML).render(filedata=inFileData)) 
#w2d("E:\\python\\1.jpg",'haar','111')
#print(form.getvalue("fid"))

#userid=form.getvalue("userid")

###dt=form.getvalue("dt")
#tm=form.getvalue("tm")
#category=form.getvalue("category")

print(docid)
#print(title+" " +category)
 
#hog1=hogFeatures(filename,category)
#print(hog1)
#insert(docid,title,userid,filename, dt,tm,category)
print("<html>")
print("<head>")
print("<meta http-equiv='refresh' content='0;url=http://localhost:8080/datasetInsrtPython?sts=success&criminal_id="+criminal_id+"&criminal_name="+criminal_name+"' />")
print("</head>")
print("</html>")