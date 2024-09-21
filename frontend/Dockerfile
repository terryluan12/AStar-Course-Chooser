FROM node:21.5 AS base

# Install dependencies only when needed
FROM base AS deps
WORKDIR /astar
COPY package.json package-lock.json* ./
RUN npm ci

# Rebuild the source code only when needed
FROM base AS builder
WORKDIR /astar
COPY --from=deps /astar/node_modules ./node_modules
COPY . .

# Production image, copy all the files and run next
FROM base AS runner
WORKDIR /astar
ENV NODE_ENV=production
COPY --from=builder /astar/public ./public

# Set the correct permission for prerender cache
RUN mkdir .next
RUN ls -l

# Automatically leverage output traces to reduce image size
# https://nextjs.org/docs/advanced-features/output-file-tracing
COPY --from=builder /astar/.next/standalone ./
COPY --from=builder /astar/.next/static ./.next/static

EXPOSE 3000
ENV PORT=3000

CMD [ "node", "server.js" ]
