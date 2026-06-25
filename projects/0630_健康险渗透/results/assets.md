# 健康险渗透 - 资产清单（整合版）

> 更新时间：2026-06-25
> 数据来源：手动收集 + crt.sh 证书透明度 + TscanPlus 子域名爆破
> 总计：**244 条**（去重后）
> TscanPlus 确认存活：**170 条**

---

## 统计概览

| 主域 | 原有 | TscanPlus 新增 | 合计 |
|------|------|---------------|------|
| `*.health.pingan.com` | 40 | +4 | 44 |
| `*.pingan.com.cn` | 34 | +68 | 102 |
| `*.pingan.com` | 9 | +89 | 98 |
| **合计** | **83** | **+161** | **244** |

---

## 一、`*.health.pingan.com`（44条）

### TscanPlus 确认存活

| # | 域名 | IP | Title | 关键指纹 |
|---|------|-----|-------|---------|
| 1 | activity.health.pingan.com | 58.216.14.91, 58.216.14.92, 58.216.14.93 | activity | Tengine,Citrix-NetScaler... |
| 2 | cdn-suishenyi.health.pingan.com | - | - | - |
| 3 | ehis-activity-stg1.health.pingan.com | - | - | - |
| 4 | ehis-activity-stg5.health.pingan.com | - | - | - |
| 5 | ehis-content.health.pingan.com | - | - | - |
| 6 | ehis-golden-key.health.pingan.com | - | - | - |
| 7 | ehis-hisos.health.pingan.com | - | - | - |
| 8 | ehis-hsms-dmzweb.health.pingan.com | - | - | - |
| 9 | ehis-hsms-openresty-dmzweb-prd.health.pingan.com | - | - | - |
| 10 | ehis-icp-dmz-web.health.pingan.com | - | - | - |
| 11 | ehis-iproductmarket-stg1.health.pingan.com | - | - | - |
| 12 | ehis-iproductmarket-stg2.health.pingan.com | - | - | - |
| 13 | ehis-iproductmarket-stg5.health.pingan.com | - | - | - |
| 14 | ehis-mcore-stg1.health.pingan.com | - | - | - |
| 15 | ehis-mini-program-dmzweb-stg1.health.pingan.com | - | - | - |
| 16 | ehis-mini-program-dmzweb-stg2.health.pingan.com | - | - | - |
| 17 | ehis-mini-program-dmzweb-stg5.health.pingan.com | - | - | - |
| 18 | ehis-store.health.pingan.com | - | - | - |
| 19 | ehis-tcm-dmzweb.health.pingan.com | - | - | - |
| 20 | ehis-unity.health.pingan.com | - | - | - |
| 21 | ehis-wbzs-minio.health.pingan.com | - | - | - |
| 22 | ehis-wbzs-web.health.pingan.com | - | - | - |
| 23 | ehis-yedi-ngweb-stg5.health.pingan.com | - | - | - |
| 24 | ehis.health.pingan.com | - | - | - |
| 25 | eqzprd.health.pingan.com | - | - | - |
| 26 | group-cms.health.pingan.com | - | - | - |
| 27 | group-hr.health.pingan.com | - | - | - |
| 28 | group.health.pingan.com | 58.220.6.102, 58.220.6.109 | 403 Forbidden | Byte-nginx,f5-big-ip-waf,BigIP[waf]... |
| 29 | helper-market.health.pingan.com | - | - | - |
| 30 | helper.health.pingan.com | - | - | - |
| 31 | iopen.health.pingan.com | - | - | - |
| 32 | m.health.pingan.com | 58.216.14.93, 58.216.14.94, 58.216.14.95 | None | f5-big-ip-waf,BigIP[waf],Citrix-NetScaler,Tengine... |
| 33 | mcore.health.pingan.com | - | - | - |
| 34 | mini-program.health.pingan.com | - | - | - |
| 35 | mobile.health.pingan.com | 124.196.49.105 | None | BigIP[waf],nginx,f5-big-ip-waf... |
| 36 | nbmcore.health.pingan.com | - | - | - |
| 37 | open.health.pingan.com | 58.220.6.102, 58.220.6.109 | 平安健康险开放平台 | BigIP[waf],Byte-nginx,f5-big-ip-waf... |
| 38 | product.health.pingan.com | 58.216.14.91, 58.216.14.92, 58.216.14.93 | 403 Forbidden | f5-big-ip-waf,Tengine,BigIP[waf],Citrix-NetScaler... |
| 39 | recorder.health.pingan.com | - | - | - |
| 40 | www.health.pingan.com | 58.220.6.102, 58.220.6.109 | 平安健康保险 | Byte-nginx,f5-big-ip-waf,BigIP[waf]... |
| 41 | login.health.pingan.com | 58.216.14.91, 58.216.14.92, 58.216.14.93 | 平安健康保险 | f5-big-ip-waf,Tengine,BigIP[waf],Citrix-NetScaler... |
| 42 | m1.health.pingan.com | 222.186.177.163, 61.147.235.175 | None | f5-big-ip-waf,BigIP[waf],Byte-nginx... |
| 43 | s.health.pingan.com | 58.220.6.102, 58.220.6.109 | 平安健康保险 | f5-big-ip-waf,Byte-nginx,BigIP[waf]... |
| 44 | wap.health.pingan.com | 58.220.6.102, 58.220.6.109 | 平安健康保险 | NuxtJS,Mongo-Express,f5-big-ip-waf,Byte-nginx,Node.js,BigIP[... |

### 仅证书透明度（未通过 TscanPlus 确认存活）

| # | 域名 | 备注 |
|---|------|------|
| 45 | group-hr.health.pingan.com | 生产 |
| 46 | ehis-hisos.health.pingan.com | 生产 |
| 47 | ehis-iproductmarket-stg1.health.pingan.com | STG |
| 48 | ehis-iproductmarket-stg5.health.pingan.com | STG |
| 49 | recorder.health.pingan.com | 生产 |
| 50 | group-cms.health.pingan.com | 生产 |
| 51 | iopen.health.pingan.com | 生产 |
| 52 | ehis-content.health.pingan.com | 生产 |
| 53 | eqzprd.health.pingan.com | 生产 |
| 54 | ehis-mini-program-dmzweb-stg2.health.pingan.com | STG |
| 55 | ehis-golden-key.health.pingan.com | 生产 |
| 56 | helper.health.pingan.com | 生产 |
| 57 | ehis-hsms-openresty-dmzweb-prd.health.pingan.com | 生产 |
| 58 | ehis-tcm-dmzweb.health.pingan.com | 生产 |
| 59 | helper-market.health.pingan.com | 生产 |
| 60 | ehis-hsms-dmzweb.health.pingan.com | 生产 |
| 61 | ehis-activity-stg5.health.pingan.com | STG |
| 62 | ehis-yedi-ngweb-stg5.health.pingan.com | STG |
| 63 | nbmcore.health.pingan.com | 生产 |
| 64 | mcore.health.pingan.com | 生产 |
| 65 | cdn-suishenyi.health.pingan.com | 生产 |
| 66 | ehis-unity.health.pingan.com | 生产 |
| 67 | ehis-wbzs-web.health.pingan.com | 生产 |
| 68 | ehis-mini-program-dmzweb-stg1.health.pingan.com | STG |
| 69 | ehis-icp-dmz-web.health.pingan.com | 生产 |
| 70 | ehis.health.pingan.com | 生产 |
| 71 | ehis-store.health.pingan.com | 生产 |
| 72 | ehis-mini-program-dmzweb-stg5.health.pingan.com | STG |
| 73 | ehis-wbzs-minio.health.pingan.com | 生产 |
| 74 | mini-program.health.pingan.com | 生产 |
| 75 | ehis-mcore-stg1.health.pingan.com | STG |
| 76 | ehis-iproductmarket-stg2.health.pingan.com | STG |
| 77 | ehis-activity-stg1.health.pingan.com | STG |

## 二、`*.pingan.com.cn`（102条）

### 与健康险相关（TscanPlus 新发现）

| # | 域名 | IP | Title | 关键指纹 |
|---|------|-----|-------|---------|
| 1 | healthcare.pingan.com.cn | 113.108.21.99 | None | BigIP[waf],f5-big-ip-waf... |
| 2 | mcp.pingan.com.cn | 117.186.252.205 |  | - |

### 已有资产（TscanPlus 确认存活）

| # | 域名 | IP | Title | 关键指纹 |
|---|------|-----|-------|---------|
| 1 | cdn-ehis-golden-key-stg.pingan.com.cn | - | - | - |
| 2 | cdn-ehis-golden-key-stg5.pingan.com.cn | - | - | - |
| 3 | cdn-ehis-golden-key.pingan.com.cn | - | - | - |
| 4 | ehis-audit-ivs-dmz-stg1.pingan.com.cn | - | - | - |
| 5 | ehis-audit-ivs-dmz-stg2.pingan.com.cn | - | - | - |
| 6 | ehis-audit-ivs-dmz-stg5.pingan.com.cn | - | - | - |
| 7 | ehis-br-consultant-h5-stg1.pingan.com.cn | - | - | - |
| 8 | ehis-br-consultant-h5-stg5.pingan.com.cn | - | - | - |
| 9 | ehis-br-consultant-pks.pingan.com.cn | - | - | - |
| 10 | ehis-br-consultant.pingan.com.cn | - | - | - |
| 11 | ehis-eqz-dmzweb-prd.pingan.com.cn | - | - | - |
| 12 | ehis-golden-key-stg.pingan.com.cn | - | - | - |
| 13 | ehis-golden-key-stg5.pingan.com.cn | - | - | - |
| 14 | ehis-golden-key.pingan.com.cn | - | - | - |
| 15 | ehis-hcs-stg1.pingan.com.cn | - | - | - |
| 16 | ehis-hcs-stg2.pingan.com.cn | - | - | - |
| 17 | ehis-hcs-stg3.pingan.com.cn | - | - | - |
| 18 | ehis-hcs-stg5.pingan.com.cn | - | - | - |
| 19 | ehis-hcs.pingan.com.cn | - | - | - |
| 20 | ehis-hems-dmz-stg1.pingan.com.cn | - | - | - |
| 21 | ehis-hems-dmz-stg5.pingan.com.cn | - | - | - |
| 22 | ehis-hems.pingan.com.cn | - | - | - |
| 23 | ehis-ivs-dmzweb-stg1.pingan.com.cn | - | - | - |
| 24 | ehis-ivs-dmzweb-stg2.pingan.com.cn | - | - | - |
| 25 | ehis-ivs-dmzweb-stg5.pingan.com.cn | - | - | - |
| 26 | ehis-ivs.pingan.com.cn | - | - | - |
| 27 | ehis-mcore-stg1.pingan.com.cn | - | - | - |
| 28 | ehis-mcp-gateway-wgq-padis-dmzstg5.pingan.com.cn | - | - | - |
| 29 | ehis-service-dmzweb-prd.pingan.com.cn | - | - | - |
| 30 | ehis.home.pingan.com.cn | - | - | - |
| 31 | health.pingan.com.cn | 58.220.6.102, 58.220.6.109 | 平安健康保险 | f5-big-ip-waf,BigIP[waf],Byte-nginx... |
| 32 | healthtech.pingan.com.cn | - | - | - |
| 33 | mcp-health.pingan.com.cn | - | - | - |
| 34 | mcp-test-health.pingan.com.cn | - | - | - |

### 仅证书透明度（未通过 TscanPlus 确认存活）

| # | 域名 | 备注 |
|---|------|------|
| 35 | cdn-ehis-golden-key.pingan.com.cn | 生产 |
| 36 | ehis.home.pingan.com.cn | 生产 |
| 37 | ehis-hems-dmz-stg1.pingan.com.cn | STG |
| 38 | ehis-golden-key.pingan.com.cn | 生产 |
| 39 | ehis-audit-ivs-dmz-stg5.pingan.com.cn | STG |
| 40 | ehis-br-consultant-pks.pingan.com.cn | 生产 |
| 41 | ehis-eqz-dmzweb-prd.pingan.com.cn | 生产 |
| 42 | ehis-br-consultant-h5-stg1.pingan.com.cn | STG |
| 43 | ehis-ivs-dmzweb-stg1.pingan.com.cn | STG |
| 44 | ehis-hcs-stg3.pingan.com.cn | STG |
| 45 | ehis-hcs-stg2.pingan.com.cn | STG |
| 46 | mcp-test-health.pingan.com.cn | 生产 |
| 47 | ehis-hems.pingan.com.cn | 生产 |
| 48 | ehis-hcs.pingan.com.cn | 生产 |
| 49 | ehis-golden-key-stg5.pingan.com.cn | STG |
| 50 | ehis-mcore-stg1.pingan.com.cn | STG |
| 51 | cdn-ehis-golden-key-stg5.pingan.com.cn | STG |
| 52 | healthtech.pingan.com.cn | 生产 |
| 53 | ehis-hcs-stg1.pingan.com.cn | STG |
| 54 | ehis-service-dmzweb-prd.pingan.com.cn | 生产 |
| 55 | mcp-health.pingan.com.cn | 生产 |
| 56 | ehis-ivs.pingan.com.cn | 生产 |
| 57 | ehis-golden-key-stg.pingan.com.cn | STG |
| 58 | ehis-hcs-stg5.pingan.com.cn | STG |
| 59 | ehis-audit-ivs-dmz-stg2.pingan.com.cn | STG |
| 60 | ehis-br-consultant-h5-stg5.pingan.com.cn | STG |
| 61 | ehis-audit-ivs-dmz-stg1.pingan.com.cn | STG |
| 62 | ehis-ivs-dmzweb-stg2.pingan.com.cn | STG |
| 63 | ehis-mcp-gateway-wgq-padis-dmzstg5.pingan.com.cn | STG |
| 64 | ehis-ivs-dmzweb-stg5.pingan.com.cn | STG |
| 65 | cdn-ehis-golden-key-stg.pingan.com.cn | STG |
| 66 | ehis-br-consultant.pingan.com.cn | 生产 |
| 67 | ehis-hems-dmz-stg5.pingan.com.cn | STG |

### 集团其他资产（与健康险无直接关联）

| # | 域名 | IP | Title | 关键指纹 |
|---|------|-----|-------|---------|
| 1 | ab.pingan.com.cn | 45.65.23.171 | None | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113]... |
| 2 | ant.pingan.com.cn | 211.139.177.95 | Welcome to nginx! | nginx/1.22.1,Nginx-Default-Test-Page... |
| 3 | api.pingan.com.cn | 202.69.21.123 | 平安开放平台 | Apache-Struts2,jQuery,JSP,Oracle-JAVA,YApi可视化接口管理平台,f5-big-i... |
| 4 | b1.pingan.com.cn | 45.65.23.147 | 平安银行移动官网 | Apache-Struts2,NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113... |
| 5 | bank.pingan.com.cn | 45.65.23.142 | Error | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113]... |
| 6 | bbc.pingan.com.cn | 202.69.23.230 | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113],Nginx-Default... |
| 7 | c.pingan.com.cn | 124.196.28.140 | Welcome to nginx! | Nginx-Default-Test-Page,NRPd/6.1.4[3450a98:1773:3c338a6:1870... |
| 8 | cash.pingan.com.cn | 202.69.21.176 |  | - |
| 9 | cf.pingan.com.cn | 43.230.222.162 | None | vmware-SpringBoot-Framework,Java,loading... |
| 10 | cg.pingan.com.cn | 43.230.222.56 | 待办系统 | loading... |
| 11 | creditcard.pingan.com.cn | 45.65.23.161 | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113],Nginx-Default... |
| 12 | cz.pingan.com.cn | 45.65.23.137 | None | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113]... |
| 13 | download.pingan.com.cn | 58.220.6.102, 58.220.6.109 | 302 Found | Byte-nginx... |
| 14 | dv.pingan.com.cn | 112.74.93.164 | Welcome to nginx! | Nginx-Default-Test-Page... |
| 15 | ebank.pingan.com.cn | 45.65.23.135 | HTTP Status 404 | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113]... |
| 16 | eps.pingan.com.cn | 45.65.23.65 |  | - |
| 17 | fund.pingan.com.cn | 202.69.26.4 | None | f5-big-ip-waf,BigIP[waf]... |
| 18 | futures.pingan.com.cn | 202.69.26.80 | 平安期货-平安集团旗下持牌期货公司 | loading,f5-big-ip-waf,BigIP[waf],jQuery... |
| 19 | galaxy.pingan.com.cn | 110.41.218.233, 110.41.220.180 |  | - |
| 20 | gc.pingan.com.cn | 61.241.20.132 | None | BigIP[waf],nginx,f5-big-ip-waf... |
| 21 | hermes.pingan.com.cn | 183.62.123.177 |  | - |
| 22 | home.pingan.com.cn | 61.241.20.52 | 平安好福利 | loading... |
| 23 | ibc.pingan.com.cn | 124.196.51.89 | 出错了 | loading... |
| 24 | ibs.pingan.com.cn | 115.175.196.73 | Welcome to nginx! | BigIP[waf],Nginx-Default-Test-Page,loading,f5-big-ip-waf... |
| 25 | legacy.pingan.com.cn | 47.243.3.98 | None | None... |
| 26 | link.pingan.com.cn | 45.65.23.65 |  | - |
| 27 | ltc.pingan.com.cn | 59.36.223.127 | 平安智慧长护经办管理系统 | BigIP[waf],nginx,f5-big-ip-waf... |
| 28 | mail.pingan.com.cn | 202.69.17.34 | None | None... |
| 29 | mailout2.pingan.com.cn | 202.69.19.105 |  | - |
| 30 | mall.pingan.com.cn | 58.220.6.102, 58.220.6.109 | 壹钱包 中国平安旗下品牌 | Apache-Struts2,Byte-nginx... |
| 31 | message.pingan.com.cn | 202.69.18.33 |  | - |
| 32 | mp.pingan.com.cn | 45.65.23.11 | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113],Nginx-Default... |
| 33 | mx1.pingan.com.cn | 202.69.19.105 |  | - |
| 34 | mx2.pingan.com.cn | 202.69.19.104 |  | - |
| 35 | mx4.pingan.com.cn | 47.243.3.87 |  | - |
| 36 | mx5.pingan.com.cn | 47.243.3.88 |  | - |
| 37 | mx7.pingan.com.cn | 47.243.3.88 |  | - |
| 38 | mx8.pingan.com.cn | 124.196.32.20 |  | - |
| 39 | oa.pingan.com.cn | 124.196.28.30 |  | - |
| 40 | one.pingan.com.cn | 43.230.222.37 | 平安一账通官网 | Apache-Struts2,jQuery,openresty... |
| 41 | open.pingan.com.cn | 183.237.253.179 | None | BigIP[waf],f5-big-ip-waf,JSP,openresty... |
| 42 | openapi.pingan.com.cn | 202.69.23.230 | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113],Nginx-Default... |
| 43 | portal.pingan.com.cn | 61.241.20.173 | 平安开放平台 | Apache-Struts2,BigIP[waf],jQuery,YApi可视化接口管理平台,Oracle-JAVA,J... |
| 44 | push.pingan.com.cn | 202.69.21.76 |  | - |
| 45 | realestate.pingan.com.cn | 43.230.223.234 | None | loading... |
| 46 | resources.pingan.com.cn | 58.216.14.91, 58.216.14.92, 58.216.14.93 | 设备租赁_商业租赁_委托租赁_平安车管 | Tengine,BigIP[waf],f5-big-ip-waf,jQuery,Apache-Struts2... |
| 47 | sbc.pingan.com.cn | 121.15.166.178, 58.251.11.225 |  | - |
| 48 | secmail.pingan.com.cn | 124.196.49.186 | IIS Windows Server | IIS-Windows-Server-Default-Page,Microsoft-IIS/10.0,ASP... |
| 49 | smart.pingan.com.cn | 101.89.96.220 | 403 Forbidden | nginx... |
| 50 | srm.pingan.com.cn | 120.233.193.102 | KTSRM | BigIP[waf],jQuery,f5-big-ip-waf,nginx... |
| 51 | sse.pingan.com.cn | 45.65.23.213 | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113],Nginx-Default... |
| 52 | sso.pingan.com.cn | 124.196.28.30 |  | - |
| 53 | ssologin.pingan.com.cn | 124.196.28.30 |  | - |
| 54 | statics.pingan.com.cn | 58.220.6.102, 58.220.6.109 | 平安好福利 | f5-big-ip-waf,Byte-nginx,BigIP[waf]... |
| 55 | stg.pingan.com.cn | 180.168.128.107 |  | - |
| 56 | stock.pingan.com.cn | 202.69.18.155 |  | - |
| 57 | t.pingan.com.cn | 202.69.26.20 |  | - |
| 58 | te.pingan.com.cn | 45.65.23.171 | 平安特管·特资e | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113]... |
| 59 | test-api.pingan.com.cn | 113.204.125.81 | None | f5-big-ip-waf,BigIP[waf]... |
| 60 | trip.pingan.com.cn | 221.179.19.91 | Welcome to nginx! | BigIP[waf],f5-big-ip-waf,loading,Nginx-Default-Test-Page... |
| 61 | w.pingan.com.cn | 222.186.177.163, 61.147.235.175 | None | Byte-nginx... |
| 62 | wap.pingan.com.cn | 202.69.26.16 | 301 Moved Permanently | openresty,f5-big-ip-waf,BigIP[waf]... |
| 63 | webmail.pingan.com.cn | 124.196.28.30 |  | - |
| 64 | wms.pingan.com.cn | 45.65.23.171 | Welcome to nginx! | Nginx-Default-Test-Page,NRPd/6.1.4[3450a98:1773:3c338a6:1870... |
| 65 | www.pingan.com.cn | 202.69.26.13 | 设备租赁_商业租赁_委托租赁_平安车管 | BigIP[waf],loading,f5-big-ip-waf,Apache-Struts2,jQuery... |
| 66 | yl.pingan.com.cn | 113.105.78.152 | HTTP状态 404 - 未找到 | openresty,f5-big-ip-waf,BigIP[waf]... |

## 三、`*.pingan.com`（98条）

### 已有资产（TscanPlus 确认存活）

| # | 域名 | IP | Title | 关键指纹 |
|---|------|-----|-------|---------|
| 1 | cdn-health.pingan.com | - | - | - |
| 2 | ehis-mcs.pingan.com | - | - | - |
| 3 | health.pingan.com | 58.220.6.102, 58.220.6.109 | 平安健康保险 | f5-big-ip-waf,Byte-nginx,BigIP[waf]... |
| 4 | ice-health.pingan.com | - | - | - |
| 5 | ice-stg1-health.pingan.com | - | - | - |
| 6 | ice-stg2-health.pingan.com | - | - | - |
| 7 | ice-stg5-health.pingan.com | - | - | - |
| 8 | parun.pingan.com | - | - | - |
| 9 | suishenyi.pingan.com | - | - | - |

### 仅证书透明度（未通过 TscanPlus 确认存活）

| # | 域名 | 备注 |
|---|------|------|
| 10 | parun.pingan.com | 生产 |
| 11 | cdn-health.pingan.com | 生产 |
| 12 | ice-stg1-health.pingan.com | 生产 |
| 13 | ice-stg5-health.pingan.com | 生产 |
| 14 | ice-stg2-health.pingan.com | 生产 |
| 15 | ice-health.pingan.com | 生产 |
| 16 | suishenyi.pingan.com | 生产 |
| 17 | ehis-mcs.pingan.com | 生产 |

### 集团其他资产（与健康险无直接关联）

| # | 域名 | IP | Title | 关键指纹 |
|---|------|-----|-------|---------|
| 1 | a.pingan.com | 61.241.20.108 | None | openresty... |
| 2 | api.pingan.com | 202.69.21.123 | 平安开放平台 | YApi可视化接口管理平台,f5-big-ip-waf,Oracle-JAVA,Apache-Struts2,jQuer... |
| 3 | asset.pingan.com | 58.220.6.102, 58.220.6.109 | 平安资管_平安资产管理_资产投资管理 | f5-big-ip-waf,BigIP[waf],jQuery,Byte-nginx,Apache-Struts2... |
| 4 | ats.pingan.com | 211.139.177.117 | 平安人 校招系统 | BigIP[waf],nginx,Apache-Struts2,f5-big-ip-waf... |
| 5 | b.pingan.com | 45.65.23.154 | None | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113]... |
| 6 | bank.pingan.com | 222.186.177.163, 61.147.235.175 | 平安银行官方网站 | jQuery,Byte-nginx... |
| 7 | bip.pingan.com | 45.65.23.139 | 302 Found | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113]... |
| 8 | br.pingan.com | 45.65.23.146 | None | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113]... |
| 9 | c.pingan.com | 124.196.28.139 | Welcome to nginx! | Nginx-Default-Test-Page,NRPd/6.1.4[3450a98:1773:3c338a6:1870... |
| 10 | campus.pingan.com | 61.241.22.79 | 中国平安校园招聘 | f5-big-ip-waf,nginx,Apache-Struts2,BigIP[waf]... |
| 11 | cash.pingan.com | 202.69.21.176 |  | - |
| 12 | cc.pingan.com | 202.69.26.98 | 平安银行信用卡中心官方网站_平安官网 | loading,jQuery... |
| 13 | ccp.pingan.com | 183.2.191.242 | 寿险内容云 | Apache-Struts2,jQuery,nginx... |
| 14 | cgi.pingan.com | 120.233.149.201 | Welcome to nginx! | openresty,Nginx-Default-Test-Page... |
| 15 | creditcard.pingan.com | 222.186.177.163, 61.147.235.175 | 银行信用卡-平安银行信用卡中心,网上 | jQuery,BigIP[waf],Byte-nginx,f5-big-ip-waf... |
| 16 | d.pingan.com | 61.241.22.31 | 集团客户体验调研平台 | f5-big-ip-waf,BigIP[waf]... |
| 17 | dd.pingan.com | 124.196.83.131 | 集团客户体验调研平台 | BigIP[waf],f5-big-ip-waf... |
| 18 | drs.pingan.com | 222.186.177.163, 61.147.235.175 | Welcome to nginx! | Nginx-Default-Test-Page,Byte-nginx... |
| 19 | e.pingan.com | 183.62.123.44 |  | - |
| 20 | eid.pingan.com | 113.204.125.80 | Welcome to nginx! | PA-ELB,Nginx-Default-Test-Page... |
| 21 | ex.pingan.com | 202.69.26.68 | 301 Moved Permanently | f5-big-ip-waf,loading,BigIP[waf]... |
| 22 | f.pingan.com | 61.241.22.49 | 平安基金 | Apache-Struts2,loading,BigIP[waf],f5-big-ip-waf... |
| 23 | fund.pingan.com | 183.62.123.45 | 平安基金管理有限公司 | JSP,BigIP[waf],jQuery,loading,f5-big-ip-waf... |
| 24 | futures.pingan.com | 202.69.26.80 | 骞冲畨鏈熻揣-骞冲畨闆嗗洟鏃椾笅鎸佺 | BigIP[waf],jQuery,f5-big-ip-waf,loading... |
| 25 | g.pingan.com | 211.139.177.56 | 40x | openresty,f5-big-ip-waf,BigIP[waf]... |
| 26 | gallery.pingan.com | 45.65.20.143 | None | Yii PHP Framework (Default Favicon),f5-big-ip-waf,BigIP[waf]... |
| 27 | gc.pingan.com | 113.108.21.132 | 301 Moved Permanently | nginx,f5-big-ip-waf,BigIP[waf]... |
| 28 | gj.pingan.com | 61.241.23.15 | 平安金管家，值得信赖的移动金融生活 | 平安金管家，值得信赖的移动金融生活... |
| 29 | h5.pingan.com | 211.139.177.56 | Document | f5-big-ip-waf,BigIP[waf],openresty... |
| 30 | home.pingan.com | 61.241.21.55 | 平安好福利 | loading... |
| 31 | ibank.pingan.com | 45.65.23.154 | 301 Moved Permanently | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113]... |
| 32 | icp.pingan.com | 45.65.22.154 | 电子备案 | nginx... |
| 33 | img1.pingan.com | 202.69.26.6 | 设备租赁_商业租赁_委托租赁_平安车管 | loading,Apache-Struts2,BigIP[waf],f5-big-ip-waf,jQuery... |
| 34 | img2.pingan.com | 58.220.6.102, 58.220.6.109 | 设备租赁_商业租赁_委托租赁_平安车管 | Byte-nginx,jQuery,Apache-Struts2,f5-big-ip-waf,BigIP[waf]... |
| 35 | information.pingan.com | 113.98.243.225 |  | - |
| 36 | invest.pingan.com | 202.69.26.86 | 投资银行-投行业务-平安投资银行 | Apache-Struts2,Oracle-JAVA,jQuery-ui,BigIP[waf],loading,f5-b... |
| 37 | ir.pingan.com | 202.69.26.65 | 投资者关系首页-中国平安 | f5-big-ip-waf,BigIP[waf],jQuery,Oracle-JAVA,loading... |
| 38 | irm.pingan.com | 47.243.3.69 | Smart IR | f5-big-ip-waf,loading,BigIP[waf]... |
| 39 | isrc.pingan.com | 61.241.20.113 | 平安安全应急响应中心 | Apache-Struts2,BigIP[waf],f5-big-ip-waf... |
| 40 | leasing.pingan.com | 202.69.26.118 | 302 Found | loading,BigIP[waf],f5-big-ip-waf... |
| 41 | life.pingan.com | 183.2.191.65 | 平安人寿保险官网-人寿保险,重疾保险 | openresty,jQuery... |
| 42 | loan.pingan.com | 202.69.26.40 |  | - |
| 43 | m.pingan.com | 202.69.26.16 | 中国平安移动官网提供专业的贷款、理 | Mongo-Express,Node.js,loading,f5-big-ip-waf,BigIP[waf]... |
| 44 | message.pingan.com | 120.234.65.226, 120.234.65.227, 124.196.53.109 |  | - |
| 45 | mi.pingan.com | 202.69.21.111 | None | server... |
| 46 | mx1.pingan.com | 202.69.19.104 |  | - |
| 47 | mx2.pingan.com | 202.69.19.105 |  | - |
| 48 | mx4.pingan.com | 202.69.18.86 |  | - |
| 49 | mx5.pingan.com | 202.69.19.217 |  | - |
| 50 | mx7.pingan.com | 202.69.17.26 |  | - |
| 51 | mx8.pingan.com | 202.69.17.27 |  | - |
| 52 | ok.pingan.com | 58.216.14.91, 58.216.14.92, 58.216.14.93 | Document | Tengine,Citrix-NetScaler,f5-big-ip-waf,BigIP[waf]... |
| 53 | one.pingan.com | 43.230.223.2 | None | None... |
| 54 | opa.pingan.com | 202.69.20.228 | OnepinganDesign | openresty,f5-big-ip-waf,BigIP[waf],Apache-Struts2... |
| 55 | osr.pingan.com | 61.241.21.42 | Welcome to nginx! | loading,Nginx-Default-Test-Page... |
| 56 | pms.pingan.com | 183.2.191.74 | 采购系统 | loading... |
| 57 | post.pingan.com | 113.108.21.85 | -Error report | -Error report... |
| 58 | promo.pingan.com | 58.216.14.91, 58.216.14.92, 58.216.14.93 | None | BigIP[waf],f5-big-ip-waf,Tengine... |
| 59 | property.pingan.com | 58.216.14.91, 58.216.14.92, 58.216.14.93 | 平安财产保险_中国平安 | BigIP[waf],Tengine,Citrix-NetScaler,Apache-Struts2,f5-big-ip... |
| 60 | q.pingan.com | 121.12.82.190 | None | openresty... |
| 61 | qr.pingan.com | 45.65.23.155 | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113],Nginx-Default... |
| 62 | realestate.pingan.com | 43.230.223.234 | None | loading... |
| 63 | run.pingan.com | 45.65.20.119 | -Error report | f5-big-ip-waf,openresty,BigIP[waf]... |
| 64 | s.pingan.com | 202.69.24.24 | None | Oracle-JAVA,JSP,openresty/1.21.4.1... |
| 65 | search.pingan.com | 211.139.177.62 | 平安查-中国平安 | loading... |
| 66 | security.pingan.com | 61.241.20.113 | 平安安全应急响应中心 | BigIP[waf],Apache-Struts2,f5-big-ip-waf... |
| 67 | ssl.pingan.com | 202.69.26.101 | 302 Found | loading,BigIP[waf],f5-big-ip-waf... |
| 68 | star.pingan.com | 45.65.23.39 | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113],Nginx-Default... |
| 69 | static1.pingan.com | 202.69.26.6 | 设备租赁_商业租赁_委托租赁_平安车管 | loading,f5-big-ip-waf,BigIP[waf],Apache-Struts2,jQuery... |
| 70 | static2.pingan.com | 58.215.210.132, 58.215.210.220 | 设备租赁_商业租赁_委托租赁_平安车管 | f5-big-ip-waf,jQuery,Byte-nginx,BigIP[waf],Apache-Struts2... |
| 71 | stock.pingan.com | 61.241.22.133 | 【平安证券】股票开户_理财产品_基金 | BigIP[waf],openresty,f5-big-ip-waf... |
| 72 | sx.pingan.com | 101.89.94.214 |  | - |
| 73 | t.pingan.com | 202.69.26.102 | 平安信托移动官网-中国平安 | f5-big-ip-waf,BigIP[waf],jQuery,loading,JSP... |
| 74 | talent.pingan.com | 202.69.30.155 | 中国平安 | BigIP[waf],nginx,f5-big-ip-waf... |
| 75 | taobao.pingan.com | 202.69.26.12 | 中国平安保险集团提供专业的银行、保 | JSP,BigIP[waf],f5-big-ip-waf,jQuery... |
| 76 | td.pingan.com | 45.65.20.143 | 智慧品牌流量经营平台 | BigIP[waf],f5-big-ip-waf... |
| 77 | tech.pingan.com | 202.69.20.228 | 平安科技 | openresty,f5-big-ip-waf,BigIP[waf]... |
| 78 | test-api.pingan.com | 114.141.178.28 |  | - |
| 79 | tr.pingan.com | 45.65.20.143 | None | f5-big-ip-waf,Yii PHP Framework (Default Favicon),BigIP[waf]... |
| 80 | trust.pingan.com | 183.62.123.92 | 平安信托  | 中国平安 | jQuery,JSP,Apache-Struts2... |
| 81 | u.pingan.com | 61.241.22.34 | 404 Not Found | loading,BigIP[waf],f5-big-ip-waf... |
| 82 | ued.pingan.com | 202.69.26.69 | 302 Found | BigIP[waf],loading,f5-big-ip-waf... |
| 83 | wap.pingan.com | 202.69.26.16 | 301 Moved Permanently | f5-big-ip-waf,openresty,BigIP[waf]... |
| 84 | wealth.pingan.com | 202.69.26.12 | 信托_投资理财_信托产品_平安信托_信托 | Apache-Struts2,f5-big-ip-waf,ecology泛微e-mobile,BigIP[waf]... |
| 85 | wm.pingan.com | 45.65.23.39 | 平安理财有限责任公司 | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113]... |
| 86 | wr.pingan.com | 183.2.191.207, 221.179.19.207, 61.241.23.207 |  | - |
| 87 | www.pingan.com | 211.139.177.62 | 平安集团官网_保险·车险·健康险·信用 | loading... |
| 88 | x.pingan.com | 202.69.26.13 | 设备租赁_商业租赁_委托租赁_平安车管 | BigIP[waf],loading,f5-big-ip-waf,jQuery,Apache-Struts2... |
| 89 | yl.pingan.com | 58.216.14.91, 58.216.14.92, 58.216.14.93 | 首页-平安养老险-中国平安 | Tengine,Citrix-NetScaler... |

---

## 数据来源

| 来源 | 数量 | 说明 |
|------|------|------|
| 手动收集 | 35 | 原始资产 |
| crt.sh 证书透明度 | +48 | 通过 crtsh_fetch.py 扩展 |
| TscanPlus 子域名爆破 | +148 | CLI 字典爆破三个根域名 |
| **合计（去重）** | **244** | |

---

## IP 段分布（TscanPlus 确认存活）

| IP 段 | 关联子域示例 | 推测用途 |
|-------|-------------|---------|
| 58.220.6.102-109 | www.health, open.health, wap.health, s.health, download.cn, mall.cn | 主站/CDN 段 |
| 58.216.14.91-98 | login.health, activity.health, m.health, product.health, promo.com, ok.com, yl.com | 业务段 |
| 222.186.177.163 / 61.147.235.175 | m1.health, w.cn, bank.com | 独立段 |
| 124.196.49.105 | mobile.health | 独立 IP |
| 202.69.x.x | api, ir, tech, cc, fund, one.cn, portal.cn 等 | 集团基础设施段 |
| 45.65.23.x | bank.cn, b1.cn, mp.cn, wms.cn, star.com 等 | 银行/理财段 |
| 61.241.x.x | campus, d, home, gc, security, stock 等 | 集团办公段 |

---

## 下一步方向

| 阶段 | 说明 | 状态 |
|------|------|------|
| 资产收集 | 手动 + crt.sh + TscanPlus 字典爆破 | 已完成 |
| 存活探测 | TscanPlus 已确认 157 条存活 | 已完成 |
| Web 指纹识别 | 对存活域名做详细指纹 | 待执行 |
| 端口扫描 | 对独立 IP 做全端口扫描 | 待执行 |
| JS 信息提取 | 从 Nuxt.js/Spring 等站点提取接口 | 待执行 |
| 漏洞探测 | 基于指纹做 POC 验证 | 待执行 |