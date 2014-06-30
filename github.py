import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if len(argv) != 3:
	print "Usage: python github.py github-un github-pw"
	exit(1)

reposUrl = "https://api.github.com/users/%s/repos" % argv[1]
r = requests.get(reposUrl, auth=HTTPBasicAuth(argv[1], argv[2]))
repos = r.json()

items = [{"code_type": "personal",
		  "code_year": repo["created_at"],
		 "code_title": repo["name"],
		   "code_url": repo["html_url"],
   "code_description": repo["description"]
		  } for repo in repos]
			
print items
#print requests.put("https://student.people.co/api/candidate/profile/portfolio_code_projects", params={"items": items}, verify=False)
