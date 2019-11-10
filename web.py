from flask import Flask, render_template, flash, request, redirect, url_for
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient(port=27017)
db = client.PAL

def setup_app():
    return app

@app.route("/")
def home():
    temp = db.mhistory.find()
    record = {"ratio": [0, 0]}
    matches = []

    for match in temp:
        if match["player"]["win"]:
            record["ratio"][0] += 1
        else:
            record["ratio"][1] += 1
        
        matches.append(match)

    return render_template("match_history.html", matches=matches, record=record)

@app.route("/mhistory/pname/<name>")
def page_player(name):
    temp = name.split('-')
    clan = temp[0]
    pname = temp[1]
    temp = db.mhistory.find({"opponent.name": pname, "opponent.clan_tag": clan})
    record = {"ratio": [0, 0]}
    matches = []

    for match in temp:
        if match["player"]["win"]:
            record["ratio"][0] += 1
        else:
            record["ratio"][1] += 1
        
        matches.append(match)

    return render_template("player.html", pname=pname, clan_tag=clan, matches=matches, record=record)

@app.route("/mhistory/map/<mapcode>")
def page_map(mapcode):
    matches = db.mhistory.find({"mcode": mapcode})
    name = matches[0]["map"]
    record = {}
    record["Zerg"] = [0, 0]
    record["Terran"] = [0, 0]
    record["Protoss"] = [0, 0]

    for match in matches:
        if match["player"]["win"]:
            record[match["opponent"]["race"]][0] += 1
        else:
            record[match["opponent"]["race"]][1] += 1

    return render_template("map.html", mname=name, record=record)

@app.route("/mhistory/date/<UTC>")
def page_date(UTC):
    temp = db.mhistory.find({"date": UTC})
    record = {"ratio": [0, 0]}
    matches = []

    for match in temp:
        if match["player"]["win"]:
            record["ratio"][0] += 1
        else:
            record["ratio"][1] += 1
        
        matches.append(match)

    return render_template("date.html", date=UTC, matches=matches, record=record)

@app.route("/signin")
def page_signin():
    return render_template("sign.html", msg='You have signed in!')

@app.route("/signout")
def page_signout():
    return render_template("sign.html", msg='You have signed out!')

if __name__ == "__main__":
    app = setup_app()

    app.run(debug=True)