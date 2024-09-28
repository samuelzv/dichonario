<script></script>

<article>
    {#if $$slots.header}
    <header>
        <slot name="header"></slot>
    </header>
    {/if}

    {#if $$slots.body}
    <body>
        <slot name="body"></slot>
    </body>
    {/if}

    {#if $$slots.footer}
    <footer>
        <slot name="footer"></slot>
    </footer>
    {/if}
</article>

<style></style>