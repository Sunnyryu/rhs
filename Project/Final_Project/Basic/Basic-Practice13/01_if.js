const userName1 = prompt('너의 이름이 뭐니?')
let message = ""

if (userName1 === "펭수"){
  message = "우주 대스타";
}
else if ( userName1 === "bbung"){
  message = "냄새나";
} else {
  message = "<h1>어서오세요. '${userName1}' </h1>"
}

message;

document.write(message)
