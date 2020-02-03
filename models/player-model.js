const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// create Player Schema and Model
const PlayerSchema = new Schema({
    name: String,
    sub: String,
    bnetId: Number,
    battletag: String,
    provider: String,
    token: String
});

const Player = mongoose.model('player', PlayerSchema);

module.exports = Player;