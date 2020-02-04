const router = require('express').Router();
const Match = require('../models/match-model');

//----- GET
router.get('/', function(req, res) {
    if (!req.session.loggedin) {
        return res.redirect('/');
    }

    Match.find({}).then((mhistory) => {
        if (mhistory) {

            let record_all = { ratio: [0, 0]};
            let record_ranked = { ratio: [0, 0]};

            mhistory.forEach(match => {
                if (match.player.win) {
                    record_all.ratio[0]++;

                    if (match.competitive) {
                        record_ranked.ratio[0]++;
                    }
                } else {
                    record_all.ratio[1]++;

                    if (match.competitive) {
                        record_ranked.ratio[1]++;
                    }
                }
            });

            res.render('match_history', {
                matches: mhistory,
                record: record_all,
                rrecord: record_ranked
            });
        } else {
            res.status(400).send({
                message: 'No match history for your account was found.'
            });
        }
    });
});

router.get('/map', function(req, res) {
    if (!req.session.loggedin) {
        return res.redirect('/');
    }

    if (!req.query.mcode) {
        return res.status(400).send('<h1>Invalid Query Provided</h1>');
    }

    Match.find({mcode: req.query.mcode}).then((mhistory) => {
        if (mhistory) {

            let name = mhistory[0].map;
            let record_all = {
                Zerg: [0, 0],
                Terran: [0, 0],
                Protoss: [0, 0]
            };
            let record_ranked = {
                Zerg: [0, 0],
                Terran: [0, 0],
                Protoss: [0, 0]
            };

            mhistory.forEach(match => {
                if (match.player.win) {
                    record_all[match.opponent.race][0]++;

                    if (match.competitive) {
                        record_ranked[match.opponent.race][0]++;
                    }
                } else {
                    record_all[match.opponent.race][1]++;

                    if (match.competitive) {
                        record_ranked[match.opponent.race][1]++;
                    }
                }
            });

            res.render('map', {
                matches: mhistory,
                record: record_all,
                rrecord: record_ranked,
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
    if (!req.session.loggedin) {
        return res.redirect('/');
    }

    if (!req.query.UTC) {
        return res.status(400).send('<h1>Invalid Query Provided</h1>');
    }

    Match.find({date: req.query.UTC}).then((mhistory) => {
        if (mhistory) {

            let UTC = mhistory[0].date;
            let record_all = { ratio: [0, 0]};
            let record_ranked = { ratio: [0, 0]};

            mhistory.forEach(match => {
                if (match.player.win) {
                    record_all.ratio[0]++;

                    if (match.competitive) {
                        record_ranked.ratio[0]++;
                    }
                } else {
                    record_all.ratio[1]++;

                    if (match.competitive) {
                        record_ranked.ratio[1]++;
                    }
                }
            });

            res.render('date', {
                matches: mhistory,
                record: record_all,
                rrecord: record_ranked,
                date: UTC
            });
        } else {
            res.status(400).send({
                message: 'No match history for your account was found.'
            });
        }
    });
});

router.get('/pname', function(req, res) {
    if (!req.session.loggedin) {
        return res.redirect('/');
    }

    //only check player name cause not all players are in clans and thus
    //clan_tag could be blank/undefined
    if (!req.query.pname) {
        return res.status(400).send('<h1>Invalid Query Provided</h1>');
    }

    Match.find({"opponent.name": req.query.pname, "opponent.clan_tag": req.query.clan}).then((mhistory) => {
        if (mhistory) {

            let oname = mhistory[0].opponent.name;
            let oclan = mhistory[0].opponent.clan_tag;
            let record_all = { ratio: [0, 0]};
            let record_ranked = { ratio: [0, 0]};

            mhistory.forEach(match => {
                if (match.player.win) {
                    record_all.ratio[0]++;

                    if (match.competitive) {
                        record_ranked.ratio[0]++;
                    }
                } else {
                    record_all.ratio[1]++;

                    if (match.competitive) {
                        record_ranked.ratio[1]++;
                    }
                }
            });

            res.render('player', {
                matches: mhistory,
                record: record_all,
                rrecord: record_ranked,
                pname: oname,
                clan_tag: oclan
            });
        } else {
            res.status(400).send({
                message: 'No match history for your account was found.'
            });
        }
    });
});

module.exports = router;