from flask import Blueprint, request, jsonify, render_template
from models import db, User
from helpers import token_required

api = Blueprint('api',__name__, url_prefix='/api')