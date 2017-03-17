import requests, json, sys
from bs4 import BeautifulSoup

# Print stats to console
# passed in the entire table of either the base or max
def print_stats(data, hero, stats):
	print(hero.upper() + " " +  stats)
	header = ["Rarity: ", "HP: ", "ATK: ", "SPD: ", "DEF: ", "RES: "]
	stat_counter = 0
	rarity_counter = 0
	# for each row of data in the table
	for row in data:
		# find all the <td> tags, which are the data
		# each table is split into the different rarity values
		table = data[rarity_counter].find_all("td")
		# for each header column
		for head in header:
			# print the header along with the data at i
			print(head + table[stat_counter].text)
			stat_counter+=1
		stat_counter=0	
		rarity_counter+=1
		print("--------------------")	

# Loop until quit
while True:
	hero = input("Hero Name: ")
	if (hero == "quit"):
		break
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
	# This gets all the <tr> tags in the base table
	try:
		base_rows = stats_tables[0].find_all("tr")
	except: 
		print(hero + " is not a vaild hero.")
		continue	
	# Only get the actual data, not the header
	base_stats = (base_rows[1:len(base_rows)])
	print("vvvvvvvvvvvvvvvvvvvv")
	print_stats(base_stats, hero, "BASE STATS")
	print("^^^^^^^^^^^^^^^^^^^^")
	print("vvvvvvvvvvvvvvvvvvvv")

	# This is for the max stats TABLE
	# This gets all the <tr> tags in the max table
	max_rows = stats_tables[1].find_all("tr")
	# Only get the actual data, not the header
	max_stats = (max_rows[1:len(max_rows)])
	print_stats(max_stats, hero, "MAX STATS")
	print("^^^^^^^^^^^^^^^^^^^^")
