# AI Translator

一个运行在终端中的中英互译工具，使用 DeepSeek API 完成翻译：

- 中文输入会翻译成英文
- 英文输入会翻译成中文
- 支持包含空格的文本和多个命令行参数

## 环境要求

- Python 3.9 或更高版本
- 安装requirements.txt文件中要求的第三方库
- 一个可用的 DeepSeek API Key,没有可以去官网申请

## 安装

在项目根目录参照`.env.example`创建 `.env` 文件，并填入 DeepSeek API Key,默认模型是deepseek-v4-pro,可以自行修改模型

不要将 `.env` 提交到 Git 或分享给他人。

## 使用

```bash
# 示例
python main.py "Please translate this sentence."
python main.py Please translate this sentence.
```

## 配置终端别名

为了在任意目录使用，可以在 `~/.zshrc` 或 `~/.bashrc` 中添加别名。请将路径替换为本项目的实际路径：

```bash
# 示例
alias lingo='python /path/to/AI_translator/main.py'
```

重新打开终端，或执行对应的配置文件：

```bash
source ~/.zshrc    # zsh
# source ~/.bashrc  # bash
```

之后即可使用：

```bash
# 示例
lingo "这是一段需要翻译的文字。"
```

如果使用了虚拟环境，建议把别名中的 `python` 替换为虚拟环境解释器的绝对路径：

```bash
alias lingo='/path/to/AI_translator/.venv/bin/python /path/to/AI_translator/main.py'
```

## 常见问题

### 未配置 API Key

如果看到 `未配置 DEEPSEEK_API_KEY`，请确认项目根目录存在 `.env` 文件，并检查变量名和值是否正确。

### API Key 无效或请求被限流

检查 API Key 是否有效、账户是否有可用额度；遇到限流时请稍后重试。

### 翻译失败

确认网络连接正常，并检查当前配置的模型是否可用