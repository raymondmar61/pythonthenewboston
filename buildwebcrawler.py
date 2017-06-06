import requests #module to import; request information from a webpage
from bs4 import BeautifulSoup #need to download and install BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/, http://stackoverflow.com/questions/26511791/ubuntu-how-to-install-a-python-module-beautifulsoup-on-python-3-3-instead-of

def trade_spider(max_pages):
	page = 1
	while page <= max_pages: #loops all pages, how url changes everytime
		url = "http://www.innovateinfinitely.com/animepage/2011axpicturesclass.html" #convert page as number to page as string
		source_code = requests.get(url) #connect to webpage and store webpage in source_code
		plain_text = source_code.text #take the text, links, images from source_code and store in plain_text
		soup = BeautifulSoup(plain_text) #convert webpage source code plain_text to an object store in soup
		for link in soup.findAll("a", {"class":"python"}): #get links from <a href>
			href = "http://www.innovateinfinitely.com/animepage/"+link.get("href") #get text inside href and concatenate with main url
			title = link.string
			print(href)
			print(title)
			pass
		page += 1


	pass
trade_spider(1)
#My ININ webpage didn't have convenience .php page and class in <a href>
#The skeleton works because it successfully acquired url for photo number 39