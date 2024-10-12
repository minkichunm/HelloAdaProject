from flask import Flask, request, jsonify, render_template
import spacy

# Initialize the app and NLP model
app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')  # Example using spaCy

# Define routes
@app.route('/')
def index():
    return render_template('index.html')  # Frontend page

@app.route('/process', methods=['POST'])
def process_command():
    command = request.form['command']
    response = handle_command(command)
    print(f"Command received: {command}, Response: {response}")  # Log the response

    return jsonify(response)

def handle_command(command):
    doc = nlp(command)
    # Basic keyword matching for commands
    if "left" in command:
        return {"action": "move_left"}
    elif "right" in command:
        return {"action": "move_right"}
    elif "jump" in command:
        return {"action": "jump"}
    elif "color" in command:
        return {"action": "change_color"}
    return {"action": "invalid"}

if __name__ == '__main__':
    app.run(debug=True)

