# Claude Code on Refract

Claude Code talks to the Anthropic Messages API, which Refract supports. Set these before starting `claude`.

**macOS / Linux**

```sh
export ANTHROPIC_BASE_URL=https://refracthub.com
export ANTHROPIC_AUTH_TOKEN=rf_your_key
export ANTHROPIC_MODEL=claude-sonnet-5-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-5-5
claude
```

**Windows PowerShell**

```powershell
$env:ANTHROPIC_BASE_URL = "https://refracthub.com"
$env:ANTHROPIC_AUTH_TOKEN = "rf_your_key"
$env:ANTHROPIC_MODEL = "claude-sonnet-5-5"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL = "claude-haiku-5-5"
claude
```

The base URL has no `/v1` (Claude Code adds it). You can set `ANTHROPIC_MODEL` to any model on Refract, not only Claude: for example `gpt-6.2-sol` or `gemini-4-carbon`.

Tip: give the key a spending cap in the [console](https://refracthub.com/account), so a long agent run can't spend more than you planned.
