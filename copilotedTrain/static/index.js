const cameraRealTime = document.getElementById('camera-img');

eel.expose(camera_image);
function camera_image(response){
	const image = "data:image/jpeg;base64," + response['predictions_image'];
	cameraRealTime.src = image;
	
}
window.onload = ()=>{
	eel.start_send_camera_image();
	document.getElementById("loader").classList.add('hide');
}