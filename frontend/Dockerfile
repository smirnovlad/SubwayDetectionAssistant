FROM node:21.2

WORKDIR /usr/src/app

COPY . .

COPY ./package.json .
COPY ./package-lock.json .

RUN npm install -g serve
RUN npm install

RUN npm run build