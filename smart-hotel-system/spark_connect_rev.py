import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import threading
import json
import requests

# Setup Telegram
TOKEN_BOT = "8291349270:AAGJb1p5HKt4QSL4nCWlFV_2ushU3UAaXZ8"
CHAT_ID = "738561550"

def kirim_notif_telegram(pesan):
    url = f"https://api.telegram.org/bot{TOKEN_BOT}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": pesan,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Gagal kirim Telegram: {e}")

print("Menguji koneksi Telegram...")
kirim_notif_telegram("*TESTING:* Sistem Smart Hotel mulai berjalan. Bot Telegram berhasil terhubung!")

# Koneksi Database
db_client = InfluxDBClient(host="100.127.227.8", port=31086, database="smarthotel")

try:
    db_client.switch_database('smarthotel')
    print("Terhubung ke database 'smarthotel'")
except Exception as e:
    print(f"Info database: {e}")

# Buffer untuk menyimpan status terakhir (inisialisasi dengan 0 atau None)
buffer = {"suhu": 0.0, "kelembapan": 0.0, "gerak": 0, "pintu": 0, "status": "Belum Terdeteksi"}

def kirim_ke_db():
    # Jadwalkan kirim ulang 5 detik lagi
    threading.Timer(5.0, kirim_ke_db).start()
    
    # Kirim status buffer saat ini ke InfluxDB
    json_body = [{
        "measurement": "sensor_kamar",
        "tags": {"kamar": "kamar101"},
        "fields": buffer
    }]
    db_client.write_points(json_body)
    print(f"[Snapshot 5 Detik] Data lengkap dikirim: {buffer}")

def on_message(client, userdata, msg):
    try:
        pesan = msg.payload.decode()
        data_sensor = json.loads(pesan)
        
        if "suhu" in data_sensor:
            buffer["suhu"] = float(data_sensor["suhu"])
            
        if "kelembapan" in data_sensor:
            buffer["kelembapan"] = float(data_sensor["kelembapan"])
            
        if "gerak" in data_sensor:
            buffer["gerak"] = int(data_sensor["gerak"])
            
        if "pintu" in data_sensor:
            buffer["pintu"] = int(data_sensor["pintu"])

        if "status_kamar" in data_sensor:
            status_kamar_esp32 = int(data_sensor["status_kamar"])
            
            # --- LOGIKA CERDAS DETEKSI TAMU KELUAR ---
            # Jika alat baca Kosong (0), TAPI status sebelumnya di buffer masih "Terisi"
            if status_kamar_esp32 == 0 and buffer["status"] == "Terisi":
                pesan_tele = "🧹 *INFO HOUSEKEEPING* 🧹\nKamar 101 baru saja *KOSONG*.\nSilakan bersihkan kamar!"
                print("🚨 Mengirim notif Telegram...")
                kirim_notif_telegram(pesan_tele)
                
            # Update buffer dengan status terbaru
            buffer["status"] = "Terisi" if status_kamar_esp32 == 1 else "Kosong"
            
        print(f"Buffer diperbarui dari ESP32: {data_sensor}")
        
    except json.JSONDecodeError:
        print("Error: Format JSON tidak valid!")
    except Exception as e:
        print(f"Error: {e}")

# Memulai loop kirim data
kirim_ke_db()

# Setup MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect("100.127.227.8", 31883, 60)

# 3. UBAH TOPIK SESUAI ESP32
client.subscribe("hotel/#")

print("Data siap ditampilkan.")
client.loop_forever()