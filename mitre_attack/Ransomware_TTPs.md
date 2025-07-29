# 🧬 Ransomware TTPs

## 🧠 Overview

Ransomware attacks aim to encrypt, exfiltrate, or destroy critical data to extort money from organizations. This TTP map breaks down a typical ransomware lifecycle and its mapping to the MITRE ATT\&CK framework, with tools, IOCs, and threat-hunting strategies.

---

## 🧷 Initial Access

* **T1190 – Exploit Public-Facing Application**
* **T1133 – External Remote Services**
* **T1566.001 – Spearphishing Attachment**

### 🧪 Detection Ideas

* Monitor public-facing apps for anomalies
* Analyze VPN, RDP, and SSH logs for unusual login times and IPs

### 🛠 Tools

* Zeek, Wazuh, CrowdStrike, Suricata

---

## 🧷 Execution

* **T1059.003 – Command and Scripting Interpreter: Windows Command Shell**
* **T1204.002 – User Execution: Malicious File**

### 🧪 Detection Ideas

* Detect macros/scripts executing post file open
* Script logs from PowerShell, CMD, or Bash

### 🛠 Tools

* Sysmon, Event Viewer, PowerShell Logs, ELK Stack

---

## 🧷 Persistence

* **T1547.001 – Registry Run Keys/Startup Folder**
* **T1053.005 – Scheduled Task/Job: Scheduled Task**

### 🧪 Detection Ideas

* Monitor task scheduler logs and startup registry entries

### 🛠 Tools

* Autoruns, Winlogbeat, Registry auditing tools

---

## 🧷 Privilege Escalation

* **T1068 – Exploitation for Privilege Escalation**
* **T1548.002 – Bypass User Access Control**

### 🧪 Detection Ideas

* Look for sudden admin rights acquisition

### 🛠 Tools

* Sysmon, AuditD, OSSEC

---

## 🧷 Defense Evasion

* **T1070.004 – File Deletion**
* **T1027 – Obfuscated Files or Information**

### 🧪 Detection Ideas

* Detect deletion of shadow copies
* Monitor base64 encoded PowerShell commands

### 🛠 Tools

* Velociraptor, Sigma rules, ELK Stack

---

## 🧷 Credential Access

* **T1003 – OS Credential Dumping**
* **T1555 – Credentials from Password Stores**

### 🧪 Detection Ideas

* Look for LSASS access events
* Monitor access to registry hives like SAM

### 🛠 Tools

* Mimikatz, Procdump, Sysinternals Suite

---

## 🧷 Lateral Movement

* **T1021.002 – SMB/Windows Admin Shares**
* **T1021.001 – Remote Desktop Protocol**

### 🧪 Detection Ideas

* Excessive internal RDP sessions
* Lateral SMB activity logs

### 🛠 Tools

* NetFlow, Wireshark, Arkime

---

## 🧷 Collection & Exfiltration

* **T1119 – Automated Collection**
* **T1041 – Exfiltration Over C2 Channel**

### 🧪 Detection Ideas

* Monitor for large volumes of outbound traffic
* Detect ZIP/RAR file creation on endpoints

### 🛠 Tools

* ZScaler, Darktrace, Zeek

---

## 🧷 Impact

* **T1486 – Data Encrypted for Impact**
* **T1490 – Inhibit System Recovery**

### 🧪 Detection Ideas

* Creation of ransom notes
* VSSAdmin or WBAdmin logs

### 🛠 Tools

* Velociraptor, EDR platforms, YARA

---

## 🔍 IOC Examples

* `vssadmin delete shadows /all /quiet`
* `.onion` ransom URLs
* Unusual extensions like `.locked`, `.encrypted`, `.payme`

---

## 🎯 Threat Hunting Tips

* Always baseline normal behaviors across your endpoints
* Hunt for known ransomware hash families (e.g., Ryuk, Conti, LockBit)
* Use YARA + Sigma rules to scan for ransom notes and crypto routines

---

## 📚 References

* [https://attack.mitre.org/tactics/TA0040/](https://attack.mitre.org/tactics/TA0040/)
* [https://www.nomoreransom.org/](https://www.nomoreransom.org/)
* [https://car.mitre.org/wiki/All\_Detections](https://car.mitre.org/wiki/All_Detections)

---

✅ Keep this updated per ransomware strain evolutions.
