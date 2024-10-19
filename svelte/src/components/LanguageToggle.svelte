<script>
    import Icon from '@iconify/svelte';
    import {getCookie} from 'src/lib/api';

    /**
     * @type {import('$lib/types').LanguageToggleI18n}
    */
   export let i18n

   /**
    * @type {boolean} is_english
    */
   export let is_english = false;

   /**
    * @type {boolean} is_spanish
    */
   export let is_spanish = false;


    /**
     * @param {'en'|'es'} language
     */
    async function set_language(language) {
                    // 'next': '/quotes/list?action=public',
                    // 'next': encodeURIComponent('/quotes/list?action=public'),
                    // 'Accept': 'text/html',
                    // 'Accept': 'application/json',
                    // 'next': '/' + language + '/quotes/list?action=public',
        // alert(`${window.location.pathname}--${window.location.search}`);

        // todo
// So I found the problem. Apparently, you MUST include a next parameter/input field that correspond to the current path (without the language prefix) in order for the redirect to work.
// I erroneously assumed, this was automatically figured out by Django.
        const next = (window.location.pathname + window.location.search).substring(3);
        // alert(next);
        const response = await fetch(
            '/i18n/setlang/',
            {
                method: 'POST',
                redirect: 'follow',
                headers: {
                    'Accept': 'text/html',
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'language': language || '',
                    'next': next, // '/quotes/list?action=mine',  
                    'csrfmiddlewaretoken': getCookie('csrftoken') || '', 
                }),
            }
        );
        // const data = await response.text();
        if (response.redirected) {
            window.location.href = response.url;
        }

        // console.log(data);
        // window.location.href = '/';
    }


    /**
     * @param {'en'|'es'} language
     */
    async function set_language2(language) {
                    // 'next': '/quotes/list?action=public',
                    // 'next': encodeURIComponent('/quotes/list?action=public'),
        const response = await fetch(
                    '/i18n/setlang?' + new URLSearchParams({
                    'language': language || '',
                    'next': '/quotes/list?action=public',
                    'csrfmiddlewaretoken': getCookie('csrftoken') || '', 
                }),
            {
                method: 'get',
                headers: {
                    'Accept': 'text/html',
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            }
        );
        const data = await response.json();
    }

</script>

<button type="button" 
    class="language" 
    on:click={() => set_language('en')} 
    disabled={is_english}
    aria-label={i18n.english_label} 
    data-placement="bottom"
    data-tooltip={i18n.english_description}>
    <Icon icon="flagpack:gb-ukm" />
</button>

<button type="button" 
    class="language" 
    on:click={() => set_language('es')} 
    disabled={is_spanish}
    aria-label={i18n.spanish_label} 
    data-placement="bottom"
    data-tooltip={i18n.spanish_description}>
    <Icon icon="flagpack:es" />
</button>


<style>
    :global(#languagetoggle-target) {
        display: flex;
    }

    .language {
        background: transparent;
        border: transparent;
        cursor: pointer;
    }
</style>