import requests
from bs4 import BeautifulSoup

def get_title(source_code):
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    for title in soup.findAll('div',{'class':'title_wrapper'}):
        return title.find('h1').text.rstrip()

def get_movie_data(source_code):
	text = source_code.text
	soup = BeautifulSoup(text, 'lxml')
	for div in soup.findAll('div', {'class': 'ratingValue'}):
		print ('Imdb rating of the movie/Tv Series "'+movie_name+'" is: ')
		print (div.text)
	for div in soup.findAll('div', {'class': 'summary_text'}):
		print ("Summary of the movie/TV Series \n" + div.text.lstrip())

print("Enter movie/tv series name")
movie = input()
url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+movie+'&s=all'

sc = requests.get(url)
plain_text = sc.text
soup = BeautifulSoup(plain_text, 'lxml')
#print (plain_text)

for td in soup.findAll('td', {'class':'result_text'}):
	href = td.find('a')['href']
	movie_page = "http://imdb.com" + href
	break

source_code = requests.get(movie_page)
movie_name = get_title(source_code)
print (movie_name)
get_movie_data(source_code)