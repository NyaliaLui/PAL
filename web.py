from flask import Flask, render_template, flash, request, redirect, url_for
app = Flask(__name__)
matches = [{'name': 'billy', 'map': 'Triton LE', 'result': 'Win', 'date': 'Oct. 29 1993'},
    {'name': 'bob', 'map': 'Discoblood Bath LE', 'result': 'Win', 'date': 'Oct. 29 1993'},
    {'name': 'greatest', 'map': 'Thunderbird LE', 'result': 'Loss', 'date': 'Oct. 29 1993'},
    {'name': 'ever', 'map': 'Winters Gate LE', 'result': 'Loss', 'date': 'Oct. 29 1993'}]

def setup_app():
    return app

@app.route("/")
def home():
    return render_template("match_history.html", matches=matches)

@app.route("/mhistory")
def page_mhistory():
    return render_template("match_history.html", matches=matches)

@app.route("/mhistory/pname/<name>")
def page_player(name):
    return render_template("player.html", pname=name, matches=matches)

@app.route("/mhistory/map/<name>")
def page_map(name):
    return render_template("map.html", mname=name, matches=matches)

@app.route("/mhistory/date/<UTC>")
def page_date(UTC):
    return render_template("date.html", date=UTC, matches=matches)

@app.route("/signin")
def page_signin():
    return render_template("sign.html", msg='You have signed in!')

@app.route("/signout")
def page_signout():
    return render_template("sign.html", msg='You have signed out!')

if __name__ == "__main__":
    app = setup_app()

    app.run(debug=True)