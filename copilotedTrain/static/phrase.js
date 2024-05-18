const phrasesObject = document.getElementById('phrase');
const phrases = [
	'Sólo hay dos clases de lenguajes de programación: Los lenguajes de los que se queja la gente, y los lenguajes que nadie usa. (Bjarne Stroustrup)',
	'La programación en la actualidad es una carrera entre los ingenieros informáticos que crean programas a prueba de idiotas y el Universo que crea cada vez más y mejores idiotas. De momento, el universo gana. (anónimo)',
	'Siempre programo como si la persona que mantendrá mi código fuera un psicópata que sabe donde vivo. (Martin Golding)',
	'Código eliminado es código depurado. (Jeff Sickel)',
	'Para entender la recursividad, primero se ha de entender la recursividad.',
	'No te preocupes si no funciona bien. Si lo hiciera, te quedarías sin trabajo. (Madre de todas las leyes de la ingeniería del software)',
	'Antes de que un software pueda ser reusable, primero ha de ser usable. (Ralph Johnson)',
	'Sin análisis de requisitos o sin diseño, programar es el arte de crear errores en un documento de texto vacío. (Louis Srygley)',
	'La programación es como el sexo: Un sólo error y tendrás que mantenerlo el resto de tu vida. (Michael Sinz)'
];
function getRandomElement(arr) {
	const randomIndex = Math.floor(Math.random() * arr.length);
	return arr[randomIndex];

}

phrasesObject.innerHTML = getRandomElement(phrases);