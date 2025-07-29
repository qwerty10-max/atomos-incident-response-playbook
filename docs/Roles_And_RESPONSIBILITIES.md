# 👥 Roles & Responsibilities (Roles_And_RESPONSIBILITIES.md)

## 🧭 Objective
Clearly define the roles, responsibilities, and escalation flow of all stakeholders involved in the incident response lifecycle. This ensures fast action, accountability, and minimal chaos during a live incident.

---

## 🛠️ Core IR Team Structure

| Role | Function | Key Responsibilities |
|------|----------|-----------------------|
| **Incident Response Manager** | Commander of the IR process | Coordinate all teams, lead incident triage, assign tasks, report to leadership |
| **Security Analyst (Tier 1-3)** | Hands-on technical responders | Monitor alerts, investigate indicators, perform containment/remediation actions |
| **SOC Manager** | Oversight of SOC operations | Validate escalations, approve containment plans, communicate with IR manager |
| **Forensic Investigator** | Evidence collection & analysis | Capture memory/images, preserve chain of custody, identify root cause |
| **Malware Analyst** | Reverse engineering & malware insights | Analyze payloads, extract IOCs, assist in YARA/signature creation |
| **Threat Intelligence Analyst** | Context & attribution | Map attacker TTPs, enrich IOCs with threat data, notify of linked APTs or known exploits |
| **IT/System Admin** | Infrastructure remediation | Patch systems, isolate assets, restore backups, assist in containment |
| **Network Engineer** | Traffic control | Block IPs/domains, reroute traffic, analyze PCAPs, support segmentation |
| **Legal Counsel** | Regulatory & liability guidance | Ensure IR actions comply with laws, manage disclosure, advise on 3rd-party contracts |
| **PR/Comms** | External/internal messaging | Draft official statements, handle media, align with legal on disclosure |
| **Executive Sponsor / CISO** | Leadership & funding | Authorize high-risk decisions (e.g., full shutdowns), communicate with board, approve budgets |
| **Compliance Officer** | Audit/regulatory assurance | Ensure response meets data protection & audit standards, update policies if needed |
| **HR/Insider Threat Team** | People-related investigations | Investigate insider threats, handle employee discipline and access controls |
| **Third-Party Vendor** | External support (if contracted) | Provide DFIR, MSSP support, legal handling, ransomware negotiation, or breach containment support |

---

## 🧬 Role Mapping to NIST IR Functions

| NIST Function | Team(s) Responsible |
|---------------|----------------------|
| **Prepare**   | CISO, IR Manager, Compliance Officer, SOC Manager |
| **Detect**    | Security Analysts, SOC, Threat Intel |
| **Analyze**   | Forensics, Malware Analysts, IR Manager |
| **Contain**   | IR Manager, SysAdmins, NetEng, SOC |
| **Eradicate** | IT, Forensics, Malware Analysts |
| **Recover**   | IT, CISO, Vendor Teams |
| **Post-Incident** | IR Manager, Compliance, Legal, Execs |

---

## 🔁 Escalation Flow

```text
Security Analyst → SOC Manager → IR Manager → Legal/Execs
                     ↓
                Technical SMEs (Forensics / NetEng / IT)
````

---

## 📊 Responsibility RACI Matrix

| Task                 | IR Manager | Analyst | Forensics | Legal | IT | PR |
| -------------------- | ---------- | ------- | --------- | ----- | -- | -- |
| Triage Alerts        | A          | R       | C         | I     | I  | I  |
| Containment Decision | R          | C       | C         | I     | C  | I  |
| Evidence Collection  | C          | C       | R         | I     | I  | I  |
| Public Disclosure    | I          | I       | I         | C     | I  | R  |
| Legal Notification   | C          | I       | I         | R     | I  | I  |
| Post-Incident Report | R          | C       | C         | C     | C  | I  |

> 🔑 R = Responsible | A = Accountable | C = Consulted | I = Informed

---

## 🧑‍💻 Incident On-Call Rotation

* All team members must be reachable 24/7 during assigned IR duty periods.
* On-call schedule managed via \[pager tool / Slack / Opsgenie].
* Backup responders should be trained and ready to act in primary’s absence.

---

## ✅ Role-Based Access Control (RBAC) Expectations

| Role       | IR Tools Access            | Log Access       | Containment Authority |
| ---------- | -------------------------- | ---------------- | --------------------- |
| Analyst    | SIEM, EDR                  | Alert-level logs | No                    |
| Forensics  | Disk imaging, memory tools | Full logs        | No                    |
| IR Manager | All platforms              | All logs         | Yes                   |
| Legal      | Reports, email data        | Limited          | No                    |
| IT         | Network, host systems      | System logs      | Yes                   |
| PR         | Comms platforms only       | None             | No                    |

---

## 📦 Backup / Surge Support

During severe or prolonged incidents, consider:

* Activating **external IR firms** (e.g., Mandiant, CrowdStrike)
* Calling **legal breach counsel**
* Scaling up via **contracted MSSPs**
* Engaging **crisis comms consultants**

---

## 🧩 Linked SOPs

* `docs/Atomos_Atomos_IR_Playbook.md`
* `checklists/Phishing_Response.md`
* `checklists/Insider_Threat.md`
* `docs/Legal_And_Compliance.md`

---

## 🧠 Final Thought

Your IR team is only as strong as your clarity of **roles and communication**. During a real breach, seconds count — and confusion costs more than downtime.

```

---
