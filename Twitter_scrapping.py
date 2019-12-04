import pandas as pd 
import requests
import datetime
import configparser

#maximum 10 days from current date or upgrade to premium
today = datetime.date.today()
start = today - datetime.timedelta(days=10)
config = configparser.ConfigParser()
config.read('config.ini')

#last two are left centered 
left = ['msnbc','the-huffington-post','cnn','mashable','new-york-magazine','abc-news', 'vice-news']

#'the-telegraph' and 'daily-mail'are no longer supported
right = ['national-review','fox-news','breitbart-news','the-american-conservative']

df_left = pd.DataFrame()
df_right = pd.DataFrame()

for np in left:
    
    url = ('https://newsapi.org/v2/everything?'       
               'q=Trump&'
               'sources='+np+'&'
               'from='+str(start)+'&'
               'sortBy=popularity&'
        
               'apiKey'+'='+str(config['DEFAULT']['key']))
    response = requests.get(url)
    response = response.json()
    df_left=df_left.append(pd.DataFrame(response['articles']),ignore_index=True)
print(df_left)

for np in right:
    
    url = ('https://newsapi.org/v2/everything?'       
               'q=Trump&'
               'sources='+np+'&'
               'from='+str(start)+'&'
               'sortBy=popularity&'
        
               'apiKey'+'='+str(config['DEFAULT']['key']))
    response = requests.get(url)
    response = response.json()
    df_right=df_right.append(pd.DataFrame(response['articles']),ignore_index=True)

print(df_right)

#---------------------------------------
import re
import tweepy
import pandas as pd 
####input your credentials here
consumer_key = 'tiaxyvHY2oorqfb7U26YieQ3I'
consumer_secret = 'G5TuEa0j4GIH9ovSK1sOVaBVmQMoLca3YicAu6LZ9uYqLxzFAL'
access_token = '1144220830303490048-9X1lHxQ5CKNFgqgZ0MGg8rLYUTDt71'
access_token_secret = 'ltYy2vVgxJ98E2h51Yz2V8sJYu0lkR4AMhFet91P52bbw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


y = []

for i in range(len(df_left)):
    lt= []
    a= str(df_left['url'][i])    
    results = api.search(q=a, lang="en", count=20, tweet_mode='extended')
    for tweet in results: 
        var = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.full_text).split())
        lt.append(var)
    y.append(list(set(lt)))
    print(i)    
df_left['tweets']=y

#---------------------------------------
z=[]
for j in range(len(df_right)):
    bt= []
    a= str(df_right['url'][j])    
    results = api.search(q=a, lang="en", count=20, tweet_mode='extended')
    for tweet in results: 
        var = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.full_text).split())
        bt.append(var)
    z.append(list(set(bt)))
    print(j)

df_right['tweets']=z



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
 
#df_left=df_left.drop(['neu_average', 'neg_average','pos_average'], axis=1)
df_left=df_left.drop(['author','source', 'content', 'publishedAt'], axis=1)
df_left.to_excel('outputleft6-12.xlsx')

#-------------------------------------------------------------------

df_right['pos'] = np.nan
df_right['neg'] = np.nan
df_right['neu'] = np.nan
df_right['compound'] = np.nan
#df_left['pos_average'] = np.nan
#df_left['neg_average'] = np.nan
#df_left['neu_average'] = np.nan
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

#df_left['pos'] = posg
#df_left['neg'] = negg
#df_left['neu'] = neug
df_right['compound'] = compg

#-----------------------------------------------------------------


for av in range(len(df_right)):
    df_right['compound_average'][av]= Average(df_right['compound'][av])
    if 0.5 <= df_right['compound_average'][av]  and df_right['compound_average'][av] <= 1:
        flagg.append('positive')
    elif -0.5 < df_right['compound_average'][av]  and df_right['compound_average'][av] < 0.5:
        flagg.append('neutral') 
    else:
        flagg.append('negative')
        
df_right['flag']= flagg
 
#df_left=df_left.drop(['neu_average', 'neg_average','pos_average'], axis=1)
df_right=df_right.drop(['author', 'source','content', 'publishedAt'], axis=1)
df_right.to_excel('outputright6-12.xlsx')
