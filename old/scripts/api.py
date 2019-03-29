import requests
import simplejson as json

simplePath1 = ['hi', 'good']
simplePath2 = ['hi', 'bad', 'yes']
multiplePaths = ['hi', 'good', 'hi', 'bad', 'yes', 'hi', 'bad', 'no']

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
    return event_tracker

def print_confidence(event_tracker):
    i = 0
    for event in event_tracker:
        if 'Confidence' in event[0]:
            print(event)

def print_all_data(event_tracker):
    i = 0
    for event in event_tracker:
        print(event)

def send_multiple_messages(messages):
    for userMessage in messages:
        sendMessage(userMessage)

send_multiple_messages(simplePath2)
print_all_data(get_data())
