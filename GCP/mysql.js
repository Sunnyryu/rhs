const fs = require('fs');
const mysql = require('mysql');

const connection = mysql.createCOnnection({
  host : '104.155.184.195',
  ssl : {
  ca : fs.readFileSync(dirname +'/server-ca.per'),
  cert: fs.readFileSync(dirname+ '/client-cert.pem'),
  key: fs.readFileSync(__dirname + '/client-key.pem')
}
});
