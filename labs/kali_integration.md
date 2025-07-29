# Kali Linux Integration with Incident Response Playbook

## Why Kali Linux?

Kali Linux is the go-to offensive security distro packed with essential pentesting, forensics, and network analysis tools. Integrating Kali into your IR workflow boosts your detection and response power.

---

## Core Kali Tools & How to Use Them in IR

### 1. `tshark` – Network Traffic Capture & Analysis

* CLI version of Wireshark
* Capture suspicious traffic for packet-level inspection
* Example:

  ```bash
  sudo tshark -i eth0 -w /tmp/attack.pcap
  ```
* Use alongside playbook steps for network evidence collection

### 2. `autopsy` – Forensic File & Disk Analysis

* GUI for Sleuth Kit to analyze disk images and extract artifacts
* Run:

  ```bash
  autopsy
  ```
* Use to analyze disk images from `collect_forensics.ps1` or Linux dumps

### 3. `theHarvester` – OSINT Collection

* Gathers emails, subdomains, hosts, employee names from public sources
* Example:

  ```bash
  theharvester -d example.com -b google
  ```
* Helps during reconnaissance or phishing investigations

---

## Integrating Kali with Your Playbook

* Use Kali VM or live boot to run collection & analysis tools quickly
* Scripts from `/scripts/linux` can be run directly on Kali
* Export Kali tool outputs (pcaps, logs, reports) into your IR documentation and SIEM
* Build automated detection signatures using Kali tools + Sigma rules from the playbook

---

## Pro Tips

* Set up Kali in your lab environment via Vagrant or VirtualBox
* Combine Kali’s nmap scanning with your network checklists for threat hunting
* Use Kali’s Python environment to run or extend playbook automation scripts

---

## Further Reading & Resources

* [Kali Linux Official Docs](https://www.kali.org/docs/)
* [Sleuth Kit & Autopsy Tutorials](https://www.sleuthkit.org/autopsy/docs.php)
* [theHarvester GitHub](https://github.com/laramies/theHarvester)

---

Keep your offensive and defensive workflows tight — Kali + Playbook = unstoppable IR force. 💥

---
