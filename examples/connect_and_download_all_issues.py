__author__ = 'James Veitch'

import pythreesixty.core.mobile as mobile

projects = mobile.projects()
print("User has access to {count} projects".format(count=len(projects.json())))

for p in projects.json():
    print("\n{id}: {name}".format(
        id=p['project_id'],
        name=p['name'])
    )

    # Get issues
    issues = mobile.get_issues(p['project_id'], count_only=True)  # use count_only to just return the number
    if issues.status_code == 200:
        print("  - {count} issues found.".format(count=issues.json()['count']))









