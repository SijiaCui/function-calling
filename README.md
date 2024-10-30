# Function-Calling 🚀

## 项目简介 📖

本项目旨在提供一个框架，测试多种商业大型语言模型（LLMs）对**Function-Calling**功能的支持，以及**利用工具解决广泛的复杂任务**的能力。分析多种商业大模型的Function-Calling实现细节。并进行实验测试。项目使用 [Poetry](https://python-poetry.org/) 进行依赖管理和安装，方便在不同环境中快速部署和运行。

## 项目结构 🗂️
```
📜 LICENSE
📜 README.md
📜 llms.py
📂 logs
   ├── 📝 gpt_tools.log
   ├── 📝 main.log
   ├── 📝 main_all.log
   └── 📝 main_gpt.log
📜 main.py
📜 poetry.lock
📜 pyproject.toml
📂 tools
   ├── 🔧 tools.py
   └── 🔧 tools_desc.py
```

## 安装步骤 🛠️

### 环境要求 ✅

- Python 3.9 及以上
- [Poetry](https://python-poetry.org/) 包管理器

### 安装依赖 ⚙️

1. 克隆本项目到本地：
   ```bash
   git clone https://github.com/SijiaCui/function-calling.git
   cd ./function-calling
    ```
2. 使用poetry安装依赖
    ```bash
    poetry install
    ```
3. 配置 OpenAI Key 🔑
    ```bash
    # 将API key写入到~/.bashrc文件中
    export OPENAI_API_KEY=<your_openai_api_key>
    ```
4. 运行项目 ▶️
    ```bash
    poetry shell
    python main.py
    ```

## TODO 📋
- [ ] 更多商业大模型对于工具/函数的支持测试
- [ ] 对function-calling的实现方式
- [ ] 工具调用格式
