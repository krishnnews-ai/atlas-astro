import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    slug: z.string().optional(),
    draft: z.boolean().default(false),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional().nullable().or(z.literal('')),
    author: z.string().default('Coin AI News Team'),
    category: z.string().default('Bitcoin News'),
    tags: z.array(z.string()).optional().default([]),
    description: z.string().optional(),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    canonicalURL: z.string().optional(),
  }).passthrough(),
});

export const collections = { blog };
