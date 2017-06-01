import facebook
import json
from pprint import pprint
import requests

token = 'EAACEdEose0cBAHB6vMWk3gIMk5Q68gRUPNFXWjUi09iXWPLDEGZAPJZAcMexCiXN5j6sDDZBk1VtscOFUZCndgO3fUUWY9ak0yvUrBSLUOwZAVzoxoSOOdfQg905gNmw3MZBc7gTLr88FAqDZAaEARKMXvC1AiYnXZAqcHiZBIMogVoofgq1Q1rgRAZCB2ZBDbnzHwZD'
version = '2.7'

fanpage_url = 'https://www.facebook.com/TheNewsLens/?ref=br_rs'

graph = facebook.GraphAPI(access_token=token, version=version)
fanpage_id = graph.get_object(fanpage_url)['id']

all_posts_id = []
fanpage_posts = graph.get_connections(fanpage_id, 'posts')
while(True):
    try:
        for post in fanpage_posts['data']:
            all_posts_id.append(post['id'])
        #fanpage_posts = requests.get(fanpage_posts['paging']['next']).json()
        break
    except:
        #如果沒有paging無資料跳出
        break

users_thumb_up = []
for post_id in all_posts_id:
    likes = graph.get_connections(post_id, 'likes')
    pprint(likes)
