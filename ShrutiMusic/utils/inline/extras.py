from ShrutiMusic.utils.inline.buttons import inline
from config import SUPPORT_GROUP


def botplaylist_markup(_):
    buttons = [
        [
            inline._button(
                text=_["S_B_9"],
                category="primary",
                url=SUPPORT_GROUP
            ),
            inline._button(
                text=_["CLOSE_BUTTON"],
                category="danger",
                callback_data="close"
            ),
        ],
    ]
    return buttons


def close_markup(_):
    upl = inline.ikm(
        [
            [
                inline._button(
                    text=_["CLOSE_BUTTON"],
                    category="danger",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = inline.ikm(
        [
            [
                inline._button(
                    text=_["S_B_9"],
                    category="primary",
                    url=SUPPORT_GROUP,
                ),
            ]
        ]
    )
    return upl
