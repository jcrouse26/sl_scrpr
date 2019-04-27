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

	wind = soup.find("div", {"class":"sl-spot-forecast-summary__stat-container sl-spot-forecast-summary__stat-container--wind"})
	print(wind)
	wind_mph = wind.find("div", {"class":"sl-spot-forecast-summary__stat-reading"}).text
	print(wind_mph)
	wind_direction = wind.find("span", {"sl-reading-description"}).text



	# wind = wind_mph + " @ " + wind_direction ## hide until converting wind to json

	# This will make sense eventually
		# wind_info = {
		# 	"speed" : 
		# } ## 
	current_conditions.append(daily_swells)
	# current_conditions.append(wind) ## hide while testing wind

	print(current_conditions)
	# return jsonify(current_conditions)

retreive_location_data()
