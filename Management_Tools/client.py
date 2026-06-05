import socket
import json
import urllib.request
import configparser
import os
import logging
import sys

# --- LOG SİSTEMİ YAPILANDIRMASI ---
# Manuel oluşturduğunuz Logs klasörünün yolunu yakalar
log_klasoru = os.path.join(os.path.dirname(__file__), 'Logs')
os.makedirs(log_klasoru, exist_ok=True) # Klasör olduğu için güvenle geçer
log_dosya_yolu = os.path.join(log_klasoru, 'system.log')

logger = logging.getLogger("SiberClient")
logger.setLevel(logging.DEBUG)
log_formati = logging.Formatter('%(asctime)s | [%(levelname)s] | [%(name)s] | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Logs/system.log dosyasına yazma ayarı
dosya_handler = logging.FileHandler(log_dosya_yolu, encoding='utf-8')
dosya_handler.setFormatter(log_formati)
konsol_handler = logging.StreamHandler(sys.stdout)
konsol_handler.setFormatter(log_formati)

logger.addHandler(dosya_handler)
logger.addHandler(konsol_handler)
# -------------------------------------

# .ini dosyasından ayarları yükle
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

SERVER_IP = config.get('SiberConfig', 'server_ip', fallback='127.0.0.1')
SERVER_PORT = config.getint('SiberConfig', 'server_port', fallback=9999)

def get_ip_details():
    try:
        logger.info("IP detayları ip-api.com üzerinden çekiliyor...")
        url = "http://ip-api.com/json/"
        response = urllib.request.urlopen(url, timeout=5)
        data = json.loads(response.read().decode())
        
        logger.info("IP detayları başarıyla alındı.")
        return {
            "ip": data.get("query", "Bilinmiyor"),
            "ulke": data.get("country", "Bilinmiyor"),
            "sehir": data.get("regionName", "Bilinmiyor"),
            "isp": data.get("isp", "Bilinmiyor"),
            "status": "SUCCESS"
        }
    except Exception as e:
        logger.error(f"IP detayları alınırken hata oluştu: {e}", exc_info=True)
        return {"status": "ERROR", "message": str(e)}

def send_data_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        logger.info(f"Sunucuya bağlanılmaya çalışılıyor... ({SERVER_IP}:{SERVER_PORT})")
        client_socket.connect((SERVER_IP, SERVER_PORT))
        
        payload = get_ip_details()
        json_data = json.dumps(payload)
        client_socket.send(json_data.encode('utf-8'))
        
        logger.info(f"Siber veriler {SERVER_IP}:{SERVER_PORT} adresine fırlatıldı.")
    except Exception as e:
        logger.critical(f"Server'a bağlanılamadı ({SERVER_IP}:{SERVER_PORT}): {e}")
    finally:
        client_socket.close()
        logger.info("Soket bağlantısı kapatıldı.")

if __name__ == "__main__":
    logger.info("Client uygulaması başlatıldı.")
    send_data_to_server()