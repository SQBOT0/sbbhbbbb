from typing import Union
from ShrutiMusic.utils.inline.buttons import inline


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            inline._button(
                text=_["QU_B_1"],
                category="primary",
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            inline._button(
                text=_["CLOSE_BUTTON"],
                category="danger",
                callback_data="close",
            ),
        ]
    ]
    dur = [
        [
            inline._button(
                text=_["QU_B_2"].format(played, dur),
                category="primary",
                callback_data="GetTimer",
            )
        ],
        [
            inline._button(
                text=_["QU_B_1"],
                category="primary",
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            inline._button(
                text=_["CLOSE_BUTTON"],
                category="danger",
                callback_data="close",
            ),
        ],
    ]
    upl = inline.ikm(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = inline.ikm(
        [
            [
                inline._button(
                    text=_["BACK_BUTTON"],
                    category="primary",
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                inline._button(
                    text=_["CLOSE_BUTTON"],
                    category="danger",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            inline._button(
                text=_["CLOSE_BUTTON"],
                category="danger",
                callback_data="close",
            ),
        ],
    ]
    return buttons
