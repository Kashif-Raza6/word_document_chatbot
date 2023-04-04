
Health Chatbot Flask API
========================

This is a Flask API for a  chatbot that uses OpenAI to provide responses to user queries. This API is intended to be used by clients who want to integrate the chatbot functionality into their own website or application.

Installation
------------


1.  Create a virtual environment and activate it:
    

###
    
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
    
2.  Install the required dependencies:
    
    `pip install -r requirements.txt`
    

Usage
-----

To run the Flask app, navigate to the project directory and run the following command:

`python app.py`

This will start the Flask app on `http://localhost:5000`.

### API endpoints

The following endpoints are available for interacting with the health chatbot:

#### `POST /query`

This endpoint takes a user query as input and returns a response from the chatbot.

**Request parameters**


| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| query | Yes | String | The user's query to the chatbot. |


**Response**

If the request is successful, the response will be a JSON object with the following format:

json

```json
{
    "result": "The chatbot's response."
}
```

If there is an error with the request, the response will be a JSON object with the following format:

json

```json
{
    "error": "The error message."
}
```

#### `GET /`

This endpoint returns the login page for the chatbot.

#### `POST /login`

This endpoint handles user authentication and returns the chatbot's main page.

**Request parameters**


| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| username | Yes | String | The user's username for authentication. |
| password | Yes | String | The user's password for authentication. |


Security
--------

This API requires basic authentication to access the chatbot's main page. You can change the username and password by modifying the `USERNAME` and `PASSWORD` variables in the `app.py` file.

Support
-------

For support or questions, please contact on Fiverr.