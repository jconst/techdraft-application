#!/usr/bin/env python

import requests, json, sys

# Returns the StackOverflow profile of the username.
# Returns None if the user does not exist.
def get_profile(username):
	query = {'site': 'stackoverflow', 'inname': username}
	r = requests.get('http://api.stackexchange.com/2.2/users/', params=query)
	try:
		result = r.json()
		result = result['items']
		result = [p for p in result if p['display_name'] == username]
	except KeyError:
		return None

	if (len(result) > 0):
		return result[0]
	return None

if __name__ == "__main__":
	if (len(sys.argv) > 1):
		print get_profile(sys.argv[1])