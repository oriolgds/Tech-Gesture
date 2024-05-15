const subtitles = document.getElementById("subtitles");
let html = '';
const showInSubtitles = (letter)=>{
	html += " " + letter + ",";
	subtitles.innerHTML = html;
	subtitles.scrollTop = subtitles.scrollHeight;
}