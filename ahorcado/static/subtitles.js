const subtitles = document.getElementById("subtitles");
let html = '';
palabras = [
    "Sol",
    "Mar",
    "Amor",
    "Casa",
    "Luna",
    "Nube",
    "Gato",
    "Silla",
    "Mesa",
    "Niña",
    "Niño",
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
const showInSubtitles = (letter)=>{
	// Not the same letters
	if(html[html.length - 1] == letter){
		return;
	}
	if(letter.length > 1) letter += " ";
	html.push(letter);
	subtitles.innerHTML = html.join('').trim();
	subtitles.scrollTop = subtitles.scrollHeight;
	console.log(html)
}