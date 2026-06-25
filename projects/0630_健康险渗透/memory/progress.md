# 项目进度追踪（健康险渗透）

> 关键词：`健康险渗透更新进度`
> 最后更新：2026-06-25 14:00:00

---

## 当前阶段

**信息收集（已完成）→ 准备进入漏洞探测**

---

## 已完成事项

| # | 事项 | 时间 | 产出 |
|---|------|------|------|
| 1 | 手动收集原始资产 | 2026-06-25 01:44 | 35 条域名 |
| 2 | crt.sh 证书透明度扩展 | 2026-06-25 01:44 | 扩展至 91 条 |
| 3 | TscanPlus CLI 子域名爆破 | 2026-06-25 10:00 | 发现 170 条存活（3 个根域名） |
| 4 | 资产清单整合更新 | 2026-06-25 11:00 | `assets.md` 244 条（去重后） |
| 5 | Web 指纹全量扫描 | 2026-06-25 13:30 | `web_fingerprint.md` 140 条指纹 |

---

## 关键产出文件

| 文件 | 说明 |
|------|------|
| `results/assets.md` | 244 条资产清单（含 IP、Title、Banner） |
| `results/web_fingerprint.md` | 140 条 Web 指纹报告（含 UEditor/CAS/Tomcat 等高危指纹） |
| `results/url_list.txt` | 488 条 URL 列表（http+https） |
| `results/crtsh_fetch.py` | crt.sh 证书透明度拉取脚本 |

---

## 高危发现（待验证）

| 域名 | 指纹 | 风险 |
|------|------|------|
| `ehis-wbzs-web.health.pingan.com` | RabbitMQ + UEditor | 未授权/文件上传 |
| `ehis-golden-key*.health.pingan.com` | Apereo-CAS | 反序列化 |
| `group-cms.health.pingan.com` | Apereo-CAS | 反序列化 |
| `helper.health.pingan.com` | Apereo-CAS + Apache-Struts2 | 双重高危 |
| `health.pingan.com` | Tomcat-Manager + UEditor | 弱口令/文件上传 |
| `health.pingan.com.cn` | 用友NC + UEditor | 已知漏洞 |
| `ehis-unity.health.pingan.com` | 医健工作台（无 WAF） | 防护弱 |

---

## 待办事项

| # | 事项 | 优先级 |
|---|------|--------|
| 1 | 高危目标深度验证（CAS/Tomcat/RabbitMQ/YApi） | 🔴 高 |
| 2 | 独立 IP 全端口扫描（m1/mobile 等不同 IP 段） | 🔴 高 |
| 3 | JS 文件分析（Vue.js/Nuxt.js 站点提取 API） | 🟡 中 |
| 4 | 漏洞探测（基于指纹做 POC 验证） | 🔴 高 |
| 5 | 端口扫描（联动服务指纹） | 🟡 中 |

---

## 下一阶段目标

**漏洞探测** — 基于 Web 指纹结果，对高价值目标进行 POC 验证和深度测试
