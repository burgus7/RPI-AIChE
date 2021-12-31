from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/officers")
def officers():
    return render_template("officers.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/About")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()

#TODO Update Website on https://www.aiche.org/community/students/chapters/rensselaer-polytechnic-institute-student-chapter