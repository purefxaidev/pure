# PUREFXAI Chat Bot

This project is a web-based chatbot designed to teach users about data analysis, gold trading, and Forex. It features a modern, dark-themed interface and a Python-based backend with AI integration.

## Project Structure

```
.
├── frontend/
│   ├── index.html       # The main HTML file for the chat interface
│   ├── styles.css       # CSS for styling the chatbot
│   └── script.js        # JavaScript for frontend logic and API calls
├── backend/
│   ├── app.py           # Flask backend server
│   └── requirements.txt # Python dependencies
└── README.md            # This file
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install backend dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment (optional but recommended)
    python3 -m venv venv
    source venv/bin/activate

    # Install the required packages
    pip install -r backend/requirements.txt
    ```

## Running the Application for Development

1.  **Set the AI API Key:**
    The backend is designed to work with an AI service like OpenAI. For security, the API key should be set as an environment variable.

    On Linux/macOS:
    ```bash
    export OPENAI_API_KEY='your_actual_api_key'
    ```
    On Windows:
    ```bash
    set OPENAI_API_KEY='your_actual_api_key'
    ```
    *Note: The current implementation in `backend/app.py` uses a mock AI for demonstration purposes. To connect to a real AI, you will need to uncomment the API call logic in the `get_ai_response` function and use a valid API key.*

2.  **Start the backend server:**
    ```bash
    python3 backend/app.py
    ```
    The server will start on `http://localhost:5000`.

3.  **Open the chatbot in your browser:**
    Open the `frontend/index.html` file directly in your web browser. You can do this by right-clicking the file and choosing "Open with" your favorite browser, or by navigating to it via the `file:///` protocol. The application will connect to the backend server running on `localhost`.

## Deployment

For production, it is not recommended to use the Flask development server. Instead, use a production-ready WSGI server like Gunicorn or uWSGI.

Example with Gunicorn:
```bash
# Install Gunicorn
pip install gunicorn

# Run the app with Gunicorn
gunicorn --bind 0.0.0.0:8000 backend.app:app
```
You would also typically run this behind a reverse proxy like Nginx or Apache to handle static file serving, SSL termination, and load balancing. The frontend files (`index.html`, `styles.css`, `script.js`) should be served by this reverse proxy for better performance.
