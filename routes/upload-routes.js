const router = require('express').Router();
const Match = require('../models/match-model');
const spawn = require('child_process').spawn;

//----- POST
router.post('/', function(req, res) {
  if (!req.session.loggedin) {
    return res.redirect('/');
  }
  
  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send('<h2>No files were uploaded. Try again.</h2>');
  }

  // The name of the input field (i.e. "sampleFile") is used to retrieve the uploaded file
  let sample_file = req.files.sampleFile;
  let upload_path = '/home/ec2-user/PAL/replays/' + sample_file.name;

  // move replay to proper location
  sample_file.mv(upload_path, function(err) {
    if (err)
      return res.status(500).send(err);
  });

  //extract data from replay
  let replay_only = spawn('python3', ['/home/ec2-user/PAL/replay_only.py', '--sc2name', req.body.sc2name, upload_path]);
  replay_only.stdout.on('data', (data) => {
    let match_info = JSON.parse(data.toString());
    let match = new Match(match_info);
 
    // save model to database
    match.save(function (err, _match) {
      if (err) res.status(500).send(err);
      console.log("Match with " + _match.player.name + " saved to Matches collection.");
    });
  });

  res.send('<h3>File uploaded! Go back to the home page!</h2>');
});

module.exports = router;