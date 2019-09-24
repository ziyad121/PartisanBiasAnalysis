#pip install CMake
#install dlib package using the link for windows users
#https://github.com/charlielito/install-dlib-python-windows
#pip install --no-dependencies face_recognition face_recognition_models

import newsapi_scrapping as ns
from urllib.request import urlopen
from PIL import Image
import face_recognition

known_image = face_recognition.load_image_file("biden.jpg")
unknown_image = face_recognition.load_image_file("unknown.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

#for i in range(len(ns.df_left)):
img = Image.open(urlopen(ns.df_left['urlToImage'][0]))

