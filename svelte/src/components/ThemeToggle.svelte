<script>
    import Icon from '@iconify/svelte';
    import {getCookie} from 'src/lib/api';

    /**
     * @type {'dark'|'light'} theme
     */
    export let theme = 'dark'

    /**
     * @type {string} host_element
     */
    export let host_element = 'html'

    /**
     * @type {string} data_field
     */
    export let data_field = 'data-theme'

    function toggle_theme() {
        theme = (theme === 'dark' ? 'light' : 'dark');
        set_host_element(host_element, data_field, theme)
        set_theme(theme)
    }

    /**
     * @param {string} host_element
     * @param {string} data_field
     * @param {'dark'|'light'} theme
     */
    function set_host_element(host_element, data_field, theme) {
        const host = document.querySelector(host_element);
        if (host) {
            host.setAttribute(data_field, theme);
        }
    }

    /**
     * @param {string} theme
     */
    async function set_theme(theme) {
        const response = await fetch(
            'preferences/theme',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'theme': theme || '',
                    'csrfmiddlewaretoken': getCookie('csrftoken') || '', 
                }),
            }
        );
        const data = await response.json();
        console.log(data);
    }

</script>

<button type="button" class:night={theme === 'dark'} class:light={theme === 'light'} on:click={toggle_theme} aria-label="Toggle dark theme">
    {#if theme === 'dark'}
        <Icon icon="ic:baseline-wb-sunny" />
    {:else if theme === 'light'}
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