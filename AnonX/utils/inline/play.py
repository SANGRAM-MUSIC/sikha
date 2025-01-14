import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX.utils.formatters import time_to_seconds
from AnonX import app
from AnonX.utils.inline.start import BOT_USERNAME


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    Iro = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "◉—————————"
    elif 10 < anon < 20:
        bar = "—◉————————"
    elif 20 <= anon < 30:
        bar = "——◉———————"
    elif 30 <= anon < 40:
        bar = "———◉——————"
    elif 40 <= anon < 50:
        bar = "————◉—————"
    elif 50 <= anon < 60:
        bar = "—————◉————"
    elif 60 <= anon < 70:
        bar = "——————◉———"
    elif 70 <= anon < 80:
        bar = "———————◉——"
    elif 80 <= anon < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"•─╼⃝𖠁𝐀ᴅᴅ ◈ 𝐌ᴇ ◈ 𝐁ᴀʙʏ𖠁⃝╾─•",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(

                text="ᴘʟᴀʏ",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            

        ],

        [

            InlineKeyboardButton(

                text="⏮ 10sᴇᴄ",

                callback_data=f"ADMIN 1|{chat_id}",

            ),


            InlineKeyboardButton(

                text="⏭ 10sᴇᴄ",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],
        [
            InlineKeyboardButton(
                text=f"⛦ ᴊᴏɪɴ ⛦",
              url="https://t.me/vip_creators",
            ),
        ],
    ]

    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    Iro = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "◉—————————"
    elif 10 < anon < 20:
        bar = "—◉————————"
    elif 20 <= anon < 30:
        bar = "——◉———————"
    elif 30 <= anon < 40:
        bar = "———◉——————"
    elif 40 <= anon < 50:
        bar = "————◉—————"
    elif 50 <= anon < 60:
        bar = "—————◉————"
    elif 60 <= anon < 70:
        bar = "——————◉———"
    elif 70 <= anon < 80:
        bar = "———————◉——"
    elif 80 <= anon < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"•─╼⃝𖠁𝐀ᴅᴅ ◈ 𝐌ᴇ ◈ 𝐁ᴀʙʏ𖠁⃝╾─•",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(

                text="ᴘʟᴀʏ",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            

        ],

        [

            InlineKeyboardButton(

                text="⏮ 10sᴇᴄ",

                callback_data=f"ADMIN 1|{chat_id}",

            ),


            InlineKeyboardButton(

                text="⏭ 10sᴇᴄ",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],
        [
            InlineKeyboardButton(
                text=f"⛦ ᴊᴏɪɴ ⛦",
              url="https://t.me/vip_creators",
            ),
        ],
    ]

    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"•─╼⃝𖠁𝐀ᴅᴅ ◈ 𝐌ᴇ ◈ 𝐁ᴀʙʏ𖠁⃝╾─•",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(

                text="ᴘʟᴀʏ",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            

        ],

        [

            InlineKeyboardButton(

                text="⏮ 10sᴇᴄ",

                callback_data=f"ADMIN 1|{chat_id}",

            ),


            InlineKeyboardButton(

                text="⏭ 10sᴇᴄ",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],
        [
            InlineKeyboardButton(
                text=f"⛦ ᴊᴏɪɴ ⛦",
              url="https://t.me/vip_creators",
            ),
        ],
    ]

    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"•─╼⃝𖠁𝐀ᴅᴅ ◈ 𝐌ᴇ ◈ 𝐁ᴀʙʏ𖠁⃝╾─•",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(

                text="ᴘʟᴀʏ",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            

        ],

        [

            InlineKeyboardButton(

                text="⏮ 10sᴇᴄ",

                callback_data=f"ADMIN 1|{chat_id}",

            ),


            InlineKeyboardButton(

                text="⏭ 10sᴇᴄ",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],
        [
            InlineKeyboardButton(
                text=f"⛦ ᴊᴏɪɴ ⛦",
              url="https://t.me/vip_creators",
            ),
        ],
    ]

    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
         [
            InlineKeyboardButton(
                text=f"•─╼⃝𖠁𝐀ᴅᴅ ◈ 𝐌ᴇ ◈ 𝐁ᴀʙʏ𖠁⃝╾─•",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❤ sᴛᴀʀᴛ ʟɪᴠᴇ ❤",
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"⛦ ᴊᴏɪɴ ⛦",
              url="https://t.me/vip_creators",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=f"•─╼⃝𖠁𝐀ᴅᴅ ◈ 𝐌ᴇ ◈ 𝐁ᴀʙʏ𖠁⃝╾─•",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"•─╼⃝𖠁𝐀ᴅᴅ ◈ 𝐌ᴇ ◈ 𝐁ᴀʙʏ𖠁⃝╾─•",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(

                text="ᴘʟᴀʏ",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            

        ],

        [

            InlineKeyboardButton(

                text="⏮ 10sᴇᴄ",

                callback_data=f"ADMIN 1|{chat_id}",

            ),


            InlineKeyboardButton(

                text="⏭ 10sᴇᴄ",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],
        [
            InlineKeyboardButton(
                text=f"⛦ ᴊᴏɪɴ ⛦",
              url="https://t.me/vip_creators",
            ),
        ],
    ]

    return buttons

def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
                InlineKeyboardButton(
                    text="🕒 0.5x",
                    callback_data=f"SpeedUP {chat_id}|0.5",
                ),
                InlineKeyboardButton(
                    text="ɴᴏʀᴍᴀʟ",
                    callback_data=f"SpeedUP {chat_id}|1.0",
                ),
                InlineKeyboardButton(
                    text="🕓 0.75x",
                    callback_data=f"SpeedUP {chat_id}|0.75",
                ),
            ],
            [
                InlineKeyboardButton(text="✨ ᴀᴅᴅ ᴛᴏ ᴘʟᴀʏʟɪꜱᴛ ✨", callback_data=f"add_playlist {videoid}"),
            ],
            [
                InlineKeyboardButton(
                    text="🕤 1.5x",
                    callback_data=f"SpeedUP {chat_id}|1.5",
                ),
                InlineKeyboardButton(
                    text="• ʙᴀᴄᴋ •",
                    callback_data=f"MainMarkup {videoid}|{chat_id}",
                ),
                InlineKeyboardButton(
                    text="🕛 2.0x",
                    callback_data=f"SpeedUP {chat_id}|2.0",
                ),
            ],
    ]
    return buttons
