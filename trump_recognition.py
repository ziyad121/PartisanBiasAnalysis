
import newsapi_scrapping as ns
import os 
import urllib.request
#import face_recognition

#known_image = face_recognition.load_image_file("biden.jpg")
#unknown_image = face_recognition.load_image_file("unknown.jpg")

#biden_encoding = face_recognition.face_encodings(known_image)[0]
#unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

#results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
if not os.path.exists('images'): 
    os.mkdir('images')

def downloader(image_url,file_name):
    full_file_name = str(file_name) + '.jpg'
    full = os.path.join(os.getcwd()+'/images/', full_file_name )
    urllib.request.urlretrieve(image_url,full)

for i in range(len(ns.df_left)):
    if print(str(ns.df_left['urlToImage'][i])) == 'None': 
        i= i + 1 
    elif ns.df_left['urlToImage'][i]== None :
        i= i + 1
    else:    
        img = downloader(ns.df_left['urlToImage'][i],i)

#for i in range(len(ns.df_right)):
# img = urllib.request.urlretrieve(ns.df_right['urlToImage'][i], str(len(ns.df_right)+i)+'.jpg')


