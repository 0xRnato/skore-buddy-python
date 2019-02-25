import uuid
import json
import requests

def jobs(request_data):
    url = 'https://api.recruitee.com/c/skore/careers/offers'
    response = requests.get(url)
    json_response = response.json()

    data = {}
    data['fulfillmentText'] = request_data['queryResult']['fulfillmentText']
    data['fulfillmentMessages'] = request_data['queryResult']['fulfillmentMessages']

    for job in json_response['offers']:
        data['fulfillmentMessages'].append({
            'card': {
                'title': job['title'],
                'subtitle': job['location'],
                'buttons': [{
                    'text': 'Mais detalhes',
                    'postback': job['careers_url'],
                }]
            }
        })

    return data


def about(request_data):
    url = 'https://knowledge.skore.io/workspace/v2/spaces/34137/contents'
    headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoX3Rva2VuIjoiNWlXNVdONDEzX2pSY2UtZFhfNHNsZyJ9.X8_Oz7cNsRnA42Lz0pH_X3VO-Sr3DUJsMW69O_nqqBA' }
    response = requests.get(url, headers=headers)
    json_response = response.json()

    data = {}
    data['fulfillmentText'] = request_data['queryResult']['fulfillmentText']
    data['fulfillmentMessages'] = request_data['queryResult']['fulfillmentMessages']

    for content in json_response['results']:
        data['fulfillmentMessages'].append({
            'card': {
                'title': content['name'],
                'subtitle': content['space']['name'],
                'imageUri': content['thumb_url'],
            }
        })

    return data


def get_service(intent_name):
    if intent_name == "jobs":
        return jobs
    elif intent_name == "about":
        return about

def process_text(text):
    session_id = str(uuid.uuid4())
    url = 'https://api.dialogflow.com/v1/query?v=20170712'
    headers = {
        'Authorization': 'Bearer 84601946e48342c0a530894f84c76a2d',
        'Content-Type': 'application/json'
    }
    data = {}
    data['lang'] = 'pt-BR'
    data['query'] = text
    data['sessionId'] = session_id
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

