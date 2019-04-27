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
	
	# eventual JSON object to return
	current_conditions = {
		"swells" : {
			"swell_1" : {
				"height" : 0,
				"period" : 0,
				"direction" : 0,
				"angle" : 0
			},
			"swell_2" : {},
			"swell_3" : {}
		},
		"wind" : {
			"speed" : 0,
			"angle" : 0
		}
	}

	# start index at 1 so first swell is called "swell_1"
	index = 1

	# set daily_conditions["swells"]
	for swell in swells:
        
        # remove all unicode spaces
		swell_text = swell.text.replace(u'\xa0', " ")
		
        # define swell attributes from the html
		height = float(swell_text.split("FT")[0])
		period = int(swell_text.split(" ")[2].split('s')[0])
		direction = swell_text.split(" ")[3]
		angle = swell_text.split(" ")[4].replace(u'\u00ba',"")
		
        # update value for key at swell index
		current_conditions["swells"]["swell_" + str(index)] = {
			"height" : height,
			"period" : period,
			"direction" : direction,
			"angle" : angle,
		}
		index += 1

	# set daily_conditions["wind"]
	wind_html = soup.find("div", {"class":"sl-spot-forecast-summary__stat-container sl-spot-forecast-summary__stat-container--wind"})
	wind_speed_kts = wind_html.find("div", {"class":"sl-spot-forecast-summary__stat-reading"}).text.split('K')[0]
	wind_speed_mph = int(wind_speed_kts) * 1.151
	wind_angle = int(wind_html.find("span", {"sl-reading-description"}).text.split(' ')[1].split(u'\xb0')[0].split('(')[1])
	# wind_direction = wind_html.find("span", {"sl-reading-description"}).text.split(' ')[0]

	current_conditions["wind"]["speed"] = wind_speed_mph
	current_conditions["wind"]["angle"] = wind_angle

	print(current_conditions)
	# return jsonify(current_conditions)

retreive_location_data()
