# 项目记忆 - 网络安全测试

> 以下内容适用于本项目所有会话，AI 助手需在每次对话中遵循。

---

## 一、回复风格

- **详细全面**：每个回答给出完整分析，包含背景、原理、步骤和预期结果
- 技术问题优先从底层原理出发解释
- 对不确定的内容明确标注，不编造
- 代码/命令需附带注释说明

---

## 二、项目背景

- 项目名称：20260625网络安全
- 项目性质：网络安全测试与研究
- 主要方向：Web 安全、渗透测试、漏洞分析

---

## 三、可用工具与 MCP 配置

### 3.1 Burp Suite (MCP)
本环境已连接 Burp Suite MCP 服务器，可用工具包括：

| 工具 | 用途 |
|------|------|
| `send_http1_request` / `send_http2_request` | 发送原始 HTTP/1.1 或 HTTP/2 请求 |
| `create_repeater_tab` / `create_repeater_tab_http2` | 创建 Repeater 标签页 |
| `send_to_intruder` | 发送到 Intruder 进行自动化攻击 |
| `url_encode` / `url_decode` | URL 编码/解码 |
| `base64_encode` / `base64_decode` | Base64 编码/解码 |
| `generate_random_string` | 生成随机字符串 |
| `output_project_options` / `output_user_options` | 查看项目/用户配置 |
| `set_project_options` / `set_user_options` | 设置项目/用户配置 |
| `get_scanner_issues` | 获取扫描器发现的漏洞 |
| `generate_collaborator_payload` | 生成 Collaborator 载荷 |
| `get_collaborator_interactions` | 获取 Collaborator 交互记录 |
| `get_proxy_http_history` / `get_proxy_http_history_regex` | 获取代理 HTTP 历史 |
| `get_organizer_items` / `get_organizer_items_regex` | 获取 Organizer 项目 |
| `get_proxy_websocket_history` / `get_proxy_websocket_history_regex` | 获取 WebSocket 历史 |
| `set_task_execution_engine_state` | 控制任务执行引擎 |
| `set_proxy_intercept_state` | 控制代理拦截状态 |
| `get_active_editor_contents` / `set_active_editor_contents` | 读写当前编辑器内容 |

**使用原则**：
- 所有 Burp MCP 工具通过 `run_mcp` 调用，参数放在 `args` 字段中
- 调用前先通过 LS + Read 查看工具描述文件确认参数格式
- 工具描述文件路径：`c:\Users\22381\.trae-cn\mcps\s_20260625网络安全-e8cfa3a3\solo_work_lite\mcp_burp\`

### 3.2 其他可用能力
- **WebSearch / WebFetch**：搜索安全漏洞资料、CVE、安全公告等
- **文件操作**：项目工作区为 `c:\Users\22381\Desktop\20260625网络安全`
- **定时任务 (Schedule)**：可创建周期性安全扫描/报告任务

### 3.3 TscanPlus (MCP)

> 详细行为指令见 `.trae/skills/tscanplus/SKILL.md`，调用示例见 `examples.md`

本环境已安装 TscanPlus MCP 服务（stdio 模式），路径：`D:\software\TscanPlus_Win_Amd64\TscanPlus_Win_Amd64.exe`

**八大模块与 MCP 工具对照：**

| 模块 | MCP 工具 | 说明 |
|------|---------|------|
| 端口扫描 | `ip_scan` | IP/CIDR、存活探测、服务指纹、可选联动 POC/爆破 |
| Web 指纹 | `url_scan` | URL 指纹识别、Title |
| POC 验证 | `poc_scan` | xray 1.0 格式 POC，按指纹或全量 |
| 弱口令 | `pwd_crack` | 多协议爆破，targets 为 `host:port` |
| 目录枚举 | `dir_scan` | 路径爆破 |
| JS 信息 | `js_scan` | JS 文件中密钥、接口等 |
| 子域名 | `subdomain_scan` | 字典 + API |
| 空间测绘 | `cyber_search` | Hunter/FOFA 等 |
| 综合联动 | `tscan_scan` | 多模块联动：cyber→domain→port→crack→url→poc→dir→js |

**使用原则：**
- ⚠️ 扫描前**必须**确认授权，未授权目标直接拒绝
- 默认不开 POC/爆破（`poc_check: false`、`pwd_check: false`）
- 扫描后按 SKILL.md 规范汇报（摘要 + 表格 + 高危标注）
- 默认 project 为 `MCP`，每次调用前自动清空

---

## 四、安全测试规范

### 4.1 测试方法论
- 遵循 OWASP 测试指南框架
- 测试步骤应包含：信息收集 → 漏洞探测 → 验证利用 → 报告输出
- 使用 Burp Suite 作为主要测试代理

### 4.2 报告格式
安全测试报告应包含：
1. **漏洞概述**：名称、影响、风险等级（高/中/低）
2. **受影响 URL/端点**
3. **复现步骤**
4. **请求/响应证据**
5. **修复建议**

### 4.3 风险等级定义
| 等级 | 说明 |
|------|------|
| 🔴 高 | 可直接获取敏感数据或系统控制权 |
| 🟡 中 | 可能导致信息泄露或需组合利用 |
| 🟢 低 | 信息泄露风险低或利用条件苛刻 |

### 4.4 注意事项
- 仅对授权目标进行测试
- 测试过程中记录关键请求和响应
- 发现漏洞后及时输出结构化报告
- 敏感信息（如密码、Token）在报告中脱敏处理

---

## 五、文件组织约定

```
20260625网络安全/
├── .trae/
│   ├── rules/
│   │   └── rules.md           # 项目规则文件（自动加载）
│   └── skills/               # 自定义 Skill
│       ├── auto-clean.md     # SKILL 1：智能冗余自动清理
│       ├── memory-consolidation.md  # SKILL 2：记忆自动规整沉淀
│       ├── self-evolution.md # SKILL 3：智能复盘自我进化
│       ├── progress-tracker.md # SKILL 4：子项目进度追踪
│       └── tscanplus/         # TscanPlus 官方扫描 Skill
│           ├── SKILL.md       # 行为指令+参数表+汇报格式
│           ├── examples.md    # 各模块 MCP 调用示例
│           ├── README.md      # 宿主适配指引
│           └── mcp-config-example.json
├── agent_memory/             # 记忆持久化存储 + 自进化
│   ├── memory_list.md        # 结构化记忆库
│   ├── rule_update.log       # 进化迭代日志
│   └── clean_log_*.txt       # 清理日志
├── reports/                   # 安全测试报告
├── payloads/                  # 攻击载荷/字典
├── evidence/                  # 截图/请求证据
├── scripts/                   # 用户自行存放测试脚本
└── projects/                  # 临时子项目（到期后删除）
    └── 0630_健康险渗透/       # 截止 2026-06-30
        ├── memory/
        │   └── progress.md    # 项目进度（关键词：健康险渗透更新进度）
        ├── results/            # 产出结果
        └── evidence/           # 截图/证据
```

---

## 六、每次会话启动检查清单

AI 助手应在每次对话开始时：
1. ✅ 本规则文件（自动加载）—— 项目宪章，静态
2. ✅ 读取 `agent_memory/memory_list.md` —— 对话记忆库，动态沉淀
3. ✅ 确认 Burp MCP 工具可用
4. ✅ 根据用户意图选择合适的工具组合
5. ✅ 遵循详细全面的回复风格

---

## 六点五、两类"记忆"的区别

| | rules.md | agent_memory/memory_list.md |
|---|---|---|
| **性质** | 项目宪章（静态） | 对话记忆（动态） |
| **内容** | 回复风格、工具清单、测试方法论、风险等级定义 | 历史任务经验、踩坑记录、用户偏好新发现 |
| **谁来写** | 用户手动指定，AI 辅助编辑 | SKILL 2 从对话中自动沉淀 |
| **更新频率** | 低频，手动 | 高频，每个任务结束后自动 |

---

## 七、自进化记忆系统

本项目部署了三层自进化 SKILL 系统：

| Skill | 功能 | 触发时机 |
|-------|------|---------|
| `auto-clean` | 智能冗余自动清理 | 用户说"更新记忆" / 任务结束 / 对话超 10 轮 |
| `memory-consolidation` | 记忆自动规整沉淀 | 用户说"更新记忆" / 任务结束后 |
| `self-evolution` | 智能复盘自我进化 | 用户说"更新记忆" / 结果偏差 / 用户修正 |

三者执行顺序：清理 → 沉淀 → 复盘。用户说"更新记忆"时，先沉淀本轮对话经验，再复盘是否存在可优化的问题。

---

## 八、子项目进度追踪

| Skill | 功能 | 触发关键词 | 写入位置 |
|-------|------|-----------|---------|
| `progress-tracker` | 更新健康险渗透进度 | `健康险渗透更新进度` | `projects/0630_健康险渗透/memory/progress.md` |

**与主记忆的区别**：进度只记录当前阶段、完成事项、待办事项，不做经验沉淀。经验沉淀走"更新记忆"写入 `agent_memory/memory_list.md`。
