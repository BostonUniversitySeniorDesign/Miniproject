import os
import time
hour=100
wifi_scan = 'sudo python3 wifi_scan.py miniproject -N 1'
wifi_bluetooth='sudo python3 ble_scan.py > tuesday'+ hour +'.txt'
while True:
    os.system(wifi_scan)
    os.system(wifi_bluetooth)
    time.sleep(300)
    hour+=5
    
