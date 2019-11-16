const express = require('express');
const authRoutes = require('./routes/auth-routes');
const playerRoutes = require('./routes/player-routes');
const exphbs = require('express-handlebars');
const bodyParser = require('body-parser');
const passportSetup = require('./services/passport-setup');
const cookieSession = require('cookie-session');
const config = require('./config.json');
const passport = require('passport');
const mongoose = require('mongoose');

const app = express();

app.use('/static', express.static('public'));
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
// parse application/json
app.use(bodyParser.json());

app.use(cookieSession({
    maxAge: 60 * 1000, //cookie lasts 1 minute
    keys: [config.session.cookieKey]
}));

app.use(passport.initialize());
app.use(passport.session());

app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

//Routes
app.use('/auth', authRoutes);
app.use('/player', playerRoutes);

// ------ GET ------
app.get('/', function(req, res) { 
    res.render('home');
});

app.get('/dashboard', function(req, res) { 
    res.render('dashboard');
});

app.get('/panel', function(req, res) { 
    res.render('panel');
});

// Connect to mongodb
mongoose.connect('mongodb://localhost/brawlersdb', { useNewUrlParser: true, useFindAndModify: false });
mongoose.connection.once('open', function(){
    console.log('Connect to brawlersdb successfull.');
}).on('error', function(error){
    console.log('Connect to brawlersdb error:', error);
});

app.listen(3000, () => console.log('Listening on port 3000.'));

module.exports = app;