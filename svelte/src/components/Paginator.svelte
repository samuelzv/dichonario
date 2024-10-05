<script>
    /**
     * @type {import('$lib/types').I18n}
     */
    export let i18n;

    /**
     * @type {import('$lib/types').Pagination}
     */
    export let pagination;

    const current_url = window.location.href
    console.log(current_url);

    /**
     * @param {'previous'|'next'} type
     */
    function make_pagination_url(type) {
        const url = new URL(window.location.href);
        if (type === 'previous' && pagination.previous_page) {
            url.searchParams.set('page', pagination.previous_page.toString());
            return url.href;
        } 
        if (type === 'next' && pagination.next_page) {
            url.searchParams.set('page', pagination.next_page.toString());
            return url.href;
        }

        return 'javascript:void(0)';
    }
</script>

{#if pagination.total_records > 1}
    <div class="row center-xs">
        <div class="col-xm-12">
            <a href="{make_pagination_url('previous')}">
                <button type="button" title="{i18n.previous_page}" class="outline secondary" disabled={!pagination.has_previous}>
                    &lt;
                </button>
            </a>
            <span>Page 1 from 5</span>
            <a href="{make_pagination_url('next')}">
                <button type="button" title="{i18n.next_page}" class="outline secondary" disabled={!pagination.has_next}>
                    &gt;
                </button>
            </a>
        </div>
    </div>
{/if}

<style>
    button[disabled] {
        cursor: not-allowed;
    }
</style>