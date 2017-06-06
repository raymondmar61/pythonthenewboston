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
			word_list.append(each_word) #takes each word add each word or append each word to word_list = []
	clean_up_list(word_list)

def clean_up_list(word_list):
	clean_word_list = [] #store the clean words in a list
	for word in word_list: #loops all words individually
		symbols = "!@#$%^&*()_+{}:\"<>?,./;\'[]-='"
		for i in range(0,len(symbols)):
			word = word.replace(symbols[i], "") #loop through each symbols replace symbols with nothing
		if len(word) > 0: #adds words only to clean_word_list[], don't add nothing
			clean_word_list.append(word)
	create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
	word_count = {}
	for word in clean_word_list: #loop to count words
		if word in word_count:
			word_count[word] += 1 #if word in dictionary, add one
		else:
			word_count[word] = 1 #if word not in dictionary or first time seeing the word, start with one or set counter to one
	for key, value in sorted(word_count.items(),key=operator.itemgetter(1)): #key is the word, value is number or frequency word appeared--word counter in this case. operator.itemgetter(1) gets the second item which is value for sorting.
		print(key,value)

start("http://www.innovateinfinitely.com/animepage/2011axpicturesclass.html")			