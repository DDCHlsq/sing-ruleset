# sing-ruleset 简介

本项目每天于北京时间 8:00 生成适用于 [sing-box](https://github.com/SagerNet/sing-box) 的二进制 `.srs` 格式的规则文件。

本项目的部分源数据（10 种基础分流规则）基于 [Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules) 项目。

## 二进制规则

本项目包含了来自 [Xbox 下载助手](https://github.com/skydevil88/XboxDownload/blob/master/README_OpenWrt.md) 的 Xbox 域名规则，分别为：

- Xbox 全球下载域名
  - - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/xboxdlglobal.srs
- Xbox 中国大陆下载域名
  - - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/xboxdlcn.srs

本项目包含收集自 lhie1 放行规则（已经被删库，可在[此处](https://cdn.jsdelivr.net/gh/dler-io/Rules@master/Clash/Provider/Special.yaml)找到遗留）的 Steam 中国大陆域名规则，为：

- Steam CN 域名二进制规则
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/steamcn.srs

本项目中包含了来自多个来源收集的 PCDN 以及 HTTP DNS 域名规则，分别为：

- PCDN 域名二进制规则
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/pcdn.srs
- HTTP DNS 域名二进制规则
  - https://raw.githubusercontent.com/DDCHlsq/sing-ruleset/ruleset/httpdns.srs

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

## 使用说明

可以依照自己的需求自由使用所有规则。

如果希望免去配置的麻烦，可以尝试本项目中的 `sconfer.py` 工具，示例的 `inbounds` 和 `template` 可以直接使用，`outbounds` 还请自行依照需求更改。

```shell
Usage: python3 sconfer.py <template> <inbounds> <outbounds>
```
