// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import react from '@astrojs/react';
import node from '@astrojs/node';
import dotenv from 'dotenv';
import path from 'path';

// 1. Load base .env to determine ENV
dotenv.config({ path: path.resolve(process.cwd(), '.env') });
const envMode = process.env.ENV || 'dev';

// 2. Load context-specific .env
dotenv.config({ path: path.resolve(process.cwd(), `.env.${envMode}`), override: true });

// https://astro.build/config
export default defineConfig({
  output: 'server',
  adapter: node({
    mode: 'standalone',
  }),
  vite: {
    plugins: [tailwindcss()],
    // Ensure Vite passes the explicitly loaded PUBLIC_ variables to the client
    define: Object.keys(process.env)
      .filter(key => key.startsWith('PUBLIC_'))
      .reduce((acc, key) => {
        acc[`import.meta.env.${key}`] = JSON.stringify(process.env[key]);
        return acc;
      }, {})
  },
  integrations: [react()]
});