import markup
import json

# Method that reads the data from the web_files resutls.json and tweets.txt and creates the trump.html page
def build_page():
	with open('web_files/results.json') as json_data:
	    array = json.load(json_data) 

	with open('web_files/tweets.txt', encoding='utf8') as tweet_data:
		all_tweets = tweet_data.read()
		array_tweets = all_tweets.split('\n\n')

	page = markup.page()
	page.init(header="Trump's great CNN and Twitter feed", title="Trump's great CNN and Twitter feed")

	page.ul(class_='cnn_list')
	for dictionary in array:
		page.li(page.a(dictionary['title'], href='web_files/'+dictionary['url']))
	page.ul.close()

	page.ul(class_='tweet_list')
	for tweet in array_tweets:
		page.li(tweet)
	page.ul.close()

	with open('trump.html', 'wb') as f:
		f.write(str(page).encode())

if __name__ == '__main__':
    build_page()