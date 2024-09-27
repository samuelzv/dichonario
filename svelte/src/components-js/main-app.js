import App from '../components/App.svelte';

const app = new App({
	target: document.getElementById("main-app-target"),
	props: JSON.parse(document.getElementById("main-app-props").textContent),
});

export default app;