function show_contacts() {
	for (let element of document.getElementsByTagName('li')) {
		element.style.display = '';
	}
}

function contact_lookup(name_lookup) {
	name_lookup = name_lookup.toLowerCase()
	show_contacts()

	for (let element of document.getElementsByClassName('nameElement')) {
		let name = element.innerHTML.substring(5).toLowerCase() // element.innerHTML = 'Nom: Bobby' --> element.innerHTML.lower() = 'nom: bobby' --> element.innerHTML.lower() = 'bobby'
		name.includes(name_lookup) ? undefined : element.parentElement.style.display = 'none';
	}
}