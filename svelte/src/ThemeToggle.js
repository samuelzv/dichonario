import ThemeToggle from './components/ThemeToggle.svelte'

const themetoggle = new ThemeToggle({
	target: document.getElementById("themetoggle-target"),
	props: JSON.parse(document.getElementById("themetoggle-props").textContent),
});

export default themetoggle;