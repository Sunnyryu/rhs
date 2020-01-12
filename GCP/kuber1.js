const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('hello world!');

});

app.listen(8080, '0.0.0.0', () => {
  console.log('hello wolrd app is listening on port 8080.');

});
