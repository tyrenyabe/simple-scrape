import requests, json, sys
from bs4 import BeautifulSoup

def print_stats(data, hero, stats):
	print(hero + " " +  stats)
	header = ["Rarity: ", "HP: ", "ATK: ", "SPD: ", "DEF: ", "RES: "]
	stat_counter = 0
	rarity_counter = 0
	for row in data:
		table = data[rarity_counter].find_all("td")
		for head in header:
			print(head + table[stat_counter].text)
			stat_counter+=1
		stat_counter=0	
		rarity_counter+=1
		print("\n")	


hero = input("Hero Name:	")
url = ("https://feheroes.wiki/" + hero)
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

# This will always have 2 elements
# 0 is for base stats
# 1 is for max stats
stats_tables = soup.find_all("table", class_="wikitable default")


# This is for the base stats TABLE
# Base stats is separated in TABLE
# 0 = Rarity
# 1 = HP
# 2 = ATK
# 3 = SPD
# 4 = DEF
# 5 = RES
base_rows = stats_tables[0].find_all("tr")
# Only get the actual data, not the header
base_stats = (base_rows[1:len(base_rows)])
print_stats(base_stats, hero, "base stats")




# This is for the max stats TABLE
max_rows = stats_tables[1].find_all("tr")
# Only get the actual data, not the header
max_stats = (max_rows[1:len(max_rows)])
print_stats(max_stats, hero, "max stats")
