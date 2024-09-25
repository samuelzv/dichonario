<script>
    export let text;
</script>

<main>
    <h1 class="neon">{text}</h1>
</main>

<style>
    .neon {
        color: #fff;
        text-shadow:
            0 0 5px #fff,
            0 0 10px #fff,
            0 0 20px #fff,
            0 0 40px #0ff,
            0 0 80px #0ff,
            0 0 90px #0ff,
            0 0 100px #0ff,
            0 0 150px #0ff;
    }

    h1 {
        font-weight: 400;
        text-align: center;
        text-transform: uppercase;
    }
</style>