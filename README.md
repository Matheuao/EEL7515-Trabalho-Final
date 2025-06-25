

# Projeto LoRaWAN Forest — Monitoramento Acústico de Florestas 🌳📡

Este projeto tem como objetivo implementar uma prova de conceito para a tarefa de **monitoramento acústico de florestas** utilizando conectividade **LoRaWAN**, um backend baseado em **Node-RED** para aquisição, visualização e armazenamento dos dados, e scripts auxiliares em Python para apoio à análise e manutenção.

---

## 🔧 Tecnologias utilizadas

- **C (bare-metal)** para programação do dispositivo embarcado
- **MQTT** via **The Things Network (TTN)**
- **Node-RED** com **SQLite** para backend e dashboard
- **Python** para scripts de utilidade
- **Docker** para empacotamento e portabilidade da aplicação
- **LocalTunnel** para acesso remoto ao dashboard

---

## 🗂️ Estrutura do projeto

O projeto está organizado em três diretórios principais, cada um com seu próprio `README.md` explicando como usar:

### `LoRaWANForest/` — Código do dispositivo embarcado

Contém o firmware escrito em **C**, responsável por capturar e transmitir dados acústicos via LoRaWAN.

- Envio de pacotes para a TTN

[Veja o `README.md` da pasta `LoRaWANForest`](./LoRaWANForest/README.md)

OBS: o payload contem dados ficticiosl, em uma aplicação real os dados são gerados por um modelo de machine learning, em futuros trabalhos pretendemos fazer isso.

---

### `Node-red/` — Backend e dashboard

Contém os arquivos usados pela aplicação Node-RED, como:

- `Dockerfile` para criar a imagem personalizada
- Banco de dados `floresta.db` (SQLite)
- Flows do Node-RED e configuração MQTT com TTN
- Scripts de inicialização e integração com **LocalTunnel**

[Veja o `README.md` da pasta `Node-red`](./Node-red/README.md)

---

### `scripts/` — Utilitários em Python

Scripts para:

- Consulta e verificação do banco de dados
- Testes de conexão MQTT
- Conversão de payloads
- Auxílio ao debug de dados

[Veja o `README.md` da pasta `scripts`](./scripts/README.md)

---

## 🚀 Como rodar o projeto

As instruções completas estão no `README.md` da pasta `Node-red`, mas o fluxo básico é:

```bash
# Construir a imagem Docker
sudo docker build -t trabalho_iot ./Node-red

# Criar a pasta com o banco de dados
mkdir projeto
cp Node-red/floresta.db ./projeto/
sudo chown 1000:1000 ./projeto/floresta.db

# Executar o container
sudo docker run -it -p 1880:1880 -v ./projeto:/data --name florest1 trabalho_iot

# Instalar e rodar o LocalTunnel (uma vez)
sudo npm install -g localtunnel
lt --port 1880
````

Acesse a interface via:

```
https://<seu-endereco-localtunnel>.loca.lt/ui
```

A senha de acesso é seu **endereço IP público**, que pode ser verificado em:

```
https://nordvpn.com/pt-br/what-is-my-ip/
```

---

## ❗ Observação sobre a TTN

Para que a aplicação funcione corretamente, é necessário que a sua aplicação esteja registrada na **The Things Network (TTN)** e que a **App Access Key** esteja válida.

Se necessário, **gere uma nova App Key** na plataforma TTN.

---

## 👥 Autoria

Projeto desenvolvido como parte de um trabalho acadêmico de IoT, com foco em aplicações ambientais baseadas em LoRaWAN e análise local dos dados.

Autores: Matheus A. de Oliveira e Pedro F. Bender

---


