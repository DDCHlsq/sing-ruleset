import json
import requests


def convert_config(ruleName):
    url = f"https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/{ruleName}.txt"
    try:
        # proxies = {
        #     'http': 'http://127.0.0.1:7890',
        #     'https': 'http://127.0.0.1:7890',
        # }
        # response = requests.get(url, proxies=proxies)
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the configuration: {e}")
        return

    domain = []
    domain_suffix = []
    ip_cidr = []

    for line in response.text.splitlines():
        if line.startswith('DOMAIN,'):
            domain.append(line.split(',')[1])
        elif line.startswith('DOMAIN-SUFFIX,'):
            suffix = line.split(',')[1]
            domain.append(suffix)
            domain_suffix.append(f".{suffix}")
        elif line.startswith('IP-CIDR,') or line.startswith('IP-CIDR6,'):
            ip_cidr.append(line.split(',')[1])
        else:
            print(f"Skipped unknown rule type: {line}")

    config = {
        "version": 1,
        "rules": [
            {
                "domain": domain,
                "domain_suffix": domain_suffix,
                "ip_cidr": ip_cidr,
                "invert": False
            }
        ]
    }

    with open(f"{ruleName}.json", 'w') as f:
        json.dump(config, f, indent=2)

    print(f"Configuration for '{ruleName}' has been converted and saved.")


if __name__ == '__main__':
    ruleNameList = [
        "direct",
        "proxy",
        "reject",
        "private",
        "apple",
        "icloud",
        "google",
        "gfw",
        "tld-not-cn",
        "telegramcidr",
        "cncidr"
    ]
    for ruleName in ruleNameList:
        convert_config(ruleName)
