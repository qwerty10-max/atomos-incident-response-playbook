# ⚖️ Legal & Compliance Guidelines (Legal_And_Compliance.md)

## 🧭 Objective
Ensure incident response activities are legally sound, respect regulatory mandates, and follow proper breach notification requirements across jurisdictions. This module serves as a quick reference for IR teams, legal counsel, and compliance officers.

---

## 🔐 Core Legal & Compliance Principles

| Principle               | Description |
|-------------------------|-------------|
| **Confidentiality**      | Limit access to incident data to only necessary parties |
| **Chain of Custody**     | Maintain verifiable records of how digital evidence is collected, stored, and transferred |
| **Data Protection**      | Protect sensitive/regulated data (PII, PHI, PCI, etc.) throughout the IR process |
| **Notification Obligation** | Disclose breaches to regulators/customers within mandated timeframes |
| **Legal Hold**           | Preserve evidence relevant to current or future legal investigations or litigation |

---

## 📜 Global Breach Notification Requirements

| Region       | Regulation        | Timeline          | Trigger                   |
|--------------|------------------|-------------------|---------------------------|
| **EU**       | GDPR             | Within 72 hours   | Breach involving PII      |
| **USA**      | State Laws (e.g., CCPA, NYDFS) | Varies (72h to 30 days) | Breach involving PII/PHI |
| **Nigeria**  | NDPR             | Within 72 hours   | Breach involving personal data |
| **Canada**   | PIPEDA           | “As soon as feasible” | Real risk of significant harm |
| **HIPAA (US)** | Healthcare      | 60 days           | PHI breach affecting 500+ individuals |

> ⚠️ Always consult your legal team for jurisdiction-specific requirements.

---

## 👩‍⚖️ Roles & Responsibilities

| Role           | Responsibilities |
|----------------|------------------|
| **Legal Counsel** | Provide legal advice, manage third-party notifications, ensure compliance |
| **Compliance Officer** | Oversee regulatory mapping and ensure incident documentation meets requirements |
| **IR Manager** | Collaborate with legal and compliance, maintain incident logs |
| **Comms/PR**   | Handle public statements and disclosures in coordination with legal |

---

## 🧾 Required Documentation for Legal Compliance

- 📄 **Incident Report** (timeline, scope, impact)
- 🔐 **Chain of Custody** logs (who handled what data and when)
- 🧪 **Forensic Evidence** (e.g., malware samples, memory images, logs)
- 📬 **Notification Records** (when and how stakeholders were informed)
- 📁 **Remediation Actions** (e.g., patching, password resets, backups restored)
- ✅ **Post-Incident Review** (lessons learned, gaps closed, process improvements)

---

## 🧱 Data Privacy & Retention Guidelines

| Data Type      | Storage Duration | Special Handling |
|----------------|------------------|------------------|
| PII / PHI       | As per regulatory policy (e.g., 6 years HIPAA) | Encryption at rest & in transit |
| Logs / Audit Trails | Min. 1 year (varies by sector) | Integrity verification (hashes) |
| Forensic Images | Until closed + legal retention policy | Stored securely, limited access |
| Incident Reports | 3–7 years, based on org policy | Must include version control |

---

## 🤝 Third-Party Disclosure Template

```text
Subject: Security Incident Notification

Dear [Vendor/Partner/Client],

We are informing you of a recent cybersecurity incident that may have affected [data/system] related to your account. As of [timestamp], our investigation shows [summary of impact].

We have taken the following actions:
- Containment measures
- Ongoing forensic analysis
- Risk mitigation steps

We will follow up with further updates as they become available. If required by regulation, we will notify relevant authorities.

Please contact [contact person] at [email/phone] for further assistance.

Sincerely,  
[Legal/IR Team Name]
````

---

## 🛑 Legal “Do Not Do” List During IR

* ❌ **Don't delete evidence** without legal/forensic approval
* ❌ **Don't make public statements** without PR/legal sign-off
* ❌ **Don't contact threat actors** unless authorized (e.g., ransomware)
* ❌ **Don't attribute blame** without full proof and legal input
* ❌ **Don't ignore disclosure requirements** – they can result in fines or lawsuits

---

## 📎 Templates & Resources

* `templates/incident_report.yaml`
* `templates/chain_of_custody.xlsx`
* `templates/notification_letter.docx`
* `policies/privacy_policy.pdf`
* `logs/evidence_preservation_log.csv`

---

## ✅ Compliance Checklist

* [ ] Is the data breach reportable under local law?
* [ ] Has legal counsel reviewed the incident scope?
* [ ] Has chain of custody been preserved?
* [ ] Have impacted parties been notified?
* [ ] Is all documentation archived securely?

---

## 🔚 Final Note

Cyber incidents are legal minefields. Aligning IR with compliance is non-negotiable — it protects your org from **regulatory penalties**, **brand damage**, and **legal liabilities**. Always involve legal early in the IR lifecycle.

```

---
