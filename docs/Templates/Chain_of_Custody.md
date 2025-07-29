# 📜 Chain of Custody Template (Chain_of_Custody.md)

## 🧭 Purpose
To maintain a documented trail of the **possession, handling, analysis, and transfer** of digital evidence during incident response. This ensures **evidentiary integrity** and **legal admissibility** in investigations or court proceedings.

---

## 🧾 Evidence Collection Summary

| Field | Description |
|-------|-------------|
| **Case ID:** | `IR-YYYYMMDD-###` |
| **Incident Name:** | [Example: Ransomware_Attack_DC01] |
| **Evidence ID:** | [Unique identifier for item, e.g., EV-001] |
| **Description of Evidence:** | [e.g., Disk image from endpoint WIN-DC01] |
| **Collected By:** | [Full Name, Role] |
| **Date & Time Collected:** | [YYYY-MM-DD HH:MM] |
| **Location of Collection:** | [e.g., Server Room, Data Center 2] |
| **Collection Method:** | [e.g., FTK Imager, dd command, Memory dump script] |
| **Hash (MD5/SHA256):** | [e.g., SHA256: 52ac8f5f...b99d] |
| **Chain of Custody Start:** | [Initial Handler’s Name and Signature] |

---

## 🔁 Custody Transfer Log

| Step | Handler Name | Role | Date/Time | Purpose of Transfer | Signature |
|------|--------------|------|-----------|----------------------|-----------|
| 1 | Jane Doe | Forensic Analyst | 2025-07-29 13:00 | Evidence Collection | 🖋️ |
| 2 | John Smith | IR Manager | 2025-07-29 13:45 | For Review | 🖋️ |
| 3 | Alice Kim | Legal Counsel | 2025-07-29 14:20 | Legal Review | 🖋️ |
| ... | ... | ... | ... | ... | ... |

---

## 📦 Evidence Storage Location

- Physical: `Secured Evidence Locker – Data Center Room B`
- Digital: `/mnt/evidence/IR-YYYYMMDD-###/WIN-DC01.dd`
- Access Controlled By: `Forensic Team Lead`

---

## 🔒 Integrity Verification

| Hash Type | Value |
|-----------|--------|
| MD5 | `d41d8cd98f00b204e9800998ecf8427e` |
| SHA1 | `da39a3ee5e6b4b0d3255bfef95601890afd80709` |
| SHA256 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

> Re-verify hashes at each transfer point to ensure evidence was not tampered with.

---

## 🧑‍⚖️ Legal Notes

- DO NOT alter or interact with the evidence beyond **read-only forensic procedures**.
- All individuals handling evidence must **sign off in the custody log**.
- This record must be **retained in original and digital form** for a minimum of 3–7 years (based on jurisdiction).
- Breach in chain invalidates evidence for legal use.

---

## 📎 Appendix

- Attach: Screenshots, device labels, hash logs, tool output files
- Reference: `docs/Legal_And_Compliance.md`

---

## ✅ Final Checklist Before Submission

- [ ] All handlers signed
- [ ] Hashes verified and logged
- [ ] Physical storage labeled and locked
- [ ] Digital evidence stored on write-protected media
- [ ] Copy of this document stored in secure IR documentation archive

---

## 🔐 Template Maintainer

| Name | Role | Contact |
|------|------|---------|
| Atomos O.| Cybersecurity Lead | Atomos@example.com |
---

**Reminder:** Integrity lost is evidence tossed. Document *everything*.

