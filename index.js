import express from "express";
import fetch from "node-fetch";

const app = express();
app.use(express.json());

// === CONFIG ===
const BOT_TOKEN = process.env.BOT_TOKEN; // Heroku config var me set karna
const CHANNELS = [
  { username: "@BotzEmpire", url: "https://t.me/BotzEmpire" },
  { username: "@Yaaro_kimehfill", url: "https://t.me/Yaaro_kimehfill" },
  { username: "@BotsDeal", url: "https://t.me/BotsDeal" }
];
const ADMINS = [7538572906];

// === TERI FONT LOGIC (AS-IT-IS) ===
// ⚠️ Yahan tu apna poora fontStyles, convertText, buttons, etc
// Jo tune bheja hai, **exact same** paste kar de:
// - fontStyles
// - convertText()
// - userTexts
// - fontButtons, fButtons, forceJoinButtons
// - checkChannels(), sendMessage(), editMessage(), answerCallbackQuery()
// - extractTextFromMessage()
// - handleUpdate(update)
//
// ❗ Sirf last wala Cloudflare part (export default { fetch... }) REMOVE kar dena

// -------------------------------
// 👇 YAHI SE WEBHOOK ROUTE
// -------------------------------
app.get("/", (req, res) => {
  res.send("🤖 Font Bot is running on Heroku!");
});

app.post("/webhook", async (req, res) => {
  try {
    const update = req.body;
    await handleUpdate(update);
    res.send("OK");
  } catch (err) {
    console.error("Webhook error:", err);
    res.status(500).send("Error");
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log("Server running on port", PORT);
});
