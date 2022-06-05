from cgitb import text
from urllib import response
from flask import Blueprint, render_template, request, jsonify
from Backend.Learn.tliorai import get_response

homepage = Blueprint('homepage', __name__)


@homepage.get("/")
def home():
    return render_template('index.html')


@homepage.post('/analy')
def analy():
    text = request.get_json().get("user_message")
    response = get_response(text)
    user_message = {"reply": response}
    return jsonify(user_message)
