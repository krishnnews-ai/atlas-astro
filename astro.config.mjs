import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://coinainews.com',
  integrations: [sitemap()],
  // Static output → deployed to Cloudflare Pages via `wrangler pages deploy ./dist`.
  build: { format: 'directory' },
});
