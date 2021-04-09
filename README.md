# PartisanBiasAnalysis

Identifying Partisan Affect Online with Visual Semantic Embedding by conducting sentiment analysis of tweets' comments related to biased news about Donald Trump.

![Screenshot](newspaper_bias.pjg)
# 1st step : 

Identifying the top left, and top  right news websites using MediaBiasChart and checked whether they are considered as sources for the news API: https://newsapi.org/sources.

top Left : 'msnbc','the-huffington-post','cnn','mashable','new-york-magazine', 'mirror','abc-news', 'vice-news' <br/>
top Right: 'the-telegraph','national-review','daily-mail','fox-news','breitbart-news','the-american-conservative'

# 2nd step : 

Scrapping the news related to those newspapers (two dataframes one for each side)<br/>
Scrapped data : 'author', 'content', 'description', 'publishedAt', 'source', 'title','url', 'urlToImage'


# 3rd step :
Face recognition phase where we try to identify trumps face through 'urlToImage' using this library https://github.com/ageitgey/face_recognition

Installation on linux : https://github.com/cftang0827/python-computer-vision-environment-setting
pip install openpyxl

# 4th step :
Scraping the tweets related to scraped news, cleaning and application of Sentiment analysis of the comments, and categorize the comments based on entity
linker 

tweet scraper : https://github.com/lschmelzeisen/nasty 
Sentiment detection: https://github.com/cjhutto/vaderSentiment


Checkout the data.csv file for results


