import os
from flask import Flask, render_template, request, redirect, jsonify
import csv
import openai

app = Flask(__name__)

CSV_FILE = 'contacts.csv'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def write_to_csv(data, file_path=CSV_FILE):
    file_exists = os.path.exists(file_path)
    with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Email', 'Message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

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
        write_to_csv({'Name': name, 'Email': email, 'Message': message})
        return redirect('/contact')
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

# New /chat endpoint for the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    # Example: You can process the message here.
    # For now, we'll simply echo the user's message.
    # Optionally, you can integrate OpenAI's API or other chatbot logic.
    bot_response = f"Echo: {user_message}"
    
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
