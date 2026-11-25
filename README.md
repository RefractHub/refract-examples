# Refract API examples

[Refract](https://refracthub.com) is one API key for 47 AI models (Claude, GPT, Gemini, Grok, DeepSeek, Kimi, Qwen, GLM), at up to 95% below the official prices. It speaks both the **OpenAI Chat Completions API** and the **Anthropic Messages API**, so most tools work after changing two settings.

| Setting  | Value                                                   |
|----------|---------------------------------------------------------|
| Base URL | `https://refracthub.com/v1`                             |
| API key  | your `rf_…` key from [the console](https://refracthub.com/account) |
| Model    | any ID from [the models page](https://refracthub.com/models), e.g. `claude-sonnet-5-5` |

Prices per 1M tokens and every model ID: https://refracthub.com/pricing

## Examples

| File | What it shows |
|------|---------------|
| [`curl.sh`](curl.sh) | A plain HTTP request |
| [`python_openai.py`](python_openai.py) | The OpenAI Python SDK, with streaming |
| [`node_openai.mjs`](node_openai.mjs) | The OpenAI Node SDK |
| [`python_anthropic.py`](python_anthropic.py) | The Anthropic Python SDK |
| [`claude-code.md`](claude-code.md) | Running Claude Code on Refract (any model) |
| [`cursor.md`](cursor.md) | Using Refract models in Cursor |
| [`opencode.json`](opencode.json) | An OpenCode provider config |
| [`roblox-studio-mcp.md`](roblox-studio-mcp.md) | Letting an AI build in Roblox Studio with the Refract desktop app |

## Keep your key safe

Every example reads the key from the `REFRACT_API_KEY` environment variable. Never paste a key into code you commit. You can give each key a spending cap, and revoke it any time, in the console.

## Links

- Website and web chat: https://refracthub.com
- API docs: https://refracthub.com/docs
- Models and prices: https://refracthub.com/models
- Model status: https://refracthub.com/status
- Support: https://refracthub.com/support
