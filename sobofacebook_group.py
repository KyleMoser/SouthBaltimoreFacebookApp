import requests

#fields_list must be a comma separated list of field names, see Facebook Graph API for more info
def get_facebook_node(facebook_node_id, fields_list, token):
    payload = {'fields' : fields_list, 'access_token': token}
    r = requests.get(facebook_graphs_api_base + "/" + facebook_node_id, payload)
    video_metadata = r.json()
    #print (video_metadata)
    return video_metadata['source']

facebook_test_group_url = "1776313662555626"
facebook_access_token = ""
facebook_video_fields = "?fields=source"
facebook_graphs_api_base = "https://graph.facebook.com/v12.0/"

#Get videos posted to the given group
request_payload = {'access_token': facebook_access_token}
facebook_videos_url = facebook_graphs_api_base + "/" + facebook_test_group_url + "/videos"
r = requests.get(facebook_videos_url, request_payload)
facebook_response = r.json()
print (facebook_response)

#Look up the source URL for the actual video content
for video_node in facebook_response['data']:
    print('Video ... \n\n')
    #Get the video node ID and look up the content
    video_url = get_facebook_node(video_node['id'], 'source', facebook_access_token)
    print(video_url)
    print('\n\n\n')

