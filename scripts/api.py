import requests

#URL = 'http://localhost:5005/conversations/default/respond'
#PARAMS = {'query':'hi'}
#request = requests.get(url = URL, params = PARAMS)
#data = request.json()
#print(data)

URL = 'http://localhost:5005/conversations/default/tracker'
request = requests.get(url = URL)
data = request.json()
print(len(data))
print('-'*20)
print(data)
print('-'*20)
#print(data['events'][1]['parse_data']['intent'])
for e in data['events']:
    #print(e)
    if 'parse_data' in e:
        print(e['parse_data']['intent'])
        print('-'*50)
#for i in range(len(data)):
#    print(data['events'][i]['parse_data']['intent'])
