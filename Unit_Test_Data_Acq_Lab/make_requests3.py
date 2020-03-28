import urllib.request
import urllib.parse
import json

#file_counter = 0
#offset_counter = 1
#while file_counter < 39


def check_int(x):
	return type(x) == int

def check_str(x):
	return type(x) == str

def check_page_end(file_counter, results_page, total_results):
	if file_counter != 0:
		page_end = (total_results/results_page)
		return page_end
	else:
		page_end = (total_results/results_page) -1
		return page_end

def get_save_info(results_page, total_results, header_token = 'ZdddCOPWbdpPiBCqGVZPuuniLYnxGkzI', file_counter = 0):

	file_counter = check_page_end(file_counter, results_page, total_results)
	offset_counter = 1

	if check_str(header_token) == str and check_int(file_counter) == int:

		headers = {'token': header_token}

		while file_counter < page_end:

			myurl = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit='+str(results_page)+'&' + 'offset=' + str(offset_counter)
			request = urllib.request.Request(myurl, headers = headers)
			file_path = './locations_'+str(file_counter)+'.json'

			with urllib.request.urlopen(request) as f:
				data = json.load(f)

				with open(file_path, 'w') as g:
					json.dump(data,g)

			file_counter += 1
			offset_counter += 1000

get_save_info(1000,38860)

