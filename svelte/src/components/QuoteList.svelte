<script>
    import BlockQuote from "./BlockQuote.svelte";
    import Card from './Card.svelte';
    /**
     * @type {Array<{quote: string, author__name: string}>}
     */
     export let quotes = [];
</script>

{#each quotes as quote }
    <Card>
        <svelte:fragment slot="body">
            <BlockQuote>
                <p>"{quote.quote}"</p>
                <footer>
                    <cite> - {quote.author__name}</cite>
                </footer>
            </BlockQuote>
        </svelte:fragment>
        <svelte:fragment slot="footer"></svelte:fragment>
    </Card>
{/each}

<style>
</style>