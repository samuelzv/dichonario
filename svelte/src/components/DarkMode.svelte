<script>
    import Icon from '@iconify/svelte';

    /**
     * @type {'dark'|'light'} mode
     */
    export let mode = 'dark'

    /**
     * @type {string} host_element
     */
    export let host_element = 'html'

    /**
     * @type {string} data_field
     */
    export let data_field = 'data-theme'

    function toggle_mode() {
        mode = (mode === 'dark' ? 'light' : 'dark');
        set_host_element(host_element, data_field, mode)
    }

    /**
     * @param {string} host_element
     * @param {string} data_field
     * @param {'dark'|'light'} mode
     */
    function set_host_element(host_element, data_field, mode) {
        const host = document.querySelector(host_element);
        if (host) {
            host.setAttribute(data_field, mode);
        }
    }

</script>

<button type="button" class:night={mode === 'dark'} class:light={mode === 'light'} on:click={toggle_mode} aria-label="Toggle dark mode">
    {#if mode === 'dark'}
        <Icon icon="ic:baseline-wb-sunny" />
    {:else if mode === 'light'}
        <Icon icon="ic:baseline-mode-night" />
{/if}
</button>


<style>
    .light,
    .night {
        background: transparent;
        border: transparent;
        cursor: pointer;
    }
    .light {
        color: #13171f;
    }
</style>