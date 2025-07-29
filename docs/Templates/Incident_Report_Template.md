# 📝 Incident Report Template

## 🧾 Incident Summary

| Field | Description |
|-------|-------------|
| **Report ID:** | IR-YYYYMMDD-### |
| **Date/Time Reported:** | [YYYY-MM-DD HH:MM] |
| **Reported By:** | [Name, Role, Contact Info] |
| **Detection Method:** | [SIEM Alert, Employee Report, IDS, etc.] |
| **Initial Severity Level:** | [Low, Medium, High, Critical] |
| **Current Status:** | [Open, Contained, Resolved, Escalated] |
| **IR Lead Assigned:** | [Name] |

---

## 📍 Affected Assets

| Asset Name | Type | IP/Hostname | Location | Owner | Impact |
|------------|------|-------------|----------|-------|--------|
| WIN-DC01 | Server | 152.112.1.1 | Data Center A | IT Team | Ransomware |

---

## 📣 Incident Description

> Provide a detailed, non-technical summary of the incident:
- What happened?
- When was it discovered?
- Who discovered it?
- Any known attackers or origin IPs?

**Example:**
> On July 29, 2025, the SOC detected multiple failed RDP login attempts followed by unusual PowerShell activity on WIN-DC01. A Cobalt Strike beacon was identified and blocked. Evidence suggests lateral movement to HR-Laptop01.

---

## 🔍 Investigation Details

### 📌 Timeline of Events

| Timestamp | Event |
|-----------|-------|
| 2025-07-29 08:15 | Alert triggered in Splunk: Excessive login failures |
| 2025-07-29 08:22 | Endpoint flagged suspicious PowerShell |
| 2025-07-29 08:30 | IR team activated, host isolated from network |
| 2025-07-29 09:00 | Forensic image taken, memory dump initiated |

---

### 🧪 Indicators of Compromise (IOCs)

| Type | IOC |
|------|-----|
| IP Address | `144.202.41.77` |
| File Hash | `e3b0c44298fc1...` |
| Domain | `malicious-updates[.]com` |
| Registry Key | `HKCU\Software\Run\malware.exe` |

---

### 🧰 Tools & Logs Used

- SIEM (Splunk)
- EDR (CrowdStrike/Falcon)
- Memory Analysis (Volatility)
- Packet Captures (Wireshark)
- Logs: Windows Event, Firewall, DNS, Sysmon

---

## 🧯 Containment Actions

| Action | Responsible | Timestamp |
|--------|-------------|-----------|
| Host Isolation | IR Lead | 2025-07-29 08:30 |
| Admin creds reset | SysAdmin | 2025-07-29 08:45 |
| Blocked malicious domain | Network Team | 2025-07-29 09:00 |

---

## 🔄 Recovery Plan

- Restored DC from clean backup
- Reimaged HR-Laptop01
- Hardened RDP access with MFA
- Rolled out patch KB500123

---

## 📢 Communication Log

| Time | Message | Audience | Channel |
|------|---------|----------|---------|
| 08:45 | Initial alert sent | IR Team | Slack |
| 09:10 | Incident escalated to CISO | Exec Team | Email |
| 10:30 | Legal briefed | Legal | Phone Call |

---

## 📈 Post-Incident Analysis

### ✅ What Went Well

- Early detection via SIEM
- Rapid isolation prevented spread

### ⚠️ What Needs Improvement

- No MFA on critical accounts
- Delayed escalation to management

---

## 📌 Lessons Learned

- Implement Geo-IP blocks for RDP
- Require just-in-time access for privileged users
- Run phishing simulation every 90 days

---

## 📂 Attachments

- Logs: `splunk_events.csv`, `EDR_alerts.json`
- Screenshots: `memory_analysis.png`
- Chain of Custody: See `docs/templates/Chain_of_Custody.md`

---

## 🧾 Final Sign-Off

| Name | Role | Signature | Date |
|------|------|-----------|------|
| Atomos O. | IR Lead | 🖋️ | 2025-07-29 |
| Jane Doe | CISO | 🖋️ | 2025-07-29 |

---

**Keep this report securely stored for legal and audit purposes. Do not share externally without proper clearance.**
