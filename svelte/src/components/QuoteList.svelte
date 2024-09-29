<script>
    import BlockQuote from "./BlockQuote.svelte";
    import Card from './Card.svelte';
    import CardIsInView from "./CardIsInView.svelte";
    /**
     * @type {Array<{quote: string, author__name: string}>}
     */
     export let quotes = [];
    /**
     * @type {Array<{id: string, text: string, url: Location | (string & Location)}>}
     */
     export let command_buttons = [];
     export let selected_command = '';

     /**
     * @param {string} buttton_id
     */
     function is_button_selected(buttton_id) {
         return selected_command === buttton_id;

     }
     /**
     * @param {string} url
     */
     function go_to_url(url) {
         window.location.href = url;
     }
</script>

<div class="container">
    <div role="group">
        {#each command_buttons as b }
            <button on:click={() => !is_button_selected(b.id) && go_to_url(b.url.toString())} class:secondary={!is_button_selected(b.id)}>{b.text}</button>
        {/each}
    </div>
</div>

<div class="wrapper">
    {#each quotes as quote }
        <CardIsInView>
            <svelte:fragment slot="body">
                <BlockQuote>
                    <p>"{quote.quote}"</p>
                    <footer>
                        <cite> - {quote.author__name}</cite>
                    </footer>
                </BlockQuote>
            </svelte:fragment>
            <svelte:fragment slot="footer"></svelte:fragment>
        </CardIsInView>
{/each}
</div>
<style>
    .wrapper {
        /* background-color: yellow; */
    }
</style>