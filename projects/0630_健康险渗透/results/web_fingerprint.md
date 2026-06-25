# 健康险渗透 - Web 指纹扫描报告

> 扫描时间：2026-06-25
> 扫描模块：TscanPlus URL 指纹识别（-finger all 主动指纹）
> 扫描目标：244 条域名（488 条 URL）
> 识别结果：269 条 URL 指纹记录，覆盖 207 个独立域名

---

## 统计概览

| 分类 | 域名数 | 说明 |
|------|--------|------|
| 健康险相关（生产） | 54 | health/ehis/mcp/golden-key 等 |
| 健康险相关（STG） | 32 | 预发布/测试环境 |
| 集团其他资产 | 121 | 银行/证券/基金/信托等 |
| **合计** | **207** | |

## 一、健康险相关 - 生产环境（54个域名）

| # | 域名 | Title | 关键指纹（去常见） | 中间件 | 特殊路径 |
|---|------|-------|-----------------|--------|---------|
| 1 | activity.health.pingan.com | activity | - | Tengine | - |
| 2 | cdn-ehis-golden-key.pingan.com.cn | - | None | - | - |
| 3 | cdn-health.pingan.com | - | None | - | - |
| 4 | cdn-suishenyi.health.pingan.com | - | None | - | - |
| 5 | ehis-br-consultant-pks.pingan.com.cn | 快捷服务 | - | Tengine | - |
| 6 | ehis-br-consultant.pingan.com.cn | 快捷服务 | - | Tengine | - |
| 7 | ehis-content.health.pingan.com | 平安健康保险 | - | Tengine | - |
| 8 | ehis-eqz-dmzweb-prd.pingan.com.cn | - | None | - | - |
| 9 | ehis-golden-key.health.pingan.com | 金钥匙 | Moxa_NPort_5150A, Apereo-CAS | Byte-nginx | /cas/login |
| 10 | ehis-golden-key.pingan.com.cn | 金钥匙 | Moxa_NPort_5150A, Apereo-CAS | Byte-nginx | /cas/login |
| 11 | ehis-hcs.pingan.com.cn | - | None | - | - |
| 12 | ehis-hems.pingan.com.cn | - | None | - | - |
| 13 | ehis-hisos.health.pingan.com | - | None | - | - |
| 14 | ehis-hsms-dmzweb.health.pingan.com | Welcome to OpenResty! | OpenResty-Default-Page | Byte-nginx | - |
| 15 | ehis-hsms-openresty-dmzweb-prd.health.pingan.com | Welcome to OpenResty! | OpenResty-Default-Page | Byte-nginx | - |
| 16 | ehis-icp-dmz-web.health.pingan.com | 403 Forbidden | - | Tengine | - |
| 17 | ehis-ivs.pingan.com.cn | EHIS-IVS | - | Tengine | - |
| 18 | ehis-mcs.pingan.com | 正在加载中... | - | Byte-nginx | - |
| 19 | ehis-service-dmzweb-prd.pingan.com.cn | - | None | - | - |
| 20 | ehis-store.health.pingan.com | 404 Not Found | - | Byte-nginx | - |
| 21 | ehis-tcm-dmzweb.health.pingan.com | 403 Forbidden | - | Byte-nginx | - |
| 22 | ehis-unity.health.pingan.com | 医健工作台 | - | Byte-nginx | - |
| 23 | ehis-wbzs-minio.health.pingan.com | - | amazon-waf | - | - |
| 24 | ehis-wbzs-web.health.pingan.com | 平安健康险企业微信助手 | RabbitMQ, 百度-UEditor, Tencent-企业微信 | Byte-nginx | /rabbitmq/ |
| 25 | ehis.health.pingan.com | - | None | - | - |
| 26 | ehis.home.pingan.com.cn | 平安好福利 | 七牛CDN | nginx | - |
| 27 | eqzprd.health.pingan.com | e企赚 | - | Byte-nginx | - |
| 28 | group-cms.health.pingan.com | 团险e键通 | Apereo-CAS | Byte-nginx | /cas/login, /cas/login |
| 29 | group-hr.health.pingan.com | E企投线上保单服务平台 | - | Byte-nginx | - |
| 30 | group.health.pingan.com | 403 Forbidden | - | Byte-nginx | - |
| 31 | health.pingan.com | 平安健康保险 | 百度-UEditor, 用友NC, Tomcat-Manager | Byte-nginx | /js/ueditor/ueditor.all.js, /manager/status |
| 32 | health.pingan.com.cn | 平安健康保险 | 百度-UEditor, 用友NC, Tomcat-Manager | Byte-nginx | /nc/servlet/, /manager/status |
| 33 | healthcare.pingan.com.cn | - | None | - | - |
| 34 | healthtech.pingan.com.cn | - | None | - | - |
| 35 | helper-market.health.pingan.com | 403 Forbidden | - | Byte-nginx | - |
| 36 | helper.health.pingan.com | 加载中 | Apache-Struts2, Apereo-CAS, Ruby | Tengine | /cas/login |
| 37 | ice-health.pingan.com | - | - | Tengine | - |
| 38 | iopen.health.pingan.com | 平安健康险开放平台 | None, Nginx | openresty | - |
| 39 | login.health.pingan.com | 平安健康保险 | - | Tengine | - |
| 40 | m.health.pingan.com | - | - | Tengine | - |
| 41 | m1.health.pingan.com | - | - | Byte-nginx | - |
| 42 | mcore.health.pingan.com | 平安健康保险 | - | Byte-nginx | - |
| 43 | mcp-health.pingan.com.cn | - | None | - | - |
| 44 | mcp-test-health.pingan.com.cn | - | None, PA-ELB | PA-ELB | - |
| 45 | mcp.pingan.com.cn | - | None | - | - |
| 46 | mini-program.health.pingan.com | 403 Forbidden | - | Tengine | - |
| 47 | mobile.health.pingan.com | - | - | nginx | - |
| 48 | nbmcore.health.pingan.com | - | - | Byte-nginx | - |
| 49 | open.health.pingan.com | 平安健康险开放平台 | - | Byte-nginx | - |
| 50 | product.health.pingan.com | 403 Forbidden | - | Tengine | - |
| 51 | recorder.health.pingan.com | Welcome to nginx! | PHPInfo, Nginx-Default-Test-Page | loading | /info.php |
| 52 | s.health.pingan.com | 平安健康保险 | - | Byte-nginx | - |
| 53 | suishenyi.pingan.com | - | SpringBoot-Error, Spring框架, vmware-SpringBoot-Framework | Byte-nginx | /error |
| 54 | wap.health.pingan.com | 平安健康保险 | Vue.js, NuxtJS, Mongo-Express, Node.js | Tengine | - |

## 二、健康险相关 - 预发布/测试环境（32个域名）

| # | 域名 | Title | 关键指纹（去常见） | 中间件 |
|---|------|-------|-----------------|--------|
| 1 | cdn-ehis-golden-key-stg.pingan.com.cn | - | None | - |
| 2 | cdn-ehis-golden-key-stg5.pingan.com.cn | - | None | - |
| 3 | ehis-activity-stg1.health.pingan.com | activity | - | Byte-nginx |
| 4 | ehis-activity-stg5.health.pingan.com | activity | - | Byte-nginx |
| 5 | ehis-audit-ivs-dmz-stg1.pingan.com.cn | 403 Forbidden | - | Byte-nginx |
| 6 | ehis-audit-ivs-dmz-stg2.pingan.com.cn | - | None | - |
| 7 | ehis-audit-ivs-dmz-stg5.pingan.com.cn | - | None | - |
| 8 | ehis-br-consultant-h5-stg1.pingan.com.cn | - | None | - |
| 9 | ehis-br-consultant-h5-stg5.pingan.com.cn | - | None | - |
| 10 | ehis-golden-key-stg.pingan.com.cn | 金钥匙 | Moxa_NPort_5150A, Apereo-CAS | Byte-nginx |
| 11 | ehis-golden-key-stg5.pingan.com.cn | 金钥匙 | Moxa_NPort_5150A, Apereo-CAS | Byte-nginx |
| 12 | ehis-hcs-stg1.pingan.com.cn | - | None | - |
| 13 | ehis-hcs-stg2.pingan.com.cn | - | None | - |
| 14 | ehis-hcs-stg3.pingan.com.cn | - | None | - |
| 15 | ehis-hcs-stg5.pingan.com.cn | - | None | - |
| 16 | ehis-hems-dmz-stg1.pingan.com.cn | - | None | - |
| 17 | ehis-hems-dmz-stg5.pingan.com.cn | - | None | - |
| 18 | ehis-iproductmarket-stg1.health.pingan.com | 403 Forbidden | - | Byte-nginx |
| 19 | ehis-iproductmarket-stg2.health.pingan.com | - | None | - |
| 20 | ehis-iproductmarket-stg5.health.pingan.com | - | None | - |
| 21 | ehis-ivs-dmzweb-stg1.pingan.com.cn | EHIS-IVS | - | Byte-nginx |
| 22 | ehis-ivs-dmzweb-stg2.pingan.com.cn | - | None | - |
| 23 | ehis-ivs-dmzweb-stg5.pingan.com.cn | EHIS-IVS | - | Byte-nginx |
| 24 | ehis-mcore-stg1.health.pingan.com | - | None | - |
| 25 | ehis-mcore-stg1.pingan.com.cn | - | None | - |
| 26 | ehis-mcp-gateway-wgq-padis-dmzstg5.pingan.com.cn | - | None | - |
| 27 | ehis-mini-program-dmzweb-stg1.health.pingan.com | 403 Forbidden | - | Byte-nginx |
| 28 | ehis-mini-program-dmzweb-stg2.health.pingan.com | - | None | - |
| 29 | ehis-yedi-ngweb-stg5.health.pingan.com | Welcome to nginx! | PA-ELB, Nginx-Default-Test-Page | PA-ELB |
| 30 | ice-stg1-health.pingan.com | 智能营销平台 | Ruby | Byte-nginx |
| 31 | ice-stg2-health.pingan.com | - | None | - |
| 32 | ice-stg5-health.pingan.com | 智能营销平台 | Ruby | Byte-nginx |

## 三、集团其他资产（121个域名）

| # | 域名 | Title | 关键指纹（去常见） |
|---|------|-------|-----------------|
| 1 | a.pingan.com | - | Apereo-CAS, Nginx |
| 2 | ab.pingan.com.cn | - | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], None |
| 3 | ant.pingan.com.cn | - | None |
| 4 | api.pingan.com | 平安开放平台 | JSP, YApi可视化接口管理平台, Apache-Struts2, Oracle-JAVA |
| 5 | api.pingan.com.cn | 平安开放平台 | JSP, YApi可视化接口管理平台, Apache-Struts2, Oracle-JAVA |
| 6 | asset.pingan.com | 平安资管_平安资产管理_资产投资管理 | Apache-Struts2, 百度-UEditor |
| 7 | ats.pingan.com | 平安人 校招系统 | Apache-Struts2 |
| 8 | b.pingan.com | - | - |
| 9 | b1.pingan.com.cn | 平安银行移动官网 | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], None, Apache-Struts2, SpringBoot-Error |
| 10 | bank.pingan.com | 平安银行官方网站 | 百度-UEditor |
| 11 | bank.pingan.com.cn | Error | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113] |
| 12 | bbc.pingan.com.cn | - | None |
| 13 | bip.pingan.com | - | None |
| 14 | br.pingan.com | 平安银行官方网站 | Tomcat-Manager |
| 15 | c.pingan.com | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], Nginx-Default-Test-Page |
| 16 | c.pingan.com.cn | - | None |
| 17 | campus.pingan.com | 中国平安校园招聘 | Apache-Struts2, 百度-UEditor |
| 18 | cash.pingan.com | - | None |
| 19 | cash.pingan.com.cn | - | None |
| 20 | cc.pingan.com | 平安银行信用卡中心官方网站_平安官网 | 百度-UEditor |
| 21 | ccp.pingan.com | 寿险内容云 | Apache-Struts2 |
| 22 | cf.pingan.com.cn | - | None, Java, vmware-SpringBoot-Framework |
| 23 | cg.pingan.com.cn | 待办系统 | - |
| 24 | cgi.pingan.com | Welcome to nginx! | Nginx-Default-Test-Page |
| 25 | creditcard.pingan.com | 银行信用卡-平安银行信用卡中心,网上 | 百度-UEditor |
| 26 | creditcard.pingan.com.cn | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], PHPInfo, Nginx-Default-Test-Page |
| 27 | cz.pingan.com.cn | 平安银行官方网站 | 百度-UEditor |
| 28 | d.pingan.com | 集团客户体验调研平台 | - |
| 29 | dd.pingan.com | 集团客户体验调研平台 | - |
| 30 | download.pingan.com.cn | 平安集团官网_保险·车险·健康险·信用 | - |
| 31 | drs.pingan.com | Welcome to nginx! | Nginx-Default-Test-Page |
| 32 | dv.pingan.com.cn | Welcome to nginx! | Nginx-Default-Test-Page |
| 33 | e.pingan.com | 平安寿险官方网站（e.pingan.com）-互联网 | Nginx |
| 34 | ebank.pingan.com.cn | HTTP Status 404 | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], SpringBoot-Error |
| 35 | eid.pingan.com | - | None |
| 36 | eps.pingan.com.cn | - | None |
| 37 | ex.pingan.com | - | None |
| 38 | f.pingan.com | 平安基金 | Apache-Struts2 |
| 39 | fund.pingan.com | 平安基金管理有限公司 | Tomcat-Manager |
| 40 | fund.pingan.com.cn | - | Tomcat-Manager |
| 41 | futures.pingan.com | 骞冲畨鏈熻揣-骞冲畨闆嗗洟鏃椾笅鎸佺 | sogou站长平台, 百度-UEditor |
| 42 | futures.pingan.com.cn | 平安期货-平安集团旗下持牌期货公司 | sogou站长平台, 百度-UEditor |
| 43 | g.pingan.com | 40x | Nginx |
| 44 | gallery.pingan.com | 平安品牌资产管理平台 | 易软天创-禅道系统 |
| 45 | gc.pingan.com | - | - |
| 46 | gc.pingan.com.cn | - | - |
| 47 | gj.pingan.com | 平安金管家，值得信赖的移动金融生活 | 平安金管家，值得信赖的移动金融生活 |
| 48 | h5.pingan.com | OneKey | jQuery-ui, Nginx |
| 49 | hermes.pingan.com.cn | - | None |
| 50 | home.pingan.com | 平安好福利 | - |
| 51 | home.pingan.com.cn | 平安好福利 | - |
| 52 | ibank.pingan.com | 平安个人网上银行交易系统 | - |
| 53 | ibc.pingan.com.cn | 出错了 | None, React |
| 54 | ibs.pingan.com.cn | Welcome to nginx! | None, Nginx-Default-Test-Page |
| 55 | icp.pingan.com | 电子备案 | - |
| 56 | img1.pingan.com | 设备租赁_商业租赁_委托租赁_平安车管 | Apache-Struts2, 百度-UEditor |
| 57 | img2.pingan.com | 设备租赁_商业租赁_委托租赁_平安车管 | Apache-Struts2, 百度-UEditor |
| 58 | information.pingan.com | - | None |
| 59 | invest.pingan.com | 投资银行-投行业务-平安投资银行 | jQuery-ui, Apache-Struts2, fortinet-fortimail, Oracle-JAVA, 百度-UEditor |
| 60 | ir.pingan.com | 投资者关系首页-中国平安 | Oracle-JAVA, 百度-UEditor |
| 61 | irm.pingan.com | Smart IR | - |
| 62 | isrc.pingan.com | 平安安全应急响应中心 | None, Apache-Struts2 |
| 63 | leasing.pingan.com | 中国平安保险集团提供专业的银行、保 | 百度-UEditor |
| 64 | legacy.pingan.com.cn | - | None |
| 65 | life.pingan.com | 平安人寿保险官网-人寿保险,重疾保险 | Nginx, 和欣控制(Hysine) Webtalk 系统 |
| 66 | link.pingan.com.cn | - | None |
| 67 | loan.pingan.com | - | None |
| 68 | ltc.pingan.com.cn | 平安智慧长护经办管理系统 | - |
| 69 | m.pingan.com | 中国平安移动官网提供专业的贷款、理 | qingyuan-management-system, Mongo-Express, sogou站长平台, Vue.js, 阿里巴巴ottermanager |
| 70 | mailout2.pingan.com.cn | - | None |
| 71 | mall.pingan.com.cn | 壹钱包 中国平安旗下品牌 | Apache-Struts2 |
| 72 | message.pingan.com | - | None |
| 73 | message.pingan.com.cn | - | None |
| 74 | mi.pingan.com | - | server, http基本认证 |
| 75 | mp.pingan.com.cn | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], None, Nginx-Default-Test-Page |
| 76 | mx4.pingan.com.cn | - | None |
| 77 | mx5.pingan.com | - | None |
| 78 | mx5.pingan.com.cn | - | None |
| 79 | mx7.pingan.com.cn | - | None |
| 80 | mx8.pingan.com | - | None |
| 81 | oa.pingan.com.cn | - | None |
| 82 | ok.pingan.com | Document | ETUNG-router |
| 83 | one.pingan.com | 平安一账通官网 | Apache-Struts2, Apereo-CAS, Nginx |
| 84 | one.pingan.com.cn | 平安一账通官网 | Apache-Struts2, Nginx |
| 85 | opa.pingan.com | OnepinganDesign | Apache-Struts2, Nginx |
| 86 | open.pingan.com.cn | - | Swagger-API, Apereo-CAS, Nginx, JSP |
| 87 | openapi.pingan.com.cn | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], Nginx-Default-Test-Page |
| 88 | osr.pingan.com | Welcome to nginx! | Nginx-Default-Test-Page |
| 89 | parun.pingan.com | -Error report | - |
| 90 | pms.pingan.com | 采购系统 | None |
| 91 | portal.pingan.com.cn | 平安开放平台 | JSP, YApi可视化接口管理平台, Apache-Struts2, Oracle-JAVA |
| 92 | post.pingan.com | -Error report | -Error report |
| 93 | promo.pingan.com | - | - |
| 94 | push.pingan.com.cn | - | None |
| 95 | q.pingan.com | - | Nginx |
| 96 | qr.pingan.com | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], None, Nginx-Default-Test-Page |
| 97 | realestate.pingan.com | - | - |
| 98 | resources.pingan.com.cn | 设备租赁_商业租赁_委托租赁_平安车管 | Apache-Struts2, 百度-UEditor |
| 99 | run.pingan.com | -Error report | Nginx |
| 100 | s.pingan.com | - | openresty/1.21.4.1, Oracle-JAVA, Nginx, JSP |
| 101 | secmail.pingan.com.cn | IIS Windows Server | IIS-Windows-Server-Default-Page, Microsoft-IIS/10.0, Microsoft-ASP.NET |
| 102 | security.pingan.com | 平安安全应急响应中心 | Apache-Struts2 |
| 103 | smart.pingan.com.cn | 403 Forbidden | - |
| 104 | srm.pingan.com.cn | - | None |
| 105 | sse.pingan.com.cn | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], Nginx-Default-Test-Page |
| 106 | sso.pingan.com.cn | - | None |
| 107 | star.pingan.com | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], Nginx-Default-Test-Page |
| 108 | static2.pingan.com | - | Tomcat-Manager |
| 109 | stock.pingan.com | 【平安证券】股票开户_理财产品_基金 | openresty/1.21.4.1, None, Nginx |
| 110 | stock.pingan.com.cn | - | None |
| 111 | t.pingan.com.cn | - | None |
| 112 | talent.pingan.com | 中国平安 | - |
| 113 | te.pingan.com.cn | 平安特管·特资e | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113] |
| 114 | tr.pingan.com | - | ArcGIS |
| 115 | trip.pingan.com.cn | Welcome to nginx! | Nginx-Default-Test-Page |
| 116 | trust.pingan.com | 平安信托  | 中国平安 | Apache-Struts2, JSP |
| 117 | w.pingan.com.cn | - | - |
| 118 | wealth.pingan.com | 信托_投资理财_信托产品_平安信托_信托 | Apache-Struts2, ecology泛微e-mobile |
| 119 | webmail.pingan.com.cn | - | None |
| 120 | wm.pingan.com | 平安理财有限责任公司 | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113] |
| 121 | wms.pingan.com.cn | Welcome to nginx! | NRPd/6.1.4[3450a98:1773:3c338a6:1870:20250113], None, Nginx-Default-Test-Page |

## 四、高价值发现

| 指纹 | 数量 | 关联域名 | 风险/利用方向 |
|------|------|---------|-------------|
| UEditor | 18 | asset.pingan.com, bank.pingan.com, campus.pingan.com (+15) | 百度 UEditor 可能存在文件上传/SSRF 漏洞 |
| Nginx-Default | 16 | c.pingan.com, cgi.pingan.com, creditcard.pingan.com.cn (+13) | Nginx 默认页面，可能配置不当 |
| Apereo-CAS | 9 | a.pingan.com, ehis-golden-key-stg.pingan.com.cn, ehis-golden-key-stg5.pingan.com.cn (+6) | CAS 登录系统，可能存在反序列化漏洞 |
| Tomcat-Manager | 6 | br.pingan.com, fund.pingan.com.cn, fund.pingan.com (+3) | Tomcat Manager 暴露，可能弱口令/部署 WAR |
| SpringBoot | 4 | b1.pingan.com.cn, cf.pingan.com.cn, ebank.pingan.com.cn (+1) | SpringBoot 应用，可能 Actuator 未授权 |
| Moxa | 4 | ehis-golden-key-stg.pingan.com.cn, ehis-golden-key-stg5.pingan.com.cn, ehis-golden-key.health.pingan.com (+1) | Moxa 工业设备，可能未授权 |
| YApi | 3 | api.pingan.com, api.pingan.com.cn, portal.pingan.com.cn | YApi 接口管理，可能未授权/SQL注入 |
| Ruby | 3 | helper.health.pingan.com, ice-stg1-health.pingan.com, ice-stg5-health.pingan.com | Ruby 应用，可能存在反序列化 |
| PHPInfo | 2 | creditcard.pingan.com.cn, recorder.health.pingan.com | PHPInfo 页面泄露，信息泄露 |
| OpenResty-Default | 2 | ehis-hsms-dmzweb.health.pingan.com, ehis-hsms-openresty-dmzweb-prd.health.pingan.com | OpenResty 默认页面，可能配置不当 |
| 用友NC | 2 | health.pingan.com.cn, health.pingan.com | 用友 NC ERP，可能存在已知漏洞 |
| Mongo-Express | 2 | m.pingan.com, wap.health.pingan.com | MongoDB Express，可能未授权 |
| Vue.js | 2 | m.pingan.com, wap.health.pingan.com | 前端框架，JS 文件可能泄露接口 |
| Node.js | 2 | m.pingan.com, wap.health.pingan.com | Node.js 应用，可能 SSRF/原型链污染 |
| RabbitMQ | 1 | ehis-wbzs-web.health.pingan.com | RabbitMQ 管理界面，可能未授权访问 |
| 禅道 | 1 | gallery.pingan.com | 禅道项目管理，可能存在已知漏洞 |
| NuxtJS | 1 | wap.health.pingan.com | Nuxt.js 框架，JS 文件可能泄露接口 |
| 七牛CDN | 1 | ehis.home.pingan.com.cn | 七牛云 CDN，Bucket 可能配置不当 |
| 企业微信 | 1 | ehis-wbzs-web.health.pingan.com | 企业微信集成，可能信息泄露 |
| fortinet-fortimail | 1 | invest.pingan.com | Fortinet 邮件安全，可能配置泄露 |

---

## 五、WAF 部署情况

- **部署 F5 Big-IP WAF**：75 个域名
- **未检测到 WAF**：132 个域名

### 无 WAF 域名列表（可能防护较弱）

- a.pingan.com
- ab.pingan.com.cn
- activity.health.pingan.com
- ant.pingan.com.cn
- asset.pingan.com
- b.pingan.com
- b1.pingan.com.cn
- bank.pingan.com
- bank.pingan.com.cn
- bbc.pingan.com.cn
- bip.pingan.com
- br.pingan.com
- c.pingan.com
- c.pingan.com.cn
- cash.pingan.com
- cash.pingan.com.cn
- cc.pingan.com
- ccp.pingan.com
- cdn-ehis-golden-key-stg.pingan.com.cn
- cdn-ehis-golden-key-stg5.pingan.com.cn
- cdn-ehis-golden-key.pingan.com.cn
- cdn-health.pingan.com
- cdn-suishenyi.health.pingan.com
- cf.pingan.com.cn
- cg.pingan.com.cn
- cgi.pingan.com
- creditcard.pingan.com.cn
- cz.pingan.com.cn
- download.pingan.com.cn
- drs.pingan.com
- dv.pingan.com.cn
- ebank.pingan.com.cn
- ehis-activity-stg1.health.pingan.com
- ehis-activity-stg5.health.pingan.com
- ehis-audit-ivs-dmz-stg1.pingan.com.cn
- ehis-audit-ivs-dmz-stg2.pingan.com.cn
- ehis-audit-ivs-dmz-stg5.pingan.com.cn
- ehis-br-consultant-h5-stg1.pingan.com.cn
- ehis-br-consultant-h5-stg5.pingan.com.cn
- ehis-eqz-dmzweb-prd.pingan.com.cn
- ehis-golden-key-stg.pingan.com.cn
- ehis-golden-key-stg5.pingan.com.cn
- ehis-hcs-stg1.pingan.com.cn
- ehis-hcs-stg2.pingan.com.cn
- ehis-hcs-stg3.pingan.com.cn
- ehis-hcs-stg5.pingan.com.cn
- ehis-hcs.pingan.com.cn
- ehis-hems-dmz-stg1.pingan.com.cn
- ehis-hems-dmz-stg5.pingan.com.cn
- ehis-hems.pingan.com.cn
- ehis-hisos.health.pingan.com
- ehis-iproductmarket-stg1.health.pingan.com
- ehis-iproductmarket-stg2.health.pingan.com
- ehis-iproductmarket-stg5.health.pingan.com
- ehis-ivs-dmzweb-stg1.pingan.com.cn
- ehis-ivs-dmzweb-stg2.pingan.com.cn
- ehis-ivs-dmzweb-stg5.pingan.com.cn
- ehis-mcore-stg1.health.pingan.com
- ehis-mcore-stg1.pingan.com.cn
- ehis-mcp-gateway-wgq-padis-dmzstg5.pingan.com.cn
- ehis-mcs.pingan.com
- ehis-mini-program-dmzweb-stg1.health.pingan.com
- ehis-mini-program-dmzweb-stg2.health.pingan.com
- ehis-service-dmzweb-prd.pingan.com.cn
- ehis-wbzs-minio.health.pingan.com
- ehis-yedi-ngweb-stg5.health.pingan.com
- ehis.health.pingan.com
- ehis.home.pingan.com.cn
- eid.pingan.com
- eps.pingan.com.cn
- ex.pingan.com
- fund.pingan.com.cn
- gj.pingan.com
- health.pingan.com
- healthtech.pingan.com.cn
- helper-market.health.pingan.com
- hermes.pingan.com.cn
- home.pingan.com
- home.pingan.com.cn
- ibank.pingan.com
- ibc.pingan.com.cn
- ice-health.pingan.com
- ice-stg1-health.pingan.com
- ice-stg2-health.pingan.com
- ice-stg5-health.pingan.com
- icp.pingan.com
- information.pingan.com
- leasing.pingan.com
- legacy.pingan.com.cn
- life.pingan.com
- link.pingan.com.cn
- loan.pingan.com
- mailout2.pingan.com.cn
- mall.pingan.com.cn
- mcp-health.pingan.com.cn
- mcp-test-health.pingan.com.cn
- mcp.pingan.com.cn
- message.pingan.com
- message.pingan.com.cn
- mi.pingan.com
- mp.pingan.com.cn
- mx4.pingan.com.cn
- mx5.pingan.com
- mx5.pingan.com.cn
- mx7.pingan.com.cn
- mx8.pingan.com
- oa.pingan.com.cn
- open.health.pingan.com
- openapi.pingan.com.cn
- osr.pingan.com
- pms.pingan.com
- post.pingan.com
- push.pingan.com.cn
- q.pingan.com
- qr.pingan.com
- realestate.pingan.com
- s.pingan.com
- secmail.pingan.com.cn
- smart.pingan.com.cn
- srm.pingan.com.cn
- sse.pingan.com.cn
- sso.pingan.com.cn
- star.pingan.com
- static2.pingan.com
- stock.pingan.com.cn
- t.pingan.com.cn
- te.pingan.com.cn
- trust.pingan.com
- w.pingan.com.cn
- webmail.pingan.com.cn
- wm.pingan.com
- wms.pingan.com.cn
