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

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        mess = request.form['message']
        with smtplib.SMTP("smtp.gmail.com", port=PORT) as conn:
            conn.starttls()
            conn.login(user=my_email, password=password)
            conn.sendmail(from_addr=my_email, to_addrs=my_email,
                          msg=f"Subject:{name} Contacted You!\n\nName: {name}\nEmail: {email}\nMessage: {mess}")
            return render_template('index.html')
    return render_template('contact.html')

