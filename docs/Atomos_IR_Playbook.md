# 🛡️ Incident Response Playbook (Atomos_Atomos_IR_Playbook.md)

## 🎯 Objective
Provide a structured, actionable, and repeatable process for identifying, containing, eradicating, and recovering from cybersecurity incidents. This playbook aligns with NIST 800-61r2, MITRE ATT&CK, and real-world SOC practices.

---

## 📍 IR Phases Overview

| Phase            | Goal                                           | Key Actions |
|------------------|------------------------------------------------|-------------|
| 1. Preparation    | Be ready before incidents happen               | IR team roles, tools, access, baselines, training |
| 2. Detection      | Identify & confirm the incident                | Log analysis, alerts, EDR/SIEM, user reports |
| 3. Containment    | Stop the bleeding                              | Isolate host/network, block C2/IPs, disable accounts |
| 4. Eradication    | Remove threats completely                      | Clean malware, remove persistence, patch vulnerabilities |
| 5. Recovery       | Restore systems safely                         | Restore backups, reimage, password resets, service checks |
| 6. Lessons Learned| Prevent recurrence & improve IR program        | RCA, update detections, stakeholder report, team debrief |

---

## 👥 Roles & Responsibilities

| Role             | Responsibility |
|------------------|----------------|
| **IR Manager**    | Coordinates response, escalates to leadership |
| **SOC Analyst**   | Detects, triages, escalates alerts |
| **Forensic Lead** | Collects evidence, memory dumps, malware analysis |
| **IT Ops**        | Isolate systems, assist recovery, patching |
| **Legal & PR**    | Handles compliance, disclosures, external communication |

---

## 🔀 Escalation Flow

1. **Tier 1 Analyst** receives alert from SIEM/EDR
2. If validated → escalate to **Tier 2 or IR Lead**
3. IR Lead engages:
   - Forensics
   - IT Ops
   - Legal (if PII/IP is involved)
   - Management (if impact is critical)
4. Begin phase-by-phase incident handling

---

## 📁 Linked Playbooks by Incident Type

| Incident Type       | Checklist Link                       |
|---------------------|---------------------------------------|
| 🛑 DDoS Attack       | `checklists/DDoS_Mitigation.md`       |
| 🧬 Malware Infection | `checklists/Malware_Containment.md`   |
| 🎣 Phishing Email    | `checklists/Phishing_Response.md`     |
| 🧍 Insider Threat    | `checklists/Insider_Threat.md`        |
| 🛡️ Ransomware        | `checklists/Ransomware_Recovery.md`   |
| 🔍 Malware TTPs      | `checklists/Malware_TTPs.md`          |

---

## 🧰 Core Tooling

| Tool         | Purpose                     |
|--------------|-----------------------------|
| EDR (CrowdStrike, SentinelOne) | Threat detection, isolation |
| SIEM (Splunk, ELK, Wazuh) | Log collection, correlation |
| Volatility   | Memory forensics            |
| KAPE / Velociraptor | Triage evidence collection |
| MISP / OpenCTI | Threat intel sharing      |
| Ansible      | Mass remediation + patching |
| Suricata/Zeek | Network-based detection     |

---

## 🧠 MITRE ATT&CK Phase Mapping

| IR Phase         | MITRE Coverage Examples                    |
|------------------|--------------------------------------------|
| Initial Access   | T1190, T1133, T1566                        |
| Execution        | T1059, T1204                               |
| Persistence      | T1547, T1053                               |
| Defense Evasion  | T1070, T1562                               |
| Command & Control| T1071, T1095                               |
| Impact           | T1486, T1490                               |

---

## 📜 Compliance Notes

| Framework | Relevant IR Requirements                         |
|-----------|---------------------------------------------------|
| GDPR      | Report breach within 72 hours, protect PII        |
| HIPAA     | Document incident and PHI impact                  |
| ISO 27001 | Maintain IR plan, testing, and lessons learned    |
| PCI DSS   | Contain, notify, and document cardholder incidents|

---

## 📌 Incident Documentation Template

```yaml
incident_id: IR-2025-0021
type: Ransomware
detected_by: SentinelOne Alert
initial_vector: Spearphishing Attachment
affected_hosts:
  - host1.corp.local
  - dc1.corp.local
containment_actions:
  - EDR isolate
  - IP block on firewall
recovery_actions:
  - Restored from backup
  - Applied MS17-010 patch
lessons_learned:
  - Phishing simulation for staff
  - Enhanced SOC detection rules
````

---

## 🔄 Post-Incident Debrief Checklist

* [ ] Was the incident documented clearly?
* [ ] Did escalation flow follow protocol?
* [ ] Any detection or process gaps discovered?
* [ ] Which tools worked best / worst?
* [ ] Should this incident inform tabletop exercises?
* [ ] Update detection rules, SIEM dashboards, or user awareness?

---

## 🚀 Appendix

* `scripts/containment_quick.sh` – Auto-isolate infected host
* `policies/IR_Policy.pdf` – Official policy document
* `ioc/malware_samples/` – IOC collections for future detection tuning

```

---
