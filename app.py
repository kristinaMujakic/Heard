from flask import Flask, redirect, render_template
from models import db, Submission

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
# Playlist routes 