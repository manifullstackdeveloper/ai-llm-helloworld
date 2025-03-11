import OpenAI from "openai";

/*
* #use key in env variable or paste it here and run code
*/
const openai = new OpenAI({
    apiKey: process.env.apiKey 
})


const completion = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    store: true,
    messages: [
        {"role": "user", "content": "Tell me about AI in 2 sentences few shot"},
    ]
});

console.log(completion.choices[0].message?.content);