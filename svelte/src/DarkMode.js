import DarkMode from './components/DarkMode.svelte'

const darkmode = new DarkMode({
	target: document.getElementById("darkmode-target"),
	props: JSON.parse(document.getElementById("darkmode-props").textContent),
});

export default darkmode;