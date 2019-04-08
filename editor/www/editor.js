function solidRock2DMap(rows, cols) {
	let arr = new Array(rows).fill('').map(row => new Array(cols).fill('0'));
  for(let y = 0; y < 10; y++) {
    for(let x = 0; x < 8; x++) { arr[y][x]='2'; }
    let finish = cols - 8;
    for(let x = finish; x < cols; x++) { arr[y][x]='2'; }
  }
  return arr;
}
const SCROLL_SPEED = 10;
const MAP_ROWS = 10;
const MAP_COLS = 160;
const TILE_SIZE = 50;

let enemies = [];
let items = [];

let canvas = document.querySelector('#canvas');
const ctx = canvas.getContext('2d');

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

const other = {
  gem: new Image(),
  exit_door: new Image(),
  e0: new Image(),
  e2: new Image()
};
other.gem.src = 'http://localhost:3000/items/gem.png';
other.exit_door.src = 'http://localhost:3000/items/door.png';
other.e0.src = 'http://localhost:3000/enemies/enemy_1_left0.png';
other.e2.src = 'http://localhost:3000/enemies/enemy_2_left1.png';


const saveButton = document.querySelector('#save');
saveButton.addEventListener('click', (e) => {

  const fileName = document.querySelector('#file').value;
  const musicFileName = document.querySelector('#music').value;
  if(fileName.length > 0 && musicFileName.length > 0) {
 
    const data = { 
        map,
        enemies,
        items,
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


function readSingleFile(evt) {
    //Retrieve the first (and only!) File from the FileList object
    var f = evt.target.files[0]; 

    if (f) {
      var r = new FileReader();
      r.onload = function(e) { 
	      var contents = e.target.result;
        alert( "Got the file.n" 
              +"name: " + f.name + "n"
              +"type: " + f.type + "n"
              +"size: " + f.size + " bytesn"
              + "starts with: " + contents.substr(1, contents.indexOf("n"))
        );  
      }
      r.readAsText(f);
    } else { 
      alert("Failed to load file");
    }
  }

  document.getElementById('fileinput').addEventListener('change', readSingleFile, false);



canvas.addEventListener('contextmenu', (e) => {
    e.preventDefault();
    let screenPosition = canvas.getBoundingClientRect();
    let mouseX = e.clientX - screenPosition.left;
	  mouseX = mouseX.toFixed(0);
    let mouseY = e.clientY - screenPosition.top;
	  mouseY = mouseY.toFixed(0);
   
    let temp_x = Math.floor((e.clientX - screenPosition.left) + pos.x);
    let temp_y = Math.floor(mouseY);

    const possibleEnemy = enemies.find((enemy) => isAnythingHere(
      { x1: enemy.x, y1: enemy.y, x2: enemy.x + enemy.w, y2: enemy.y + enemy.h }, 
      { x: temp_x, y: temp_y }));

    const possibleItem = items.find((item) => isAnythingHere(
      { x1: item.x, y1: item.y, x2: item.x + item.w, y2: item.y + item.h }, 
      { x: temp_x, y: temp_y }));

    if(possibleEnemy || possibleItem) {
      if(possibleEnemy) {
        const newEnemies = enemies.filter((enemy) => enemy.x !== possibleEnemy.x && enemy.y !== possibleEnemy.y);
        enemies = [];
        enemies = [...newEnemies];
      } else if(possibleItem){
        const newItems = items.filter((item) => item.x !== possibleItem.x && item.y !== possibleItem.y);
        items = [];
        items = [...newItems];        
      }
    } else {
      let temp_x = Math.floor((pos.x + 25) / TILE_SIZE) + Math.floor(mouseX / TILE_SIZE);
      let temp_y = Math.floor(mouseY / TILE_SIZE);
      map[temp_y][temp_x] = '0';
    }
    return false;
});

function isAnythingHere(pos1, pos2) {

    if (pos2.x > pos1.x1 &&
       pos2.x < pos1.x2 &&
       pos2.y > pos1.y1 &&
       pos2.y < pos1.y2) { 
       return true;
    } else {
       return false;
    }
}



document.addEventListener('click', (e) => {
  let id = e.target.id;
  if(id.startsWith('tile-')) {
    let currentTile = document.querySelector(`#${id}`);
    currentChoice = id[5];
    resetAll();
    canvas.style.cursor = `url(${e.target.src}), auto`;
    currentTile.style.border = '1px solid green';
  } else if(id.startsWith('other-')) {
    let currentTile = document.querySelector(`#${id}`);
    const thisChoice = id.substr(6);
    currentChoice = thisChoice;
    resetAll();
    canvas.style.cursor = `url(${e.target.src}), auto`;
    currentTile.style.border = '1px solid green';
  }
});

function resetAll() {
  for(let i = 0; i < Object.keys(tiles).length; i++) {
    let currentTile = document.querySelector(`#tile-${Object.keys(tiles)[i]}`);
    currentTile.style.border = '';
  }
  for(let i = 0; i < Object.keys(other).length; i++) {
    let currentTile = document.querySelector(`#other-${Object.keys(other)[i]}`);
    currentTile.style.border = '';
  }
}


document.addEventListener('keydown', (event) => keyboardAction = event.key);

canvas.addEventListener('click', (e) => {
   let screenPosition = canvas.getBoundingClientRect();
   let mouseX = e.clientX - screenPosition.left;
	 mouseX = mouseX.toFixed(0);
   let mouseY = e.clientY - screenPosition.top;
	 mouseY = mouseY.toFixed(0);

   if(currentChoice === 'exit_door' || currentChoice === 'gem' || currentChoice === 'e0' || currentChoice === 'e2') {

     let temp_x = Math.floor(e.clientX - screenPosition.left) + pos.x;    
     let temp_y = parseInt(mouseY, 10);

     if(currentChoice === 'exit_door' || currentChoice === 'gem') {
       let item = {
         id: currentChoice === 'exit_door'? 'exit_door' : 'gem',
         x: temp_x,
         y: temp_y,
         w: currentChoice === 'exit_door'? 128 : 22,
         h: currentChoice === 'exit_door'? 128 : 25
       };
       items.push(item);
     } else {
      let enemy = {
         id: currentChoice,
         x: temp_x,
         y: temp_y,
         w: currentChoice === 'e0'? 60 : 68,
         h: currentChoice === 'e0'? 60 : 68
       };
       enemies.push(enemy);
     }
   } else if(parseInt(currentChoice, 10) !== 'NaN' || currentChoice === 'X') {   
     let temp_x = Math.floor((pos.x + 25) / TILE_SIZE) + Math.floor(mouseX / TILE_SIZE);
     let temp_y = Math.floor(mouseY / TILE_SIZE);
     map[temp_y][temp_x] = currentChoice;
   }
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

function drawItemsAndEnemies() {
  if(enemies.length > 0) {
    for(let i = 0; i < enemies.length; i++) {
      const tempKey = enemies[i].id
      const temp_x = enemies[i].x - pos.x;
      ctx.drawImage(other[tempKey], temp_x, enemies[i].y); 
    }
  }
  if(items.length > 0) {
    for(let i = 0; i < items.length; i++) {
      const tempKey = items[i].id
      const temp_x = items[i].x - pos.x;
      ctx.drawImage(other[tempKey], temp_x, items[i].y); 
    }
  }

}

setInterval(() => {
  drawMap();
  drawItemsAndEnemies();
  move();
  }, 1000/30);


