# 🛡️ DDoS Mitigation Checklist

## 🧪 Step 1: Detection & Triage
- [ ] Confirm high network traffic or degraded service (check with NOC/monitoring tools)
- [ ] Use monitoring platforms (e.g., Zabbix, Nagios, Grafana) to spot anomalies
- [ ] Run traffic inspection:
  ```bash
  sudo netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n
  sudo tcpdump -nn -i eth0
````

* [ ] Identify attack vector:

  * Volumetric (UDP floods, ICMP)
  * Protocol (SYN floods)
  * Application Layer (HTTP GET/POST)

## 🚨 Step 2: Containment

* [ ] Geo-block suspicious IPs/ranges using:

  ```bash
  sudo iptables -A INPUT -s <malicious-ip> -j DROP
  ```

* [ ] Throttle or filter traffic with:

  * `fail2ban`
  * `mod_evasive` (Apache)
  * `mod_security` (WAF)
  * `rate limiting` on NGINX or Cloudflare

* [ ] Enable CDN/WAF protections (e.g., Cloudflare “Under Attack Mode”, AWS Shield)

* [ ] Contact ISP or upstream provider for traffic filtering / blackhole routing

* [ ] Use sinkhole/DNS firewall if available

## 🧹 Step 3: Eradication

* [ ] Monitor traffic post-mitigation — ensure attack has stopped
* [ ] Remove temporary blocks after confirmation
* [ ] Sanitize and secure exposed services (API endpoints, DNS resolvers)

## 🔁 Step 4: Recovery

* [ ] Restore affected services and configurations
* [ ] Confirm DNS routing and load balancing are back to normal
* [ ] Conduct performance testing to ensure no latent impact
* [ ] Log all timestamps, IPs, traffic snapshots (retain for post-mortem)

## 🧠 Step 5: Lessons Learned

* [ ] Perform Root Cause Analysis (RCA)
* [ ] Update IR playbook with new IOCs, IP ranges, attack patterns
* [ ] Share anonymized data with trusted ISACs or cert groups
* [ ] Train engineering teams on prevention & early detection

---

## 🛠 Tools To Use

* `tcpdump`, `iftop`, `netstat`, `nmap`, `fail2ban`
* Cloudflare / Akamai / AWS Shield
* Splunk or ELK for traffic anomaly detection
* Wireshark for packet-level inspection
* OpenVAS/Nessus for exposure checks

---

## 🔍 MITRE ATT\&CK Mapping

* **TA0011 – Command and Control**

  * T1498 – Network Denial of Service

    * T1498.001 – Direct Network Flood
    * T1498.002 – Reflection Amplification
  * T1499 – Endpoint Denial of Service

    * T1499.001 – OS Exhaustion Flood
    * T1499.003 – Application Exhaustion Flood

---

## 📁 Related Files

* `firewall_block.sh` – for fast IP/domain blocking
* `slack_alert.py` – notify SOC via Slack webhook
* `ddos_analysis_script.py` (optional) – for future correlation logic

---

## 🧷 Notes

* Always ensure logs are captured **before** mitigation for evidence.
* Engage legal/compliance team if business-critical assets were impacted.
* Consider scripting automatic block thresholds if you detect repeat IP patterns.

```

---
