# Shigure II 月金主题整合 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** 将用户确认的四图与月金配色整合为可安装、可审查的第二版主题候选。

**Architecture:** 根目录继续使用 Omarchy 声明式主题格式，概念目录保留完整创作来源。生产活动图片仅四张，作者校验器匹配实际候选资源；文档及兼容性记录分别更新。

**Tech Stack:** PNG/JPEG/SVG、TOML、Python 3.11 标准库校验器、bundled Pillow 解码、macOS sips 展示副本、官方 v4.0.0 Bash 模板。

## Global Constraints

- 已确认设计：`docs/superpowers/specs/2026-10-01-shigure-v2-integration-design.md`。
- 配色仅更改 accent、bright_foreground、hyprland_active_border 三项值，使用已确认候选。
- 活动壁纸恰好月、雨、无人雪、俯视潮；原样复制 1672 × 941 PNG。
- 不添加主题钩子、应用配置覆盖或依赖；不推送或发布，不进行实际桌面安装。
- 所有检查须有实际输出；真实 Linux 会话不可用时准确记录限制。

---

### Task 1: 生产资源与作者校验器

**Files:** 根 `colors.toml`、`backgrounds/`、`preview.png`、`docs/images/`、`scripts/validate-theme.py`。

**Interfaces:** 消费概念目录最终四图与 colors.toml；产出活动图像、展示副本和能够验证新版本资源的 CLI。

- [x] 原样复制以下映射并移除活动目录中的第一版四图，第一版由 Git 原提交保留。

```text
docs/v2-concepts/01-moon.png -> backgrounds/01-moon.png
docs/v2-concepts/02-rain-refined.png -> backgrounds/02-rain.png
docs/v2-concepts/03-snow-refined.png -> backgrounds/03-snow.png
docs/v2-concepts/04-tide-refined.png -> backgrounds/04-tide.png
docs/v2-concepts/colors.toml -> colors.toml
```

- [x] 用 `sips --resampleHeightWidth 900 1600 backgrounds/01-moon.png --out preview.png` 制作预览；用 `sips -Z 1024 -s format jpeg -s formatOptions 75` 制作四张对应图库图。更新可编辑 `palette.svg`，体现月白和旧金。
- [x] 校验器的活动文件改为 `['01-moon.png', '02-rain.png', '03-snow.png', '04-tide.png']`，尺寸检查改为 `(1672, 941)`，输出明确真实尺寸；Hyprland 渲染校验从 `colors['hyprland_active_border']` 提取两个 RGBA token，检查都出现在输出且角度45。保留现有其余校验。
- [x] 执行 bundled Python `scripts/validate-theme.py`，再用 Pillow 完整解码四图、预览及图库，核对所选概念图 SHA-256 一致。

### Task 2: 三语说明与来源记录

**Files:** `README.md`、`README.zh-CN.md`、`README.ja.md`、`docs/DESIGN.md`、`docs/ARTWORK.md`。

**Interfaces:** 消费 Task 1 的文件命名及配色，产出一致的默认月、四图描述、安装方式与来源说明。

- [x] 标题改为 Shigure II · 月下，明确月／雨／雪／潮、月金交互、月白光标与旧金雾蓝焦点渐变。
- [x] README 使用新的图库和原图链接；写明 1672 × 941 原始生成尺寸、RGB 无 ICC，不宣称4K；顶图是壁纸展示副本。
- [x] 本地安装使用 `~/.config/omarchy/themes/shigure-ii` 新目录。远程 URL 安装只在候选发布后使用，并说明其名称仍为 shigure。
- [x] 来源记录链接完整创作提示词和修订过程，描述雪为空景、潮为俯视近景；三语传达一致事实。
- [x] 用现有 CLI 检查本地 Markdown 链接，并独立复核文档内容与文件一致。

### Task 3: 兼容性、打包与复核

**Files:** `docs/COMPATIBILITY.md`、`docs/VALIDATION.json`、`dist/shigure-ii-moon-gold.zip`。

**Interfaces:** 消费候选主题和既有官方 v4.0.0 校验机制，产出有证据的本地安装包与验证结果。

- [x] 获取或定位官方 v4.0.0 源码，先核对 `docs/upstream-v4.0.0.sha256`，存在支持 Bash 时运行 `scripts/validate-theme.py --upstream ... --bash /opt/homebrew/bin/bash`。隔离临时 HOME，绝不选中当前桌面主题。
- [x] 更新兼容性记录日期、壁纸/预览/配色数据及实际覆盖；记录真实 Omarchy 会话未测试。
- [x] 标准库 zipfile 制作含 `shigure-ii/colors.toml`、`icons.theme`、`preview.png`、四图及 LICENSE 的安装包；解压到临时目录后再次核对文件集合、尺寸、SHA-256和TOML。
- [x] 运行完整 CLI 与 `git diff --check`；独立评审实现、规格覆盖和文档。修复发现后重新执行受影响检查。
- [x] 将准确结果写入 JSON，更新计划勾选，向用户交付主题候选、安装包与剩余实机验证范围。
