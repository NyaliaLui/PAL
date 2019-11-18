const express = require('express');
const authRoutes = require('./routes/auth-routes');
const mhistoryRoutes = require('./routes/match-routes');
const exphbs = require('express-handlebars');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();

app.use('/static', express.static('public'));
app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
// parse application/json
app.use(bodyParser.json());

//Routes
app.use('/auth', authRoutes);
app.use('/mhistory', mhistoryRoutes);

// ------ GET ------
app.get('/', function(req, res) { 
    res.redirect('/mhistory');
});

app.get('/signin', function(req, res) { 
    res.render('sign', { msg: 'You have signed in!' });
});

app.get('/signout', function(req, res) { 
    res.render('sign', { msg: 'You have signed out!' });
});

// Connect to mongodb
mongoose.connect('mongodb://localhost:27017/PAL', { useNewUrlParser: true, useFindAndModify: false, useUnifiedTopology: true});
mongoose.connection.once('open', function(){
    console.log('Connect to PALdb successfull.');
}).on('error', function(error){
    console.log('Connect to PALdb error:', error);
});

app.listen(5000, () => console.log('Listening on port 5000.'));

module.exports = app;