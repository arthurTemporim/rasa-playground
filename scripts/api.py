import requests

asks = ['hi', 'good', 'hi', 'bad', 'yes', 'hi', 'bad', 'no']
answers = []
answers_data = []

def sendMessage(message):
    URL = 'http://localhost:5005/conversations/default/respond'
    PARAMS = {'query':message}
    request = requests.get(url = URL, params = PARAMS)
    data = request.json()
    answers.append(data)

def get_data():
    URL = 'http://localhost:5005/conversations/default/tracker'
    request = requests.get(url = URL)
    data = request.json()
    #print(len(data))
    #print('-'*20)
    #print(data)
    #print('-'*20)
    for e in data['events']:
        if 'parse_data' in e:
            #print(e['parse_data']['intent'])
            #print('-'*50)
            answers_data.append(e['parse_data']['intent'])
    print(len(answers))
    i = 0
    for i in range(len(answers)):
        print(i)
        print('Ask:',asks[i])
        print('Answer:',answers[i][0]['text'])
        print(answers_data[i])
        i+=1
    #for i in range(len(data)):
    #    print(data['events'][i]['parse_data']['intent'])

for ask in asks:
    sendMessage(ask)
get_data()
