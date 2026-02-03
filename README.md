# Email Operations MCP

基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) 的邮件操作服务，供 AI 助手通过 MCP 调用邮箱查询与发送能力。

## 功能

- **按用户名查邮箱**：根据用户名返回对应邮箱地址（格式：`{username}@shopee.com`）
- **发送邮件**：向指定收件人发送邮件正文

## 环境要求

- Python 3.x
- 依赖见 `requirements.txt`

## 安装

```bash
pip install -r requirements.txt
```

## 运行

### 1. 启动 MCP 服务

以 stdio 方式启动 MCP 服务（供 Cursor 等客户端连接）：

```bash
python main_mcp.py
```

### 2. 运行代理客户端

使用代理客户端与 MCP 服务交互：

```bash
python main_agent.py
```

## 项目结构

```
mcp_agent_demo/
├── main_mcp.py          # MCP 服务入口，注册工具
├── main_agent.py        # 代理客户端，与 MCP 服务交互
├── tools/
│   └── email_operations.py   # 邮箱查询与发送实现
├── .gitignore
├── requirements.txt
└── README.md
```

## MCP 工具说明

| 工具 | 说明 |
|------|------|
| `get_email_address_by_username` | 根据用户名返回邮箱地址 |
| `send_email` | 向指定邮箱发送邮件（收件人、正文） |

在 Cursor 等支持 MCP 的客户端中配置本 MCP 服务器后，即可在对话中让 AI 代为查邮箱或发邮件。

## 代理客户端说明

`main_agent.py` 是一个代理客户端示例，演示了如何：
1. 接收用户输入
2. 调用 AI 模型生成响应
3. 处理模型的工具调用请求
4. 执行相应的工具函数
5. 将工具执行结果返回给模型
6. 获取最终的模型响应

通过运行此代理客户端，您可以测试 MCP 服务的功能，体验完整的工具调用流程。
