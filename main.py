import json
import re
from ipaddress import ip_network
from pathlib import Path

import requests

RULE_NAMES = (
    "direct", "proxy", "reject", "private", "apple", "icloud",
    "google", "gfw", "tld-not-cn", "telegramcidr", "cncidr",
)
DOMAIN_PATTERN = re.compile(r"[-\w]+(?:\.[-\w]+)*")
IP_VERSIONS = {"IP-CIDR": 4, "IP-CIDR6": 6}


def parse_rules(text):
    domains = []
    suffixes = []
    cidrs = []

    for number, raw_line in enumerate(text.splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith(("#", "//")):
            continue

        rule_type, separator, value = line.partition(",")
        rule_type, value = rule_type.strip(), value.strip()
        if not separator or not value:
            raise ValueError(f"line {number}: missing rule type or value")

        if rule_type in ("DOMAIN", "DOMAIN-SUFFIX"):
            if not DOMAIN_PATTERN.fullmatch(value):
                raise ValueError(f"line {number}: invalid domain {value!r}")
            domains.append(value)
            if rule_type == "DOMAIN-SUFFIX":
                suffixes.append("." + value)
        elif rule_type in IP_VERSIONS:
            try:
                prefix = ip_network(value, strict=False)
            except ValueError as error:
                raise ValueError(f"line {number}: invalid CIDR {value!r}") from error
            if "/" not in value or prefix.version != IP_VERSIONS[rule_type]:
                raise ValueError(f"line {number}: invalid {rule_type} prefix {value!r}")
            cidrs.append(value)
        else:
            raise ValueError(f"line {number}: unsupported rule type {rule_type!r}")

    if not (domains or suffixes or cidrs):
        raise ValueError("upstream file contains no rules")

    return {
        "version": 1,
        "rules": [{
            "domain": domains,
            "domain_suffix": suffixes,
            "ip_cidr": cidrs,
            "invert": False,
        }],
    }


def convert_config(rule_name):
    url = f"https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/{rule_name}.txt"
    response = requests.get(url, timeout=(10, 60))
    response.raise_for_status()
    config = parse_rules(response.text)

    output = Path(f"{rule_name}.json")
    output.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    print(f"Configuration for {rule_name!r} has been converted and saved.")


if __name__ == "__main__":
    for rule_name in RULE_NAMES:
        try:
            convert_config(rule_name)
        except (requests.RequestException, ValueError) as error:
            raise SystemExit(f"{rule_name}: {error}") from error
