import os
import requests
from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route("/")
def ok():
    return "Index page OK"
app.run(host="localhost", port=2000, debug=False)

