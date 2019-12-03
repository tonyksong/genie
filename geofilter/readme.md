[How it works?]
 Get start and end address from user input, then create filtered are based on start/end point and diameter/width parameter.
 Determine if each point is within the filtered area or not.

[Each function]
  get_longlat()
    This function called by main
  	INPUT: address
  	OUTPUT: latitude, longitude

  main()
    INPUT: start_address, end_address
    OUTPUT: start_latitude, start_longitude, end_latitude, end_longitude

  longlat_filter_bone()
    INPUT: diameter, width, start_latitude, start_longitude, end_latitude, end_longitude, sample_point_latitude, sample_point_longitude
    OUTPUT: True/False

    diameter (in mile) = search radius around start/end point, default = 0.5
    width (in mile) = width of rectangle area between start/end point, default = 0.3
    This function create "bone shape" area between start/end address and determine if sample point is within that range or not.

[Example implementation]
	#1: convert start/end address to latitude/longitude 
	#2: create list of recommendations in df or csv format and sort in the preffered order
	#3: For each items in the list apply longlat_filter_bone(), if True save it to "filtered_list", if False move next
	#4: Pass items in "filtered_list" for later process
