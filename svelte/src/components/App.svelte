<script>
	// export let name;
	let value = "Hello 7"
	let x = "World 7"
</script>

<main>
	<h1>a:{value} {x}!</h1>
	<input type="text" bind:value />
	<p>Viiwwwwsit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>