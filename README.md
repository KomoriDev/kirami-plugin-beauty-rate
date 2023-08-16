<div align="center">
  <a href="#"><img src="https://kiramibot.dev/img/logo.svg" width="180" height="180" alt="KiramiBotPluginLogo"></a>
</div>

<div align="center">

# kirami-plugin-beauty-rate

_✨ 让 Bot 为你的颜值打分！ ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/KomoriDev/kirami-plugin-beauty-rate.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/kirami-plugin-beauty-rate">
    <img src="https://img.shields.io/pypi/v/kirami-plugin-beauty-rate.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">

</div>

## 📖 介绍

颜值打分插件。使用 [百度云人脸识别云服务](https://cloud.baidu.com/product/face)

## 💿 安装

在 KiramiBot 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>
  
```bash
pip install kirami-plugin-beauty-rate
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add kirami-plugin-beauty-rate
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add kirami-plugin-beauty-rate
```

</details>
<details>
<summary>conda</summary>

```bash
conda install kirami-plugin-beauty-rate
```

</details>

打开 KiramiBot 项目根目录下的配置文件文件, 以 `kirami.toml` 为例，在 `[plugin]` 部分追加写入

```toml
plugins = ["kirami_plugin_beauty_rate"]
```

## ⚙️ 配置

在 KiramiBot 项目的 `.env` 文件中添加下表中的必填配置

> `api_key` 和 `secret_key` 可以从 [这里](https://cloud.baidu.com/product/face) 获取

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| api_key | 是 | 无 | 无 |
| secret_key | 是 | 无 | 无 |
| ALCONNA_USE_COMMAND_START | 否 | false | [详见](https://github.com/nonebot/plugin-alconna/tree/master#%E9%85%8D%E7%BD%AE)

## 🎉 使用

### 指令表

| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 颜值评分 | 无 | 否 | 私聊/群聊 | 别名：颜值打分 |

### 效果图

~~理论上，这里应该有些图片~~