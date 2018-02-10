# trump-crawler
Crawls 25 articles from CNN and 25 Tweets of Donald Trump, using Scrapy, Tweepy, Newspaper and MarkupPy

### How do I run the code ? ###

Execute the bash script run.sh
The bash script would execute in order the CNN scraping, twitter crawling, and the htmlbuilder.
```
#!bash
bash run.sh
```

# Dependecies
```
#!bash
pip3 install scrapy==1.50
pip3 install tweepy==3.5.0
pip3 install newspaper3k==0.2.6
```

# Acknowledgment and useful links
https://www.data-blogger.com/2016/08/18/scraping-a-website-with-python-scrapy/
https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash/
https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
https://tylerbakke.github.io/MarkupPy/#ex_xml
https://github.com/codelucas/newspaper
