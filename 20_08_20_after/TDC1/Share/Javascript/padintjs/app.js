const canvas = document.getElementById("jsCanvas");
const ctx = canvas.getContext("2d");
const colors = document.getElementsByClassName("jsColor");
const range = document.getElementById("jsRange");
const mode = document.getElementById("jsMode");
const saveBtn = document.getElementById("jsSave");

const INITIAL_COLOR = "#2c2c2c";
const CANVAS_SIZE = 700;

canvas.width = CANVAS_SIZE;
canvas.height =  CANVAS_SIZE;

ctx.fillStyle = "white"; // 투명으로 할 경우에 저장 시... 하얀색이 아닌 회색이 나옴
ctx.fillRect(0,0, CANVAS_SIZE, CANVAS_SIZE);
ctx.strokeStyle = INITIAL_COLOR;
ctx.fillStyle = INITIAL_COLOR;

//ctx.strokeStyle = "blue";  => 선 색
ctx.lineWidth = 2.5; // 선 굵기

//ctx.fillStyle = "green"; => 채움 색
//ctx.fillRect(50, 20, 100, 49);// x축, y축 가로, 세로


let painting = false;
let filling = false;

function stopPainting(){
    painting = false;
}

function startPainting(){
    painting = true;
}

function onMouseMove(event){
    const x = event.offsetX;
    const y = event.offsetY;
    if(!painting){
        ctx.beginPath();
        ctx.moveTo(x, y);
    }else{
        ctx.lineTo(x,y);
        ctx.stroke();
    }
}


function onMouseUp(event){
    stopPainting();
}

function onMouseLeave(event){
    painting = false;
}

function handleColorClick(event){
    const color = event.target.style.backgroundColor;
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
}

function handleRangeChange(event){
    const size = event.target.value;
    ctx.lineWidth = size;    
}

function handleModeClick(event){
    if(filling === true){
        filling = false;
        mode.innerText = "Fill";
    }else {
        filling = true;
        mode.innerText = "Paint";
    }
}

function handleCanvasClick(){
    if(filling){
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
}

function handleCM(event){
    event.preventDefault();
}

function handleSaveClick(){
    const image = canvas.toDataURL();
    const link = document.createElement("a");
    link.href = image;
    link.download = "PaintJS[🎨]";
    link.click();
}
if(canvas){
    canvas.addEventListener("mousemove", onMouseMove);
    canvas.addEventListener("mousedown", startPainting);
    canvas.addEventListener("mouseup", stopPainting);
    canvas.addEventListener("mouseleave", stopPainting);
    canvas.addEventListener("click", handleCanvasClick);
    canvas.addEventListener("contextmenu", handleCM);
}

Array.from(colors).forEach(color =>
    color.addEventListener("click", handleColorClick)
  );

  if(range){
      range.addEventListener("input", handleRangeChange);
  }

  if(mode){
      mode.addEventListener("click", handleModeClick);
  }

  if(saveBtn){
      saveBtn.addEventListener("click", handleSaveClick);
  }