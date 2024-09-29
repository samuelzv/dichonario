<script>
    import { createEventDispatcher } from 'svelte';

    export let search = '';
    export let data_target = 'search_modal'; // search_modal
    export let placeholder = 'Search';

    const dispatch = createEventDispatcher();

    function submit_form() {
        dispatch('submit', { search });
    }

    /**
     * @param {MouseEvent & { currentTarget: EventTarget & HTMLButtonElement; }} event
     */
    function cancel(event) {
        dispatch('cancel', { event });
    }
</script>

<!-- Search modal -->
<dialog id="{data_target}">
    <article>
    <header>
        <button aria-label="Close" rel="prev"  data-target="{data_target}" ></button>
        <p>
        </p>
    </header>
    <p>
        Drop some text to search for 
    </p>
    <input type="search" id="search_modal_field" placeholder="{placeholder}" aria-label="Search" bind:value="{search}" />
    <footer>
        <button
            role="button"
            class="secondary"
            on:click={event => cancel(event)}
            data-target="{data_target}"
        >
            Cancel</button
        >
        <button on:click={() => submit_form()} data-target="{data_target}"  >Confirm</button>
    </footer>
    </article>
</dialog>