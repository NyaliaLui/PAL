const router = require('express').Router();
const passport = require('passport');

//auth with bnet
router.get('/bnet', passport.authenticate('bnet'));

//bnet callback route
router.get('/bnet/redirect', passport.authenticate('bnet', { failureRedirect: '/' }), (req,res) => {
    res.render('connected', {"battletag": req.user.battletag, layout: 'nologin'});
});

module.exports = router;