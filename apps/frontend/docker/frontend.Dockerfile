FROM node:21-alpine3.17 as builder

WORKDIR /app
 
COPY . .

RUN npm install --force
RUN npx webpack --env mode=production

# Run the application.
ENTRYPOINT ["node","--env-file",".env", "server.cjs"]