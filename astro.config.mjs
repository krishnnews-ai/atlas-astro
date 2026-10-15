import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build
export default defineConfig({
  site: 'https://www.coinainews.com',
  integrations: [
    sitemap({
      filter: (page) => {
        // Dummy posts ko sitemap se hatao
        const DUMMY_SLUGS = [
          'blog-post',
          'coconut-curry-soup-with-chickpeas',
          'dark-chocolate-self-saucing-pudding',
          'delicious-chicken-meatball-soup',
          'fairy-potion-summer-fruit-drink',
          'fashion-tips-trends-and-celebrity-style',
          'fruit-yogurt-easy-homemade-fruit-drink',
          'healthy-chicken-and-rice-soup',
          'melt-and-mix-chocolate-and-ginger-mud-cake',
          'pecan-chocolate-bread-and-butter',
          'refreshing-summer-fruit-drink',
          'spicy-crispy-chicken-burger-recipe',
          'spiked-strawberry-slushies-for-a-crowd',
          'tomato-bisque-with-fried-cheese',
          'tortellini-soup-with-italian-sausage-and-kale',
          'vegan-chocolate-avocado-milkshakes',
          'wild-mushroom-chowder-with-leeks',
          'why-do-restaurant-burgers-taste-better',
          'a-mild-sweet-fruit-with-a-fibrous-center',
          'always-keep-your-drone-within-the-vlos',
          'comfortable-pairs-of-sneakers-to-walk-all-day',
          'essential-tech-tips-for-your-business',
          'finally-found-a-work-computer-setup-thats-practically-perfect',
          'for-good-results-must-be-make-good-plan',
          'gadgets-that-will-upgrade-your-home',
          'headsets-are-better-if-youre-playing-games',
          'hot-new-releases-in-audio-headphones',
          'how-to-do-the-superman-standing-exercise',
          'how-to-organize-and-write-content-for',
          'in-fact-certainly-influenced-seldes-the-leftist-journalist-i-f-stone',
          'laptops-tend-to-be-smaller-than-desktops',
          'laugh-cry-and-learn-within-virtual-reality',
          'make-your-gaming-setup-look-better',
          'make-your-phone-feel-new-again',
          'mistakes-you-might-be-making-with-your-watch',
          'mobile-camera-makes-a-huge-leap-in-quality',
          'rugby-african-ations-are-singing-to-save-their-wildlif',
          'surprising-benefits-of-honeydew-melon',
          'the-inbound-marketing-methodology-method-of-drawing-the-right',
          'the-secret-of-buzzfeeds-success-has-a-lot-to-do-with-the-image-heavy',
          'there-are-several-differences-between-outbound',
          'tips-to-ensure-you-always-look-stylish',
          'top-12-health-benefits-of-eating-grapes',
          'top-classic-style-inspiration-ideas',
          'top-mens-fashion-trends-from-spring',
          'vr-headset-virtual-reality-glasses',
          'will-humans-be-able-to-live-in-mars-in-the-future',
          'winter-dressing-tips-when-its-really-cold-out'
        ];

        // Agar URL mein dummy slug hai, toh exclude karo
        for (const slug of DUMMY_SLUGS) {
          if (page.includes(`/${slug}/`)) return false;
        }

        // Tag pages, author pages, search page exclude karo
        if (page.includes('/tag/')) return false;
        if (page.includes('/author/')) return false;
        if (page.includes('/search/')) return false;
        if (page.includes('/404')) return false;

        return true;
      },
    }),
  ],
  build: { format: 'directory' },
  redirects: {
    '/2026/:month/:slug.html': '/:slug/'
  }
});
