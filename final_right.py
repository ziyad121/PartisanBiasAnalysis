# not trump    58.924205
# no face      20.537897
# trump        20.537897




import pandas as pd 
import requests
import nasty
from datetime import datetime
import re
subscription_key = "dcb69dd803c84fc9a4b4a05b3775532e"
search_terms = {"Washington Times" : "washingtontimes.com trump", 
	       "Reason": "reason.com trump", 
               "The Fiscal Times": "thefiscaltimes.com trump", 
               "National Review": "nationalreview.com trump",
               "The Hill":"thehill.com trump",
               "New York Post": "nypost.com trump",
               "Fox News": "foxnews.com/opinion trump", #fox news opinion
               "The American Spectator":"spectator.org trump",
               "Mail Online" : "dailymail.co.uk trump"} #dailymail 

search_url = "https://ziyad.cognitiveservices.azure.com/bing/v7.0/news/search?"
headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
simple_list=[["Title","description","url","date_published","image", "Newspaper"]]



list_values = list(search_terms.values())

params  = {"q": "washingtontimes.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
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


params  = {"q": "reason.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
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

params  = {"q": "thefiscaltimes.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
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



params  = {"q": "nationalreview.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
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


params  = {"q": "thehill.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
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


params  = {"q": "nypost.com trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
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


params  = {"q": "foxnews.com/opinion trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
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


params  = {"q": "spectator.org trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
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

params  = {"q": "dailymail.co.uk trump" ,"count":"100", "mkt":"en-US","originalImg":"true"}
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
    
df_right= pd.DataFrame(simple_list[1:],columns=simple_list[0])


y = []

for i in range(len(df_right)):
    lt= []
    a= str(df_right['url'][i])    
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

df_right['tweets']=y

df_right= df_right[df_right.astype(str)['tweets'] != '[]']
df_right=df_right.reset_index()

#---------------------------------------------------------------------

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np



analyzer = SentimentIntensityAnalyzer()


df_right['pos'] = np.nan
df_right['neg'] = np.nan
df_right['neu'] = np.nan
df_right['compound'] = np.nan
#df_right['pos_average'] = np.nan
#df_right['neg_average'] = np.nan
#df_right['neu_average'] = np.nan
df_right['compound_average'] = np.nan
df_right['flag'] = np.nan

#posg=[]
#negg=[]
#neug=[]
compg=[]
flagg=[]
for i in range(len(df_right['tweets'])):
    pos=[]
    neg=[]
    neu=[]
    comp=[]
    for j in range(len(df_right['tweets'][i])):
        # calculate the senti-index for each advert text
        tempRespond = analyzer.polarity_scores(df_right['tweets'][i][j])   
        pos.append(tempRespond['pos'])
        neg.append(tempRespond['neg'])
        neu.append(tempRespond['neu'])
        comp.append(tempRespond['compound'])
#    posg.append(pos)
#    negg.append(neg)
#    neug.append(neu)
    compg.append(comp)

#df_right['pos'] = posg
#df_right['neg'] = negg
#df_right['neu'] = neug
df_right['compound'] = compg

#-----------------------------------------------------------------
def Average(lst): 
    if len(lst)==0:
        return 0
    else : return sum(lst) / len(lst) 

for av in range(len(df_right)):
    df_right['compound_average'][av]= Average(df_right['compound'][av])
    if 0.5 <= df_right['compound_average'][av]  and df_right['compound_average'][av] <= 1:
        flagg.append('positive')
    elif -0.5 < df_right['compound_average'][av]  and df_right['compound_average'][av] < 0.5:
        flagg.append('neutral') 
    else:
        flagg.append('negative')
        
df_right['flag']= flagg
 

df_right=df_right.drop(['pos','neg', 'neu','index'], axis=1)
df_right.to_excel('cleanedDataright.xlsx')
