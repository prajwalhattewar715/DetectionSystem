import cv2 
   
      
# test image 
image = cv2.imread('D:\\xampp\\htdocs\\CriminalDetectionPython\\DataSet\\1111101101/1005_1006sksharp7_3.jpg') 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
histogram = cv2.calcHist([gray_image], [0],  
                         None, [256], [0, 256]) 
   
# data1 image 
image = cv2.imread('D:\\xampp\\htdocs\\CriminalDetectionPython\\DataSet\\1111101101/1005_1006_sketch2_10.jpg') 
gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
histogram1 = cv2.calcHist([gray_image1], [0],  
                          None, [256], [0, 256]) 
    
   
   
c1, c2 = 0, 0
   
# Euclidean Distance between data1 and test 
i = 0
while i<len(histogram) and i<len(histogram1): 
    c1+=(histogram[i]-histogram1[i])**2
    i+= 1
c1 = c1**(1 / 2) 
    
print("dist")
print(c1)