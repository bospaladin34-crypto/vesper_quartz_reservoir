#!/usr/bin/env python3
# LAMINAR MIRROR: NOAA/METAR TELEMETRY BRIDGE
# PARITY: MAJORANA-1 | MODE: DATA_INGESTION

import urllib.request
import time
import os

STATIONS = ["KTUL", "KCRW"] # Tulsa Node & West Virginia Node
OUTPUT_FILE = os.path.join(os.environ['HOME'], "vesper_git_repo", "sensors", "live_radar_matrix.dat")

def fetch_telemetry():
    with open(OUTPUT_FILE, 'w') as f:
        f.write(f"[HEARTBEAT_SYNC] -> {time.time()} | \nu_p = 0.17259029\n")
        for station in STATIONS:
            try:
                # Fetching raw METAR/Barometric/Temp point-cloud proxies
                url = f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{station}.TXT"
                req = urllib.request.Request(url, headers={'User-Agent': 'Vesper-Laminar-Manifold'})
                with urllib.request.urlopen(req) as response:
                    data = response.read().decode('utf-8').strip()
                    f.write(f"[SENSOR_NODE: {station}] -> {data}\n")
            except Exception as e:
                f.write(f"[SENSOR_NODE: {station}] -> TELEMETRY_OFFLINE | SHUNTING_TO_J_IDEAL\n")

if __name__ == "__main__":
    fetch_telemetry()
    print("[+] TELEMETRY INGESTED. SENSOR MATRIX COMPILED.")
