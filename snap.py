from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import random

SNAP_TOKEN = "7794306440:AAEjsBTFTf5RQoHfqhuwmkJwgCLZWrVSXPc"
SNAP_VIDEO_ORDNER = "/home/EuroHunter/videos"

snap_nachricht = (
    "🔥 Du wolltest schon immer heimlich Snapchat-Videos, Bilder oder Chats sehen? 🔥\n"
    "Dann bist du hier genau richtig! 👀\n\n"
    "Schick mir einfach den Snap Username vom Acc, um zu gucken, ob es für uns machbar ist,\n"
    "Dann überweist du das Geld, sendest ein Beweisfoto 💸,\n"
    "Innerhalb von 5-10 Minuten hast du Zugriff auf den privaten Bereich – Videos, Bilder, Nachrichten – alles! 🎥📸💬\n"
    "Auf Wunsch kann der Account auch komplett gelöscht werden. 🗑\n\n"
    "Preise:\n"
    "1 Account – 50€ 💸\n"
    "2 Accounts – 60€ 💸\n"
    "5 Accounts – 75€ 💸\n\n"
    "Schnell ⚡️, diskret 🤫 und zuverlässig! ✔️\n\n"
    "Bei Interesse / Fragen schreibt @xeurohunter\n\n"
    "*👇Beispiel👇*"
)

async def snap_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat

    await context.bot.send_message(chat_id=chat.id, text=snap_nachricht, parse_mode="Markdown")

    try:
        alle_dateien = [f for f in os.listdir(SNAP_VIDEO_ORDNER) if f.lower().endswith(('.mp4', '.mov', '.avi'))]
    except Exception as e:
        await context.bot.send_message(chat_id=chat.id, text=f"⚠️ Fehler beim Zugriff auf den Ordner: {e}")
        return

    if not alle_dateien:
        await context.bot.send_message(chat_id=chat.id, text="⚠️ Keine Beispielvideos im Ordner gefunden.")
        return

    video_dateien = random.sample(alle_dateien, min(2, len(alle_dateien)))

    for datei in video_dateien:
        video_pfad = os.path.join(SNAP_VIDEO_ORDNER, datei)
        try:
            with open(video_pfad, "rb") as video:
                await context.bot.send_video(chat_id=chat.id, video=video)
        except Exception as e:
            await context.bot.send_message(chat_id=chat.id, text=f"⚠️ Fehler beim Senden von {datei}: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(SNAP_TOKEN).build()
    app.add_handler(CommandHandler("snap", snap_command))
    print("✅ Snap-Bot läuft...")
    app.run_polling()
