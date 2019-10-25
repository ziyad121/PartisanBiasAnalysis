
import newsapi_scrapping as ns
import os 
import urllib.request
import face_recognition
if not os.path.exists('images'): 
    os.mkdir('images')

def downloader(image_url,file_name):
    full_file_name = str(file_name) + '.jpg'
    #full = os.path.join(os.getcwd()+'/images/', full_file_name)
    full = os.path.join(os.getcwd(), full_file_name )
    urllib.request.urlretrieve(image_url,full)

#for i in range(len(ns.df_left)):
#    if print(str(ns.df_left['urlToImage'][i])) == 'None': 
#        i= i + 1 
#    elif ns.df_left['urlToImage'][i]== None :
#        i= i + 1
#    else:    
img = downloader(ns.df_left['urlToImage'][16],16)

known_image = face_recognition.load_image_file("trump.jpg")
unknown_image = face_recognition.load_image_file("1.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

if len(unknown_encodings) > 0:
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
else:
   print("No faces found in the image!")
   quit()




print(results)


