# scripts/utils/ioc_extractor.py

import re
import json
import pandas as pd
from stix2 import Indicator, Bundle

IOC_PATTERNS = {
    "IPv4": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
    "IPv6": r"\b(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}\b",
    "Domain": r"\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?:[a-z]{2,})\b",
    "URL": r"http[s]?://[^\s\"'>]+",
    "MD5": r"\b[a-fA-F\d]{32}\b",
    "SHA1": r"\b[a-fA-F\d]{40}\b",
    "SHA256": r"\b[a-fA-F\d]{64}\b",
}

def extract_iocs(text):
    found = {}
    for ioc_type, pattern in IOC_PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            found[ioc_type] = list(set(matches))
    return found

def export_to_csv(iocs, output_file="iocs.csv"):
    flat = []
    for ioc_type, values in iocs.items():
        for val in values:
            flat.append({"Type": ioc_type, "Value": val})
    pd.DataFrame(flat).to_csv(output_file, index=False)
    print(f"[+] Exported to {output_file}")

def export_to_stix(iocs, output_file="iocs.json"):
    indicators = []
    for ioc_type, values in iocs.items():
        for val in values:
            pattern = ""
            if ioc_type == "IPv4":
                pattern = f"[ipv4-addr:value = '{val}']"
            elif ioc_type == "Domain":
                pattern = f"[domain-name:value = '{val}']"
            elif ioc_type == "URL":
                pattern = f"[url:value = '{val}']"
            elif ioc_type in ["MD5", "SHA1", "SHA256"]:
                pattern = f"[file:hashes.{ioc_type.lower()} = '{val}']"
            if pattern:
                indicators.append(Indicator(name=f"{ioc_type} Indicator", pattern=pattern, pattern_type="stix"))

    bundle = Bundle(indicators)
    with open(output_file, "w") as f:
        f.write(bundle.serialize(pretty=True))
    print(f"[+] STIX exported to {output_file}")

def auto_tag_mitre(iocs):
    # Placeholder for future logic using mitreattack-python or ATT&CK Navigator JSONs
    tagged = {}
    for ioc_type, values in iocs.items():
        tagged[ioc_type] = []
        for val in values:
            # Dummy tagging based on type
            if ioc_type in ["MD5", "SHA1", "SHA256"]:
                tagged[ioc_type].append((val, "T1204.002"))  # Malicious file
            elif ioc_type == "URL":
                tagged[ioc_type].append((val, "T1566.002"))  # Spearphishing Link
    return tagged

if __name__ == "__main__":
    sample = """
        Suspicious IP: 45.77.60.233
        URL: http://malicious.biz/attack.exe
        SHA256: 3a7bd3e2360a3d665a0450a3d4f5dc2425be07bff710ce0117a0e4ec9464e62a
        Domain: click.evildomain.com
    """

    iocs = extract_iocs(sample)
    print("[+] Extracted IOCs:", iocs)

    export_to_csv(iocs)
    export_to_stix(iocs)

    tags = auto_tag_mitre(iocs)
    print("[+] Tagged ATT&CK IDs:", json.dumps(tags, indent=2))

