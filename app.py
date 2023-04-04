from flask import Flask, render_template, request, redirect, url_for
from langchain.agents import create_csv_agent
from flask_restful import Api, Resource
from langchain.llms import OpenAI
from PIL import Image

app = Flask(__name__)

# Embedding the OpenAI API key
OPENAI_API_KEY = "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"

# Adding username and password for authentication
USERNAME = "health_chatbot"
PASSWORD = "12345678"

# Initialize the Flask-RESTful API
api = Api(app)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth or auth.username != USERNAME or auth.password != PASSWORD:
        return ('Invalid credentials', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    return redirect(url_for('query'))

@app.route("/query", methods=["GET", "POST"])
def query():
    auth = request.authorization
    if not auth or auth.username != USERNAME or auth.password != PASSWORD:
        return redirect(url_for('home'))
    
    if request.method == "POST":
        query = request.form["query"]
        if OPENAI_API_KEY:
            agent = create_csv_agent(
                OpenAI(
                    openai_api_key=OPENAI_API_KEY,
                    temperature=0,
                  #  model_name="text_davinci-003",
                ),
                "datapoint.csv",
                verbose=True,
            )
            result = agent.run(query)
            return {"result": result}
        else:
            return {"error": "Please enter your OpenAI API Key."}, 400
    else:
        return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=False)
