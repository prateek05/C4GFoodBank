# Use an official node runtime as a parent image
FROM node:17-alpine as build

WORKDIR /app/

# Install dependencies
COPY package.json  .
COPY package-lock.json .

RUN npm ci --silent

# Add rest of the client code
COPY . .


RUN npm run-script build

FROM nginx:stable-alpine
RUN  rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]