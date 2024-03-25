from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os


DB_NAME = 'contador.db'

app = Flask(__name__)
CORS(app)

path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, DB_NAME)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
