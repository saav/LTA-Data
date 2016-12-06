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
	path = '/ltaodataservice/TrafficIncidents?$skip='
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

	outfile = open('Traffic_Incidents.csv', 'w')
	writer = csv.writer(outfile)
	writer.writerow(['Latitude', 'Longitude', 'Message', 'Type'])
	for item in values:
		writer.writerow([item['Latitude'], item['Longitude'], 
				item['Message'], item['Type']])