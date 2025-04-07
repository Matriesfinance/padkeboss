# Padke Boss - AI Chatbot

Padke Boss is an AI-powered chatbot that blends **Padke Boss's meme-style responses** with **ChatGPT's intelligent conversation skills**. It provides fun, meme-based responses, as well as deep knowledge for cryptocurrency predictions, astronomy, and cybersecurity.

## Requirements

- Python 3.8 or higher
- Flask for the web server
- OpenAI API Key

## Setup

1. Clone this repository or download the files:

    ```bash
    git clone https://github.com/padke-boss.git
    cd padke-boss
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set your **OpenAI API Key** in the `app.py` file:

    ```python
    openai.api_key = "YOUR_OPENAI_API_KEY"
    ```

## Running Locally

To run the application locally:

```bash
python app.py
