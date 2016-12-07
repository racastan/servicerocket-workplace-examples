import requests
import json

# Constants
GRAPH_URL_PREFIX = 'https://graph.facebook.com/'

access_token = ''
community_id = ''
impersonate_user_id = ''  # post as this user
group_to_post_to_id = ''  # post to this group
message_to_post = 'hello world'  # post this message
file_to_post = 'logo.png'


# Methods#

def buildHeader(access_token):
    return {'Authorization': 'Bearer ' + access_token}


def postToGroupWithFile(access_token):
    headers = buildHeader(access_token)
    result = requests.get(GRAPH_URL_PREFIX + impersonate_user_id + '?fields=impersonate_token', headers=headers)
    data = json.loads(result.text, result.encoding)
    impersonate_token = data["impersonate_token"]
    headers = buildHeader(impersonate_token)

    files = {'file': open(file_to_post, 'rb')}
    data = {
        "name": message_to_post
    }
    result = requests.post(GRAPH_URL_PREFIX + group_to_post_to_id + '/photos', headers=headers, files=files, data=data)

    return json.loads(result.text, result.encoding)


result = postToGroupWithFile(access_token)
print(result)
