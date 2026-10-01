# Shigure II · 月下第一轮概念制作 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 制作一张可评审的月主题浮世绘候选图和桌面概念预览，为 Shigure II 的统一夜色与后续系列提供依据。

**Architecture:** 图像与来源记录保存在独立的 `docs/v2-concepts/` 中；桌面概念预览保存在当前任务的可视化目录。先检查月主题的木版语言、构图与窗口覆盖效果，再由用户评审决定是否扩展雨、雪、潮。

**Tech Stack:** 内置 ImageGen；PNG；Markdown；单文件 HTML/CSS/JavaScript；浏览器检查；工作区捆绑 Python 与 Pillow 用于完整解码和元数据读取。

**制作状态（2026-10-01）：** 第一张候选图、生成记录和交互预览已制作；完整解码、对比度、静态结构与 Node VM 状态检查已执行。浏览器显示检查因本地页面安全策略未执行；用户视觉评审与真实 Omarchy 验证尚未完成。详细证据见 `docs/v2-concepts/ARTWORK.md`。

## Global Constraints

- 设计依据：`docs/superpowers/specs/2026-10-01-shigure-v2-moon-design.md`。
- 本轮只制作“月”的主视觉、来源记录与桌面概念预览。
- 不改 `colors.toml`、`icons.theme`、`backgrounds/`、`preview.png` 或现有 README，不安装或发布主题。
- 统一色彩：墨蓝 `#101F2B`、次表面 `#1B3040`、暖纸 `#E3DDCF`、月白 `#F0E7D5`、雾蓝 `#84A7BD`、旧金 `#CBB98B`，少量保留朱色 `#D58B72`。
- 月轮位于右上区域，低岛与远岸位于下三分之一，右下角少量芦苇，中央约一半面积保持低细节。
- 木版墨线、平涂色块；bokashi 晕染仅用于天空和水面；纸纹很淡，不做旧。
- 不出现船、文字、题签、印章、签名或标志；避免摄影式光效、写实月光反射与立体渲染。
- 图像通过内置 ImageGen 新生成；参考历史作品的构图与色彩关系，不复制完整画面。
- 目标画幅为 16:9；尺寸按实际文件记录，不宣称原生 4K 细节。
- 预览明确标注“概念模拟”；macOS 工作环境不能证明真实 Omarchy 运行。
- 本计划的检查为图像与概念预览验收，不新增代码测试框架、提交或发布流程。

---

## 文件边界

| 路径 | 责任 |
|---|---|
| `docs/v2-concepts/01-moon.png` | 第一张月主题候选图 |
| `docs/v2-concepts/ARTWORK.md` | 生成提示词、来源、实际图像元数据、处理与检查结果 |
| `/Users/yonglun/.codex/visualizations/2026/10/01/01a0f777-910d-7351-8bf8-fae86b21200b/shigure-moon-preview.html` | 以候选图为背景的交互桌面模拟 |

上述文件是本轮交付边界。既有设计与制作记录只作为阅读背景，不覆盖第一版的来源记录。

### Task 1: 生成并检查月主题候选图

**Files:**
- Create: `docs/v2-concepts/01-moon.png`

**Interfaces:**
- Consumes: 设计说明中的构图、绘画语言与统一色彩；[广重馆藏参考](https://www.clevelandart.org/art/1924.967)。
- Produces: 可完整解码的月主题 PNG，供来源记录和桌面预览使用。

- [x] **Step 1: 使用内置 ImageGen 生成一张新构图**

以下提示词作为本轮的制作依据；将实际提交给工具的完整提示词写入来源记录。

```text
Create one original 16:9 landscape desktop wallpaper for Shigure II · Moonlit. This is a newly composed contemporary interpretation of Utagawa Hiroshige's Japanese ukiyo-e woodblock language. Use Eight Views of Kanazawa at Night as a reference for the relationship of a moon, low distant shore and quiet night color, without reproducing the historical composition.

The image must visibly read as a multicolor woodblock print: crisp fine sumi keyblock contours enclosing broad flat pigment shapes, simplified pictorial perspective, restrained carved line patterns, and delicate bokashi gradients ONLY in the sky and water. Extremely faint fresh washi texture, not a distressed antique scan. Limited night palette based on ink indigo #101F2B, secondary blue #1B3040, warm paper #E3DDCF, moon ivory #F0E7D5, mist blue #84A7BD and restrained old gold #CBB98B.

Place one clear pale moon in the upper-right region. Keep low island and distant shoreline silhouettes within the lower third. Add only a small cropped cluster of reeds in the lower-right corner, with fine carved dark outlines. Keep approximately the central half of the frame low in detail, with broad quiet night sky and water, suitable for terminal and editor windows. Establish distance with overlapping flat silhouettes and restrained color steps. Use sparse woodblock water lines, with no realistic moonlight reflection path.

Full-bleed single scene, no border, no boat, no lettering, no calligraphy, no cartouche, no seal, no signature and no logo. No photographic lighting, lens flare, cinematic glow, volumetric shading, 3D rendering, airbrushed forms or realistic textures. Modernity comes from the asymmetric widescreen crop and generous negative space. The moon and water are printed color planes, not a photographic night landscape.
```

- [x] **Step 2: 在原图上逐项视觉检查**

打开生成结果，检查右上月轮、低岸、少量右下芦苇与中央低细节区域；检查墨线和平涂可见，晕染只在天空水面，纸纹克制，无禁止元素。若任一主约束明显失败，保留准确的反馈并重新生成或通过内置 ImageGen 修改，再检查。

- [x] **Step 3: 保存候选图**

将选定的生成输出保存到 `docs/v2-concepts/01-moon.png`，保留该输出的真实尺寸。若处理文件格式或尺寸，逐项记录操作，不用请求尺寸代替输出尺寸。

### Task 2: 完整解码与来源记录

**Files:**
- Create: `docs/v2-concepts/ARTWORK.md`
- Inspect: `docs/v2-concepts/01-moon.png`

**Interfaces:**
- Consumes: 选定 PNG、ImageGen 调用中实际使用的提示词与输出信息。
- Produces: 可核对的来源与元数据记录；本轮图像检查结果。

- [x] **Step 1: 完整解码并输出实际元数据**

从仓库根目录运行：

```bash
/Users/yonglun/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
from PIL import Image

path = Path('docs/v2-concepts/01-moon.png')
with Image.open(path) as image:
    image.load()
    print(f'file={path}')
    print(f'format={image.format}')
    print(f'width={image.width}')
    print(f'height={image.height}')
    print(f'mode={image.mode}')
    print(f'icc_profile_present={bool(image.info.get("icc_profile"))}')
    print(f'aspect_ratio={image.width / image.height:.6f}')
print(f'sha256={sha256(path.read_bytes()).hexdigest()}')
PY
```

预期：进程成功退出，格式为 PNG，宽高为实际正整数，输出可复核的 SHA-256。`image.load()` 必须成功；存在 ICC 配置只作为元数据记录，不能单凭这一项宣称色彩管理准确。

- [x] **Step 2: 写入来源与处理说明**

记录项目名、候选编号、内置 ImageGen、实际生成日期、完整实际提示词、馆藏参考链接、上一项输出的宽高／格式／色彩模式／ICC 情况／SHA-256，以及实际处理操作。说明新图是当代生成诠释；原图未经重采样时直接说明，经过处理时写出操作与前后尺寸。另列视觉检查的已检查项及发现，不写未执行的通过结论。

### Task 3: 构建桌面概念预览

**Files:**
- Create: `/Users/yonglun/.codex/visualizations/2026/10/01/01a0f777-910d-7351-8bf8-fae86b21200b/shigure-moon-preview.html`
- Consume: `docs/v2-concepts/01-moon.png`

**Interfaces:**
- Consumes: 当前月主题 PNG 和设计说明中的候选色值。
- Produces: 单文件可交互概念预览，支持月金／朱色比较及隐藏／恢复窗口。

- [x] **Step 1: 制作统一的工作场景**

以当前 PNG 为背景，放置并排终端与编辑器；窗口表面使用墨蓝与次表面，正文使用暖纸，高亮使用月白，冷色边界使用雾蓝。两种强调色状态必须保持同一布局、文本和背景，只有用于比较的交互强调色变化。将图片嵌入单文件或使用可验证的资源引用，保证打开预览时当前候选图正常出现。

- [x] **Step 2: 添加评审交互与说明**

提供标明“月金”和“朱色”的选择控件；提供可隐藏并恢复全部窗口的控件。页面可见位置写明“概念模拟”，说明该画面不是真实 Omarchy 截图。将纯壁纸与被窗口覆盖后的画面纳入同一评审流程。

- [ ] **Step 3: 检查浏览器交互**

在浏览器打开该文件，切换两种强调色，隐藏并恢复窗口；检查控件状态与画面一致。检查宽幅桌面尺寸下窗口、月轮和控制区域的关系，以及浏览器控制台错误。记录实际检查的浏览器、视口和结果；若存在布局或交互故障，修复后重查对应操作。

### Task 4: 对比度检查与概念评审交付

**Files:**
- Modify: `docs/v2-concepts/ARTWORK.md`
- Inspect: `/Users/yonglun/.codex/visualizations/2026/10/01/01a0f777-910d-7351-8bf8-fae86b21200b/shigure-moon-preview.html`

**Interfaces:**
- Consumes: 候选色值、图像检查结果和预览交互结果。
- Produces: 有明确证据范围的第一轮交付，供用户评审构图与暖色强调。

- [x] **Step 1: 测量指定不透明颜色对**

从仓库根目录运行：

```bash
/Users/yonglun/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 - <<'PY'
def luminance(value):
    values = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in values]
    return sum(v * w for v, w in zip(linear, (0.2126, 0.7152, 0.0722)))

def contrast(first, second):
    high, low = sorted((luminance(first), luminance(second)), reverse=True)
    return (high + 0.05) / (low + 0.05)

surfaces = {'墨蓝': '#101F2B', '次表面': '#1B3040'}
foregrounds = {'暖纸': '#E3DDCF', '月白': '#F0E7D5', '雾蓝': '#84A7BD', '旧金': '#CBB98B', '朱色': '#D58B72'}
for surface_name, surface in surfaces.items():
    for foreground_name, foreground in foregrounds.items():
        print(f'{foreground_name} {foreground} / {surface_name} {surface}: {contrast(foreground, surface):.2f}:1')
for accent_name in ('旧金', '朱色'):
    accent = foregrounds[accent_name]
    print(f'墨蓝文字 #101F2B / {accent_name}底 {accent}: {contrast("#101F2B", accent):.2f}:1')
PY
```

预期：列出十个前景／表面颜色对，以及两种强调色底上的墨蓝文字颜色对。按实际角色评估：正文至少 4.5:1；必要控件轮廓和大字信息至少 3:1。只说明这些指定不透明颜色对的测量结果，不外推到透明窗口、壁纸底色或真实应用。

- [x] **Step 2: 补全交付记录**

将对比度结果、图像完整解码结果、视觉检查发现、预览交互结果和环境限制记入来源记录；只把已实际执行的检查写成完成。确认生成图尺寸与文档一致，概念预览说明可见，现有发布主题文件没有被本轮替换。

- [x] **Step 3: 向用户交付第一轮评审材料**

展示当前候选图并打开概念预览，附上设计说明与来源记录链接。请用户围绕月轮与留白、浮世绘语言、月金／朱色强调提出反馈；收到评审后，先调整月主题，再进入雨、雪、潮的制作。

## 本轮之后

2026-10-01 用户已明确选择月金。系列扩展中的月、雨、雪、潮候选及月金语义配色保存于 `docs/v2-concepts/`，准确进度和检查范围见该目录的 `ARTWORK.md`；浏览器显示与实际 Omarchy 验证仍未完成。

同日系列反馈修订：月与潮远景相似，雨与雪右下人物相似。保留月、雨；通过内置 ImageGen 将雪改为无人屋舍雪路，将潮重构为俯视礁石潮汐。当前所选为 `03-snow-refined.png`、`04-tide-refined.png`，完整提示词及初稿对照留在制作记录中；同一四图预览同步更新。

本计划结束于第一轮概念材料可供评审，不自动触发另外三张生成或主题发布。后续依次为：月主题收敛；雨、雪、潮独立构图；四图与语义配色整合；实际 Omarchy 版本兼容性和真实环境验证；发布候选。每个阶段以上一阶段的用户评审结果为依据。
