import BlockQuote from './components/BlockQuote.svelte';

const blockQuote = new BlockQuote({
	target: document.getElementById("block-quote-target"),
	props: JSON.parse(document.getElementById("block-quote-props").textContent),
});

export default blockQuote;