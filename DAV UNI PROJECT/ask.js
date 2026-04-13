import express from "express";
import OpenAI from "openai";
import { retrieveContext } from "../ragEngine.js";

const router = express.Router();
const openai = new OpenAI();

router.post("/", async (req, res) => {
    const { question } = req.body;

    const context = await retrieveContext(question);

    const stream = await openai.chat.completions.create({
        model: "gpt-4o-mini",
        stream: true,
        messages: [
            {
                role: "system",
                content: "You are a DAV University assistant. Answer only from context."
            },
            {
                role: "user",
                content: `Context:\n${context}\n\nQuestion: ${question}`
            }
        ]
    });

    res.setHeader("Content-Type", "text/plain");

    for await (const chunk of stream) {
        res.write(chunk.choices[0]?.delta?.content || "");
    }

    res.end();
});

export default router;