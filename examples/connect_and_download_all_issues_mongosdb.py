__author__ = 'James Veitch'

'''
Example to connect and download all issues on the remote server to a
running mongodb instance using pymongo http://api.mongodb.org/python/current/tutorial.html
'''

import sys

import pythreesixty.core.mobile as mobile
import pythreesixty.core.field.companies as companies
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

client = MongoClient('localhost', 27017)  # Create connection to server
db = client['test-database']
collections = ['issues', 'projects', 'companies']
try:
    for c in collections:
        print("dropping {0} collection from mongodb".format(c))
        db[c].drop()  # wipe/remove for testing
except ServerSelectionTimeoutError as e:
    print(e)
    print("unable to connect to server. check connection settings?")
    sys.exit(1)
except Exception as e:
    print(e)
    print("unable to drop {0} collection".format(c))
col_issues = db.issues
col_projects = db.projects
col_companies = db.companies


# Download header information and linked tables
print("\n\n===Downloading linked collections===")
companies_request = companies.companies()
print("Discovered {count} companies in masterdata".format(count=len(companies_request.json())))

for c in companies_request.json():
    print("{id}: {name}".format(
        id=c['id'],
        name=c['name'])
    )
    col_companies.insert(c)

print("Companies BSON collection contains {0} projects.".format(col_companies.count()))
#pprint(col_companies.find().sort('_id', DESCENDING).next())  # print the last one inserted

# Download all projects and associated issues
print("\n\n===Downloading projects and issues===")
projects_request = mobile.projects()
print("User has access to {count} projects".format(count=len(projects_request.json())))

for p in projects_request.json():
    print("\n{id}: {name}".format(
        id=p['project_id'],
        name=p['name'])
    )
    col_projects.insert(p)
    print("Projects BSON collection contains {0} projects.".format(col_projects.count()))
    # pprint(projects.find().sort('_id', DESCENDING).next())  # print the last one inserted

    # Get issues
    issues_request = mobile.get_issues(p['project_id'], count_only=True)  # use count_only to just return the number
    if issues_request.status_code == 200:
        print("  - {count} issues found.".format(count=issues_request.json()['count']))

    # Use upsert functionality?
    if issues_request.json()['count'] > 0:
        issues_list = mobile.get_issues(p['project_id']).json()
        # inject project_id as, weirdly, it isn't in the native data model
        for i in issues_list:
            i['project_id'] = p['project_id']
            i['project_name'] = p['name']
        col_issues.insert_many(issues_list)
        print("Issues BSON collection contains {0} issues.".format(col_issues.count()))
    else:
        print("No issues to insert")
    # pprint(issues.find().sort('_id', DESCENDING).next())  # print the last one inserted










