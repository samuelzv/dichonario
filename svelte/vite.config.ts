import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    rollupOptions: {
      input: [
        // 'src/main-app.js',
        'src/components-js/main-type-writer-1.js',
        'src/components-js/main-type-writer-2.js',
        'src/components-js/main-type-writer-3.js',
        'src/components-js/main-type-writer-4.js',
        'src/components-js/main-neon-text.js'
      ],
    },
    manifest: true,
  },
  plugins: [svelte()],
})
