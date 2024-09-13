FROM node:21.5
EXPOSE 3000
WORKDIR /astar
COPY . .
RUN npm i
RUN npm run build
CMD [ "npm", "start" ]
