import requests

#fields_list must be a comma separated list of field names, see Facebook Graph API for more info
def get_facebook_node(facebook_node_id, fields_list, token):
    payload = {'fields' : fields_list, 'access_token': token}
    r = requests.get(facebook_graphs_api_base + "/" + facebook_node_id, payload)
    node_metadata = r.json()
    return node_metadata
    
#fields_list must be a comma separated list of field names, see Facebook Graph API for more info
def get_facebook_video(facebook_graphs_api_base, video_id, fields_list, token):
    payload = {'access_token': token, 'fields': fields_list}
    r = requests.get(facebook_graphs_api_base + "/" + video_id, payload)
    video_metadata = r.json()
    return video_metadata

def get_page_id(token, facebook_graphs_api_base, facebook_user_id, page_name):
    #100990405705357
    #Get page ID for page with given name
    request_payload = {'access_token': token}
    facebook_account_url = facebook_graphs_api_base + "/" + facebook_user_id + "/accounts"
    r = requests.get(facebook_account_url, request_payload)
    facebook_response = r.json()
    #print(facebook_response)

    #Look up the source URL for the actual video content
    for page_node in facebook_response['data']:
        #Get the page node ID where the page name is correct and print it out
        if page_node['name'] == page_name:
            return page_node['id']
    return ''


facebook_page_name = "Testing Sobo Apps"
facebook_user_id = "104636535334690"
facebook_access_token = "EAACwNOuFtmwBAAn2myjeGYIhVlc7JEOPpL6ZB58U8HmTP8VQbP1q6cgt8KCnLod1E1AZAj5qxjKPc85li2fLuha0XlzkrqcZBBZAZAIjoz8wDkIjCHBsbZBwZCkfEKLSbJjeRssvmZBif79ZAo2tRHc4PpU5maXVsZAi6PPA2gZBf5cKMBbFp1gS06SgQkLfOPkuKv8naGsqxZAf1oyqJF5UkgW4"
facebook_video_fields = "?fields=source"
facebook_graphs_api_base = "https://graph.facebook.com/v12.0/"
#sobo_page_id = get_page_id(facebook_access_token, facebook_graphs_api_base, facebook_user_id, facebook_page_name)
#print('Page ID for the page ' + facebook_page_name + ' is ' + sobo_page_id)
sobo_page_id = '100990405705357'
facebook_response = get_facebook_node(sobo_page_id + '/videos', '', facebook_access_token)
print(facebook_response)

#Look up the source URL for the actual video content
for video_node in facebook_response['data']:
    video_id = video_node['id']
    print('Found a video on the page. Video ID: ' + video_id)
    print(get_facebook_video(facebook_graphs_api_base, video_id, 'source', facebook_access_token))
