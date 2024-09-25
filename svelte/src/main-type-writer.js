import TypeWriter from './components/TypeWriter.svelte';

const typeWriter = new TypeWriter({
	target: document.getElementById("main-type-writer-target"),
	props: JSON.parse(document.getElementById("main-type-writer-props").textContent),
});

export default typeWriter;