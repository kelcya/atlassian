#!/usr/local/bin/python3.9

from atlassian import Confluence

confluence = Confluence(
    url='https://<name>.atlassian.net',
    username="",
    password="",
    cloud=True)

result = confluence.get_all_spaces(start=0, limit=500, expand=None, space_type='global')
spaces = result['results']
group_name = "test_users"


# The following combinations of operation.key and operation.target values are valid for the operation object:

# Copy
# 'create': 'page', 'blogpost', 'comment', 'attachment'
# 'read': 'space'
# 'delete': 'page', 'blogpost', 'comment', 'attachment'
# 'export': 'space'
# 'administer': 'space'

for space in spaces:
    key = space['key']
    print(key)
    print("Adding", group_name)
    confluence.add_space_permissions(key, "group", group_name, "read", 'space' )
    confluence.add_space_permissions(key, "group", group_name, "create", 'page' )
    confluence.add_space_permissions(key, "group", group_name, "create", 'comment' )
    confluence.add_space_permissions(key, "group", group_name, "create", 'attachment' )
    confluence.add_space_permissions(key, "group", group_name, "create", 'blogpost' )
    confluence.add_space_permissions(key, "group", group_name, "export", 'space' )
    confluence.add_space_permissions(key, "group", group_name, "delete", 'page' )
