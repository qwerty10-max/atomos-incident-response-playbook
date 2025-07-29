# Insider Threat TTPs – MITRE ATT\&CK Mapping

Insider threats involve malicious or negligent actors within the organization who intentionally or unintentionally cause harm to systems, data, or reputation. These can range from disgruntled employees to careless users or compromised internal accounts.

---

## 🔍 Common Tactics & Techniques

### 📥 Initial Access

* **T1078** – Valid Accounts

  * Abuse of legitimate credentials to gain or maintain access.
* **T1556.001** – Credentials from Password Stores

  * Extracting credentials stored in browsers or password managers.

### 🛠️ Execution

* **T1059** – Command and Scripting Interpreter

  * Use of PowerShell, Bash, or Python for malicious actions.
* **T1569.002** – Service Execution

  * Abuse of Windows services to run unauthorized code.

### 💾 Persistence

* **T1136.001** – Create Account: Local Account

  * Creation of new user accounts for persistence.
* **T1547.001** – Registry Run Keys/Startup Folder

  * Modify registry to run malicious code on startup.

### 📡 Command and Control

* **T1071.001** – Application Layer Protocol: Web Protocols

  * Use of HTTPS or HTTP to exfiltrate data or issue commands.
* **T1102.002** – Web Service: File Sharing Services

  * Dropbox, Google Drive used to transfer stolen data.

### 📤 Exfiltration

* **T1041** – Exfiltration Over C2 Channel

  * Covert transfer of data via existing command channels.
* **T1020** – Automated Exfiltration

  * Use of scripts or malware to automatically extract data.

### 🎯 Impact

* **T1485** – Data Destruction

  * Wiping or corrupting files or systems.
* **T1491** – Defacement

  * Changing web content or digital assets.

---

## 🛠️ Detection & Monitoring

* Monitor for abnormal user behavior (e.g., file access spikes, off-hour logins).
* Use UEBA (User & Entity Behavior Analytics) to detect anomalies.
* Correlate unusual activity with insider role or recent HR events (e.g., termination).
* Deploy DLP (Data Loss Prevention) tools for real-time detection.

---

## 🧪 Tools and Resources

* **SIEM**: Splunk, ELK, QRadar
* **Behavior Analytics**: Varonis, Exabeam, Microsoft Defender for Endpoint
* **Investigation**: Sysmon, Auditd, PowerShell logs

---

## 📘 References

* [MITRE T1078 – Valid Accounts](https://attack.mitre.org/techniques/T1078/)
* [CERT Insider Threat Center](https://insights.sei.cmu.edu/insider-threat/)
* \[NIST 800-53 Rev 5 – System and Communications Protection]

---

✅ Include this in your SOC/CSIRT toolkit to quickly triage and detect insider threats aligned with real-world behaviors.
