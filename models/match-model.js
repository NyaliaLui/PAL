const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// create Player Schema and Model
const MatchSchema = new Schema({
    battletag: String,
    map: String,
    mcode: String,
    timestamp: Number,
    date: String,
    competitive: Boolean,
    player: {
        win: Boolean,
        team_id: Number,
        race: String,
        name: String,
        clan_tag: String
    },
    opponent: {
        win: Boolean,
        team_id: Number,
        race: String,
        name: String,
        clan_tag: String
    }
}, {
    collection: 'mhistory'
});

const Match = mongoose.model('mhistory', MatchSchema);

module.exports = Match;