function goto(url){
	window.open(url);
}
function get_window_size(){
	var winHeight=0;
	if (window.innerHeight){
    	winHeight = window.innerHeight;
	}
	else if ((document.body) && (document.body.clientHeight)){
    	winHeight = document.body.clientHeight;
	}
	document.getElementsByTagName('main').style.height=winHeight;
	alert(winHeight)
}
function mouseout(){
	document.getElementById('only').style.textDecoration="none";
}
function mousein(){
	document.getElementById('only').style.textDecoration="underline";
}
function sendmail(people){
	location="mailto:"+people;
}