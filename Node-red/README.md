Claro! Abaixo está um `README.md` bem organizado e claro para que qualquer pessoa consiga rodar seu projeto IoT com Node-RED, Docker, MQTT (TTN), SQLite e LocalTunnel.

---

````markdown
# Projeto IoT - Monitoramento com Node-RED + TTN + SQLite

Este projeto é uma aplicação Node-RED empacotada com Docker, que se conecta à The Things Network (TTN) via MQTT, armazena os dados recebidos em um banco de dados SQLite e disponibiliza um painel (`dashboard`) acessível pela internet via LocalTunnel.

---

## ✅ Pré-requisitos

- Docker e Docker Compose instalados
- Node.js e npm instalados
- Banco de dados `floresta.db` fornecido ou gerado no primeiro uso
- Acesso a uma aplicação na TTN com App Access Key ativa

---

## 🛠️ Instalação

### 1. Clone ou copie este repositório

```bash
git clone <este_repositorio>
cd <pasta_do_projeto>
````

### 2. Construa a imagem Docker do projeto

```bash
sudo docker build -t trabalho_iot .
```

### 3. Crie a pasta de dados e adicione o banco SQLite

```bash
mkdir projeto
cp floresta.db ./projeto/floresta.db
sudo chown 1000:1000 ./projeto/floresta.db
```

### 4. Rode o container com volume montado

```bash
sudo docker run -it -p 1880:1880 -v ./projeto:/data --name florest1 trabalho_iot
```

---

## 🌐 Tornar o painel acessível via internet

### 1. Instale o LocalTunnel globalmente

```bash
sudo npm install -g localtunnel
```

### 2. Execute o LocalTunnel apontando para a porta do Node-RED

```bash
lt --port 1880
```

### 3. Acesse o dashboard

Pegue a URL gerada pelo localtunnel, por exemplo:

```
https://exemplo.loca.lt
```

E **acrescente `/ui` no final**:

```
https://exemplo.loca.lt/ui
```

---

## 🔐 Senha do dashboard

A senha de acesso é o seu **endereço IP público**.
Você pode obtê-lo acessando:

```
https://nordvpn.com/pt-br/what-is-my-ip/
```

---

## 🌩️ Integração com The Things Network (TTN)

A aplicação se conecta ao broker MQTT da TTN para receber dados dos dispositivos.

### Configuração do nó MQTT no Node-RED

* **Server:** `eu1.cloud.thethings.network`
* **Porta:** `1883`
* **Username:** `nomedasuaplicacao@ttn`
* **Password:** sua **App Access Key** (começa com `NNSXS...`)
* **Topic:** `v3/nomedasuaplicacao@ttn/devices/+/up`
* **QoS:** `2`

> ⚠️ Talvez seja necessário gerar uma nova App Access Key diretamente na TTN, caso a anterior expire ou seja revogada.

---

## 🧪 Testes

1. Acesse o editor Node-RED via:

   ```
   http://localhost:1880
   ```

2. Ou, caso esteja usando LocalTunnel:

   ```
   https://exemplo.loca.lt
   ```

3. O dashboard estará em `/ui`, por exemplo:

   ```
   https://exemplo.loca.lt/ui
   ```

---

## 📦 Estrutura esperada do projeto

```
.
├── Dockerfile
├── projeto/
│   └── floresta.db
├── flows.json (gerado automaticamente após deploy)
└── README.md
```

---

## 🧹 Parar e limpar containers

```bash
sudo docker stop florest1
sudo docker rm florest1
```

---

## ✅ Dica final

Se ao rodar o projeto aparecer o erro:

```
SQLITE_ERROR: no such table: eventos
```

Verifique se o arquivo `floresta.db` está corretamente copiado para `./projeto/` e se contém a tabela `eventos`. Você pode verificar isso com:

```bash
sqlite3 ./projeto/floresta.db
.tables
```

---

Feito por Matheus A de Oliveira e Pedro F. Bender 

```

---

Se quiser, posso já gerar esse `README.md` como arquivo e te mandar como download. Deseja?
```
