# Design: Tours API

This design outlines the implementation of a local JSON mirror and an Astro endpoint to serve it.

## Architecture

### Data Layer
The data will be stored in `src/data/tours.json`. This file is a direct copy of the external source. Storing it in `src/` allows for better integration with Astro's build process if we decide to use it for static site generation later, and keeps it out of the `public/` folder to avoid direct file serving if we want to add logic (like filtering or transformation) in the API layer.

### API Layer
An Astro endpoint will be created at `src/pages/api/tours.json.ts`.
- **Method**: GET
- **Format**: JSON
- **Endpoint**: `/api/tours.json`

## Implementation Details

### Copying Data
We will use a simple shell command to copy the data initially.
```bash
cp /mnt/hd/develop/vanilla/granada-go-custom-code/tours.json src/data/tours.json
```

### Endpoint Implementation
The endpoint will import the JSON file directly or use `fs` if preferred. Importing is more idiomatic in Astro/Vite environments.

```typescript
import tours from '../../data/tours.json';

export const GET = async () => {
  return new Response(JSON.stringify(tours), {
    status: 200,
    headers: {
      'Content-Type': 'application/json'
    }
  });
};
```

## Alternatives Considered

### Direct Serving from `public/`
- **Pros**: Zero code, just copy file.
- **Cons**: No ability to add headers (CORS, cache-control) easily or transform data in the future without moving it.

### Fetching on Request
- **Pros**: Data is always fresh.
- **Cons**: Depends on external file system being accessible at runtime (might not be in production environments like Vercel/Netlify). Local mirroring is safer for static/edge deployments.
