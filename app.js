const express = require('express');
const authRoutes = require('./routes/auth-routes');
const mhistoryRoutes = require('./routes/match-routes');
const uploadRoutes = require('./routes/upload-routes');
const exphbs = require('express-handlebars');
const fileUpload = require('express-fileupload');
const bodyParser = require('body-parser');
const passportSetup = require('./services/passport-setup');
const cookieSession = require('cookie-session');
const config = require('./config.json');
const passport = require('passport');
const mongoose = require('mongoose');

const app = express();

//default ops
app.use('/static', express.static('public'));
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
// parse application/json
app.use(bodyParser.json());

//set cookie session
app.use(cookieSession({
    maxAge: 60 * 1000, //cookie lasts 1 minute
    keys: [config.session.cookieKey]
}));

//init passport SSO
app.use(passport.initialize());
app.use(passport.session());

app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');
app.use(fileUpload());

//Routes
app.use('/auth', authRoutes);
app.use('/mhistory', mhistoryRoutes);
app.use('/upload', uploadRoutes);

// ------ GET ------
app.get('/', function(req, res) { 
    if (req.session.loggedin) {
        res.redirect('/mhistory');
    } else {
        res.render('front', {layout: 'nologin'});
    }
});

// ------ POST ------
app.post('/', function(req, res) {
    if (req.body.btag) {
        req.session.loggedin = true;
        req.session.btag = req.body.btag;
        res.redirect('/mhistory');
    } else {
        res.render('front', {layout: 'nologin'});
    }
});

// Connect to mongodb
mongoose.connect('mongodb://noticals:thelegend27@localhost:27017/PAL', { useNewUrlParser: true, useFindAndModify: false, useUnifiedTopology: true});
mongoose.connection.once('open', function(){
    console.log('Connect to PALdb successfull.');
}).on('error', function(error){
    console.log('Connect to PALdb error:', error);
});

app.listen(5000, () => console.log('Listening on port 5000.'));

module.exports = app;
