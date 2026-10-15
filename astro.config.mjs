import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.coinainews.com',
  integrations: [sitemap()],
  build: { format: 'directory' },
  redirects: {
    '/20/:month/:slug.html': '/:slug/',
    '/20/:year/:month/:slug.html': '/:slug/',
    '/p/:slug.html': '/:slug/'
  }
});
