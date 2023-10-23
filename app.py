from flask import Flask, redirect, render_template, jsonify, request
from models import db, Submission
from mock_data import mock_employees, mock_submissions

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///heard-app'
app.config['SECRET_KEY'] = 'sage123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

with open("prompt.txt", "r") as file:
    prompt_text = file.read()

conversation = [{"role": "system", "content": prompt_text}]

@app.route("/")
def show_index():
    """Homepage"""

    return render_template("index.html")


##############################################################################
# OpenAI routes

@app.route("/send", methods=['POST'])
def send_submission():
    """Send initial submission to OpenAI"""

    user_submission = {"role": "user", "content": request.json.get('user_submission', '')}

    conversation.append(user_submission)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    conversation.append({"role": "system", "content": completion.choices[0].message.content})
    print(conversation)

    response = { "message": completion.choices[0].message }

    return jsonify(response)  # Return the response as JSON


# Route to render mock employee results

@app.route("/data", methods=['GET'])
def show_data():
    """Display the mock employee and submission data."""

    return render_template("data.html", employees=mock_employees, submissions=mock_submissions)
