from flask import Flask, render_template, request, send_from_directory, url_for
import smtplib
from dotenv import load_dotenv
import os


load_dotenv()

password = os.environ.get('PASSWORD')
app = Flask(__name__)
my_email = os.environ.get("my_email")
PORT = 587


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/download')
def download():
    return send_from_directory('static', path="files/my_cv.docx")



