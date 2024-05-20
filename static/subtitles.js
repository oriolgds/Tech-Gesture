const subtitles = document.getElementById("subtitles");
const wrapTextButton = document.getElementById("wrap-text-button");
const gameEnabled = document.getElementById('toggle-modes');
const ahorcadoDisplay = document.getElementById('ahorcado-display');
let gameEnabledValue = false;
let html = [];
const showInSubtitles = (letter)=>{
	// Not the same letters
	if(html[html.length - 1] == letter){
		return;
	}
	if(letter.length === 1 && gameEnabledValue) showInAhorcado(letter);
	if(gameEnabledValue) return;
	if(letter.length > 1) letter += " ";

	html.push(letter);
	subtitles.innerHTML = html.join('').trim();
	subtitles.scrollTop = subtitles.scrollHeight;
	console.log(html)
}
wrapTextButton.addEventListener('click', ()=>{
	showInSubtitles('<br>');
});
gameEnabled.addEventListener('change', changeGame);
eel.start_process();
function changeGame(){
	if(gameEnabled.checked) {
		gameEnabledValue = true;
		subtitles.style.display = 'none';
		ahorcadoDisplay.style.display = '';
	}
	else {		
		gameEnabledValue = false;		
		subtitles.style.display = '';
		ahorcadoDisplay.style.display = 'none';
	}
}
changeGame();

