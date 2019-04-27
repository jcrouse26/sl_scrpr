from bs4 import BeautifulSoup
import requests

def retreive_location_data():

	## for projections
	url =  "https://www.surfline.com/surf-report/princeton-jetty/5842041f4e65fad6a7708970"

	source = requests.get(url).text

	soup = BeautifulSoup(source, 'lxml')

	swells = soup.find("div", {"class":"sl-spot-forecast-summary__stat-swells" })

	daily_swells = []
	current_conditions = []

	for swell in swells:
		# swell_info = {"text" : swell.text}
		swell_text = swell.text.replace(u'\xa0', " ")
		# \xa0at\xa0
		# {'height': '1.4FT\xa0at\xa015s SSW 205º', 'period': '', 'direction': '', 'angle': ''}

		height = float(swell_text.split("FT")[0])
		period = int(swell_text.split(" ")[2].split('s')[0])
		direction = swell_text.split(" ")[3]
		angle = swell_text.split(" ")[4]

		swell_info = {
			"height" : height,
			"period" : period,
			"direction" : direction,
			"angle" : angle
		}
		
		daily_swells.append(swell_info)

	wind = soup.find("div", {"class":"sl-spot-forecast-summary__stat-container sl-spot-forecast-summary__stat-container--wind"})
	wind_mph = wind.find("div", {"class":"sl-spot-forecast-summary__stat-reading"}).text
	wind_direction = wind.find("span", {"sl-reading-description"}).text

	wind = wind_mph + " @ " + wind_direction

	current_conditions.append(daily_swells)
	current_conditions.append(wind)

	print current_conditions
	return current_conditions


retreive_location_data()
	

# 	info_table = soup.find('div', {'class':'players'})
# 	players_list = info_table.find('tbody')

# 	players = players_list.find_all('tr')

# 	for player in players:
# 		player_info = player.find_all('td')[1]
# 		player_name = player_info.find('div', {'class':'ysf-player-name Nowrap Grid-u Relative Lh-xs Ta-start'}).text
# 		points = player.find_all('td')[7].find('div').text
# 		print player_name, points
# 		csv_writer.writerow([player_name, points])

# csv_file.close()