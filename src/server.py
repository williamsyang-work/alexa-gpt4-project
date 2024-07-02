import logging
from flask import Flask, request, jsonify
from utils import call_openai_gpt

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/alexa', methods=['POST'])
def alexa_handler():
    data = request.json
    logging.debug(f"Incoming request data: {data}")

    try:
        if 'request' in data and 'intent' in data['request']:
            user_input = data['request']['intent']['slots']['UserInput']['value']
            logging.info(f"Received user input: {user_input}")

            response = call_openai_gpt(user_input)
            logging.info(f"Generated response from OpenAI: {response}")

            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": response
                    },
                    "shouldEndSession": True
                }
            })
        else:
            logging.warning("Invalid request format received from Alexa.")
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "Error: No input received from Alexa."
                    },
                    "shouldEndSession": True
                }
            })
    except Exception as e:
        logging.error(f"Exception occurred: {str(e)}")
        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": f"Error processing request: {str(e)}"
                },
                "shouldEndSession": True
            }
        })

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Alexa GPT-4 Integration!"

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Not Found",
        "message": "The requested URL was not found on the server."
    }), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)