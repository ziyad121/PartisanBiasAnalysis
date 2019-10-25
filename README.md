# PartisanBiasAnalysis

Identifying Partisan Affect Online with Visual Semantic Embedding by conducting sentiment analysis of tweets' comments related to biased news about Donald Trump.

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

