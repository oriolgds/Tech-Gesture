const predictionsImage = document.getElementById('predictions-show');
eel.expose(fetchImage);
function fetchImage(data){  
  console.log(data);
  const dataURL = "data:image/jpeg;base64," + data.predictions_image;
  predictionsImage.src = dataURL;
}