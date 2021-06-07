#!/usr/local/bin/python3.9
# Get list of confluence keys and print total space count

from atlassian import Confluence

confluence = Confluence(
    url='https://<name>.atlassian.net',
    username="",
    password="",
    cloud=True)

groups = confluence.get_all_groups()
result = confluence.get_all_spaces(start=0, limit=500, expand=None, space_type='global')
#print(result)

spaces = result['results']

print(spaces)
i = 0
for space in spaces:
    key = space['key']
    i += 1
    print(key)
print(i)

