# sing-ruleset 简介

本项目每天于北京时间 8:00 生成适用于 [sing-box](https://github.com/SagerNet/sing-box) 的二进制 `.srs` 格式的规则文件。

本项目的源数据基于 [Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules) 项目。

## 二进制规则

本项目的 `ruleset` 分支中包含了 [Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules) 中提供的 10 种规则，分别为：

- 直连域名二进制规则 direct.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/direct.srs
- 代理域名二进制规则 proxy.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/proxy.srs
- 广告域名二进制规则 reject.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/reject.srs
- 私有网络专用域名二进制规则 private.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/private.srs
- Apple 在中国大陆可直连的域名二进制规则 apple.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/apple.srs
- iCloud 域名二进制规则 icloud.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/icloud.srs
- \[慎用\]Google 在中国大陆可直连的域名二进制规则 google.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/google.srs
- GFWList 域名二进制规则 gfw.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/gfw.srs
- 非中国大陆使用的顶级域名二进制规则 tld-not-cn.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/tld-not-cn.srs
- Telegram 使用的 IP 地址二进制规则 telegramcidr.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/telegramcidr.srs
- 中国大陆 IP 地址二进制规则 cncidr.srs
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/cncidr.srs

## 示例配置

遵循 [Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules) 提供的白名单配置方法，下面给出对应的 [sing-box](https://github.com/SagerNet/sing-box) 的白名单路由配置（即没有命中的流量通通走代理）。

这里的配置应该填入 [sing-box](https://github.com/SagerNet/sing-box) 配置中的 `route` 模块。

**特别说明**：原配置中，设置了 `google` 这个规则走直连，经测试去除了这个配置。

```json
{
  "rules": [
    {
      "protocol": "dns",
      "outbound": "dns-out"
    },
    {
      "rule_set": "rule-private",
      "outbound": "direct"
    },
    {
      "rule_set": "rule-reject",
      "outbound": "block"
    },
    {
      "rule_set": "rule-icloud",
      "outbound": "direct"
    },
    {
      "rule_set": "rule-apple",
      "outbound": "direct"
    },
    {
      "rule_set": "rule-proxy",
      "outbound": "proxy"
    },
    {
      "rule_set": "rule-direct",
      "outbound": "direct"
    },
    {
      "rule_set": "rule-telegramcidr",
      "outbound": "proxy"
    },
    {
      "rule_set": "rule-cncidr",
      "outbound": "direct"
    },
    {
      "ip_is_private": true,
      "outbound": "direct"
    }
  ],
  "rule_set": [
    {
      "tag": "rule-direct",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/direct.srs",
      "download_detour": "proxy"
    },
    {
      "tag": "rule-proxy",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/proxy.srs",
      "download_detour": "proxy"
    },
    {
      "tag": "rule-reject",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/reject.srs",
      "download_detour": "proxy"
    },
    {
      "tag": "rule-private",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/private.srs",
      "download_detour": "proxy"
    },
    {
      "tag": "rule-apple",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/apple.srs",
      "download_detour": "proxy"
    },
    {
      "tag": "rule-icloud",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/icloud.srs",
      "download_detour": "proxy"
    },
    {
      "tag": "rule-google",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/google.srs",
      "download_detour": "proxy"
    },
    {
      "tag": "rule-gfw",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/gfw.srs",
      "download_detour": "proxy"
    },
    {
      "tag": "rule-tld-not-cn",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/tld-not-cn.srs",
      "download_detour": "proxy"
    },
    {
      "tag": "rule-telegramcidr",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/telegramcidr.srs",
      "download_detour": "proxy"
    },
    {
      "tag": "rule-cncidr",
      "type": "remote",
      "format": "binary",
      "url": "https:\/\/raw.githubusercontent.com\/DDCHlsq\/sing-ruleset\/ruleset\/cncidr.srs",
      "download_detour": "proxy"
    }
  ],
  "final": "proxy",
  "auto_detect_interface": true
}
```

