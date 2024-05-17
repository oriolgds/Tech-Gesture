const subtitles = document.getElementById("subtitles");
const wrapTextButton = document.getElementById("wrap-text-button");
let html = [];
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
wrapTextButton.addEventListener('click', ()=>{
	showInSubtitles('<br>');
})
