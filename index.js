import express from "express";
import fetch from "node-fetch";
import worker from "./worker.js";

const app = express();
app.use(express.json());

app.get("/", (req, res) => {
  res.send("Bot is running on Heroku 🚀");
});

// Telegram webhook endpoint
app.post("/webhook", async (req, res) => {
  try {
    // yahan tera worker logic call hoga
    const result = await worker.fetch({
      json: async () => req.body,
    });
    res.status(200).send("OK");
  } catch (err) {
    console.error(err);
    res.status(500).send("Error");
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log("Server running on port", PORT);
});
