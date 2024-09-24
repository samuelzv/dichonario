import TypeWriter from './components/TypeWriter.svelte';

const typeWriter = new TypeWriter({
	target: document.getElementById("main-typewriter-target"),
	props: JSON.parse(document.getElementById("main-typewriter-props").textContent),
});

export default typeWriter;