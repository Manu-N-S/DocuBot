import requests
import json

def test_ask_question():
    # URL of the Flask endpoint
    url = 'http://127.0.0.1:5000/ask_question'
    
    # Sample question to send in the POST request
    sample_question = {
        'question': 'What is the total amount of the invoice?'
    }

    # Headers for the POST request
    headers = {
        'Content-Type': 'application/json'
    }

    # Sending POST request to the Flask endpoint
    response = requests.post(url, headers=headers, data=json.dumps(sample_question))

    # Checking if the request was successful
    if response.status_code == 200:
        print('Response:', response.json())
    else:
        print('Failed to get response. Status code:', response.status_code)

if __name__ == '__main__':
    test_ask_question()
