import bluetooth
import time

print("BLUETOOTH QIDIRLYAPDI...")
nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)

if len(nearby_devices) == 0:
    print("BLUETOOTH DEVICES TOPILMADI")
else:
    print("BLUETOOTH QURULMALARI")
    for idx, (addr, name) in enumerate(nearby_devices, 1):
        print(f"{idx}. {name} - {addr}")


    try:
        choice = int(input("RAQAM KIRITISH:"))
        if 1 <= choice <= len(nearby_devices):
            target_address = nearby_devices[choice - 1][0]
            target_name = nearby_devices[choice - 1][1]
            print(f"TANLAGAN BLUETOOTH: {target_name} | MAC: {target_address}")
        else:
            print("HATOLIK !")
            exit()
    except ValueError:
        print("FAQAT RAQAM KIRITISH KERAK")
        exit()


    print(f"SIGNAL {target_name} YUBORILYAPDI...")
    while True:
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.settimeout(10) 

            sock.connect((target_address, 1)) 
            sock.send("BU TEST SIGNAL")  
            print("SIGNAL JO'NATLDI !")
            time.sleep(0.5)  
            sock.close()  

        except bluetooth.BluetoothError as e:
            print(f"PACKETLAR YUBORILYAPDI: {e}")
            time.sleep(2)
        except Exception as e:
            print(f"XATOLIK: {e}")
            break
        else:
           print("QURULMA TOPILMADI")

