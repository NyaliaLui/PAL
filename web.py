from flask import Flask, render_template, flash, request, redirect, url_for
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient(port=27017)
db = client.PAL

def setup_app():
    return app

@app.route("/")
def home():
    matches = db.mhistory.find()

    return render_template("match_history.html", matches=matches)

@app.route("/mhistory")
def page_mhistory():
    matches = db.mhistory.find()

    return render_template("match_history.html", matches=matches)

@app.route("/mhistory/pname/<name>")
def page_player(name):
    temp = name.split('-')
    clan = temp[0]
    pname = temp[1]
    matches = db.mhistory.find({"opponent.name": pname, "opponent.clan_tag": clan})

    return render_template("player.html", pname=pname, clan_tag=clan, matches=matches)

@app.route("/mhistory/map/<mapcode>")
def page_map(mapcode):
    matches = db.mhistory.find({"mcode": mapcode})
    name = matches[0]["map"]
    record = {}
    record["Zerg"] = {"win": 0, "loss": 0}
    record["Terran"] = {"win": 0, "loss": 0}
    record["Protoss"] = {"win": 0, "loss": 0}

    for match in matches:
        if match["player"]["win"]:
            record[match["opponent"]["race"]]["win"] += 1
        else:
            record[match["opponent"]["race"]]["loss"] += 1

    return render_template("map.html", mname=name, record=record)

@app.route("/mhistory/date/<UTC>")
def page_date(UTC):
    matches = db.mhistory.find({"date": UTC})

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