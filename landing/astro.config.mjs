// @ts-check
import { defineConfig } from 'astro/config';

import sitemap from '@astrojs/sitemap';

import react from '@astrojs/react';

import tailwindcss from '@tailwindcss/vite';
import { loadEnv } from 'vite';

const env = loadEnv(process.env.NODE_ENV || 'development', process.cwd(), '');
const apiUrl = env.PUBLIC_API_URL || 'http://localhost:8000';
let apiHostname = 'localhost';
try {
  apiHostname = new URL(apiUrl).hostname;
} catch (e) {}

// https://astro.build/config
export default defineConfig({
  site: 'https://conhilodepilo.com',
  integrations: [sitemap(), react()],

  vite: {
    plugins: [tailwindcss()],
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