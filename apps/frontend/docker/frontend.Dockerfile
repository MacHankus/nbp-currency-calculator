FROM node:21-alpine3.17

WORKDIR /app
 
COPY . .

RUN npm install --force
 

# Run the application.
CMD ["npm","start"]