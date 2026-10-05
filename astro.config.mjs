import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build
export default defineConfig({
  site: 'https://www.coinainews.com',
  integrations: [sitemap()],
  build: { format: 'directory' },
  redirects: {
    '/2026/:month/:slug.html': '/:slug/'
  }
});
