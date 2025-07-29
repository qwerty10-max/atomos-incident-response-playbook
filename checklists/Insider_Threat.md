# 🕵️ Insider Threat Response Checklist

## 🧪 Step 1: Detection & Triage
- [ ] Receive alert via DLP, SIEM, UEBA, HR report, or whistleblower tip
- [ ] Correlate activity with user identity and behavior:
  - Unusual access times or locations
  - Mass data access/downloads
  - Access to systems outside user role
- [ ] Review logs:
  - File access logs, VPN logs, system audit trails
  - Email activity and USB usage
- [ ] Prioritize based on impact: IP theft, sabotage, fraud, unauthorized access?

## 🚨 Step 2: Containment
- [ ] Discreetly isolate user account (disable AD, Okta, MFA tokens)
- [ ] Block user’s access to sensitive systems and cloud apps
- [ ] Remove device access from MDM (Intune, Jamf, etc.)
- [ ] Preserve user session for forensic analysis (don’t log them out immediately if observation needed)
- [ ] Monitor attempts to escalate privileges or bypass controls

## 🧹 Step 3: Eradication
- [ ] Remove any unauthorized files, scripts, or scheduled tasks created by insider
- [ ] Audit and clean up file shares or database dumps accessed
- [ ] Change credentials and reset passwords for shared resources
- [ ] Reimage or wipe affected devices if tampering is detected
- [ ] Capture chat logs, emails, and screen recordings if policy allows

## 🔁 Step 4: Recovery
- [ ] Restore business systems affected (stolen credentials, config changes)
- [ ] Review and enforce proper access control policies (RBAC, Zero Trust)
- [ ] Notify legal, HR, and management for disciplinary, legal, or criminal proceedings
- [ ] If negligence was involved: Re-train employee and monitor closely

## 🧠 Step 5: Lessons Learned
- [ ] Conduct formal RCA (Root Cause Analysis)
- [ ] Update insider threat indicators in UEBA/SIEM platforms
- [ ] Refine access control and DLP rules
- [ ] Share anonymized IOCs with industry peers (ISACs, FS-ISAC, etc.)
- [ ] Recommend behavioral monitoring (AI/ML-based platforms like Exabeam, Splunk UBA)

---

## 🛠 Tools To Use
- `Sysmon`, `OSQuery`, `Velociraptor`, `CrowdStrike`, `Microsoft Defender for Insider Risk`
- SIEM: Splunk, ELK, QRadar
- DLP: Digital Guardian, Symantec DLP, Code42
- AD logs, Windows Event Viewer, email logs

---

## 🔍 MITRE ATT&CK Mapping

- **Initial Access**:
  - T1078 – Valid Accounts

- **Persistence**:
  - T1136 – Create Account  
  - T1078.003 – Cloud Accounts

- **Defense Evasion**:
  - T1070 – Indicator Removal  
  - T1562 – Impair Defenses

- **Credential Access**:
  - T1003 – OS Credential Dumping  
  - T1056 – Input Capture (Keyloggers)

- **Exfiltration**:
  - T1041 – Exfiltration Over C2 Channel  
  - T1020 – Automated Exfiltration  
  - T1052 – Exfil via Removable Media

- **Impact**:
  - T1485 – Data Destruction  
  - T1491 – Defacement  
  - T1499 – Endpoint DoS

---

## 📁 Related Files
- `log_analysis.py` – Flag unusual user behavior from logs
- `ioc_extractor.py` – Parse insider’s activities from logs
- `isolate_host.ps1` – Immediately cut network access for suspected machine

---

## 🧷 Notes
- Coordinate closely with **HR and Legal** before taking action — insider threats can involve employment contracts and laws.
- Document **everything**: actions taken, evidence gathered, decisions made.
- Ensure **chain-of-custody** if you're pursuing civil/criminal prosecution.
