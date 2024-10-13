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
        const response = await fetch(
            'preferences/language',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'language': language || '',
                    'csrfmiddlewaretoken': getCookie('csrftoken') || '', 
                }),
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
    .language {
        background: transparent;
        border: transparent;
        cursor: pointer;
    }
</style>