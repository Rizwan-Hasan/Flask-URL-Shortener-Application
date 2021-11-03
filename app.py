from datetime import timedelta

from flask import Flask

from database.DbConnector import DbConnect
from rediscache.RedisConnector import RedisConnect

# Application Variable ↓
app = Flask(__name__)

# Base26 Configuration↓
Base26Counter: dict = {"name": "BaseIntegerCounter", "value": 308915776}

# Application Configuration ↓
app.config["ENV"] = "production"
app.config["SECRET_KEY"] = "STEINS_GATE"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(seconds=15)
app.config["PREFERRED_URL_SCHEME"] = "https"

# Database Object Initialization ↓
db = DbConnect()
app.config["SQLALCHEMY_DATABASE_URI"] = db.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_SIZE"] = db.SQLALCHEMY_POOL_SIZE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = db.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = db.SQLALCHEMY_ENGINE_OPTIONS
db.connect(app=app)

# Redis Cache Initialization ↓
cache = RedisConnect(counter=Base26Counter["value"], counterName=Base26Counter["name"])

# All Routes ↓
# noinspection PyUnresolvedReferences
from routes import *

if __name__ == "__main__":
    print("Hello World")
