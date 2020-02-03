const passport = require('passport');
const BnetStrategy = require('passport-bnet').Strategy;
const config = require('../config.json');
const Player = require('../models/player-model');
const rp = require('request-promise');

passport.serializeUser((user, done) => {
    done(null, user.id);
});

passport.deserializeUser((id, done) => {
    Player.findById(id).then((user) => {
        done(null, user);
    });
});

passport.use(new BnetStrategy({
    callbackURL: 'http://localhost:5000/auth/bnet/redirect',
    clientID: config.BNET.ID,
    clientSecret: config.BNET.SECRET,
    scope: 'sc2.profile'
}, (accessToken, refreshToken, profile, done) => { 
    Player.findOne({bnetId: profile.id}).then((currentPlayer) => {
        if(currentPlayer) {
            console.log('Player ', currentPlayer.name, ' already created');
            done(null, currentPlayer);
        } else {

            let hIndex = profile.battletag.indexOf('#');
            let pname = profile.battletag.substring(0, hIndex);

            let player = new Player({
                name: pname,
                sub: profile.sub,
                bnetId: profile.id,
                battletag: profile.battletag,
                provider: profile.provider,
                token: profile.token
            });

            player.save().then(() => {
                done(null, player);
            });
        }
    });
}));