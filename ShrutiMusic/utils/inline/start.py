import config
from ShrutiMusic import app
from ShrutiMusic.utils.inline.buttons import inline


def start_panel(_):
    buttons = [
        [
            inline._button(
                text=_["S_B_1"],
                category="success",
                url=f"https://t.me/{app.username}?startgroup=true"
            ),
            inline._button(
                text=_["S_B_2"],
                category="primary",
                url=config.SUPPORT_GROUP
            ),
        ],
        [
            inline._button(
                text=_["E_X_1"],
                category="danger",
                url=config.SUPPORT_CHANNEL
            ),
            inline._button(
                text=_["S_B_11"],
                category="primary",
                callback_data="about_page"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            inline._button(
                text=_["S_B_3"],
                category="success",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            inline._button(
                text=_["S_B_11"],
                category="danger",
                callback_data="about_page"
            ),
            inline._button(
                text=_["S_B_12"],
                category="primary",
                callback_data="owner_page"
            )
        ],
        [
            inline._button(
                text=_["E_X_1"],
                category="danger",
                callback_data="fork_repo"
            ),
            inline._button(
                text=_["S_B_5"],
                category="success",
                user_id=config.OWNER_ID
            ),
        ],
        [
            inline._button(
                text=_["S_B_4"],
                category="primary",
                callback_data="help_page_1"
            )
        ],
    ]
    return buttons


def about_panel(_):
    buttons = [
        [
            inline._button(
                text=_["S_B_6"],
                category="danger",
                url=config.SUPPORT_CHANNEL
            ),
            inline._button(
                text=_["S_B_2"],
                category="primary",
                url=config.SUPPORT_GROUP
            ),
        ],
        [
            inline._button(
                text=_["BACK_BUTTON"],
                category="danger",
                callback_data="settingsback_helper"
            )
        ]
    ]
    return buttons


def owner_panel(_):
    buttons = [
        [
            inline._button(
                text=_["S_H_1"],
                category="success",
                url=config.INSTAGRAM
            ),
            inline._button(
                text=_["S_H_2"],
                category="success",
                url=config.YOUTUBE
            ),
        ],
        [
            inline._button(
                text=_["S_H_3"],
                category="primary",
                url=config.GITHUB
            ),
            inline._button(
                text=_["S_H_4"],
                category="danger",
                url=config.DONATE
            ),
        ],
        [
            inline._button(
                text=_["BACK_BUTTON"],
                category="danger",
                callback_data="settingsback_helper"
            )
        ]
    ]
    return buttons
