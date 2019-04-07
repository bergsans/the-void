function solidRock2DMap(rows, cols) {
	return new Array(rows).fill('').map(row => new Array(cols).fill('2'));
}
const SCROLL_SPEED = 10;
const MAP_ROWS = 10;
const MAP_COLS = 160;
const TILE_SIZE = 50;


let pos = {
  x: 0,
  y: 0
};

let keyboardAction = null;
let map = solidRock2DMap(MAP_ROWS, MAP_COLS);
let currentChoice = null;
const tiles = {
  0: new Image(),
  1: new Image(),
  2: new Image(),
  3: new Image(),
  4: new Image(),
  5: new Image(),
  6: new Image(),
  7: new Image(),
  X: new Image()
};
tiles['0'].src = 'http://localhost:3000/tiles/background.png';
tiles['1'].src = 'http://localhost:3000/tiles/1.png';
tiles['2'].src = 'http://localhost:3000/tiles/2.png';
tiles['3'].src = 'http://localhost:3000/tiles/3.png';
tiles['4'].src = 'http://localhost:3000/tiles/4.png';
tiles['5'].src = 'http://localhost:3000/tiles/5.png';
tiles['6'].src = 'http://localhost:3000/tiles/6.png';
tiles['7'].src = 'http://localhost:3000/tiles/7.png';
tiles['X'].src = 'http://localhost:3000/tiles/X.png';


const saveButton = document.querySelector('#save');
saveButton.addEventListener('click', (e) => {

  const fileName = document.querySelector('#file').value;
  const musicFileName = document.querySelector('#music').value;
  if(fileName.length > 0 && musicFileName.length > 0) {
 
    const data = { 
        map,
        file: fileName,
        music: musicFileName
    };
    const formattedData = JSON.stringify(data);

    const config = {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      method: 'POST',
      body: formattedData
    };
    fetch('http://localhost:3000/save', config)
      .then((res) => window.alert(res.status === 200? 'FILE SAVED' : 'FAIL'))
      .catch((e) => console.error(e));

  } else {
    window.alert("NAME YOUR FILES, STUPID.");
  }
});

const tilesArea = document.querySelector('#tiles');

document.addEventListener('click', (e) => {
  let id = e.target.id;
  if(id.startsWith('tile-')) {
    let currentTile = document.querySelector(`#${id}`);
    currentChoice = id[5];
    resetAll();
    canvas.style.cursor = `url(${e.target.src}), auto`;
    currentTile.style.border = '1px solid green';
  } 
});

function resetAll() {
  for(let i = 0; i < 9; i++) {
    let currentTile = document.querySelector(`#tile-${Object.keys(tiles)[i]}`);
    currentTile.style.border = '';
  }
}

let canvas = document.querySelector('#canvas');
const ctx = canvas.getContext('2d');




document.addEventListener('keydown', (event) => keyboardAction = event.key);

canvas.addEventListener('click', (e) => {
   let screenPosition = canvas.getBoundingClientRect();
   let mouseX = e.clientX - screenPosition.left;
	 mouseX = mouseX.toFixed(0);
   let mouseY = e.clientY - screenPosition.top;
	 mouseY = mouseY.toFixed(0);

   let temp_x = Math.floor(pos.x + 25 / TILE_SIZE) + Math.floor(mouseX / TILE_SIZE);
   let temp_y = Math.floor(mouseY / TILE_SIZE);
   map[temp_y][temp_x] = currentChoice;
});


function move() {
  switch (keyboardAction) {
    case 'ArrowRight':
      pos.x + SCROLL_SPEED < (MAP_COLS * TILE_SIZE)? pos.x += SCROLL_SPEED : null;
    break;
    case 'ArrowLeft':
      pos.x - SCROLL_SPEED > 0? pos.x -= SCROLL_SPEED : null;
    break;
  }
  keyboardAction = null;
}

function drawMap() {
  for(let y = 0; y < MAP_ROWS; y++) {
    for(let x = 0; x < MAP_COLS; x++) {
      let tileKey = map[y][x];
      let tempX = (x * TILE_SIZE) - (pos.x); 
      ctx.drawImage(tiles[tileKey], tempX, y * TILE_SIZE);
    } 
  }
}

setInterval(() => {
  drawMap();
  move();
  }, 1000/30);


