import { defineConfig } from 'vite'
import { run } from 'vite-plugin-run'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import path from "path";

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
        'src/components-js/main-neon-text.js',
        'src/Card.js',
        'src/BlockQuote.js',
        'src/QuoteList.js',
        'src/SearchModal.js',
        'src/CardIsInView.js',
        'src/Paginator.js',
        'src/ThemeToggle.js',
      ],
    },
    manifest: true,
  },
  plugins: [
    svelte(),
    run([
      {
        name: 'docker restart web app',
        run: ['docker', 'restart', 'dichonario-app-1'],
        startup: true,
      }
    ]),
  ],
  resolve: {
    alias: {
      src: path.resolve(__dirname, "./src"),
    },
  },
})
