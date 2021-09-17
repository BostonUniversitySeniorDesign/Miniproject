"""
Scanning in legacy Bluetooth mode shows devices in discoverable pairing mode.
Only a few devices like TVs might stick in discoverable mode semi-permanently.

BLE scans as in ble_scan.py are usually needed for human mobility detection.
The legacy Bluetooth used by bt_scan.py will usually not find enough
non-fixed devices.
"""

import bluetooth

disc_devs = bluetooth.discover_devices(duration=5)
print(f"Found {len(disc_devs)} devices.")

for a, n in disc_devs:
    print(a, n)
