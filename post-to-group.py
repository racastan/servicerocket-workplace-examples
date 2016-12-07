import requests
import json

# Constants
GRAPH_URL_PREFIX = 'https://graph.facebook.com/'

access_token = ''
community_id = ''
impersonate_user_id = ''  # post as this user
group_to_post_to_id = ''  # post to this group
message_to_post = 'hello world'  # post this message


# Methods#

def buildHeader(access_token):
    return {'Authorization': 'Bearer ' + access_token}


def postToGroup(access_token):
    headers = buildHeader(access_token)
    result = requests.get(GRAPH_URL_PREFIX + impersonate_user_id + '?fields=impersonate_token', headers=headers)
    data = json.loads(result.text, result.encoding)
    impersonate_token = data["impersonate_token"]
    headers = buildHeader(impersonate_token)

    data = {
        "message": message_to_post,
        "type": "status"
    }

    result = requests.post(GRAPH_URL_PREFIX + group_to_post_to_id + '/feed', headers=headers, data=data)
    return json.loads(result.text, result.encoding)


result = postToGroup(access_token)
print(result)
