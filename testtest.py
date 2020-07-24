import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

activites_url = "https://www.strava.com/api/v3/athlete/activities"
auth_url = 'https://www.strava.com/oauth/token'

payload = {
    'client_id': "50903",
    'client_secret': 'e47ee1f8b3dbfb7a188d09bddaebaca729dce3dd',
    'refresh_token': '9b219b30280f1521ca1696d6aa0f72c062fce02a',
    'grant_type': "refresh_token",
    'f': 'json'}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token ={}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

print(my_dataset[0:])
print(my_dataset[1]["name"])
print(my_dataset[2]["name"])


