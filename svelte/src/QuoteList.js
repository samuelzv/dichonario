import QuoteList from './components/QuoteList.svelte'

const quoteList = new QuoteList({
	target: document.getElementById("quotelist-target"),
	props: JSON.parse(document.getElementById("quotelist-props").textContent),
});

export default quoteList;