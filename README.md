---
date: 2023-02-28 18:25
title: README
---

## 什么是 front matter
front matter的中文意思是前言，几乎每本书都会有前言，用来说明写书目的或者内容总结。

而 markdown 文件中的front matter指的是以yaml格式在文件开头增加的元数据，示例如下：

```
---
title: "为 obsidian 中的文件批量添加 front matter"
date: 2023-02-28 18:25
tags:
- obsidian
- frontmatter
---
```
front matter需要用---包裹

笔记软件或博客软件会拿到这些元数据做相应处理，比如上面这个front matter中 title 字段用来作为文章题目，date作为发布日期，tags 作为文章的标签列表

## 使用方法

下载 `python-frontmatter`
```sh
pip3 install python-frontmatter
```

执行本脚本

```sh
python3 front-matter.py
```

## 效果

```sh
请选择操作：
1. 添加标题和日期，如果已存在则不进行操作 （1f，强制覆盖）
2. 识别标签(未完工)
3. 批量添加 yaml 属性名和属性值
4. quit
```

自动添加 `标题` 和 `日期`

```
---
date: 2023-02-28 18:25
title: README
---
```