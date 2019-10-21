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
left = ['msnbc','the-huffington-post','cnn','mashable','new-york-magazine', 'mirror','abc-news', 'vice-news']

right = ['the-telegraph','national-review','daily-mail','fox-news','breitbart-news','the-american-conservative']
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

for np in left:
    
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
