const router = require('express').Router();
const Match = require('../models/match-model');

//----- GET
router.get('/', function(req, res) {
    Match.find({}).then((mhistory) => {
        if (mhistory) {

            let record = { ratio: [0, 0]};

            mhistory.forEach(match => {
                if (match.player.win) {
                    record.ratio[0]++;
                } else {
                    record.ratio[1]++;
                }
            });

            res.render('match_history', {
                matches: mhistory,
                record: record
            });
        } else {
            res.status(400).send({
                message: 'No match history for your account was found.'
            });
        }
    });
});

router.get('/map', function(req, res) {
    Match.find({mcode: req.query.mcode})
    .then((mhistory) => {
        if (mhistory) {

            let name = mhistory[0].map;
            let record = {
                Zerg: [0, 0],
                Terran: [0, 0],
                Protoss: [0, 0]
            };

            mhistory.forEach(match => {
                if (match.player.win) {
                    record[match.opponent.race][0]++;
                } else {
                    record[match.opponent.race][1]++;
                }
            });

            res.render('map', {
                matches: mhistory,
                record: record,
                mname: name
            });
        } else {
            res.status(400).send({
                message: 'No match history for your account was found.'
            });
        }
    });
});

router.get('/date', function(req, res) {
    Match.find({date: req.query.UTC})
    .then((mhistory) => {
        if (mhistory) {

            let record = { ratio: [0, 0]};

            mhistory.forEach(match => {
                if (match.player.win) {
                    record.ratio[0]++;
                } else {
                    record.ratio[1]++;
                }
            });

            res.render('date', {
                matches: mhistory,
                record: record,
                date: req.body.UTC
            });
        } else {
            res.status(400).send({
                message: 'No match history for your account was found.'
            });
        }
    });
});

router.get('/pname', function(req, res) {
    Match.find({"opponent.name": req.query.pname, "opponent.clan_tag": req.query.clan})
    .then((mhistory) => {
        if (mhistory) {

            let record = { ratio: [0, 0]};

            mhistory.forEach(match => {
                if (match.player.win) {
                    record.ratio[0]++;
                } else {
                    record.ratio[1]++;
                }
            });

            res.render('player', {
                matches: mhistory,
                record: record,
                pname: req.body.pname,
                clan_tag: req.body.clan
            });
        } else {
            res.status(400).send({
                message: 'No match history for your account was found.'
            });
        }
    });
});

module.exports = router;