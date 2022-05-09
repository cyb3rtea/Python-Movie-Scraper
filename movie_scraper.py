from bs4 import BeautifulSoup
from time import sleep
import requests

# setting some constants
url = 'https://www.showboxmovies.net/'
line_break = '|-----------------------------------------------------------|'

# main function that is run
def main():
	print('requesting url:', url)
	# using requests to retrieve the webpage.
	page = requests.get(url).text
	sleep(0.5)

	print('parsing HTML...')
	# parsing the whole page with beautifulsoup
	page_html = BeautifulSoup(page, 'html.parser')
	sleep(0.5)

	print('Parsing for film name and quality...')
	# finding all instances of the classes that titles and qualities
	# 	that are children of.
	movies = page_html.find_all(class_="film-name")
	quality= page_html.find_all(class_="pick film-poster-quality")
	# parsing again due to datatype error.
	movies = BeautifulSoup(str(movies), 'html.parser')
	qualtiy= BeautifulSoup(str(quality), 'html.parser')
	sleep(0.5)

	print('creating lists to sort through...')
	# creating a list of all movies and qualities by splitting at every new line
	str(movies).split('\n')
	str(quality).split('\n')
	# these are the lists the final information will be stored in
	# a dictionary could've been used but the way the movie titles get parsed
	# 	makes this unecessarily complex
	list_movies = []
	list_quality= []
	sleep(0.5)

	print('sorting lists...')
	# loop through the whole list and only store the first 24
	# the first 24 are the trending movies. The following 24 are the trending shows
	for i,value in enumerate(quality):
		if i >= 24:
			continue
		else:
			value = BeautifulSoup(str(value), 'html.parser')
			value = value.text
			list_quality.append(value)

	# loop through the whole list and store the first 24
	# A slight difference in the splitting causes there to be an extra '-1' before every title
	for i,movie in enumerate(movies):
		if i >= 24*2:
			continue
		else:
			link_tag = movie.find('a')
			link_tag = BeautifulSoup(str(link_tag), 'html.parser')
			title = link_tag.text
			# the extra '-1' is handled here by ignoring it
			if title != '-1':
				list_movies.append(title)

	sleep(0.5)

	print('formatting output...')
	sleep(0.5)

	print('printing to screen...')
	print(line_break)
	# finally loop 24 times and display out to buffer
	# some odd formatting had to be done here to give a clean output
	for i in range(24):
		# this adds a space to make it the same length as 'CAM'
		if list_quality[i] == 'HD':
			list_quality[i] += ' '

		# this calculates extra spaces needed to tack onto the end of
		# 	the movies titles to make the line the same length every time
		extra_space = ''
		extra = (len(line_break)-9) - len(list_movies[i])
		for ind in range(extra):
			extra_space += ' '

		# printing out the formatted output
		print('| '+list_quality[i]+' | '+list_movies[i]+extra_space+'|')
		print(line_break)
		sleep(0.1)

# check if imported or not
# FALSE: continue as normal
# TRUE : print out small message and continue
if __name__ == '__main__':
	main()
else:
	print('Successfully imported movie_Scraper.py')
	print('Visit https://github.com/cyb3rtea/ for more interesting projects.\n\n')
	main()
