import socket
import json
import urllib.request

# Server bilgileri (Lokalde test için localhost, uzak sunucu için IP yazılır)
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

def get_ip_details():
    try:
        # Güvenilir bir API üzerinden dış IP ve konum bilgilerini çekiyoruz
        url = "http://ip-api.com/json/"
        response = urllib.request.urlopen(url, timeout=5)
        data = json.loads(response.read().decode())
        
        info = {
            "ip": data.get("query", "Bilinmiyor"),
            "ulke": data.get("country", "Bilinmiyor"),
            "sehir": data.get("regionName", "Bilinmiyor"),
            "isp": data.get("isp", "Bilinmiyor"),
            "status": "SUCCESS"
        }
        return info
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}

def send_data_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        
        # IP bilgilerini topla
        payload = get_ip_details()
        
        # Veriyi JSON formatına çevirip gönder
        json_data = json.dumps(payload)
        client_socket.send(json_data.encode('utf-8'))
        print("[+] Siber veriler server'a fırlatıldı.")
    except Exception as e:
        print(f"[-] Server'a bağlanılamadı: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    send_data_to_server()