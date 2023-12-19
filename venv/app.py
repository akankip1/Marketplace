from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load variables from .env file into environment
load_dotenv()

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

if __name__ == '__main__':
    # Get environment variables or default values
    flask_debug = os.getenv('FLASK_DEBUG', default='0')
    # Convert string to boolean for debug
    debug = flask_debug.lower() in ['true', '1', 'yes']

    # Run the app with debug mode based on environment variable
    app.run(debug=debug)
