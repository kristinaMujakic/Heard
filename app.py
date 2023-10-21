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


@app.route("/")
def show_index():
    """Homepage"""

    return render_template("index.html")


##############################################################################
# OpenAI routes

@app.route("/send", methods=['POST'])
def send_submission():
    """Send initial submission to OpenAI"""

    user_submission = request.json.get('user_submission', '')

    messages = [
        {"role": "system", "content": "You are a chat bot listening to an employee's concern about a blocker at work. Respond with thank you if the user has provided enough information, like the team they are on. Or respond with a question to gather a better understanding of what is blocking them."},
        {"role": "user", "content": user_submission}
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print(completion.choices[0].message)
    print(user_submission)

    response = {
        # Convert the message to a JSON object
        "message": completion.choices[0].message
    }

    return jsonify(response)  # Return the response as JSON


# Route to render mock employee results

@app.route("/data", methods=['GET'])
def show_data():
    """Display the mock employee and submission data."""

    return render_template("data.html", employees=mock_employees, submissions=mock_submissions)
