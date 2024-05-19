eel.expose(camera_image);
function camera_image(response){
	const image = "data:image/jpeg;base64," + response['predictions_image'];
}