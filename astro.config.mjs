import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  output: 'static',
  site: 'https://columbusconcretecontractor.co',
  compressHTML: true,
  build: {
    inlineStylesheets: 'auto'
  }
});
