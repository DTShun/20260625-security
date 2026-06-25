# Agent 专属记忆库（自进化迭代）

> 本文件由 SKILL 2（记忆自动规整沉淀）自动维护
> 记录用户偏好、任务经验、避坑清单等持久化记忆

---

## [偏好] 2026-06-25 00:30:00
- 内容：用户偏好详细全面的回复风格，技术问题优先从底层原理出发解释
- 关联：项目初始化
- 标签：#回复风格 #偏好设置

---

## [偏好] 2026-06-25 00:30:00
- 内容：用户注重文件组织清晰性，脚本和数据放在一起更直观；目录命名偏好直观易懂（如 rules 而非 memory）
- 关联：项目初始化
- 标签：#文件组织 #目录命名

---

## [方案] 2026-06-25 00:30:00
- 内容：长期记忆通过 .trae/rules/rules.md（静态规则，TRAE 自动加载）+ agent_memory/memory_list.md（动态记忆，SKILL 自动沉淀）双层实现。部署了三层自进化 SKILL：auto-clean（冗余清理）→ memory-consolidation（记忆沉淀）→ self-evolution（复盘进化）
- 关联：项目初始化
- 标签：#长期记忆 #自进化 #SKILL #rules.md #双层记忆

---

## [避坑] 2026-06-25 00:30:00
- 内容：TRAE rules 目录和 agent_memory 目录易混淆，明确区分：rules.md 是项目宪章（静态），memory_list.md 是对话记忆（动态）。早期用了 memory 目录名后来改回 rules 更准确
- 关联：项目初始化
- 标签：#目录命名 #避坑

---

## [方案] 2026-06-25 01:30:00
- 内容：记忆操作不再使用 Python 脚本，AI 直接用 Read + SearchReplace 读写文件，更快更灵活零维护。三个脚本（memory_clean/store/evolve/init）全部删除
- 关联：项目初始化
- 标签：#文件组织 #去脚本化

---

## [方案] 2026-06-25 01:00:00
- 内容："更新记忆"为统一触发口令，一条指令串联三 SKILL 完整闭环：SKILL 1（清理冗余）→ SKILL 2（沉淀经验）→ SKILL 3（复盘进化）。三个 SKILL 文件中均写入该触发词
- 关联：自进化系统最终定型
- 标签：#更新记忆 #SKILL闭环 #触发词

---

## [避坑] 2026-06-25 01:00:00
- 内容：修改 SKILL 触发词时，必须检查整条链上的所有 SKILL，不能只改被明确提及的那一两个。本次先漏掉了 SKILL 1，后被用户指出才补上，根本原因是"局部执行、缺全局视角"
- 关联：SKILL 闭环完整性
- 标签：#避坑 #全局视角 #SKILL修改

---

## [方案] 2026-06-25 01:30:00
- 内容：TscanPlus 官方 Skill 包已安装至 .trae/skills/tscanplus/，含 SKILL.md（行为指令+参数表）、examples.md（MCP调用示例）、README.md（宿主指引）、mcp-config-example.json。rules.md 注册为 3.3 节。
- 关联：TscanPlus MCP 集成
- 标签：#TscanPlus #Skill安装 #MCP

---

## [方案] 2026-06-25 01:30:00
- 内容：TscanPlus MCP 使用 stdio 模式连接，EXE 路径 D:\software\TscanPlus_Win_Amd64\TscanPlus_Win_Amd64.exe，args 为 ["mcp", "stdio"]。仅保留一种连接方式（stdio），去掉 http 和 sse-legacy
- 关联：TscanPlus MCP 配置
- 标签：#TscanPlus #MCP配置 #stdio

---

## [避坑] 2026-06-25 01:30:00
- 内容：TRAE 的 MCP 配置界面一次只能配置一个 Server，不要一次贴多个。三种连接方式（stdio/http/sse）选其一即可，推荐 stdio 最稳定
- 关联：MCP 配置
- 标签：#TRAE #MCP配置 #避坑

---

## [偏好] 2026-06-25 01:30:00
- 内容：用户对官方提供的 Skill 包（如 TscanPlus Skill）倾向于直接安装到 .trae/skills/ 下，同时在 rules.md 注册，使 AI 能自动获取行为指令和参数规范
- 关联：Skill 管理
- 标签：#偏好 #Skill管理

---

## [方案] 2026-06-25 01:30:00
- 内容：建立子项目进度追踪体系：projects/0630_健康险渗透/ 含 memory（progress.md）、results、evidence。新增 SKILL 4（progress-tracker.md）用独立口令"健康险渗透更新进度"仅追踪进度，不做经验沉淀。进度和经验完全分离
- 关联：子项目管理
- 标签：#子项目 #进度追踪 #SKILL4

---

## [避坑] 2026-06-25 01:30:00
- 内容：之前两次错误表述"方案A混在一起"和"方案B需单独配MCP"，均被用户指出不准确。MCP 是全局层配置不绑定项目，子项目记忆物理隔离。AI 回答需更严谨
- 关联：子项目管理
- 标签：#避坑 #表述准确性

---

## [偏好] 2026-06-25 01:30:00
- 内容：用户担心口令过多记不住，要求在项目根目录放置 口令速查表.md 汇总所有触发词。后续新增口令需同步更新该文件
- 关联：口令管理
- 标签：#偏好 #口令管理 #速查表

---

## [方案] 2026-06-25 10:00:00
- 内容：TscanPlus 支持 CLI 模式直接执行，不依赖 MCP 连接。命令格式：`TscanPlus -m <模块> -h/-u/-d/-ck <目标> [参数]`。结果写入 TscanPlus-Result.txt 和 config.db（与 GUI 共用）。MCP 不可用时 CLI 是首选替代方案。八大模块 CLI 参数：port(-h/-p)、url(-u/-finger)、poc(-u/-pocname)、crack(-h/-s)、dir(-u/-dd)、js(-u)、domain(-d/-api)、cyber(-ck)
- 关联：TscanPlus MCP 集成
- 标签：#TscanPlus #CLI #命令行 #MCP替代

---

## [避坑] 2026-06-25 10:00:00
- 内容：TscanPlus CLI 直接运行 `-h`、`help`、无参数均无帮助输出，不会打印 usage 信息。获取 CLI 用法的唯一可靠途径是参考 SKILL.md 第 357-373 行的 CLI 示例，或查阅官方文档
- 关联：TscanPlus CLI 使用
- 标签：#TscanPlus #CLI #避坑 #帮助信息

---

## [方案] 2026-06-25 14:00:00
- 内容：TscanPlus CLI 多模块联动流程：domain（子域名枚举）→ url（Web 指纹）→ 后续可接 port/poc/dir/js。使用 `-pr 项目名` 统一归档到 config.db，CLI 和 GUI 数据互通。生成 URL 列表文件后通过 `-uf` 批量传入
- 关联：健康险渗透资产收集
- 标签：#TscanPlus #CLI #多模块联动 #资产收集

---

## [避坑] 2026-06-25 14:00:00
- 内容：config.db 实际 schema 与 SKILL.md 文档描述不完全一致。例如 urlscan 表的 Status 字段存的是 URL 而非状态码，Title 字段才是状态码。查询前必须通过 sqlite3 `PRAGMA table_info(表名)` 实际确认列结构，不能仅凭文档推断
- 关联：TscanPlus 数据库查询
- 标签：#TscanPlus #避坑 #config.db #schema差异

---

## [方案] 2026-06-25 14:00:00
- 内容：资产清单整合流程：从 config.db 提取 TscanPlus 扫描结果 → Python 脚本去重合并（crt.sh 结果 + TscanPlus 结果）→ 按健康险关联度分类（health/ehis 关键词匹配）→ 写入 assets.md。集团其他资产（银行/证券/基金）单独标注
- 关联：健康险渗透资产整合
- 标签：#资产整合 #去重 #分类 #Python脚本

---

## [偏好] 2026-06-25 14:00:00
- 内容：用户倾向 TscanPlus CLI 模式直接执行，不关心 MCP 是否已连接，优先出结果。对大量资产扫描接受后台运行 + 定期 poll 检查的方式
- 关联：工具使用偏好
- 标签：#偏好 #CLI优先 #效率优先

---

## [方案] 2026-06-25 16:00:00
- 内容：项目已托管至 GitHub 仓库 https://github.com/DTShun/20260625-security（public），21 个文件、3282 行。使用 gh CLI 认证（账号 DTShun，token scope: gist/repo/workflow），git 全局配置 user.name=DTShun、email=145439031+DTShun@users.noreply.github.com。已打 v1.0 标签
- 关联：项目版本管理
- 标签：#Git #GitHub #版本控制 #gh_CLI

---

## [方案] 2026-06-25 16:00:00
- 内容：Git 工作流：git status → git add -A → git commit -m "xxx" → git push。回退三层次：未 commit 用 git checkout -- 文件；已 commit 未 push 用 git reset --soft/hard HEAD~1；已 push 用 git reset --hard + git push --force。tag 是不可移动的路标：git tag -a v1.0 -m "xxx" → git push --tags
- 关联：项目版本管理
- 标签：#Git #工作流 #回退 #tag

---

## [偏好] 2026-06-25 16:00:00
- 内容：用户对 Git 学习偏好"理解概念模型再记命令"（如 tag 不可移动 vs branch 跟随 commit），不满足于只给命令。对新工具（Git/渗透测试 skill）先理解原理再看操作
- 关联：用户学习偏好
- 标签：#偏好 #学习方式 #概念优先

---

## [偏好] 2026-06-25 16:00:00
- 内容：用户重视项目版本管理，在安装新渗透测试 Skill 前坚持先上传 Git 并打 tag，形成可回退的版本节点后再继续
- 关联：项目版本管理
- 标签：#偏好 #版本管理 #先提交再变更
