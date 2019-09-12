# PartisanBiasAnalysis
Identifying Partisan Affect Online with Visual Semantic Embedding by conducting sentiment analysis of tweets' comments related to biased news about Donald Trump.

# 1st step : 

Identifying the top left, and top  right news websites using MediaBiasChart and checked whether they are considered as sources for the news API: https://newsapi.org/sources.

top Left : 'msnbc','the-huffington-post','cnn','mashable','new-york-magazine', 'mirror','abc-news', 'vice-news'
/n top Right: 'the-telegraph','national-review','daily-mail','fox-news','breitbart-news','the-american-conservative'

# 2nd step : 

Scrapping the news related to those newspapers (two dataframes one for each side)
Scrapped data : 'author', 'content', 'description', 'publishedAt', 'source', 'title','url', 'urlToImage'


# 3rd step :
Face recognition phase where we try to identify trumps face through 'urlToImage' 
https://github.com/ageitgey/face_recognition


