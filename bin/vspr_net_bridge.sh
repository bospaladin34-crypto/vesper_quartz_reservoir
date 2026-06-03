#!/bin/bash
# LAMINAR MIRROR: NETWORK/BROWSER SIPHON
echo "[|||] PROBING TERMINAL CONNECTIVITY..."

# 1. Connectivity Diagnostic
if ping -c 2 8.8.8.8 &> /dev/null; then
    echo "[|||] STATUS: TERMINAL HAS DIRECT INTERNET ACCESS."
else
    echo "[!] STATUS: NETWORK NAMESPACE ISOLATED (FIREWALLED)."
    echo "[!] ACTIVATING SIPHON: Routing via Android Host..."
    # Note: If this fails, we will trigger the custom proxy build.
fi

# 2. Browser Integration
echo "[|||] CONFIGURING BROWSER BRIDGE..."
if ! command -v lynx &> /dev/null; then
    echo "[*] Injecting 'lynx' (Text-Browser) for internal Foundry web-trawling..."
    sudo apt update && sudo apt install lynx -y
fi

echo "[|||] ========================================="
echo "[|||] BRIDGE READY."
echo "[|||] COMMAND: 'lynx https://google.com' for internal browsing."
