import requests
import urllib
import re
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1
import pandas as pd 

#Variables that contains the user credentials to access Twitter API 
#consumer_key = 'r70WuTxeCRVweMVdqz6DONg72'
#consumer_secret = '5NLhmrWdqjzh7TmJ4LLD16WBM38QKNtoHtSVO7TlosQ372DHnc'
#access_token = '708300857163567104-buOrNINky34zMftRwcKSJ2BvKF2cmYK'
#access_token_secret = 'koHzhZYDCIU32tE27g3B9E6Mr8c9fZNgDdoOXk2XqHijr'

auth_params = {
    'app_key':'r70WuTxeCRVweMVdqz6DONg72',
    'app_secret':'5NLhmrWdqjzh7TmJ4LLD16WBM38QKNtoHtSVO7TlosQ372DHnc',
    'oauth_token':'708300857163567104-buOrNINky34zMftRwcKSJ2BvKF2cmYK',
    'oauth_token_secret':'koHzhZYDCIU32tE27g3B9E6Mr8c9fZNgDdoOXk2XqHijr'
}

# Creating an OAuth Client connection
auth = OAuth1 (
    auth_params['app_key'],
    auth_params['app_secret'],
    auth_params['oauth_token'],
    auth_params['oauth_token_secret']
)

df = pd.read_excel(open('table.xlsx','rb'), sheet_name='Sheet1')
url_rest = "https://api.twitter.com/1.1/search/tweets.json"
# getting rid of retweets in the extraction results and filtering all replies to the tweet often uncessary for the analysis

q = 'http://www.msnbc.com/rachel-maddow-show/trump-doesnt-seem-realize-he-was-outmaneuvered-mideast-deal'
params = {'q': q, 'count': 100, 'lang': 'en',  'result_type': 'recent'}
results = requests.get(url_rest, params=params, auth=auth)
tweets = results.json()
messages = [BeautifulSoup(tweet['text'], 'html5lib').get_text() for tweet in tweets['statuses']]


url_rest = "https://api.twitter.com/1.1/search/tweets.json"
y = []
# getting rid of retweets in the extraction results and filtering all replies to the tweet often uncessary for the analysis
for i in range(len(df)):
    q= str(df['url'][i])
    params = {'q': q, 'count': 100, 'lang': 'en',  'result_type': 'recent' , 'tweet_mode':'extended'}
    results = requests.get(url_rest, params=params, auth=auth)
    tweets = results.json()
    messages = [BeautifulSoup(tweet['full_text'], 'html5lib').get_text() for tweet in tweets['statuses']]
    for i in range(len(messages)):
        messages[i] = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",messages[i]).split())
    y.append(list(set(messages)))
