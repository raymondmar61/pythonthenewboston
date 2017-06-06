#download a csv file
from urllib import request #a different way download module

goog_stock_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=4&e=17&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv"

def download_stock_data(csv_url):
	response = request.urlopen(csv_url) #urlopen() function gets url
	csv = response.read() #read data from csv_url; read the variable response
	csv_string = str(csv) #convert to string, store to variable csv_string
	lines = csv_string.split("\\n") #take a string and breaks it up when it sees \
	dest_url = r"goog.csv" #save file in current directory
	fx = open(dest_url, "w") #open file as read and write
	for line in lines:
		fx.write(line + "\n") #write the file and print each line separated
	fx.close()

download_stock_data(goog_stock_url) #call the function with variable containing URL