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
#####United Airlines
df = pd.read_excel(open('table_left.xlsx','rb'), sheet_name='Sheet1')
y = []
# getting rid of retweets in the extraction results and filtering all replies to the tweet often uncessary for the analysis
for i in range(len(df)):
    lt= []
    a= str(df['url'][i])    
    for tweet in tweepy.Cursor(api.search,q=a, count=20,
                                   lang="en",
                                   since="2017-04-03").items(): 
        lt.append(tweet.text)
    y.append(lt)
    print(i)


df['tweets']=y

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
