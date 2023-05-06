function contact_lookup(name_lookup) {
	name_lookup = name_lookup.toLowerCase()
	show_contacts()

	for (let element of document.getElementsByClassName('nameElement')) {
		let name = element.innerHTML.substring(5).toLowerCase() // (excludes 'Nom: ')
		document.getElementsByClassName('nameElement')[0].innerHTML
		name.includes(name_lookup) ? undefined : element.parentElement.style.display = 'none';
	}
}

function show_contacts() {
	for (let element of document.getElementsByTagName('li')) {
		element.style.display = '';
	}
}