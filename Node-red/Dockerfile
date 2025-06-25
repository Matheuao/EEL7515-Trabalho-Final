FROM nodered/node-red

USER root

# Usa apk (gerenciador de pacotes do Alpine) para instalar dependências
RUN apk add --no-cache \
    build-base \
    python3 \
    g++ \
    sqlite \
    sqlite-dev

# Instala os nodes adicionais
RUN npm install --unsafe-perm --no-update-notifier --no-fund --only=production \
    node-red-dashboard \
    node-red-contrib-web-worldmap \
    node-red-node-sqlite \
    && npm install -g localtunnel

USER node-red
