import TypeWriter from './components/TypeWriter.svelte';

const typeWriter = new TypeWriter({
	target: document.getElementById("app-target"),
	props: JSON.parse(document.getElementById("app-props").textContent),
});

export default typeWriter;