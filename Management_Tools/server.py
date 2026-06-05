import socket
import json
import configparser
import os

# .ini dosyasından ayarları yükle
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

# Server tüm ağ kartlarını dinlemek için 0.0.0.0 kullanır, portu ini'den alır
BIND_IP = "0.0.0.0"
BIND_PORT = config.getint('SiberConfig', 'server_port', fallback=9999)

def start_siber_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(10000)
    
    print(f"[*] Siber Merkez Dinlemede... (Port: {BIND_PORT})")
    
    try:
        while True:
            client_sock, addr = server.accept()
            print(f"\n[+] Hedef baglantisi yakalandi! Kaynak: {addr[0]}:{addr[1]}")
            
            request = client_sock.recv(4096).decode('utf-8')
            if request:
                try:
                    data = json.loads(request)
                    if data.get("status") == "SUCCESS":
                        print("="*40)
                        print("        SİBER İSTİHBARAT RAPORU        ")
                        print("="*40)
                        print(f" Hedef Dış IP : {data['ip']}")
                        print(f" Ülke         : {data['ulke']}")
                        print(f" Şehir        : {data['sehir']}")
                        print(f" İnternet Sağ.: {data['isp']}")
                        print("="*40)
                    else:
                        print(f"[-] Hedef bilgi toplayamadı: {data.get('message')}")
                except Exception as json_err:
                    print(f"[-] Veri cozulemedi: {json_err}")
                    
            client_sock.close()
    except KeyboardInterrupt:
        print("\n[*] Sunucu kapatılıyor...")
    finally:
        server.close()

if __name__ == "__main__":
    start_siber_server()