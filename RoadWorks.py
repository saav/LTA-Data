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
	path = '/ltaodataservice/RoadWorks?$skip='
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

	outfile = open('Road_Works.csv', 'w')
	writer = csv.writer(outfile)
	writer.writerow(['EndDate', 'EventID', 'Other', 'RoadName', 'StartDate', 'SvcDept'])
	for item in values:
		writer.writerow([item['EndDate'], item['EventID'],
		 	item['Other'], item['RoadName'], 
		 	item['StartDate'], item['SvcDept']])