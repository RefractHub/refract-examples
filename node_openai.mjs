// npm install openai
// Set your key first:  export REFRACT_API_KEY=rf_...
import OpenAI from 'openai';

const client = new OpenAI({ baseURL: 'https://refracthub.com/v1', apiKey: process.env.REFRACT_API_KEY });

const reply = await client.chat.completions.create({
  model: 'gemini-4-carbon',
  messages: [{ role: 'user', content: 'Give me three names for a coffee shop.' }],
});
console.log(reply.choices[0].message.content);
