FROM node:21-alpine3.17

WORKDIR /app
 
COPY package.json .

RUN npm install --force
 
COPY . .
 
# Run the application.
CMD ["npm","start"]