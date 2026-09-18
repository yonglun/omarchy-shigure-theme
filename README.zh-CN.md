# Shigure / 時雨

**四种安静的风景，一张藍色的桌面。**

[English](README.md) · [日本語](README.ja.md) · 简体中文

![Shigure — 斜雨中的木桥](preview.png)

为 **Omarchy 4.0** 设计的深色主题：墨藍底色、暖纸文字、雾蓝窗口边框，以及恰到好处的朱色。
**雨、雪、山、水**，四幅内容独立的壁纸，共同构成一处适合专注工作的空间。

## 在风景中工作

Shigure 的设计灵感来自**歌川广重的浮世绘**。细密的墨线轮廓、平涂套色、
渐层晕染与纸白雪景，保留日本木版画的鲜明特征；不对称的宽幅构图和充分的留白，
则让这种绘画语言融入现代桌面。

我们借鉴的是构图语言：斜落的雨线、被画面边缘裁切的近景、层层退远的山色，
以及墨色与纸面留白之间的关系。广重的
[《大桥安宅骤雨》](https://www.metmuseum.org/art/collection/search/55433)
可以帮助理解这一来源。这里的壁纸是重新生成的当代诠释，并非历史作品的扫描、复制，也不是广重原作。

朱色像一个小小的标点。藍色组织画面，暖纸色承载文字，让桌面在长时间工作中保持温和。

## 安装

在 **Omarchy 4.0.x** 上，待本仓库发布后运行：

```bash
omarchy theme install https://github.com/yonglun/omarchy-shigure-theme
```

安装器会自动识别名称 `shigure` 并应用主题。再次选择主题，或切换下一张壁纸：

```bash
omarchy theme set shigure
omarchy theme bg next
```

**发布前使用本地文件夹：** 在下载或解压后的主题目录中执行以下命令。
如果已有 `shigure`，请先备份；命令会替换同名文件。

```bash
mkdir -p ~/.config/omarchy/themes/shigure/backgrounds
cp colors.toml icons.theme preview.png ~/.config/omarchy/themes/shigure/
cp backgrounds/*.png ~/.config/omarchy/themes/shigure/backgrounds/
omarchy theme set shigure
```

首次应用时，按文件名排序从 **Rain／雨** 开始。之后的选择行为由 Omarchy 版本决定。
页首展示的是壁纸预览，并非真实桌面截图。

## 四幅风景

| Rain · 雨 | Snow · 雪 |
|:---:|:---:|
| [![雨](docs/images/01-rain.jpg)](backgrounds/01-rain.png) | [![雪](docs/images/02-snow.jpg)](backgrounds/02-snow.png) |
| 斜贯画面的木桥、撑伞行人，与细密的雨线。 | 覆雪的宿场屋舍、梅枝，与沿白色小径前行的旅人。 |

| Mountain · 山 | Water · 水 |
|:---:|:---:|
| [![山](docs/images/03-mountain.jpg)](backgrounds/03-mountain.png) | [![水](docs/images/04-water.jpg)](backgrounds/04-water.png) |
| 以近景苍松取框，远眺藍色山麓与富士。 | 鸢尾、两尾游鲤，以及舒展的水纹和大面积藍色水面。 |

点击图片可查看完整壁纸。四张均为无文字的 **4096 × 2304 PNG，16:9，sRGB**。
每幅拥有独立题材与构图，不再出现重复的舟；共用一套配色，切换壁纸后仍保持完整的桌面风格。

生成源图尺寸为 **1672 × 941**，交付文件经过重采样放大。
它们具有 4K 级尺寸，但不应被称为包含原生 4K 生成细节的图像。

## 配色

![Shigure 配色](docs/images/palette.svg)

| 角色 | 色值 | 用途 |
|---|---|---|
| 墨藍 | `#101F2B` | 主背景 |
| 浅藍 | `#1B3040` | 次级表面 |
| 暖纸 | `#E3DDCF` | 正文 |
| 雪白 | `#F3EFE6` | 光标与高亮文字 |
| 雾蓝 | `#84A7BD` | 蓝色语法与窗口边框 |
| 水绿 | `#8FB8B5` | 青色语法与渐变终点 |
| 松叶 | `#9CAC89` | 绿色语法 |
| 朱色 | `#D58B72` | 选中控件与交互强调 |
| 赭黄 | `#D3B57D` | 黄色语法 |

这些是为 Shigure 调整的专属色值，不代表历史颜料的标准色。
正文与背景的对比度为 **12.38:1**，八种基础命名彩色与该背景的对比度均超过 **5.9:1**，
选区文字为 **7.75:1**。这些是指定不透明颜色对的测量结果，不代表所有应用最终显示效果。

## Omarchy 兼容性

[`colors.toml`](colors.toml) 提供完整语义配色、明确的 `mode = "dark"`、亮色组及受支持的冷色边框渐变。
终端、编辑器、Hyprland 与 Shell 配置由 Omarchy 自带模板生成。
`icons.theme` 使用官方文档列出的 `Yaru-prussiangreen`。主题不包含可执行钩子，也不覆盖应用配置。

兼容性以 **v4.0.0** 的颜色解析器与模板为依据，详见[验证记录与限制](docs/COMPATIBILITY.md)。
当前工作环境为 macOS，尚未在真实 Omarchy 桌面上完成安装验证。

## 来源与使用

本系列以歌川广重的浮世绘为灵感来源。
[图像制作记录](docs/ARTWORK.md)保留了图像制作方式与处理过程。
Shigure 是社区主题，与 Omarchy 官方项目相互独立。

配置、文档与随附图像均以 [MIT License](LICENSE) 发布。
分享桌面截图或衍生作品时，欢迎附上 Shigure 项目链接，让更多人发现它。

推荐项目简介：*为 Omarchy 设计的静谧藍色主题，以歌川广重的浮世绘为灵感，呈现雨、雪、山、水。*

推荐 Topics：`omarchy-theme`、`omarchy`、`hiroshige`、`ukiyo-e`、`dark-theme`、`wallpaper`、`indigo`。
