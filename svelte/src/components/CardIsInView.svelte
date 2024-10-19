<script>
    import {fade,fly} from 'svelte/transition';
    import { inview } from 'svelte-inview';

    let isInView = false;
    const id = self.crypto.randomUUID();

</script>
<!-- <article use:inview={{ unobserveOnEnter: true, rootMargin: '-20%' }} -->
<article id="{id}" use:inview={{ unobserveOnEnter: true, rootMargin: '-180px' }}
    on:inview_change={({ detail }) => {
    isInView = detail.inView;
    console.log("isInView",isInView);
    if (isInView) {
        setTimeout(() => {
            htmx.process(document.getElementById(id));
        }, 0);
    }

}}>
    {#if isInView && $$slots.header}
    <header in:fade>
        <slot name="header"></slot>
    </header>
    {/if}

    {#if isInView && $$slots.body}
    <body in:fly={{ x: -200, duration: 2000 }} >
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
    article {
        position: relative;
        overflow: hidden;
    }
    article > div {
        position: relative;
    }
</style>