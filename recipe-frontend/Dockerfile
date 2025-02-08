FROM node:16 as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY serve.json /usr/share/nginx/html/serve.json
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]