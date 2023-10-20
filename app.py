from flask import Flask, redirect, render_template
from models import db, Submission
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

@app.route("/send")
def send_submission():
    """Send initial submission to OpenAI"""

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )
    print(completion.choices[0].message)