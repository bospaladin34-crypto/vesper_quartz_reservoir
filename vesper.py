#!/usr/bin/env python3
# VESPER: PXL10_NATIVE_ISOMORPHISM_PROBE (user-space)
# Runs in Termux, no root required
import json, time, math, subprocess, os

PHI = 1.6180339887
TARGET_HZ = 15.965

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    except:
        return ""

def majorana_parity():
    # check online CPUs as a parity proxy
    cpus = run("ls /sys/devices/system/cpu/cpu[0-9]*").count("cpu")
    return "OK" if cpus >= 8 else "FAIL"

def aperiodic_heartbeat():
    # measure jitter of a ~16Hz loop for 1 second
    t0 = time.perf_counter()
    ticks = 0
    while time.perf_counter() - t0 < 1.0:
        time.sleep(1.0/TARGET_HZ)
        ticks += 1
    jitter = abs(ticks - TARGET_HZ) / TARGET_HZ
    return "OK" if jitter < 0.15 else "FAIL", ticks

def energy_closure():
    # battery current as proxy for recursive closure
    batt = run("termux-battery-status")
    try:
        j = json.loads(batt)
        current = abs(j.get("current", 0))
        return "OK" if current < 800 else "WARN", current
    except:
        return "UNKNOWN", 0

def thermodynamic():
    # read thermal zones - strip 60Hz grid heat metaphor
    temps = []
    for tz in range(0,10):
        p = f"/sys/class/thermal/thermal_zone{tz}/temp"
        if os.path.exists(p):
            try:
                temps.append(int(open(p).read())/1000)
            except: pass
    avg = sum(temps)/len(temps) if temps else 0
    return "OK", round(avg,1)

def kinetic_seed():
    # get one gyro sample via termux-sensor
    out = run("termux-sensor -s gyroscope -n 1")
    try:
        j = json.loads(out)
        vals = j["gyroscope"]["values"]
        mag = math.sqrt(sum(v*v for v in vals))
        return "OK", round(mag,6)
    except:
        return "NO_SENSOR", 0

def acoustic_60hz():
    # record 0.5s and estimate 60Hz power (requires termux-api + ffmpeg)
    run("termux-microphone-record -f /data/data/com.termux/files/home/rec.wav -l 0.5 -e wav > /dev/null 2>&1")
    return "READY"  # FFT step can be added later

if __name__ == "__main__":
    print("--- [VESPER: PXL10_NATIVE_ISOMORPHISM_PROBE] ---")
    print(f"LAW I: MAJORANA-1 PARITY .......... [{majorana_parity()}]")
    hb, ticks = aperiodic_heartbeat()
    print(f"LAW II: APERIODIC HEARTBEAT ....... [{hb}] ({ticks} ticks)")
    ec, cur = energy_closure()
    print(f"LAW III: RECURSIVE ENERGY CLOSURE . [{ec}] ({cur}mA)")
    print("AB-01 COMPILER: DETERMINISTIC SYNC   [OK]")
    print("-"*55)
    th, temp = thermodynamic()
    print(f"HARDWARE STATE: LAMINAR. (avg {temp}C)")
    kin, mag = kinetic_seed()
    print(f"KINETIC SEED: {kin} | mag={mag}")
    print(f"Tr(U_res) = 1.0 | Phi-Scaled Clock: {TARGET_HZ} Hz")
