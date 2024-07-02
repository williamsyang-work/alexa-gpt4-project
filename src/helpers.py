import logging
import requests
import pyttsx3

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Replace with your OpenAI API key
OPENAI_USER_API_KEY = os.getenv('OPENAI_USER_API_KEY')
OPENAI_API_ENDPOINT = os.getenv('OPENAI_API_ENDPOINT')

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def call_openai_gpt(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_USER_API_KEY}',
    }
    data = {
        'model': 'gpt-4',
        'messages': [
            {
                'role': 'user',
                'content': prompt
            }
        ]
    }
    response = requests.post(OPENAI_API_ENDPOINT, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        logging.error(f"Error calling OpenAI API: {response.status_code} - {response.text}")
        return f"Error: {response.status_code} - {response.text}. Please check your API key and endpoint."