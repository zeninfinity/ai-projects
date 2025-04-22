# Travel Projects

This directory contains travel-related projects, including the Wanderly application.

## Wanderly

Wanderly is a modern travel application built with Next.js 15 and React 19. It features a rich user interface with various components and functionality for travel planning and management.

### Tech Stack

- **Framework**: Next.js 15
- **UI Library**: React 19
- **Styling**: Tailwind CSS with animations
- **Component Library**: Radix UI primitives
- **Form Handling**: React Hook Form with Zod validation
- **State Management**: React Hooks
- **Date Handling**: date-fns
- **Charts**: Recharts
- **Type Safety**: TypeScript

### Project Structure

```
wanderly/
├── app/           # Next.js app directory (pages and layouts)
├── components/    # Reusable UI components
├── hooks/         # Custom React hooks
├── lib/          # Utility functions and configurations
├── public/       # Static assets
├── styles/       # Global styles and Tailwind configuration
└── img/          # Image assets
```

### Features

- Modern, responsive UI with Radix UI components
- Dark/light theme support
- Form validation with Zod
- Interactive charts and data visualization
- Date picker and calendar functionality
- Toast notifications
- Responsive navigation
- Custom animations and transitions

### Getting Started

1. Navigate to the wanderly directory:
   ```bash
   cd wanderly
   ```

2. Install dependencies:
   ```bash
   pnpm install
   ```

3. Run the development server:
   ```bash
   pnpm dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

### Available Scripts

- `pnpm dev`: Start development server
- `pnpm build`: Build for production
- `pnpm start`: Start production server
- `pnpm lint`: Run ESLint 