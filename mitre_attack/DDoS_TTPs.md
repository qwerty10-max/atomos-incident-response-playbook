# 🛡️ DDoS TTPs (Tactics, Techniques, and Procedures)

This document outlines common Tactics, Techniques, and Procedures (TTPs) associated with Distributed Denial-of-Service (DDoS) attacks, mapped to the [MITRE ATT\&CK](https://attack.mitre.org/) framework where applicable.

---

## 🎯 Tactic: Impact (TA0040)

### 🔹 Technique: Network Denial of Service ([T1498](https://attack.mitre.org/techniques/T1498/))

* **Description**: Flooding network services to degrade availability.
* **Sub-techniques**:

  * **T1498.001: Direct Network Flood** – Sends large volumes of traffic directly to the target.
  * **T1498.002: Reflection Amplification** – Leverages misconfigured servers (e.g., DNS, NTP) to amplify attack volume.
  * **T1498.003: Application Layer Flood** – Targets application endpoints (e.g., HTTP, SIP).

### 🔹 Indicators of Compromise (IOCs):

* Huge spike in incoming traffic volume
* Repeated traffic from spoofed or unusual IPs
* Abnormal requests per second (RPS)
* Alerts from anti-DDoS services (Cloudflare, Akamai, AWS Shield)

---

## 🧰 TTP Summary Table

| Tactic | Technique | Sub-technique | Example Tool                      | Detection Strategy                             |
| ------ | --------- | ------------- | --------------------------------- | ---------------------------------------------- |
| Impact | T1498     | T1498.001     | LOIC, HOIC, Hping3                | Traffic volume monitoring, NetFlow, IDS alerts |
| Impact | T1498     | T1498.002     | Memcached, NTP reflection scripts | Anomalous packet size, known reflector IPs     |
| Impact | T1498     | T1498.003     | Slowloris, RUDY                   | Application performance monitoring, WAF logs   |

---

## 🧠 Adversary Behavior

* Use of botnets (e.g., Mirai, Mozi)
* Targeting high-value apps (e.g., web login, APIs)
* Attack timing coincides with product launches or political events
* Use of traffic obfuscation (encrypted HTTPS floods)

---

## 🛡️ Detection & Response Recommendations

* Implement rate-limiting and geo-blocking
* Monitor NetFlow and connection attempts per IP
* Utilize anti-DDoS platforms (Cloudflare, AWS Shield, Akamai)
* Keep contact with ISP for traffic null-routing during attacks
* Log and store traffic metadata for forensic analysis

---

## 📚 References

* [MITRE ATT\&CK T1498](https://attack.mitre.org/techniques/T1498/)
* [Cloudflare DDoS Trends Report](https://www.cloudflare.com/ddos/)
* [US-CERT DDoS Guidance](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)

---

*Last updated: July 2025*

---

> 💡 **Pro Tip**: Map these TTPs to your SIEM rules and detection logic to improve DDoS alerting capabilities.
