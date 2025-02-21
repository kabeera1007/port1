import os
import datetime
from flask import Flask, render_template, request, redirect, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask(__name__)

# Database Configuration - Use environment variables for security
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://flaskuser:kabeera1007@localhost/user_tracking')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Session Configuration
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for sessions
Session(app)

db = SQLAlchemy(app)

# Define User Activity Model
class UserActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100))
    ip_address = db.Column(db.String(100))
    user_agent = db.Column(db.String(255))
    referrer = db.Column(db.String(255))
    page_url = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    time_spent = db.Column(db.Integer, nullable=True)
    action = db.Column(db.String(255))

# Define Contact Form Model
class ContactForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Create Tables in Database
with app.app_context():
    db.create_all()

# Track User Activity
@app.before_request
def log_request():
    if "session_id" not in session:
        session["session_id"] = os.urandom(16).hex()

    activity = UserActivity(
        session_id=session["session_id"],
        ip_address=request.remote_addr,
        user_agent=request.headers.get("User-Agent"),
        referrer=request.referrer,
        page_url=request.path
    )
    db.session.add(activity)
    db.session.commit()

@app.route('/track', methods=['POST'])
def track_user_action():
    data = request.get_json()
    if data:
        activity = UserActivity(
            session_id=session.get("session_id"),
            ip_address=request.remote_addr,
            user_agent=request.headers.get("User-Agent"),
            referrer=request.referrer,
            page_url=data.get("page_url"),
            time_spent=data.get("time_spent"),
            action=data.get("action")
        )
        db.session.add(activity)
        db.session.commit()
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "Invalid data"}), 400

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        contact_entry = ContactForm(name=name, email=email, message=message)
        db.session.add(contact_entry)
        db.session.commit()
        return redirect('/contact')
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == "__main__":
    app.run(debug=True)

