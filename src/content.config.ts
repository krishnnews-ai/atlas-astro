import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    slug: z.string().optional(),
    // draft ko strict boolean banane ke bajaye loose rakhein taaki missing hone par false ho jaye
    draft: z.preprocess((val) => val === true || val === 'true', z.boolean()).default(false),
    
    // pubDate chahe ISO string ho, timezone ke sath ho, ya date object - yeh hamesha safely parse karega
    pubDate: z.preprocess((val) => {
      if (!val) return new Date();
      const parsed = new Date(val as string | number | Date);
      return isNaN(parsed.getTime()) ? new Date() : parsed;
    }, z.date()),

    updatedDate: z.preprocess((val) => {
      if (!val) return undefined;
      const parsed = new Date(val as string | number | Date);
      return isNaN(parsed.getTime()) ? undefined : parsed;
    }, z.date().optional().nullable()),

    author: z.string().optional().default('Coin AI News Team'),
    category: z.string().optional().default('Bitcoin News'),
    tags: z.array(z.string()).optional().default([]),
    description: z.string().optional(),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    canonicalURL: z.string().optional(),
  }).passthrough(),
});

export const collections = { blog };
