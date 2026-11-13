import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// base './' keeps the build relocatable (GitHub Pages project sites, Cloudflare Pages, or a plain folder)
export default defineConfig({ base: './', plugins: [react()] })
