<script>
    export let search = '';
    export let data_target = 'search_modal'; // search_modal
    export let placeholder = 'Search2';

    function submitForm() {
        document.getElementById("search").value = document.getElementById("search_modal_field").value;
        var form = document.getElementById("quote_list_form");
        if (form) {
            form.submit();
        }
    }
</script>

<!-- Search modal -->
<dialog id="{data_target}">
    <article>
    <header>
        <!-- onclick="toggleModal(event)" -->
        <button aria-label="Close" rel="prev"  data-target="{data_target}" ></button>
        <p>
        </p>
    </header>
    <p>
        Drop some text to search for 
    </p>
    <input type="search" id="search_modal_field" placeholder="{placeholder}" aria-label="Search" bind:value="{search}" />
    <footer>
            <!-- onclick="toggleModal(event)" -->
        <button
            role="button"
            class="secondary"
            on:click={() => toggleModal(event)}
            data-target="{data_target}"
        >
            Cancel</button
        >
            <!-- onclick="toggleModal(event)" -->
        <button on:click={() => submitForm()} data-target="{data_target}"  >Confirm</button>
    </footer>
    </article>
</dialog>