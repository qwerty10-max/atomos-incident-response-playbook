# 🎣 Phishing Incident Response Checklist

## 🧪 Step 1: Detection & Triage
- [ ] Alert from email gateway, user report, or SIEM
- [ ] Collect the phishing email sample (headers, body, attachments, links)
- [ ] Analyze sender:
  - `whois`, `MXToolbox`, `urlscan.io`
  - Inspect DKIM/SPF/DMARC alignment
- [ ] Investigate attachments/URLs:
  - `VirusTotal`, `Any.run`, `Hybrid Analysis`
  - `curl -I`, `unzip -l file.doc`, `oletools`
- [ ] Interview target users: Did they click? Download? Enter credentials?

## 🚨 Step 2: Containment
- [ ] Block sender domain/IP in email gateway (Proofpoint, O365, Mimecast)
- [ ] Remove/quarantine similar messages from mailboxes (eDiscovery, Defender, Gmail admin)
- [ ] Reset credentials for affected users (AD, Okta, Google Workspace)
- [ ] Block malicious URLs/domains on web proxy/DNS filter
- [ ] Monitor for lateral movement or privilege abuse

## 🧹 Step 3: Eradication
- [ ] Remove registry/startup entries if malware was executed
- [ ] Delete dropped payloads, scripts, or backdoors
- [ ] Update AV/EDR definitions and re-scan systems
- [ ] Check logs for malicious macros, processes, or downloads

## 🔁 Step 4: Recovery
- [ ] Restore user access securely with MFA
- [ ] Review and adjust email filters/rules
- [ ] Provide anti-phishing awareness training to targeted users
- [ ] Run targeted phishing simulation (optional)

## 🧠 Step 5: Lessons Learned
- [ ] Identify phishing campaign patterns (subject line, spoofing method, lure type)
- [ ] Extract IOCs and share with threat intel tools (MISP, OpenCTI)
- [ ] Update detection rules (e.g., YARA, Sigma, email gateway policies)
- [ ] Tag affected users as “high-risk” for enhanced monitoring

---

## 🛠 Tools To Use
- `mxtoolbox.com`, `VirusTotal`, `Any.run`, `oleid`, `theHarvester`
- Email console: Microsoft Defender, G Workspace, Proofpoint, etc.
- `curl`, `dig`, `oletools`, `urlscan.io`
- SIEM: Splunk, ELK stack

---

## 🔍 MITRE ATT&CK Mapping

- **Initial Access**:
  - T1566.001 – Spearphishing Attachment  
  - T1566.002 – Spearphishing Link  
  - T1566.003 – Spearphishing via Service  

- **Execution**:
  - T1204 – User Execution

- **Persistence**:
  - T1547 – Boot or Logon Autostart Execution

- **Credential Access**:
  - T1078 – Valid Accounts  
  - T1556 – Credential Phishing  

- **Command and Control**:
  - T1105 – Ingress Tool Transfer  
  - T1071 – Application Layer Protocol

---

## 📁 Related Files
- `slack_alert.py` – SOC alert for phishing indicators
- `ioc_extractor.py` – Extract URLs/hashes from email headers/logs
- `email_parser.sh` – (coming soon) CLI-based .eml parser

---

## 🧷 Notes
- Never click or interact with suspicious emails using your primary machine — use a sandbox.
- Always collect and preserve email headers for forensics.
- Reporting: Notify legal if sensitive data/phishing site was credential-harvesting.

