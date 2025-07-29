# 🎯 MITRE ATT\&CK Mapping: Phishing

---

## 📌 Initial Access

* **T1566 – Phishing**

  * T1566.001: Spearphishing Attachment
  * T1566.002: Spearphishing Link
  * T1566.003: Spearphishing via Service

---

## ⚙️ Execution

* **T1204 – User Execution**

  * T1204.001: Malicious Link
  * T1204.002: Malicious File
  * T1204.003: Malicious Script

---

## 🔄 Persistence

* **T1053 – Scheduled Task/Job**
* **T1547 – Boot or Logon Autostart Execution**

  * T1547.001: Registry Run Keys
  * T1547.006: Kernel Modules and Extensions (Linux/Mac)

---

## 📥 Credential Access

* **T1110 – Brute Force**

  * T1110.001: Password Guessing
* **T1555 – Credentials from Password Stores**

  * T1555.003: Credentials from Web Browsers

---

## 📡 Command & Control

* **T1071 – Application Layer Protocol**

  * T1071.001: Web Protocols (HTTP/HTTPS)
  * T1071.003: Mail Protocols

---

## 🔎 Detection Opportunities

* Alert on execution of email attachments or links from unusual domains.
* Flag use of LOLBins like `powershell`, `mshta`, `certutil`.
* Correlate login from new geolocations after phishing events.

---

## 🛡️ Tools to Use

* Email header analyzer (MXToolbox, Microsoft 365 Defender)
* Threat intel enrichment (VirusTotal, urlscan.io)
* Endpoint agents (CrowdStrike, Microsoft Defender ATP)

---

## 🧠 Threat Hunting Queries

* Look for suspicious `powershell.exe` with encoded commands
* Monitor execution of document macros from Office apps
* Scan logs for external emails with executable attachments

---

## 🔗 References

* [MITRE T1566](https://attack.mitre.org/techniques/T1566/)
* [MITRE T1204](https://attack.mitre.org/techniques/T1204/)
* [Phishing Simulation Guidance - NIST](https://csrc.nist.gov/publications/detail/sp/800-177/rev-1/final)
