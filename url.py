from urllib.request import urlopen
import json
import pprint

request = "https://api.vk.com/method/users.get?user_ids=1,1264893,vonkuptschino&v=5.8&fields=status"
print('Final request: {}\n'.format(request))

try:
	request_api = urlopen(request)
	data = json.loads(request_api.read())
	pprint.pprint(data)
except:
	print('SSL: CERTIFICATE_VERIFY_FAILED')
