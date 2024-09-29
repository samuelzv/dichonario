<script>
    import {fade} from 'svelte/transition';
    import { inview } from 'svelte-inview';

    let isInView = false;
</script>
<article use:inview={{ unobserveOnEnter: true, rootMargin: '-20%' }}
on:inview_change={({ detail }) => {
    isInView = detail.inView;
    console.log("isInView",isInView);
}}>
    {#if isInView && $$slots.header}
    <header in:fade>
        <slot name="header"></slot>
    </header>
    {/if}

    {#if isInView && $$slots.body}
    <body in:fade={{ delay: 250, duration: 2000 }} >
        <slot name="body"></slot>
    </body>
    {/if}

    {#if isInView && $$slots.footer}
    <footer in:fade>
        <slot name="footer"></slot>
    </footer>
    {/if}
</article>

<style>
</style>