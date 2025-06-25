import subprocess
import json
import threading

def processar_linha(linha):
    try:
        mensagem = json.loads(linha)
        # Extrai decoded_payload
        decoded_payload = mensagem.get("uplink_message", {}).get("decoded_payload", {})
        dados = decoded_payload

        # Remove decoded_payload para formar os meta_dados
        meta_dados = mensagem.copy()
        if "uplink_message" in meta_dados and "decoded_payload" in meta_dados["uplink_message"]:
            del meta_dados["uplink_message"]["decoded_payload"]

        print("\n--- NOVA MENSAGEM ---")
        print("Dados decodificados:")
        print(dados)
        print("Meta dados:")
        print(meta_dados)
    except json.JSONDecodeError as e:
        print("Erro ao decodificar JSON:", e)
    except Exception as e:
        print("Erro ao processar linha:", e)

def executar_mqtt():
    comando = [
        "mosquitto_sub",
        "-h", "au1.cloud.thethings.network",
        "-p", "1883",
        "-u", "trabalhofinal@ttn",
        "-P", "NNSXS.FTAGPKCEE3Z3YJBIJY2GCTIJATN765PWKBNRAUA.7NMWN5GNMXNJXMTPCVJ4SXHOSCMD3KFMB5VUN66FK5R4S5257YLQ",
        "-t", "v3/trabalhofinal@ttn/devices/forest1/up"
    ]

    processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for linha in processo.stdout:
        linha = linha.strip()
        if linha:
            processar_linha(linha)

if __name__ == "__main__":
    thread_mqtt = threading.Thread(target=executar_mqtt)
    thread_mqtt.daemon = True
    thread_mqtt.start()

    print("Aguardando mensagens MQTT da TTN. Pressione Ctrl+C para sair.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nEncerrando o programa.")
