$(document).ready(function(){
  $("#btn_load").click(function(){
    $.getJSON("image.jsp",null, createImages);
  });
});


  function createImages(data){
    var images = data.rows;
    var strDOM = "";
        for(var i = 0;i<images.length;i++){
          var image = images[i];
          strDOM += '<div class="image_panel">'
          strDOM += '           <img src= "'+image.url+'">'
          strDOM += '           <p class = "title">'+image.title+'</p>'
          strDOM += '</div>';
        }
        var $imageContainer       = $("#image_container");
        $imageContainer.append(strDOM);
        $(document).ajaxComplete(function(){
          console.log("ajax event : complete");
        });
        $(document).ajaxSend(function(){
          comsole.log("ajax event : send");
        })
        $(document).ajaxStart(function(){
          console.log("ajax event : start");
        })
        $(document).ajaxSuccess(function(){
          console.log("ajax event : success");
        })
        document.querySelector("#image_container").innerHTML = strDOM;
      }
