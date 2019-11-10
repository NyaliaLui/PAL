from flask import Flask, render_template, flash, request, redirect, url_for
app = Flask(__name__)

def setup_app():
    return app

@app.route("/")
def home():
    return render_template("match_history.html")

@app.route("/mhistory")
def page_mhistory():
    return render_template("match_history.html")

@app.route("/mhistory/pname/<name>")
def page_player(name):
    return render_template("player.html", pname=name)

@app.route("/mhistory/map/<name>")
def page_map(name):
    return render_template("map.html", mname=name)

@app.route("/mhistory/date/<UTC>")
def page_date(UTC):
    return render_template("date.html", date=UTC)

@app.route("/signin")
def page_signin():
    return render_template("sign.html", msg='You have signed in!')

@app.route("/signout")
def page_signout():
    return render_template("sign.html", msg='You have signed out!')

if __name__ == "__main__":
    app = setup_app()

    app.run(debug=True)