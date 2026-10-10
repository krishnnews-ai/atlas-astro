import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    slug: z.string().optional(),
    draft: z.boolean().optional().default(false),
    pubDate: z.union([z.string(), z.date()]).transform((val) => new Date(val)),
    updatedDate: z.union([z.string(), z.date()]).optional().nullable().transform((val) => val ? new Date(val) : undefined),
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
