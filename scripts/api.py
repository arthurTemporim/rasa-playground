import requests
import simplejson as json

userMessages = ['hi', 'good', 'hi', 'bad', 'yes', 'hi', 'bad', 'no']

def sendMessage(message):
    URL = 'http://localhost:5005/conversations/default/respond'
    PARAMS = {'query':message}
    request = requests.get(url = URL, params = PARAMS)
    return request.json()

def get_data():
    URL = 'http://localhost:5005/conversations/default/tracker'
    request = requests.get(url = URL)
    data = request.json()
    #print(json.dumps(data, indent=4, sort_keys=True))
    event_tracker = []
    for e in data['events']:
        if 'event' in e:
            if 'action' in e['event']:
                event_tracker.append(['Utter: ', e['name']])
        if 'parse_data' in e:
            event_tracker.append(['User Message: ', e['text']])
            event_tracker.append(['Intent: ', e['parse_data']['intent']['name']])
            event_tracker.append(['Confidence: ', e['parse_data']['intent']['confidence']])
            event_tracker.append('-'*50)
    i = 0
    print('-'*50)
    for event in event_tracker:
        print(event)

for userMessage in userMessages:
    sendMessage(userMessage)

get_data()
