from deepface import DeepFace
f1 = "D:\\xampp\\htdocs\\CriminalDetectionPython\\DataSet\\1111101101/1005_1006_sketch2_2.jpg"
f2 = "D:\\xampp\\htdocs\\CriminalDetectionPython\\DataSet\\1111101101/1005_1006_sketch2_10.jpg"
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
result = DeepFace.verify(img1_path=f1, img2_path=f2, detector_backend=backends[1])
print(result)

