import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const legal = defineCollection({
	loader: glob({ pattern: "**/*.mdx", base: "./src/content/legal" }),
	schema: z.object({
		title: z.string(),
		lastUpdated: z.string().optional(),
	}),
});

export const collections = {
	legal: legal,
};
