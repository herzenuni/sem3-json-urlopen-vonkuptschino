#python3 -m pytest test_api.py -v
from api import *
import pytest

def test_response():
	"""
	Checks the successfull server's answer
	"""
	re = "https://api.harvardartmuseums.org/color/34838442?apikey=ff686a00-e16c-11e7-a6c9-1fecfde3d500"
	assert str(response_get(re)) == '<Response [200]>'