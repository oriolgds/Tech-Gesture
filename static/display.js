
function resize(){
	const predictionShow = document.getElementById('predictions-show');
	predictionShow.style.maxHeight = `${window.innerHeight - 150}px`;
}

resize();
window.onresize = ()=>{
	resize();
}