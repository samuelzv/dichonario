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
        'src/ThemeToggle.js',
        'src/LanguageToggle.js',
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
