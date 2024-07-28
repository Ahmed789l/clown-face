#TELEGRAM > @ifeelscam

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text =f"<b><blockquote>★ ᴏᴡɴᴇʀ : <a href='t.me/Straw_Hat_Bots'>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ ꭙ 𝐁ᴏᴛs</a>\n★ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Straw_Hat_Bots'>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ ꭙ 𝐁ᴏᴛs</a>\n★ ᴘᴀɪᴅ ʙᴏᴛ : <a href='https://t.me/urr_sanjii_robot'>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a>\n★ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/+iEiMt9WevHwzNzM1'>ᴄᴏᴅᴇ ᴍᴏɴᴋᴇʏ's </a>\n★ ᴅᴇᴠʟᴏᴘᴇʀ : <a href='https://t.me/urr_sanjii'>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a></blockquote></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ [ InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://t.me/+htT0vqGSbBI5Yjg1"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ" , url= "https://t.me/Straw_Hat_Bots")],
                 [InlineKeyboardButton("ᴡᴀᴛᴄʜ 𝟷𝟾+ ᴠɪᴅᴇᴏs",url = "https://t.me/The_Hentai_Society")],
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    elif data == "home":
        await query.message.edit_text(
            text=f"Kᴏɴɴɪᴄʜɪᴡᴀ!! {query.from_user.mention}⚡\n\n<b><blockquote>ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote>\n\n𝐃ᴇᴠᴇʟᴏᴘᴇᴅ 𝐁ʏ : <a href='https://t.me/Straw_Hat_Bots'>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ ꭙ 𝐁ᴏᴛs</a></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton("🤖 ᴀʙᴏᴜᴛ ᴍᴇ", callback_data = "about"),
                    InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                ]
            ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    
    elif data == "me":
            await query.message.edit(
                text=f"<b>sᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ʙᴏᴛ</b>",
                disable_web_page_preview=True,
                reply_markup = InlineKeyboardMarkup(
                    [
                        [ InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ",url = "https://t.me/+iEiMt9WevHwzNzM1")],
                        [ InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data = "home"),
                         InlineKeyboardButton( "🚫 ᴄʟᴏsᴇ", callback_data = "close")]
                    ]
                )
         )

    
