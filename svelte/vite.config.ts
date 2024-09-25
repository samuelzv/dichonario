import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    rollupOptions: {
      input: [
        // 'src/main-app.js',
        'src/main-type-writer.js'
      ],
    },
    manifest: true,
  },
  plugins: [svelte()],
})
