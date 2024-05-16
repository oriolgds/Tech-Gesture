const subtitles = document.getElementById("subtitles");
let html = [];
const showInSubtitles = (letter)=>{
	// Not the same letters
	if(html[html.length - 1] == letter){
		return;
	}
	if(html.length <= 1 && letter==" ") return;
	html.push(letter);
	subtitles.innerHTML = html.join('').trim();
	subtitles.scrollTop = subtitles.scrollHeight;
	console.log(html)
}