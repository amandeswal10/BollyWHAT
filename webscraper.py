import bs4
import requests
import re
from collections import defaultdict


# html saved as a txt file
gow = requests.get("https://www.imdb.com/title/tt1954470/trivia?ref_=tt_trv_trv")
sholay = requests.get("https://www.imdb.com/title/tt0073707/trivia?ref_=tt_trv_trv")
pst = requests.get("https://www.imdb.com/title/tt1620933/trivia?ref_=tt_trv_trv")
omkara = requests.get("https://www.imdb.com/title/tt0488414/trivia?ref_=tt_trv_trv")




# using beautiful soup to parse that html
gow_soup = bs4.BeautifulSoup(gow.text, 'html.parser')
sholay_soup = bs4.BeautifulSoup(sholay.text,'html.parser')
pst_soup = bs4.BeautifulSoup(pst.text, 'html.parser')
omkara_soup = bs4.BeautifulSoup(omkara.text, 'html.parser')


# finding all the trivias on the page by using the same class
gow_trivia = gow_soup.findAll('div', class_='sodatext')
sholay_trivia = sholay_soup.findAll('div', class_='sodatext')
pst_trivia = pst_soup.findAll('div', class_='sodatext')
omkara_trivia = omkara_soup.findAll('div', class_='sodatext')


# make the trivias look better and readable by separating with a next line
num_of_gow_trivias = len(gow_trivia)
gow_regex = re.compile(r'(g|G)angs (o|O)f (w|W)asseypur')
for i in range(num_of_gow_trivias):
    gow_trivia[i] = gow_trivia[i].text.strip()
    gow_trivia[i] = gow_regex.sub('G**** O* W********', gow_trivia[i])

num_of_sholay_trivias = len(sholay_trivia)
sholay_regex = re.compile(r'(s|S)holay')
for i in range(num_of_sholay_trivias):
    sholay_trivia[i] = sholay_trivia[i].text.strip()
    sholay_trivia[i] = sholay_regex.sub('S****', sholay_trivia[i])

num_of_pst_trivias = len(pst_trivia)
pst_regex = re.compile(r'(p|P)aan (s|S)ingh (t|T)omar')
for i in range(num_of_pst_trivias):
    pst_trivia[i] = pst_trivia[i].text.strip()
    pst_trivia[i] = pst_regex.sub('P*** S**** T****', pst_trivia[i])

num_of_omkara_trivias = len(omkara_trivia)
omkara_regex = re.compile(r'(o|O)mkaara')
for i in range(num_of_omkara_trivias):
    omkara_trivia[i] = omkara_trivia[i].text.strip()
    omkara_trivia[i] = omkara_regex.sub('O*****', omkara_trivia[i])


# finding the movie n making it look more readable
gow_movie = gow_soup.select('#main > div.article.listo > div.subpage_title_block > div > div > h3 > a')
gow_movie = gow_movie[0].text.strip()
gow_movie = gow_movie.upper()

sholay_movie = sholay_soup.select('#main > div.article.listo > div.subpage_title_block > div > div > h3 > a')
sholay_movie = sholay_movie[0].text.strip()
sholay_movie = sholay_movie.upper()

pst_movie = pst_soup.select('#main > div.article.listo > div.subpage_title_block > div > div > h3 > a')
pst_movie = pst_movie[0].text.strip()
pst_movie = pst_movie.upper()

omkara_movie = omkara_soup.select('#main > div.article.listo > div.subpage_title_block > div > div > h3 > a')
omkara_movie = omkara_movie[0].text.strip()
omkara_movie = omkara_movie.upper()


# creating a list of the movie object(according to no. of trivias) since there is only one movie
gow_movie = [gow_movie]*num_of_gow_trivias
sholay_movie = [sholay_movie]*num_of_sholay_trivias
pst_movie = [pst_movie]*num_of_pst_trivias
omkara_movie = [omkara_movie]*num_of_omkara_trivias

# combine trivia and movie together in the form of a dictionary
gow_trivias = {}
gow_trivias = dict(zip(gow_trivia,gow_movie))

sholay_trivias = {}
sholay_trivias = dict(zip(sholay_trivia,sholay_movie))

pst_trivias = {}
pst_trivias = dict(zip(pst_trivia,pst_movie))

omkara_trivias = {}
omkara_trivias = dict(zip(omkara_trivia,omkara_movie))

# combining all the individual movies to one dictionary
action_trivias = {**gow_trivias, **sholay_trivias, **pst_trivias, **omkara_trivias}








#trivia_file = open('/users/amandeswal/desktop/trivias.txt', 'w')
#trivia_file.write(str(trivia))
#trivia_file.close()





