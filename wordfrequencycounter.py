import requests #use to connect to a URL
from bs4 import BeautifulSoup #use to pick out certain pieces of a url
import operator #use to create the dictionary or counting the words downloaded from the url

def start(url):
	word_list = []
	source_code = requests.get(url).text #connect to url and get text
	soup = BeautifulSoup(source_code,"html.parser") #BeautifulSoup converts source_code into something and becomes an object named soup
	for post_text in soup.findAll("a", {"class": "python"}):
		content = post_text.string #goes through source code, get links with class "class" and converts to string; i.e. remove HTML
		words = content.lower().split() #convert text to lowercase and takes a sentence and separates into individual words
		for each_word in words:
			print(each_word)
			word_list.append(each_word) #takes each word add each word or append each word to word_list = []

start("http://www.innovateinfinitely.com/animepage/2011axpicturesclass.html")			