import TypeWriter from '../components/TypeWriter.svelte';

const typeWriter = new TypeWriter({
	target: document.getElementById("components-js/main-type-writer-1-target"),
	props: JSON.parse(document.getElementById("components-js/main-type-writer-1-props").textContent),
});

export default typeWriter;