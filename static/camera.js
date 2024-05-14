const letterWaitTime = 2;
let classes = {
}

const predictionsImage = document.getElementById('predictions-show');
eel.expose(fetchImage);
function fetchImage(data){
  const dataURL = "data:image/jpeg;base64," + data.predictions_image;
  predictionsImage.src = dataURL;
  const classesDetected = data.detectedClasses;
  const timeElapsed = data.elapsedTime;

  classesDetected.forEach(element => {
    // En el caso de que este comprobar el tiempo
    // Si el tiempo es mayor a 2 mostrar en subtitulos y borrar la key.
    
    if(element in classes){
      if(timeElapsed - classes.element >= letterWaitTime){
         showInSubtitles(element);
         delete classes[element];
      }
    }
    else {
      classes[element] = timeElapsed;
    }
  });
  // Limpiar el array de letras que se han detectado sin querer
  
  console.log(classes);
}




