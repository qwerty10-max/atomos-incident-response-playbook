#!/bin/bash

# =============================
# firewall_block.sh
# Linux IP/Domain Blacklister
# =============================

# Check for root
if [[ "$EUID" -ne 0 ]]; then
  echo "[!] Please run as root."
  exit 1
fi

# Input file containing list of IPs/domains
BLOCK_LIST="blocklist.txt"

if [[ ! -f "$BLOCK_LIST" ]]; then
  echo "[!] Block list file not found: $BLOCK_LIST"
  exit 1
fi

echo "[*] Starting firewall block script..."
while IFS= read -r target; do
  if [[ "$target" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "[+] Blocking IP: $target"
    iptables -A INPUT -s "$target" -j DROP
    iptables -A OUTPUT -d "$target" -j DROP
  else
    echo "[+] Blocking domain via hosts file: $target"
    echo "0.0.0.0 $target" >> /etc/hosts
  fi
done < "$BLOCK_LIST"

echo "[✓] Blocking complete."

# Optional: Save iptables rules
# iptables-save > /etc/iptables/rules.v4
