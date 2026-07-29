from typing import Union
from ShrutiMusic.utils.inline.buttons import inline


def setting_markup(_):
    buttons = [
        [
            inline._button(text=_["ST_B_1"], category="primary", callback_data="AU"),
            inline._button(text=_["ST_B_3"], category="primary", callback_data="LG"),
        ],
        [
            inline._button(text=_["ST_B_2"], category="primary", callback_data="PM"),
        ],
        [
            inline._button(text=_["ST_B_4"], category="primary", callback_data="VM"),
        ],
        [
            inline._button(text=_["CLOSE_BUTTON"], category="danger", callback_data="close"),
        ],
    ]
    return buttons


def vote_mode_markup(_, current, mode: Union[bool, str] = None):
    buttons = [
        [
            inline._button(text="Vᴏᴛɪɴɢ ᴍᴏᴅᴇ ➜", category="primary", callback_data="VOTEANSWER"),
            inline._button(
                text=_["ST_B_5"] if mode == True else _["ST_B_6"],
                category="primary",
                callback_data="VOMODECHANGE",
            ),
        ],
        [
            inline._button(text="-2", category="primary", callback_data="FERRARIUDTI M"),
            inline._button(
                text=f"ᴄᴜʀʀᴇɴᴛ : {current}",
                category="primary",
                callback_data="ANSWERVOMODE",
            ),
            inline._button(text="+2", category="primary", callback_data="FERRARIUDTI A"),
        ],
        [
            inline._button(
                text=_["BACK_BUTTON"],
                category="primary",
                callback_data="settings_helper",
            ),
            inline._button(
                text=_["CLOSE_BUTTON"],
                category="danger",
                callback_data="close",
            ),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            inline._button(text=_["ST_B_7"], category="primary", callback_data="AUTHANSWER"),
            inline._button(
                text=_["ST_B_8"] if status == True else _["ST_B_9"],
                category="primary",
                callback_data="AUTH",
            ),
        ],
        [
            inline._button(text=_["ST_B_1"], category="primary", callback_data="AUTHLIST"),
        ],
        [
            inline._button(
                text=_["BACK_BUTTON"],
                category="primary",
                callback_data="settings_helper",
            ),
            inline._button(
                text=_["CLOSE_BUTTON"],
                category="danger",
                callback_data="close",
            ),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            inline._button(text=_["ST_B_10"], category="primary", callback_data="SEARCHANSWER"),
            inline._button(
                text=_["ST_B_11"] if Direct == True else _["ST_B_12"],
                category="primary",
                callback_data="MODECHANGE",
            ),
        ],
        [
            inline._button(text=_["ST_B_13"], category="primary", callback_data="AUTHANSWER"),
            inline._button(
                text=_["ST_B_8"] if Group == True else _["ST_B_9"],
                category="primary",
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            inline._button(text=_["ST_B_14"], category="primary", callback_data="PLAYTYPEANSWER"),
            inline._button(
                text=_["ST_B_8"] if Playtype == True else _["ST_B_9"],
                category="primary",
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            inline._button(
                text=_["BACK_BUTTON"],
                category="primary",
                callback_data="settings_helper",
            ),
            inline._button(
                text=_["CLOSE_BUTTON"],
                category="danger",
                callback_data="close",
            ),
        ],
    ]
    return buttons
