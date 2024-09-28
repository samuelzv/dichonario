<script>
    import BlockQuote from "./BlockQuote.svelte";
    import Card from './Card.svelte';
</script>

<Card>
    <div slot="body">This is the body</div>
    <div slot="footer">This is the footer</div>
</Card>

<Card>
    <div slot="header">This is the header 2</div>
    <div slot="body">This is the body 2</div>
    <div slot="footer">This is the footer 2</div>
</Card>

<Card>
    <div slot="header">This is the header 3</div>
    <div slot="body">This is the body 3</div>
</Card>

<style>
</style>