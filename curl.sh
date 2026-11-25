#!/bin/sh
# One request to Refract. Set your key first:  export REFRACT_API_KEY=rf_...
curl https://refracthub.com/v1/chat/completions \
  -H "Authorization: Bearer $REFRACT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-5-5",
    "messages": [{"role": "user", "content": "Write a haiku about cheap tokens."}]
  }'
