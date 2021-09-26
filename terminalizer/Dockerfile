FROM node:16

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin

RUN apt-get update && apt-get install -y \
    curl \
    xvfb \
    libgtk-3-0 libnss3 libasound2 \
    libxss1 libgconf-2-4 \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

USER node
RUN npm install -g terminalizer --unsafe-perm=true --allow-root

USER root
RUN chown root: /home/node/.npm-global/lib/node_modules/terminalizer/node_modules/electron/dist/chrome-sandbox && chmod 4755 /home/node/.npm-global/lib/node_modules/terminalizer/node_modules/electron/dist/chrome-sandbox

USER node

COPY config.yml /home/node/.terminalizer/config.yml

WORKDIR /home/node/gifs
