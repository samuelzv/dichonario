import Card from './components/Card.svelte'

const card = new Card({
	target: document.getElementById("card-target"),
	props: JSON.parse(document.getElementById("card-props").textContent),
});

export default card;