from bs4 import BeautifulSoup
import requests
from time import sleep

url = 'https://www.showboxmovies.net/'
line_break = '|-----------------------------------------------------------|'

def main():
	print('requesting url:', url)
	page = requests.get(url).text
	sleep(0.5)

	print('parsing HTML...')
	page_html = BeautifulSoup(page, 'html.parser')
	sleep(0.5)

	print('Parsing for film name and quality...')
	movies = page_html.find_all(class_="film-name")
	quality= page_html.find_all(class_="pick film-poster-quality")
	movies = BeautifulSoup(str(movies), 'html.parser')
	qualtiy= BeautifulSoup(str(quality), 'html.parser')
	sleep(0.5)


	print('creating lists to sort through...')
	str(movies).split('\n')
	str(quality).split('\n')
	list_movies = []
	list_quality= []
	sleep(0.5)

	print('sorting lists...')
	for i,value in enumerate(quality):
		if i >= 24:
			continue
		else:
			value = BeautifulSoup(str(value), 'html.parser')
			value = value.text
			list_quality.append(value)

	for i,movie in enumerate(movies):
		if i >= 24*2:
			continue
		else:
			link_tag = movie.find('a')
			link_tag = BeautifulSoup(str(link_tag), 'html.parser')
			title = link_tag.text
			if title != '-1':
				list_movies.append(title)

	sleep(0.5)

	print('formatting output...')
	sleep(0.5)

	print('printing to screen...')
	print(line_break)
	for i in range(24):
		if list_quality[i] == 'HD':
			list_quality[i] += ' '

		extra_space = ''
		extra = (len(line_break)-9) - len(list_movies[i])

		for ind in range(extra):
			extra_space += ' '

		print('| '+list_quality[i]+' | '+list_movies[i]+extra_space+'|')
		print(line_break)
		sleep(0.1)

if __name__ == '__main__':
	main()
else:
	print('Successfully imported movie_Scraper.py')
	print('Visit https://github.com/cyb3rtea/ for more interesting projects.\n\n')