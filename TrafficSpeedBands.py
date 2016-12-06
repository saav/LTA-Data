import json
import csv
import urllib
from urlparse import urlparse
import httplib2 as http #External library

if __name__=="__main__":
	#Authentication parameters
	headers = { 'AccountKey' : 'pqFCtMHrTYebgu64z2fYnA==',
	'UniqueUserID' : 'bc98369c-940b-4fe0-aba8-cb0ff926ba38',
	'accept' : 'application/json'} #Request results in JSON

	#API parameters
	uri = 'http://datamall2.mytransport.sg/' #Resource URL
	path = '/ltaodataservice/TrafficSpeedBands?$skip='
	count = 0
	values = []

	while True:
		#Build query string & specify type of API call
		target = urlparse(uri + path + str(count))
		print target.geturl()
		method = 'GET'
		body = ''

		#Get handle to http
		h = http.Http()
		#Obtain results
		response, content = h.request(
		target.geturl(),
		method,
		body,
		headers)

		#Parse JSON to print
		jsonObj = json.loads(content)
		value = jsonObj['value']
		values.extend(value)
		if not value:
			break
		else:
			count = count + 50

	outfile = open('Traffic_Speed_Bands.csv', 'w')
	writer = csv.writer(outfile)
	writer.writerow(['LinkID', 'Location', 'MaximumSpeed', 'MinimumSpeed', 'RoadCategory', 'RoadName', 'SpeedBand'])
	for item in values:
		writer.writerow([item['LinkID'], item['Location'], 
				item['MaximumSpeed'], item['MinimumSpeed'],
				item['RoadCategory'], item['RoadName'], item['SpeedBand']])