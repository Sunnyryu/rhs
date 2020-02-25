const { app, BrowserWindow } = require("electron");

let win;
//app.allowRendererProcessReuse = true;
function createdWindow() {
  win = new BrowserWindow({ width: 800, height: 600 });
  win.loadURL(`file://${__dirname}/index.html`);
  win.on("closed", () => { win = null });
}
app.on("ready", createdWindow);
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  if (win === null){
    createdWindow();
  }
});

