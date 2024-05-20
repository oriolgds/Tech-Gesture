const predictionsImage = document.getElementById('predictions-show');
const spaceCountSpan = document.getElementById('space-count')
// Array para almacenar las letras detectadas
let detectedLetters = [];

// Función para procesar el array JSON recibido desde el backend
eel.expose(fetchImage);
// Función para procesar el array JSON recibido desde el backend
function fetchImage(jsonData) {
    
    const dataURL = "data:image/jpeg;base64," + jsonData.predictions_image;
    predictionsImage.src = dataURL;
    // Verificar si se detectaron nuevas letras o actualizar el tiempo para las existentes
    detectedLetters = jsonData.detectedClasses;
    // checkLetters(jsonData.detectedClasses);

    removeLoader();
}



let spaceCount = 0;
let previousLettersDetected = [];
setInterval(() => {    
    if(spaceCount >= 5){
        showInSubtitles(' ');
        spaceCount = 0;
    }
    spaceCountSpan.innerHTML = spaceCount;
    previousLettersDetected.forEach(letter => {
        if(detectedLetters.includes(letter)){
            showInSubtitles(letter);
        }
    });
    previousLettersDetected = detectedLetters;
    if(detectedLetters.length <= 0){
        spaceCount++;
    }
}, 1000);

function removeElements(inputArray, elementsToRemove) {
    return inputArray.filter(item => !elementsToRemove.includes(item));
}

document.addEventListener('load', ()=>{    
    setTimeout(() => {
        
        document.getElementById('loader').classList.add('hide')
    }, 1000);
})
eel.start_process();

let loaderRemoved = false;
function removeLoader(){
    if(loaderRemoved) return;
    document.getElementById('loader').classList.add('hide');
    loaderRemoved = true;
}












// function checkLetters(letters){
//     letters.forEach(letter => {
//         const existingLetterIndex = detectedLetters.findIndex(obj => obj === letter);
//         if(existingLetterIndex !== -1){
//             setTimeout(() => {
//                 const existingLetterIndex = detectedLetters.findIndex(obj => obj.letter === letter);
//                 removeElements([letter]);
//                 if(existingLetterIndex !== -1){
//                     showInSubtitles(letter);
//                 } 
//             }, 1900);
//         }
//     });
// }
// function removeElements(elementsToRemove) {
//     detectedLetters.filter(item => !elementsToRemove.includes(item));
// }




