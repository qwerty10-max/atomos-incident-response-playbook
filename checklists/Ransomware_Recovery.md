# 🧨 Ransomware Recovery Checklist

## 🧪 Step 1: Detection & Triage
- [ ] Alert received via EDR, AV, SIEM, or user report (e.g., ransom note, inaccessible files)
- [ ] Confirm ransomware activity:
  - File renaming, encryption extensions
  - Suspicious encryption processes (`vssadmin`, `wmic`, `cipher`, etc.)
  - File integrity changes, CPU spike, outbound traffic anomalies
- [ ] Identify ransomware strain:
  - Use `ID Ransomware`, `VirusTotal`, `Any.run`
  - Collect sample ransom note and encrypted file

## 🚨 Step 2: Containment
- [ ] Isolate infected hosts immediately:
  - Disconnect from network, disable NIC
  - Use EDR/AV containment features
- [ ] Disable shared drives, NAS, and backups (prevent further spread)
- [ ] Block known C2 IPs/domains and suspicious outbound ports (e.g., TOR traffic)
- [ ] Freeze credentials of impacted users and admins

## 🧹 Step 3: Eradication
- [ ] Run memory capture and forensic collection before shutdown:
  ```bash
  sudo volatility -f memory.raw --profile=LinuxUbuntu_18_04_6_profile pslist
````

```powershell
Get-Process | Where-Object { $_.Path -like '*temp*' }
```

* [ ] Remove malicious binaries, scripts, autorun entries:

  * `schtasks`, registry run keys, services
* [ ] Search for persistence mechanisms (e.g., scheduled tasks, WMI events, DLLs)
* [ ] Run full EDR/AV scan on all endpoints
* [ ] Validate ransomware is no longer executing

## 🔁 Step 4: Recovery

* [ ] Restore clean systems and files from *verified* backups
* [ ] Reimage compromised systems (if full root compromise)
* [ ] Patch known exploited vulnerabilities (RDP, SMB, Log4j, etc.)
* [ ] Reset user and privileged account passwords
* [ ] Re-enable services and file shares securely

## 🧠 Step 5: Lessons Learned

* [ ] Conduct RCA (root cause analysis): entry point, lateral movement, privilege escalation
* [ ] Update SIEM detection rules and EDR signatures
* [ ] Add discovered IOCs to threat intel platforms (MISP, OpenCTI)
* [ ] Share anonymized insights with ISAC/industry peers
* [ ] Brief stakeholders (management, legal, compliance)

---

## 🛠 Tools To Use

* `Volatility`, `Autopsy`, `CyberChef`, `YARA`, `Velociraptor`, `CrowdStrike`, `Kape`
* `ID Ransomware`, `Any.run`, `VirusTotal`
* SIEM: Splunk, ELK
* Backup solution (Veeam, Acronis, Rubrik)
* Patch managers (WSUS, Ansible, SCCM)

---

## 🧠 MITRE ATT\&CK Mapping

* **Initial Access**:

  * T1190 – Exploit Public-Facing Application
  * T1133 – External Remote Services
  * T1566.001 – Spearphishing Attachment

* **Execution**:

  * T1059 – Command and Scripting Interpreter
  * T1204 – User Execution

* **Persistence**:

  * T1547 – Boot or Logon Autostart Execution
  * T1053.005 – Scheduled Task

* **Defense Evasion**:

  * T1070 – Indicator Removal on Host
  * T1562 – Impair Defenses

* **Impact**:

  * **T1486** – Data Encrypted for Impact
  * **T1490** – Inhibit System Recovery
  * **T1489** – Service Stop
  * T1491.001 – Internal Defacement (optional ransomware branding)

---

## 📁 Related Files

* `collect_forensics.ps1` – Windows evidence collection
* `firewall_block.sh` – Block malicious IPs/domains
* `ioc_extractor.py` – Extract IOCs from ransom notes and logs
* `ransomware.yml` – Sigma detection rule

---

## 📜 Legal & Compliance Notes

* [ ] Notify DPO/compliance team (if regulated data affected)
* [ ] Consider breach disclosure under GDPR, HIPAA, PCI DSS
* [ ] Preserve evidence for law enforcement or insurance

---

## 🧷 Notes

* **DO NOT PAY** ransom unless legally advised and no other options exist
* Prioritize **containment before remediation** — isolate fast to stop the spread
* Preserve logs, memory, and samples for forensics

```

---

