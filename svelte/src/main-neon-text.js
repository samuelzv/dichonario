import App from './components/NeonText.svelte';

const app = new App({
	target: document.getElementById("main-neon-text-target"),
	props: JSON.parse(document.getElementById("main-neon-text-props").textContent),
});

export default app;