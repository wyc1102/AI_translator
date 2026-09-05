# AI Translator

一个运行在终端中的中英互译工具，使用 DeepSeek API 完成翻译：

- 中文输入会翻译成英文
- 英文输入会翻译成中文
- 支持包含空格的文本和多个命令行参数

## 环境要求

- Python 3.9 或更高版本
- 安装requirements.txt文件中要求的第三方库
- 一个可用的 DeepSeek API Key, 没有可以去官网申请

## 安装

在项目根目录参照`.env.example`创建 `.env` 文件，并填入 DeepSeek API Key,默认模型是deepseek-v4-pro,可以自行修改模型

不要将 `.env` 提交到 Git 或分享给他人。

## 配置终端别名

为了在任意目录使用，可以在 `~/.zshrc` 或 `~/.bashrc` 中添加别名,如果使用了虚拟环境，请使用虚拟环境中的python解释器

```bash
# 如果将项目放在 ~/shell_scripts 下,可以按如下配置,根据你使用的python解释器选一个
# 如果放在其他路径下,按实际目录修改即可
alias lingo="python $HOME/shell_scripts/AI_translator/main.py" # 使用系统python解释器
alias lingo="$HOME/shell_scripts/AI_translator/.venv/bin/python $HOME/shell_scripts/AI_translator/main.py" # 使用虚拟环境python解释器
```

重新打开终端, 或者执行对应的配置文件：

```bash
source ~/.zshrc    # zsh
# source ~/.bashrc  # bash
```

之后即可使用：

```bash
# 示例
lingo "这是一段需要翻译的文字。"
```

## 常见问题

### 未配置 API Key

如果看到 `未配置 DEEPSEEK_API_KEY`，请确认项目根目录存在 `.env` 文件，并检查变量名和值是否正确。

### API Key 无效或请求被限流

检查 API Key 是否有效、账户是否有可用额度；遇到限流时请稍后重试。

### 翻译失败

确认网络连接正常，并检查当前配置的模型是否可用