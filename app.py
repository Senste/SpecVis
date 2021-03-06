# To start server:
# Open a new command prompt and navigate to the directory this file is in
# Activate the virtual env as necessary
# To activate venv: venv/Scripts/Activate.bat
# flask run to start server  
 
from flask import Flask, send_from_directory
from flask_restful import Api
from backend.api.api import ApiHandler

from flask_cors import CORS # When experimenting locally, prevent CORS errors.
import warnings
warnings.filterwarnings('ignore') # This is just for the: `warnings.warn("PySoundFile failed. Trying audioread instead.")` that occurs with certain files

app = Flask(__name__, static_url_path='/', static_folder='frontend/build')

api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/check")
def test_backend_connection():
    return {
            'resultStatus': 'SUCCESS',
            'message': "Backend connection successful!"
        }

api.add_resource(ApiHandler, '/flask/check', '/flask/check/<file_name>')   

if __name__ == '__main__':
    app.debug = True
    CORS(app) # When experimenting locally - comment out on deployment
    app.run()