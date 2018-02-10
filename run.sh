
scrapy crawl cnn -o results.json
rm -rf web_files
mkdir web_files
mv results.json web_files/
mv *.html web_files/
python3 tweet_crawler.py
mv tweets.txt web_files/
python3 html_builder.py
