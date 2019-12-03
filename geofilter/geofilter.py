import requests
import json
import numpy as np
import math

def get_longlat(address):
	app_id = "OR6FyfZdhpelfb3DoorF"
	app_code = "1cREog5jCDNeYVTjNxBN0A"
	#app_id = "devportal-demo-20180625"
	#app_code = "9v2BkviRwi9Ot26kp2IysQ"

	here_api = "https://geocoder.api.here.com/6.2/geocode.json?app_id={id}&app_code={code}&searchtext={add}"
	url = here_api.format(id = app_id, code = app_code, add= address)
	response = requests.get(url)

	#print('Status of fetching latitude/longtitude: ', response)
	result_data = response.json()["Response"]["View"][0]["Result"][0]["Location"]

	latitude = result_data["DisplayPosition"]["Latitude"]
	longitude = result_data["DisplayPosition"]["Longitude"]

	print("address: ", address)
	print("latitude: {} Longtitude {}".format(latitude, longitude))

	return latitude, longitude


def longlat_filter_bone(diameter = 0.5, width = 0.3, start_lat, start_long, end_lat, end_long, sample_lat, sample_long):
	#set conversion parameter from mile to convert lat/long degree
	# 1 degree of latitude = 69 miles, 1 mile =  0.0145
	# longitude is vary based on the latitude (69.172 miles to 0)
	ave_lat = (start_lat + end_lat) / 2
	mile_long = 1 / (69.172 * np.cos(np.radians(ave_lat)))
	mile_latlong_ave = (1/69.172+mile_long)/2

	#print("mile_long: ", mile_long, "average: ", mile_latlong_ave)

	in_range = False

	#determine if sample point is within the diameter of start or end point
	degree_diameter = diameter*mile_latlong_ave
	if (((sample_lat - start_lat)**2 + (sample_long - start_long) ** 2 - degree_diameter ** 2) < 0 ):
		in_range = True
	elif (((sample_lat - end_lat)**2 + (sample_long - end_long) ** 2 - degree_diameter ** 2) < 0 ):
		in_range = True

	#determine if sample point is within the rectangle from start to end with the width
	theta = np.arctan2(end_lat - start_lat, end_long - start_long)
	rect_angle = np.pi/2 - abs(theta)

	#print("theta {}, rect_angle {}".format(theta, rect_angle))

	#set rectangle area
	degree_width = width * mile_latlong_ave

	dx = np.cos(rect_angle) * degree_width
	dy = np.sin(rect_angle) * degree_width

	contour = []
	contour.append([start_long + dx, start_lat + dy])
	contour.append([start_long - dx, start_lat - dy])
	contour.append([end_long + dx, end_lat + dy])
	contour.append([end_long - dx, end_lat - dy])

	contour_array = np.array(contour)
	#print("contour: ", contour_array)

	contour_array[:,0] = contour_array[:,0] - sample_long
	contour_array[:,1] = contour_array[:,1] - sample_lat
	contour_flag = contour_array.max(axis=0) * contour_array.min(axis=0)

	#print("contour: ", contour_array)
	#print("contour_flag: ", contour_flag)

	if (contour_flag[0] < 0 and contour_flag[1] <0):
		in_range = True

	return in_range

def main(s_address, d_address):
	s_lat, s_long = get_longlat(s_address)
	d_lat, d_long = get_longlat(d_address)

	return s_lat, s_long, d_lat, d_long


if __name__ == "__main__":
	start_address = "200 S Mathilda Ave, Sunnyvale, CA"
	desti_address = "2624 Homestead Rd, Santa Clara, CA"
	start_lat, start_long, end_lat, end_long = main(start_address, desti_address)

	# print("Start point latitude: {} Start point Longtitude: {}, End point latitude: {} End point Longtitude: {}".format(start_lat, start_long, end_lat, end_long))

	# start_lat = 37.37634
	# start_long = -122.03405
	# end_lat = 37.3394801
	# end_long = -121.9727751

	#in sample
	sample_lat = 37.35791005
	sample_long = -122.00341255000001

	#out sample1
	#sample_lat = 37.38534
	#sample_long = -122.04305

	#set parameter for bone shapefilter (in mile)
	diameter = 0.5
	width = 0.3

	flag = longlat_filter_bone(diameter, width, start_lat, start_long, end_lat, end_long, sample_lat, sample_long)
	print("Sample spot location latitude {}, longitude {}".format(sample_lat, sample_long))
	print("Sample spot in the area? ", flag)
