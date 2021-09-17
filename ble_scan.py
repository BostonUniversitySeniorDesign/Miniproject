#!/usr/bin/env python3
"""
Example of scanning Bluetooth Low Energy (BLE) devices.
Requires a Linux computer due to gattlib underlying BLE scanning requiring Glib.
"""

import argparse
from bluetooth.ble import DiscoveryService

p = argparse.ArgumentParser(description="BLE scanner")
p.add_argument(
    "timeout", help="number of seconds to scan for BLE devices", nargs="?", type=int, default=5
)
P = p.parse_args()

timeout = P.timeout

print(f"Scanning BLE devices for {timeout} seconds")

svc = DiscoveryService()
ble_devs = svc.discover(timeout)

for u, n in ble_devs.items():
    print(u, n)
