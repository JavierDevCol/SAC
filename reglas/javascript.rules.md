# Reglas de Detección: JavaScript / TypeScript / Node.js

```yaml
descripcion: "Detección de stack en proyectos JavaScript/TypeScript"
archivos: ["package.json", "tsconfig.json"]

# =============================================================================
# GESTOR DE PAQUETES
# =============================================================================
gestor:
  npm: { lock: "package-lock.json", install: "npm install", run: "npm run" }
  yarn: { lock: "yarn.lock", install: "yarn", run: "yarn" }
  pnpm: { lock: "pnpm-lock.yaml", install: "pnpm install", run: "pnpm" }
  bun: { lock: "bun.lockb", install: "bun install", run: "bun run" }

# =============================================================================
# VERSIÓN
# =============================================================================
version:
  node: "engines.node en package.json | .nvmrc | .node-version"
  typescript: "devDependencies.typescript + tsconfig.json"

# =============================================================================
# FRAMEWORKS FRONTEND
# =============================================================================
frontend:
  react: { detectar: "react", variantes: ["next", "gatsby", "remix", "vite"] }
  vue: { detectar: "vue", variantes: ["nuxt"] }
  angular: { detectar: "@angular/core" }
  svelte: { detectar: "svelte", variantes: ["@sveltejs/kit"] }
  solid: { detectar: "solid-js" }

# =============================================================================
# FRAMEWORKS BACKEND
# =============================================================================
backend:
  express: { detectar: "express" }
  fastify: { detectar: "fastify" }
  nestjs: { detectar: "@nestjs/core" }
  hono: { detectar: "hono" }
  koa: { detectar: "koa" }

# =============================================================================
# DEPENDENCIAS CLAVE
# =============================================================================
dependencias:
  orm: ["prisma", "typeorm", "drizzle-orm", "sequelize", "mongoose"]
  validacion: ["zod", "yup", "joi", "class-validator"]
  state: ["@reduxjs/toolkit", "zustand", "jotai", "@tanstack/react-query"]
  ui: ["tailwindcss", "@mui/material", "@chakra-ui/react", "shadcn"]
  auth: ["next-auth", "passport", "@clerk/nextjs"]

# =============================================================================
# TESTING
# =============================================================================
testing:
  unit: ["jest", "vitest", "mocha"]
  e2e: ["cypress", "@playwright/test", "puppeteer"]
  component: ["@testing-library/react", "@testing-library/vue"]

# =============================================================================
# FRAMEWORKS BACKEND
# =============================================================================
frameworks_backend:
  express:
    detectar: "dependencies.express"
    version: "dependencies.express"
    significa: "Express.js - Framework minimalista"
    ejemplo: '"express": "^4.18.0"'
  
  nestjs:
    detectar: "dependencies.@nestjs/core"
    version: "dependencies.@nestjs/core"
    significa: "NestJS - Framework empresarial con DI"
    ejemplo: '"@nestjs/core": "^10.0.0"'
    dependencias_comunes:
      typeorm: "@nestjs/typeorm → ORM integration"
      prisma: "@nestjs/prisma → Prisma integration"
      swagger: "@nestjs/swagger → OpenAPI docs"
      passport: "@nestjs/passport → Authentication"
      graphql: "@nestjs/graphql → GraphQL support"
  
  fastify:
    detectar: "dependencies.fastify"
    version: "dependencies.fastify"
    significa: "Fastify - Framework de alto rendimiento"
  
  koa:
    detectar: "dependencies.koa"
    version: "dependencies.koa"
    significa: "Koa - Framework minimalista (creadores de Express)"
  
  hono:
    detectar: "dependencies.hono"
    significa: "Hono - Framework ultraligero, edge-ready"
  
  adonis:
    detectar: "dependencies.@adonisjs/core"
    significa: "AdonisJS - Framework full-featured"

# =============================================================================
# ORMs Y BASES DE DATOS
# =============================================================================
persistencia:
  prisma:
    detectar: "@prisma/client"
    config: "prisma/schema.prisma"
    significa: "Prisma ORM - Type-safe database client"
    comandos:
      generate: "npx prisma generate"
      migrate: "npx prisma migrate dev"
      studio: "npx prisma studio"
  
  typeorm:
    detectar: "typeorm"
    significa: "TypeORM - ORM con decoradores"
  
  sequelize:
    detectar: "sequelize"
    significa: "Sequelize - ORM tradicional"
  
  drizzle:
    detectar: "drizzle-orm"
    significa: "Drizzle ORM - Type-safe, ligero"
  
  mongoose:
    detectar: "mongoose"
    significa: "Mongoose - ODM para MongoDB"
  
  knex:
    detectar: "knex"
    significa: "Knex.js - Query builder SQL"

# =============================================================================
# DEPENDENCIAS COMUNES
# =============================================================================
dependencias_clave:
  http_clients:
    axios: "axios → Cliente HTTP con interceptors"
    fetch: "node-fetch | undici → Fetch API"
    ky: "ky → Wrapper moderno sobre fetch"
  
  validacion:
    zod: "zod → Schema validation con inferencia TS"
    yup: "yup → Schema validation"
    joi: "joi → Schema validation (más antiguo)"
    class_validator: "class-validator → Validación con decoradores"
  
  utilidades:
    lodash: "lodash → Utilidades de manipulación"
    date_fns: "date-fns → Manejo de fechas (modular)"
    dayjs: "dayjs → Manejo de fechas (ligero)"
    luxon: "luxon → Manejo de fechas (completo)"
    uuid: "uuid → Generación de UUIDs"
    nanoid: "nanoid → IDs cortos únicos"
  
  estilos:
    tailwind: "tailwindcss → CSS utility-first"
    styled_components: "styled-components → CSS-in-JS"
    emotion: "@emotion/react → CSS-in-JS"
    sass: "sass → Preprocesador CSS"
    postcss: "postcss → Transformaciones CSS"
  
  ui_libraries:
    shadcn: "@radix-ui/* → Base de shadcn/ui"
    material_ui: "@mui/material → Material Design"
    chakra: "@chakra-ui/react → Component library"
    ant_design: "antd → Ant Design"
    headless_ui: "@headlessui/react → Unstyled components"

# =============================================================================
# TESTING
# =============================================================================
testing:
  jest:
    detectar: "jest | @jest/core"
    config: "jest.config.js | jest.config.ts"
    significa: "Jest - Framework de testing completo"
  
  vitest:
    detectar: "vitest"
    config: "vitest.config.ts"
    significa: "Vitest - Testing nativo para Vite"
  
  mocha:
    detectar: "mocha"
    significa: "Mocha - Framework flexible"
    complementos: "chai (assertions), sinon (mocking)"
  
  testing_library:
    detectar: "@testing-library/react | @testing-library/vue"
    significa: "Testing Library - Tests centrados en usuario"
  
  cypress:
    detectar: "cypress"
    config: "cypress.config.js | cypress.config.ts"
    significa: "Cypress - E2E testing"
  
  playwright:
    detectar: "@playwright/test"
    config: "playwright.config.ts"
    significa: "Playwright - E2E testing multi-browser"

# =============================================================================
# BUILD TOOLS
# =============================================================================
build_tools:
  vite:
    detectar: "vite"
    config: "vite.config.ts | vite.config.js"
    significa: "Vite - Build tool moderno y rápido"
  
  webpack:
    detectar: "webpack"
    config: "webpack.config.js"
    significa: "Webpack - Bundler tradicional"
  
  esbuild:
    detectar: "esbuild"
    significa: "esbuild - Bundler ultrarrápido"
  
  rollup:
    detectar: "rollup"
    config: "rollup.config.js"
    significa: "Rollup - Bundler para librerías"
  
  turbo:
    detectar: "turbo"
    config: "turbo.json"
    significa: "Turborepo - Monorepo build system"
  
  nx:
    detectar: "nx"
    config: "nx.json"
    significa: "Nx - Monorepo toolkit"

# =============================================================================
# COMANDOS DE SCRIPTS
# =============================================================================
scripts_comunes:
  buscar_en: "package.json > scripts"
  mapeo:
    dev: "Servidor de desarrollo"
    start: "Iniciar aplicación"
    build: "Build de producción"
    test: "Ejecutar tests"
    lint: "Linting de código"
    format: "Formatear código"
    preview: "Preview del build"

# =============================================================================
# CONVENCIONES DEL ECOSISTEMA
# =============================================================================
convenciones:
  estructura_carpetas:
    nextjs:
      - "app/ → App Router (Next.js 13+)"
      - "pages/ → Pages Router (legacy)"
      - "components/ → Componentes React"
      - "lib/ → Utilidades"
      - "public/ → Assets estáticos"
    
    nestjs:
      - "src/modules/ → Módulos de la aplicación"
      - "src/common/ → Código compartido"
      - "src/config/ → Configuración"
      - "test/ → Tests E2E"
    
    general:
      - "src/ → Código fuente"
      - "dist/ | build/ → Output de build"
      - "node_modules/ → Dependencias"
  
  archivos_configuracion:
    typescript: "tsconfig.json"
    eslint: ".eslintrc.js | .eslintrc.json | eslint.config.js"
    prettier: ".prettierrc | .prettierrc.js"
    git: ".gitignore"
    env: ".env | .env.local | .env.development | .env.production"
  
  naming:
    componentes: "PascalCase (UserCard.tsx, Button.vue)"
    hooks: "camelCase con prefijo use (useAuth, useState)"
    utilidades: "camelCase (formatDate, parseJson)"
    constantes: "UPPER_SNAKE_CASE o camelCase"
    archivos: "kebab-case o camelCase según proyecto"
```
