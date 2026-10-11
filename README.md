# 小迈讲故事

个人故事博客，直接由 GitHub Pages 发布根目录的静态页面。

## 内容与风格

暖纸色、墨绿与朱红点缀的阅读风格。首页展示最新故事摘要，正文提供章节目录和阅读进度。桌面与手机均可阅读，字体使用本地中文宋体与黑体，无外部字体或 CDN 依赖。

第一篇文章是《从首日 12 人到日增 945 人，我的小程序上线经历》，根据博饼故事 V3 稿的口播内容整理，保留统计时间与口径，去除制作备注。

## 更新文章

- 正文源文件：`source/le-bobing.md`
- 首页摘要及布局：`templates/home.html`
- 文章布局：`templates/article.html`
- 公共页头、元信息与页脚：`templates/base.html`
- 样式、交互和插画：`assets/`

编辑后运行：

```sh
python3 scripts/build.py
```

生成 `index.html` 和 `stories/le-bobing/index.html`。构建仅使用 Python 3 标准库。

本地预览：

```sh
python3 -m http.server 8000
```

访问 http://localhost:8000 。提交源文件与生成的页面后，沿用仓库的 GitHub Pages 发布设置。

## 原博客说明

原仓库仅有 Hexo 4.2.0 生成的静态产物，没有 Hexo 配置、文章源文件或主题源码。本次用可编辑的 Markdown、HTML 模板和轻量构建脚本接续维护。旧文章、归档与主题资源已从当前站点移除，历史内容仍可在 Git 历史中找回。

当前先发布单篇故事版。后续增加第二篇时，可恢复 Hexo：将 `source/le-bobing.md` 加入文章 front matter 后放到 Hexo 的 `source/_posts/`，并迁移当前样式与模板；保留 `stories/le-bobing/` 的文章链接。
