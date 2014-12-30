import requests
import re
import json

# AIP Interactions viewer webservices by Asher

def search(arg):
	
	# Return nothing if client didn't pass in a locus parameter
	if not ('locus' in arg):
		return

	# Check for published
	if ('published' in arg):
		published = arg['published']
	else:
		published = "false"
	
	# Validate locus against a reqular expression
	locus = arg['locus']
	locus = locus.upper()
	p = re.compile('AT[1-5MC]G[0-9]{5,5}', re.IGNORECASE)
	if not p.search(locus):
		return

	# Validates published against a regular expression
	published = published.lower()
	p = re.compile('[true|false]', re.IGNORECASE)
	if not p.search(published):
		return

	# Make a request to the BAR server
	payload = {'locus': locus, 'published': published}
	r = requests.get("http://bar.utoronto.ca/webservices/aip/interactions/get_interactions.php", params=payload)

	# If it worked, print output
	if r.ok:
		return r.headers['Content-Type'], r.content
	else:
		return 'text/plaintext; charset=UTF-8', 'An error occurred on the remore server'

def list(arg):
	pass
