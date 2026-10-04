import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.coinainews.com',
  integrations: [sitemap()],
  build: { format: 'directory' },
});
