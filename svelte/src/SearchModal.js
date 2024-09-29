
import SearchModal from "./components/SearchModal.svelte";

const searchmodal = new SearchModal({
	target: document.getElementById("searchmodal-target"),
	props: JSON.parse(document.getElementById("searchmodal-props").textContent),
});

export default searchmodal;