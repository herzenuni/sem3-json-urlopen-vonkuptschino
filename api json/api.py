import requests
import json
import pprint

def HarvardArtMuseumsAPI(req):
	"""
	Gets JSON by users API-request
	req:  string, the request started with https://api...
	"""
	try:
		request_api = requests.get(req)
		pprint.pprint(request_api.json())
	except requests.ConnectionError:
		print('SSL: CERTIFICATE_VERIFY_FAILED')

	except requests.HTTPError:
		print('An HTTP error occurred')

	except requests.ConnectTimeout:
		print('The request timed out while trying to connect to the remote server')

	except json.decoder.JSONDecodeError:
		print('Probably you are unauthorized')
def response_get(req):
	"""
	Gets server's response
	req:  string, the request started with https://api...
	"""
	return requests.request('GET', req)

if __name__ == "__main__":
	#my repsonal API-key: ff686a00-e16c-11e7-a6c9-1fecfde3d500 
	#to obtain your own: https://docs.google.com/forms/d/e/1FAIpQLSfkmEBqH76HLMMiCC-GPPnhcvHC9aJS86E32dOd0Z8MpY2rvQ/viewform
	request = "https://api.harvardartmuseums.org/color/34838442?apikey=ff686a00-e16c-11e7-a6c9-1fecfde3d500"
	print('Final request: {}\n'.format(request))
	HarvardArtMuseumsAPI(request)
	print(response_get(request))

