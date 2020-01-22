import time
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

# url to grab from
my_url = 'https://store.steampowered.com/stats/'

# open connection / grab page
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()

# html parser
pagesoup = soup(page_html, "html.parser")

# grab each game
game = pagesoup.findAll('tr', {'class':"player_count_row"})

#create a csvfile
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = timestr+'.csv'
f = open(filename,'w')
headers = "game,current_players\n"
f.write(headers)

for mygame in game:
	name = mygame.a.next
	current = mygame.span.next

	#print out name + current players
	print("Game: " + name)
	print("Current players: " + current)

	#writen to file
	f.write(name + ',' + current.replace(",","") + "\n")

f.close()
