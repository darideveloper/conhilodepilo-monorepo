// @ts-check
import { defineConfig } from 'astro/config';

import sitemap from '@astrojs/sitemap';
import react from '@astrojs/react';
import mdx from '@astrojs/mdx';
import tailwindcss from '@tailwindcss/vite';
import dotenv from 'dotenv';
import path from 'path';

// 1. Load base .env to determine ENV
dotenv.config({ path: path.resolve(process.cwd(), '.env') });
const envMode = process.env.ENV || 'dev';

// 2. Load context-specific .env
dotenv.config({ path: path.resolve(process.cwd(), `.env.${envMode}`), override: true });

const apiUrl = process.env.PUBLIC_API_URL || 'http://localhost:8000';
let apiHostname = 'localhost';
try {
  apiHostname = new URL(apiUrl).hostname;
} catch (e) {}

// https://astro.build/config
export default defineConfig({
  site: 'https://conhilodepilo.com',
  integrations: [sitemap(), react(), mdx()],

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

  image: {
    remotePatterns: [
      {
        protocol: apiUrl.startsWith('https') ? 'https' : 'http',
        hostname: apiHostname,
      }
    ]
  }
});