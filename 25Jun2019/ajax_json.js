var req;
  window.onload=function(){
    document.querySelector("#btn_load").onclick = function(){
      var url = "image.jsp";
      req = new XMLHttpRequest();
      req.onreadystatechange = createImages;
      req.open("GET", url, "true");
      req.send(null);
    };
  }

  function createImages(){
    if(req.readyState ==4){
      if(req.status == 200){
        console.log('ok');
        var obj = JSON.parse(req.responseText);
        var images = obj["rows"];
        var strDOM = "";
        console.log(images.length)
        for(var i = 0;i<images.length;i++){
          var image = images[i];
          strDOM += '<div class="image_panel">'
          strDOM += '           <img src= "'+image.url+'">'
          strDOM += '           <p class = "title">'+image.title+'</p>'
          strDOM += '</div>';
        }
        document.querySelector("#image_container").innerHTML = strDOM;
      }else {
        alert("처리중 에러가 발생했습니다.");
      }

      }
  }
