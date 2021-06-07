#!/usr/local/bin/python3.9

from atlassian import Confluence

confluence = Confluence(
    url='https://<name>.atlassian.net',
    username="",
    password="",
    cloud=True)

result = confluence.get_all_spaces(start=0, limit=500, expand=None, space_type='global')

spaces = result['results']
# loop through each space to get the key and space permissions
for space in spaces:
    group_names = []
    key = space['key']
    print(key)
    space_info = confluence.get_space(key, expand="permissions")
    permissions = space_info['permissions']
    # check if subject is a group (not user) and append group name into a list
    for perm in permissions:
        if 'subjects' in perm:
            subjects = perm['subjects']
            if 'group' in subjects:
                group_info = subjects['group']['results'][0]
                group_names.append(group_info['name'])
    print(sorted(set(group_names)))
