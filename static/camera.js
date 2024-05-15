const predictionsImage = document.getElementById('predictions-show');

// Array para almacenar las letras detectadas
let detectedLetters = [];

// Función para verificar el tiempo de detección de las letras
function checkDetectedLetters(timeElapsed) {
    detectedLetters.forEach(letterObj => {
        if (timeElapsed - letterObj.elapsedTime >= 2) {
            showInSubtitles(letterObj.letter);
        }
    });
}

// Función para limpiar las letras no detectadas
function cleanDetectedLetters() {
    detectedLetters = detectedLetters.filter(letterObj => letterObj.elapsedTime < 2);
}


// Función para procesar el array JSON recibido desde el backend
eel.expose(fetchImage);
// Función para procesar el array JSON recibido desde el backend
function fetchImage(jsonData) {
    const dataURL = "data:image/jpeg;base64," + jsonData.predictions_image;
    predictionsImage.src = dataURL;
    // Verificar si se detectaron nuevas letras o actualizar el tiempo para las existentes
    jsonData.detectedClasses.forEach(letter => {
        const existingLetterIndex = detectedLetters.findIndex(obj => obj.letter === letter);
        if (existingLetterIndex !== -1) {
            // Actualizar el tiempo para la letra existente
            detectedLetters[existingLetterIndex].elapsedTime = jsonData.elapsedTime - detectedLetters[existingLetterIndex].elapsedTime;
        } else {
            // Agregar una nueva letra con su tiempo de detección
            detectedLetters.push({ letter: letter, elapsedTime: jsonData.elapsedTime });
        }
    });
    console.log(detectedLetters)
    // Verificar las letras detectadas y limpiar las no detectadas
    checkDetectedLetters(jsonData.elapsedTime);
    cleanDetectedLetters();
}





