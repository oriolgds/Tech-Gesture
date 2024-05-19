eel.expose(camera_image);
function camera_image(response){
	const image = "data:image/jpeg;base64," + response['predictions_image'];
	
}
window.onload = ()=>{
	eel.start_send_camera_image();
	document.getElementById("")
}