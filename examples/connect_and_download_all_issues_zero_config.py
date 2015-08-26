__author__ = 'James Veitch'

'''
Example to connect and download all issues on the remote server to a local cache nosql
database using UnQLite
'''

from unqlite import UnQLite
from pprint import pprint

import pythreesixty.core.mobile as mobile

db = UnQLite()  # Creates an in-memory database.
issues = db.collection('issues')
issues.create()  # Create the collection if it does not exist.

projects = mobile.projects()
print("User has access to {count} projects".format(count=len(projects.json())))

for p in projects.json():
    print("\n{id}: {name}".format(
        id=p['project_id'],
        name=p['name'])
    )

    # Get issues
    issues_request = mobile.get_issues(p['project_id'], count_only=True)  # use count_only to just return the number
    if issues_request.status_code == 200:
        print("  - {count} issues found.".format(count=issues_request.json()['count']))

    issues.store(mobile.get_issues(p['project_id']).json())
    print("Local cache contains {0} items.".format(db.__len__()))
    print("JSON collection contains {0} issues.".format(len(issues.all())))
    pprint(issues.fetch(issues.last_record_id()))










