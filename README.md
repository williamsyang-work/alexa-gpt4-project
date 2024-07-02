# Alexa GPT-4 Integration

This project integrates Alexa with OpenAI's GPT-4 model, allowing users to interact with GPT-4 through Alexa voice commands.

## Features

- Handles Alexa requests and interfaces with OpenAI's GPT-4
- Text-to-speech functionality
- Error handling and logging
- Flask-based web server
- Configured for deployment on Google Cloud Platform

## Prerequisites

- Python 3.9
- An OpenAI API key
- An Alexa skill set up to work with this backend

## Installation

1. Clone the repository:
```
git clone [your-repo-url]
cd [your-repo-name]
```
2. Install the required packages:
```
pip3 install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_USER_API_KEY=your_openai_api_key_here
```

## Usage

To run the server locally:
```
python server.py
```

The server will start on `http://localhost:5000`.

## Deployment

This project is configured for deployment on Google Cloud Platform using App Engine. Make sure to update the `app.yaml` file with your specific configuration before deploying.

## Project Structure

- `server.py`: Main Flask application
- `helpers.py`: Utility functions for OpenAI API calls and text-to-speech
- `requirements.txt`: Python dependencies
- `app.yaml`: Google Cloud App Engine configuration

## Security Note

Ensure that you keep your API keys secure. Never commit them directly to version control. Use environment variables or secret management systems in production.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

Copyright (c) 2024 Jayden Crocker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.