
import Paginator from "./components/Paginator.svelte";

const paginator = new Paginator({
	target: document.getElementById("paginator-target"),
	props: JSON.parse(document.getElementById("paginator-props").textContent),
});

export default paginator;