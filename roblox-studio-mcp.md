# Let an AI build in Roblox Studio

Roblox Studio has a built-in MCP server. The Refract desktop app for Windows can connect to it, so a model can read your place, write scripts and insert parts for you.

1. Install Refract for Windows from https://refracthub.com and sign in.
2. In Roblox Studio: **Assistant → … → Manage MCP Servers → Enable Studio as MCP server**.
3. In Refract: **Settings → Connections → Add a connection**, and paste this as the program:
   ```
   cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat
   ```
   Refract recognises it as Roblox Studio.
4. Switch the chat to **Code** mode and describe what you want, for example "add a spinning coin that gives 10 points when touched".

A typical task costs about $0.02 to $0.07 on Claude Sonnet 5.5, because most of the context is read from cache. Claude, GPT, Gemini and Grok models can also look at Studio screenshots.

ForgeGUI users: add a **Web address** connection and use the "Fill in ForgeGUI" button to generate UI from Refract.
