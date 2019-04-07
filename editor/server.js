const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();

app.use(express.static(__dirname + '/www'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.sendFile(path.join('www', 'index.html'));
});

app.post('/save', (req, res) => {
  const map = req.body;
  printToMapToFile(map);
  res.send('<h1>file saved</h1>');
});

const server = app.listen(3000, () => {
  const host = server.address().address;
  const port = server.address().port;
});

function printToMapToFile(undergroundMap) {
  const map = { map: [...undergroundMap.map] };
  const formattedData = JSON.stringify(map, null);
	fs.writeFile(undergroundMap.file, formattedData, (error) => {
		if (error) throw err;
		else { console.log('Map saved'); }
	});
}


