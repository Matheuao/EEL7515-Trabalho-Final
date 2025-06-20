# TTN Payload Handler

Este repositório contém dois scripts em Python que facilitam a **comunicação com a The Things Network (TTN)** usando MQTT e a **geração de payloads codificados** para serem enviados por dispositivos LoRaWAN. É útil para testes, simulações e monitoramento de dispositivos conectados à TTN.

---

## 📁 Arquivos

### `payload_local.py`
Script que escuta em tempo real os uplinks de um dispositivo registrado na TTN, usando `mosquitto_sub` (cliente MQTT). Ao receber uma nova mensagem, ele:

- Faz o parsing do JSON.
- Separa os campos decodificados (`decoded_payload`) dos metadados.
- Imprime os dois conjuntos de dados de forma clara no terminal.

#### Principais funções:
- `executar_mqtt()`: inicia o processo `mosquitto_sub` com as credenciais do TTN.
- `processar_linha(linha)`: separa e imprime os dados úteis e metadados da mensagem recebida.

> **Pré-requisito:** o comando `mosquitto_sub` deve estar instalado no sistema (`sudo apt install mosquitto-clients`).

---

### `utils.py`
Script utilitário para simular um payload LoRaWAN a partir de um dicionário com os seguintes campos:

- `latitude`: float entre -90 e +90 graus
- `longitude`: float entre -180 e +180 graus
- `classe`: inteiro entre 0 e 255 (pode representar um tipo de evento, sensor, etc.)
- `battery`: inteiro entre 0 e 255 (nível de bateria)

A função `gerar_payload_hex` codifica esses dados em um payload hexadecimal, conforme a estrutura abaixo:

| Campo      | Bits | Descrição                              |
|------------|------|----------------------------------------|
| Latitude   | 16   | Latitude normalizada e codificada      |
| Longitude  | 16   | Longitude normalizada e codificada     |
| Classe     | 8    | Classe do evento ou tipo               |
| Bateria    | 8    | Nível da bateria                       |

Exemplo de uso incluso no próprio arquivo.

---

## ▶️ Como executar

### 1. Escutar dados em tempo real da TTN:

```bash
python3 payload_local.py
