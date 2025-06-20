def gerar_payload_hex(dados):
    """
    Gera um payload hexadecimal a partir de um dicionário de dados com os campos:
    - latitude: float em graus (-90 a +90)
    - longitude: float em graus (-180 a +180)
    - classe: int (0 a 255)
    - battery: int (0 a 255)
    """
    from struct import pack

    # Constantes
    MAX_UINT16 = 2**16 - 1  # 65535
    MAX_UINT8 = 2**8 - 1    # 255

    # Normalização da latitude (-90 a 90) → [0, 1]
    lat_norm = (dados['latitude'] + 90) / 180
    lat_encoded = int(lat_norm * MAX_UINT16)

    # Normalização da longitude (-180 a 180) → [0, 1]
    lon_norm = (dados['longitude'] + 180) / 360
    lon_encoded = int(lon_norm * MAX_UINT16)

    # Classe (8 bits)
    classe = dados['classe'] & MAX_UINT8

    # Battery (8 bits)
    battery = dados['battery'] & MAX_UINT8

    # Empacota em bytes: > = big endian, H = uint16, B = uint8
    payload_bytes = pack('>HHBB', lat_encoded, lon_encoded, classe, battery)

    # Converte para hexadecimal
    payload_hex = payload_bytes.hex().upper()
    return payload_hex


dados_exemplo = {
    'latitude':-27.600686079889304,
    'longitude':-48.51745291535339,
    'classe': 2,
    'battery': 88
}

payload = gerar_payload_hex(dados_exemplo)
print(f"Payload gerado (hex): {payload}")
