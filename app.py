from flask import Flask, request, render_template, redirect
from flask_bootstrap import Bootstrap
import os
import smtplib
import csv, re

app = Flask(__name__)
bootstrap = Bootstrap(app)
# students = []


@app.route('/')
def index():

    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)
    return render_template('index.html', students=students)


@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    dorm = request.form.get("dorm")
    context = {
         'name': name,
         'dorm': dorm,
    }
    # students.append(f"{name} from {dorm}")
    if not name or not dorm or not email:
        return render_template('failure.html')
    # massage = "You are registered successfully"
    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.starttls()
    # server.login("shakil.hossian3@northsouth.edu", os.getenv("tom2jery"))
    # server.send_message("shakil.hossian3@northsouth.edu", email, massage)
    with open('registered.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((name, email, dorm))
    return render_template('success.html', context=context)


if __name__ == '__main__':
    app.run()
