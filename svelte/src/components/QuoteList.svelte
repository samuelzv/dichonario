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
        <div slot="header"></div>
        <div slot="body">
            <BlockQuote>
                <p>"{quote.quote}"</p>
            </BlockQuote>
        </div>
        <div slot="footer">{quote.author__name}</div>
    </Card>
{/each}

<style>
</style>