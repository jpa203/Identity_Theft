import requests
import pandas as pd 
import re

client_id = '5udLMTOTkdhqWCJT8xWLzQ'

secret_key = 'Yq04cd67BN-u7k8KDRKw6f9Vi-gzHA'

auth = requests.auth.HTTPBasicAuth(client_id,secret_key)

data = {
    'grant_type': 'password',
    'username' : 'jazzopardi203',
    'password' : 'XXXX'

}

headers = {'User-Agent' : 'MyAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth = auth, data = data, headers = headers)
                    
token = res.json()['access_token']

headers['Authorization'] = f'bearer {token}'


res = requests.get('https://oauth.reddit.com/r/IdentityTheft/new', headers = headers, params ={'limit':'50'})

df = pd.DataFrame()

for post in res.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title' : post['data']['title'],
        'selftext':post['data']['selftext'],
        'upvote_ratio' : post['data']['upvote_ratio'],
        'url' : post['data']['url']
    }, ignore_index = True)
df = df.dropna()

for row in df.itertuples():
    print(row[2])
    print()
    print(row[3])
    print(row[5])
    print()
    print('----------------')
    print()
    
# 1) Execute code twice a day to find new posts and send me a notification via email / or a notification about child identity theft
