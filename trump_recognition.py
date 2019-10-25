
import newsapi_scrapping as ns
import os 
import urllib.request
import face_recognition

known_image = face_recognition.load_image_file("trump.jpg")
biden_encoding = face_recognition.face_encodings(known_image)[0]

if not os.path.exists('images'): 
    os.mkdir('images')
    
os.chdir('images')

def downloader(image_url,file_name):
    full_file_name = str(file_name) + '.jpg'
    full = os.path.join(os.getcwd(), full_file_name)
    urllib.request.urlretrieve(image_url,full)

for i in range(len(ns.df_left)):
    if print(str(ns.df_left['urlToImage'][i])) == 'None': 
        ns.df_left.loc[i, 'trump_image'] = "not readable"
    elif ns.df_left['urlToImage'][i]== None :
        ns.df_left.loc[i, 'trump_image'] = "not readable"
    else:    
        img = downloader(ns.df_left['urlToImage'][i],i)
        unknown_image = face_recognition.load_image_file(str(i)+'.jpg')
        unknown_encoding = face_recognition.face_encodings(unknown_image)
        if len(unknown_encoding) > 0:
            unknown_encoding = unknown_encoding[0]
            results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
            print(results)
            if results :
                ns.df_left.loc[i, 'trump_image'] ='trump'  
            else :
                ns.df_left.loc[i, 'trump_image'] = 'not trump'  
        else:
            ns.df_left.loc[i, 'trump_image'] = 'no face' 

df_left_trump = ns.df_left
print (df_left_trump)


print(df_left_trump['trump_image'].value_counts(normalize=True) * 100)
df_left_trump.to_excel("table.xlsx", index=False)

