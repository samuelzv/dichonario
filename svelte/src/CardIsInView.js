import CardIsInView from './components/CardIsInView.svelte'

const cardIsInView = new CardIsInView({
	target: document.getElementById("cardisinview-target"),
	props: JSON.parse(document.getElementById("cardisinview-props").textContent),
});

export default cardIsInView;