import socket
import json
import urllib.request
import configparser
import os

# .ini dosyasından ayarları yükle
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

SERVER_IP = config.get('SiberConfig', 'server_ip', fallback='127.0.0.1')
SERVER_PORT = config.getint('SiberConfig', 'server_port', fallback=9999)

def get_ip_details():
    try:
        url = "http://ip-api.com/json/"
        response = urllib.request.urlopen(url, timeout=5)
        data = json.loads(response.read().decode())
        
        return {
            "ip": data.get("query", "Bilinmiyor"),
            "ulke": data.get("country", "Bilinmiyor"),
            "sehir": data.get("regionName", "Bilinmiyor"),
            "isp": data.get("isp", "Bilinmiyor"),
            "status": "SUCCESS"
        }
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}

def send_data_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        payload = get_ip_details()
        json_data = json.dumps(payload)
        client_socket.send(json_data.encode('utf-8'))
        print(f"[+] Siber veriler {SERVER_IP}:{SERVER_PORT} adresine fırlatıldı.")
    except Exception as e:
        print(f"[-] Server'a bağlanılamadı ({SERVER_IP}:{SERVER_PORT}): {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    send_data_to_server()