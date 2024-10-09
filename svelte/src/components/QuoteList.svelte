<script>
    import Icon from '@iconify/svelte';
    import '../quote-app.css';
    import {STATIC_PATH} from 'src/lib/constants';

    import BlockQuote from "./BlockQuote.svelte";
    import SearchModal from "./SearchModal.svelte";
    import CardIsInView from "./CardIsInView.svelte";
    import Paginator from "./Paginator.svelte";

    /**
     * @type {import('$lib/types').Quotes}
    */ 
    export let quotes = [];

    export let quote_list_url = '';
    export let quote_new_url = '';

    /** 
     * @type {import('$lib/types').I18n} 
     * */
    export let i18n; 

    /**
     * @type {import('$lib/types').Pagination}
     */
    export let pagination;

    /**
     * @type {string}
    */
    export let search = '';
    /**
     * @type {Array<{id: string, text: string, url: Location | (string & Location)}>}
     */
    export let command_buttons = [];
    export let selected_command = '';

    /**
     * @type {string}
    */
    export let language_code;

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
      * @param {'edit'|'delete'} action
      * @param {string} id
      */
     function get_action_url(action, id) {
        let url = `quote/${id}/${action}`;
        url += '?next=' + encodeURIComponent(`${window.location.pathname}${window.location.search}`)

        return url;
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


<div role="group">
    {#each command_buttons as b }
        <button on:click={() => !is_button_selected(b.id) && go_to_url(b.url.toString())} class:secondary={!is_button_selected(b.id)}>{b.text}</button>
    {/each}
</div>

<form id="quote_list_form" action="{quote_list_url}" class="quote-list full-height">

    <div class="row">
        <div class="col-xs-12 col-md-6">
            <div class="row center-xs start-md">
                <div class="col-xs-12">
                    {#if search}
                        <small>Results for: <ins>"{search}"</ins> <a href="#" on:click={() => clear_and_submit_form()}>Clear</a></small>
                    {/if}
                </div>
            </div>
        </div>
        <div class="col-xs-12 col-md-6">
            <div class="row center-xs end-md">
                <div class="col-xs-12 buttons-group">
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
                        <div class="row start-xs center-md middle-xs">
                            <div class="col-xs-4 col-sm-3">
                                <img src="/{STATIC_PATH}/{quote.author__image}" alt="{quote.author__name}">
                            </div>

                            <div class="col-xs-8 col-sm-9">
                                <p>"{quote.quote}"</p>
                            </div>
                        </div>
                        <div class="row start-xs center-md">
                            <div class="col-xs-12 col-sm-3">
                                <footer>
                                    <cite> - {quote.author__name}</cite>
                                </footer>
                            </div>
                            <div class="col-xs-12 col-sm-9">
                            </div>
                        </div>
                    </BlockQuote>
                </svelte:fragment>
                <svelte:fragment slot="footer">
                    <div class="row end-xs quote-actions">
                        <div class="col-xs-12">
                            {#if quote.is_owner}
                                <a  data-tooltip="{i18n.edit}" 
                                    class="secondary" 
                                    href="{get_action_url('edit', quote.id)}">
                                    <Icon icon="material-symbols-light:edit-outline" />
                                </a>
                                <a  data-tooltip="{i18n.delete}" 
                                    class="secondary"
                                    href="{get_action_url('delete', quote.id)}">
                                    <Icon icon="material-symbols-light:delete-outline" />
                                </a>
                            {/if}
                        </div>
                    </div>
               </svelte:fragment>
            </CardIsInView>
    {/each}
    </div>
    <input type="hidden" id="search" name="search" bind:value={search}>
</form>
<Paginator i18n={i18n} pagination={pagination} />
<SearchModal data_target="search_modal" placeholder="{i18n.search}" bind:search on:cancel={cancel_search} on:submit={submit_search}/>
<style>
    :global(#quotelist-target) {
        display: flex;
        flex-direction: column;
        flex: 1;
    }
    .wrapper {
        position: relative;
        /* margin-top: 0px; */
        /* margin-top: 30px; */
    }
    .buttons-group button.secondary {
        min-width: 145px;
    }
    .quote-actions a {
        cursor: pointer;
    }
    img {
        border-radius: 50%;
        width: 98px;
        height: 130px;
    }
</style>