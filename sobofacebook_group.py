"""
Get a list of video links posted to the facebook group and email the links
"""
import requests
import sns_mail

facebook_test_group_url = "1776313662555626"
facebook_access_token = ""
facebook_video_fields = "?fields=source"
facebook_graphs_api_base = "https://graph.facebook.com/v12.0/"

def get_facebook_node(facebook_node_id, fields_list, token):
    """ Gets a video node URL
        fields_list : string
            comma separated list of field names"""
    payload = {'fields' : fields_list, 'access_token': token}
    r = requests.get(facebook_graphs_api_base + "/" + facebook_node_id, payload)
    video_metadata = r.json()
    #print (video_metadata)
    return video_metadata['source']

def get_videos():
    videos = []
    """Get videos posted to the given group"""
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
        videos.append(video_url)

    return videos

def main():
    """Get a video list from the FB group and email to the group admin"""
    vids = get_videos()
    #Test group for this app. Will be changed to real group app owner installs on.
    sns_mail.send_sns('TestSouthBaltimoreApp', 90, vids)

if __name__ == '__main__':
    main()
