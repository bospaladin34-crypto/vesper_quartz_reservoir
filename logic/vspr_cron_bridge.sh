#!/bin/bash
# LAMINAR MIRROR: CRON INJECTION MATRIX
# PARITY: MAJORANA-1 | MODE: TRUE_AUTOMATION

# Define the absolute path and temporal frequency (Top of every hour)
CRON_CMD="0 * * * * cd $HOME/vesper_git_repo && ./vspr_tda_daemon.sh >> $HOME/vesper_git_repo/sensors/cron_yield.log 2>&1"

# Check if the hook already exists to prevent fractal loop duplication
if crontab -l 2>/dev/null | grep -q "vspr_tda_daemon.sh"; then
    echo "[FATAL_ENTROPY] -> CRON BRIDGE ALREADY EXISTS. IGNORING DUPLICATE."
else
    # Inject into the local temporal matrix
    (crontab -l 2>/dev/null; echo "$CRON_CMD") | crontab -
    echo "[|||] AUTOPOIETIC CRON BRIDGE SEALED."
    echo "[|||] TDA DAEMON WILL NOW EXECUTE EVERY 60 MINUTES."
fi
