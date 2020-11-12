# Loading environment variables
from dotenv import load_dotenv
load_dotenv()

# Flask application creation
from flask import Flask, jsonify
app = Flask(__name__)
app.config.from_object("default_settings.app_config")

# Database connection
from database import init_db
db = init_db(app)

# Set up serialisation and deserilaisation
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

from commands import db_commands
app.register_blueprint(db_commands)

#Controller registration
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)

# error handler for bad request (e.g. no title included in post request)
from marshmallow.exceptions import ValidationError
@app.errorhandler(ValidationError)
def handle_bad_request(error):
    return (jsonify(error.messages), 400)