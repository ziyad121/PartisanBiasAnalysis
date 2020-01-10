import pandas as pd 
import requests
import nasty
from datetime import datetime
import re
subscription_key = "dcb69dd803c84fc9a4b4a05b3775532e"
search_terms = {"The New Yorker" : "newyorker.com trump", 
               "MotherJones": "motherjones.com trump", 
               "The Nation": "thenation.com trump", 
               "The Daily Beast": "thedailybeast.com trump",
               "Jacobin":"jacobinmag.com trump",
               "The Intercept": "theintercept.com trump",
               "Slate": "slate.com trump",
               "MSNBC":"msnbc.com trump",
               "BuzzFeed News" : "buzzfeednews.com trump"}

search_url = "https://ziyad.cognitiveservices.azure.com/bing/v7.0/news/search?"
headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
simple_list=[["Title","description","url","date_published","image", "Newspaper"]]



list_values = list(search_terms.values())

params  = {"q": "newyorker.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
a = response.json()['value']
for i in range(len(a)):
    if a[i]["provider"][0]["name"] in search_terms.keys():
        if "image" in a[i]:
            simple_list.append([a[i]["name"],
                                a[i]["description"],
                                a[i]["url"],
                                a[i]["datePublished"],
                                a[i]["image"]["contentUrl"], 
                                a[i]["provider"][0]["name"]])
        else : pass


params  = {"q": "motherjones.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
a = response.json()['value']
for i in range(len(a)):
    if a[i]["provider"][0]["name"] in search_terms.keys():
        if a[i]["image"]["contentUrl"] != None:
            simple_list.append([a[i]["name"],
                                a[i]["description"],
                                a[i]["url"],
                                a[i]["datePublished"],
                                a[i]["image"]["contentUrl"], 
                                a[i]["provider"][0]["name"]])
        else : pass

params  = {"q": "thenation.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
a = response.json()['value']
for i in range(len(a)):
    if a[i]["provider"][0]["name"] in search_terms.keys():
        if "image" in a[i]:
            simple_list.append([a[i]["name"],
                                a[i]["description"],
                                a[i]["url"],
                                a[i]["datePublished"],
                                a[i]["image"]["contentUrl"], 
                                a[i]["provider"][0]["name"]])
        else : pass



params  = {"q": "thedailybeast.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
a = response.json()['value']
for i in range(len(a)):
    if a[i]["provider"][0]["name"] in search_terms.keys():
        if "image" in a[i]:
            simple_list.append([a[i]["name"],
                                a[i]["description"],
                                a[i]["url"],
                                a[i]["datePublished"],
                                a[i]["image"]["contentUrl"], 
                                a[i]["provider"][0]["name"]])
        else : pass


params  = {"q": "jacobinmag.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
a = response.json()['value']
for i in range(len(a)):
    if a[i]["provider"][0]["name"] in search_terms.keys():
        if "image" in a[i]:
            simple_list.append([a[i]["name"],
                                a[i]["description"],
                                a[i]["url"],
                                a[i]["datePublished"],
                                a[i]["image"]["contentUrl"], 
                                a[i]["provider"][0]["name"]])
        else : pass


params  = {"q": "theintercept.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
a = response.json()['value']
for i in range(len(a)):
    if a[i]["provider"][0]["name"] in search_terms.keys():
        if "image" in a[i]:
            simple_list.append([a[i]["name"],
                                a[i]["description"],
                                a[i]["url"],
                                a[i]["datePublished"],
                                a[i]["image"]["contentUrl"], 
                                a[i]["provider"][0]["name"]])
        else : pass


params  = {"q": "slate.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
a = response.json()['value']
for i in range(len(a)):
    if a[i]["provider"][0]["name"] in search_terms.keys():
        if "image" in a[i]:
            simple_list.append([a[i]["name"],
                                a[i]["description"],
                                a[i]["url"],
                                a[i]["datePublished"],
                                a[i]["image"]["contentUrl"], 
                                a[i]["provider"][0]["name"]])
        else : pass


params  = {"q": "buzzfeednews.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
a = response.json()['value']
for i in range(len(a)):
    if a[i]["provider"][0]["name"] in search_terms.keys():
        if "image" in a[i]:
            simple_list.append([a[i]["name"],
                                a[i]["description"],
                                a[i]["url"],
                                a[i]["datePublished"],
                                a[i]["image"]["contentUrl"], 
                                a[i]["provider"][0]["name"]])
        else : pass

params  = {"q": "msnbc.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
a = response.json()['value']
for i in range(len(a)):
    if a[i]["provider"][0]["name"] in search_terms.keys():
        if "image" in a[i]:
            simple_list.append([a[i]["name"],
                                a[i]["description"],
                                a[i]["url"],
                                a[i]["datePublished"],
                                a[i]["image"]["contentUrl"], 
                                a[i]["provider"][0]["name"]])
        else : pass
    
df_left= pd.DataFrame(simple_list[1:],columns=simple_list[0])


y = []

for i in range(len(df_left)):
    lt= []
    a= str(df_left['url'][i])    
    tweet_stream = nasty.Search(a,
                            until=datetime(2020, 1, 11),
                            lang="en").request()
    for tweet in tweet_stream: 
#        var = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.text).split())
        lt.append(tweet.text)
    y.append(list(set(lt)))
    print(i)    


from nltk.tokenize import WordPunctTokenizer
tok = WordPunctTokenizer()
pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))

def tweet_cleaner(text):
    souped = text
    stripped = re.sub(combined_pat, '', souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    lower_case = letters_only.lower()
    # During the letters_only process two lines above, it has created unnecessay white spaces,
    # I will tokenize and join together to remove unneccessary white spaces
    words = tok.tokenize(lower_case)
    return (" ".join(words)).strip()


for i in range(len(y)):
    for j in range(len(y[i])):
        y[i][j]= clean_text = tweet_cleaner(y[i][j])

df_left['tweets']=y

df_left= df_left[df_left.astype(str)['tweets'] != '[]']
df_left=df_left.reset_index()

#---------------------------------------------------------------------

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np



analyzer = SentimentIntensityAnalyzer()


df_left['pos'] = np.nan
df_left['neg'] = np.nan
df_left['neu'] = np.nan
df_left['compound'] = np.nan
#df_left['pos_average'] = np.nan
#df_left['neg_average'] = np.nan
#df_left['neu_average'] = np.nan
df_left['compound_average'] = np.nan
df_left['flag'] = np.nan

#posg=[]
#negg=[]
#neug=[]
compg=[]
flagg=[]
for i in range(len(df_left['tweets'])):
    pos=[]
    neg=[]
    neu=[]
    comp=[]
    for j in range(len(df_left['tweets'][i])):
        # calculate the senti-index for each advert text
        tempRespond = analyzer.polarity_scores(df_left['tweets'][i][j])   
        pos.append(tempRespond['pos'])
        neg.append(tempRespond['neg'])
        neu.append(tempRespond['neu'])
        comp.append(tempRespond['compound'])
#    posg.append(pos)
#    negg.append(neg)
#    neug.append(neu)
    compg.append(comp)

#df_left['pos'] = posg
#df_left['neg'] = negg
#df_left['neu'] = neug
df_left['compound'] = compg

#-----------------------------------------------------------------
def Average(lst): 
    if len(lst)==0:
        return 0
    else : return sum(lst) / len(lst) 

for av in range(len(df_left)):
    df_left['compound_average'][av]= Average(df_left['compound'][av])
    if 0.5 <= df_left['compound_average'][av]  and df_left['compound_average'][av] <= 1:
        flagg.append('positive')
    elif -0.5 < df_left['compound_average'][av]  and df_left['compound_average'][av] < 0.5:
        flagg.append('neutral') 
    else:
        flagg.append('negative')
        
df_left['flag']= flagg
 

df_left=df_left.drop(['pos','neg', 'neu','index'], axis=1)
df_left.to_excel('cleanedData.xlsx')
