const palabras = [
    "Sol",
    "Mar",
    "Amor",
    "Casa",
    "Luna",
    "Nube",
    "Gato",
    "Silla",
    "Mesa",
    "Risa",
    "Cielo",
    "Verde",
    "Blanco",
    "Mano",
    "Rayo",
    "Mapa",
    "Miel",
    "Caminata",
    "Aventura",
    "Familia"
];
const palabra = palabras[Math.floor(Math.random() * palabras.length)].toUpperCase();
// Palabra a adivinar
console.log('Palabra: ',palabra[0].toUpperCase() + palabra.slice(1).toLowerCase())

// Lista de letras introducidas por el usuario
let letrasIntroducidas = [];

// Función para actualizar el display y las letras incorrectas
function actualizarJuego() {
    let display = "";
    let letrasIncorrectas = [];
    
    // Recorrer cada letra de la palabra
    for (let i = 0; i < palabra.length; i++) {
        if (letrasIntroducidas.includes(palabra[i])) {
            display += palabra[i];
        } else {
            display += "_";
        }
    }

    // Verificar letras incorrectas
    for (let letra of letrasIntroducidas) {
        if (!palabra.includes(letra)) {
            letrasIncorrectas.push(letra);
        }
    }
    return {'display': display, 'incorrectDisplay': letrasIncorrectas };
}

// Ejemplo de uso
const ahorcadoResult = document.getElementById('ahorcado-result');
const ahorcadoResultIncorrect = document.getElementById('ahorcado-incorrect-letters');
const showInAhorcado = (letter)=>{
	if(!(letrasIntroducidas.includes(letter)) && letter != ' '){
		letrasIntroducidas.push(letter);
	}
	display();
}
const display = ()=>{
    const juego = actualizarJuego();
	let display = juego.display;
	let incorrectDisplay = juego.incorrectDisplay;
	ahorcadoResult.innerHTML = display;
	ahorcadoResultIncorrect.innerHTML = incorrectDisplay;
}
display();
