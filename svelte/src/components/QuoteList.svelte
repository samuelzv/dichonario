<script>
    import '../quote-app.css';

    import BlockQuote from "./BlockQuote.svelte";
    import SearchModal from "./SearchModal.svelte";
    import CardIsInView from "./CardIsInView.svelte";
    import Paginator from "./Paginator.svelte";
    /**
     * @type {Array<{quote: string, author__name: string}>}
     */
    export let quotes = [];
    export let quote_list_url = '';
    export let quote_new_url = '';
    export let i18n = {search: '', new_quote: ''};
    export let search = '';
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

    /**
     * @param {{ detail: { event: any; }; }} event
     */
    function cancel_search(event) {
        toggleModal(event.detail.event) ;
    }

    /**
     * @param {{ detail: { search: string; }; }} event
     */
    function submit_search(event) {
        document.getElementById("search").value = event.detail.search;
        var form = document.getElementById("quote_list_form");
        if (form) {
            form.submit();
        }
    }

    function clear_and_submit_form() {
        submit_search({detail: {search: ''}});
    }

</script>


<div class="container">
    <div role="group">
        {#each command_buttons as b }
            <button on:click={() => !is_button_selected(b.id) && go_to_url(b.url.toString())} class:secondary={!is_button_selected(b.id)}>{b.text}</button>
        {/each}
   </div>
</div>

<form id="quote_list_form" action="{quote_list_url}" class="quote-list full-height">

    <div class="row">
        <div class="col-xs-12 col-md-6">
            {#if search}
            <div>
              <small>Results for: <ins>"{search}"</ins> <a href="#" on:click={() => clear_and_submit_form()}>Clear</a></small>
            </div>
          {:else}
            <div></div>
          {/if}
        </div>
        <div class="col-xs-12 col-md-6">
            <div class="row center-xs end-md">
                <div class="col-xs-12">
                    <button type="button" class="outline secondary" on:click={() => go_to_url(quote_new_url)}>
                        {i18n.new_quote} 
                    </button>
                    <button type="button" class="outline secondary" data-target="search_modal" on:click="{() => toggleModal(event)}">
                        {i18n.search} 
                    </button>
                </div>
            </div>
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
    <input type="hidden" id="search" name="search" bind:value={search}>
</form>
<Paginator />
<SearchModal data_target="search_modal" placeholder="{i18n.search}" bind:search on:cancel={cancel_search} on:submit={submit_search}/>
<style>
    :global(#quotelist-target) {
        display: flex;
        flex-direction: column;
        flex: 1;
    }
    .wrapper {
        margin-top: 30px;
    }
    button.secondary {
        min-width: 145px;
    }
</style>