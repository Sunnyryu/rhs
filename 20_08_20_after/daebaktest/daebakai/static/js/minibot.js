

function delButton() {
  $("#daebakbot_button").hide();
  if($(".daebak_minibot").css("display") == "none"){
  document.getElementById("close_button").style.display = "block";
  document.getElementsByClassName("daebak_minibot")[0].style.display = "block";
}
}
function delButton2() {
  const delbutton2 = document.getElementById('close_button')
  const delbutton = document.getElementById('daebakbot_button')
  if($(".daebak_minibot").css("display") == "block"){
  document.getElementById("close_button").style.display = "none";
  document.getElementsByClassName("daebak_minibot")[0].style.display = "none";
  $("#daebakbot_button").show();

}
}
