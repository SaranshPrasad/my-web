from flask import Flask, render_template, request, send_from_directory, url_for


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')
@app.route('/download')
def download():
    return send_from_directory('static', path="files/my_cv.docx")



