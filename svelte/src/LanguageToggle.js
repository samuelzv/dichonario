import LanguageToggle from './components/LanguageToggle.svelte'

const languagetoggle = new LanguageToggle({
	target: document.getElementById("languagetoggle-target"),
	props: JSON.parse(document.getElementById("languagetoggle-props").textContent),
});

export default languagetoggle;