from bs4 import BeautifulSoup
from flask import jsonify
import requests

def retreive_location_data():

	# set url destination
	url =  "https://www.surfline.com/surf-report/princeton-jetty/5842041f4e65fad6a7708970"

	# request and initialize BeautifulSoup
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')
	
    # find swells
	swells = soup.find("div", {"class":"sl-spot-forecast-summary__stat-swells" })

	daily_swells = []
	current_conditions = []

	for swell in swells:
        
        # remove all unicode spaces
		swell_text = swell.text.replace(u'\xa0', " ")
		
        # set attributes based on array position
		height = float(swell_text.split("FT")[0])
		period = int(swell_text.split(" ")[2].split('s')[0])
		direction = swell_text.split(" ")[3]
		angle = swell_text.split(" ")[4].replace(u'\u00ba',"")
		
        # create dictionary with attributes
		swell_info = {
			"height" : height,
			"period" : period,
			"direction" : direction,
			"angle" : angle
		}
		
        # append dictionary
		daily_swells.append(swell_info)

	wind_html = soup.find("div", {"class":"sl-spot-forecast-summary__stat-container sl-spot-forecast-summary__stat-container--wind"})
	wind_speed_kts = wind_html.find("div", {"class":"sl-spot-forecast-summary__stat-reading"}).text.split('K')[0]
	wind_speed_mph = int(wind_speed_kts) * 1.151

	wind_direction = wind_html.find("span", {"sl-reading-description"}).text.split(' ')[0]
	wind_angle = wind_html.find("span", {"sl-reading-description"}).text.split(' ')[1]



	# wind = wind_speed + " @ " + wind_direction ## hide until converting wind to json

	# This will make sense eventually
	wind = {
		"speed" : wind_speed_mph,
		"direction" : wind_direction,
		"angle" : wind_angle
	} 

	current_conditions.append(daily_swells)
	current_conditions.append(wind) ## hide while testing wind

	# print(current_conditions)
	# return jsonify(current_conditions)

retreive_location_data()
