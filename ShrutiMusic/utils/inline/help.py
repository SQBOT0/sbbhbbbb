from typing import Union
from ShrutiMusic.utils.inline.buttons import inline
from ShrutiMusic import app


def help_pannel_page1(_, START: Union[bool, int] = None):
    return inline.ikm(
        [
            [
                inline._button(text=_["H_B_1"], category="success", callback_data="help_callback hb1"),
                inline._button(text=_["H_B_2"], category="primary", callback_data="help_callback hb2"),
            ],
            [
                inline._button(text=_["H_B_3"], category="primary", callback_data="help_callback hb3"),
                inline._button(text=_["H_B_4"], category="success", callback_data="help_callback hb4"),
            ],
            [
                inline._button(text=_["H_B_5"], category="success", callback_data="help_callback hb5"),
                inline._button(text=_["H_B_6"], category="primary", callback_data="help_callback hb6"),
                inline._button(text=_["H_B_7"], category="success", callback_data="help_callback hb7"),
            ],
            [
                inline._button(text=_["H_B_8"], category="primary", callback_data="help_callback hb8"),
                inline._button(text=_["H_B_9"], category="success", callback_data="help_callback hb9"),
                inline._button(text=_["H_B_10"], category="primary", callback_data="help_callback hb10"),
            ],
            [
                inline._button(text="⏮", category="primary", callback_data="help_page_4"),
                inline._button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    category="danger",
                    callback_data="settingsback_helper" if START else "close",
                ),
                inline._button(text="⏭", category="primary", callback_data="help_page_2"),
            ],
        ]
    )


def help_pannel_page2(_, START: Union[bool, int] = None):
    return inline.ikm(
        [
            [
                inline._button(text=_["H_B_11"], category="success", callback_data="help_callback hb11"),
                inline._button(text=_["H_B_12"], category="primary", callback_data="help_callback hb12"),
            ],
            [
                inline._button(text=_["H_B_13"], category="primary", callback_data="help_callback hb13"),
                inline._button(text=_["H_B_14"], category="success", callback_data="help_callback hb14"),
            ],
            [
                inline._button(text=_["H_B_15"], category="success", callback_data="help_callback hb15"),
                inline._button(text=_["H_B_16"], category="primary", callback_data="help_callback hb16"),
                inline._button(text=_["H_B_17"], category="success", callback_data="help_callback hb17"),
            ],
            [
                inline._button(text=_["H_B_18"], category="primary", callback_data="help_callback hb18"),
                inline._button(text=_["H_B_19"], category="success", callback_data="help_callback hb19"),
                inline._button(text=_["H_B_20"], category="primary", callback_data="help_callback hb20"),
            ],
            [
                inline._button(text="⏮", category="primary", callback_data="help_page_1"),
                inline._button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    category="danger",
                    callback_data="settingsback_helper" if START else "close",
                ),
                inline._button(text="⏭", category="primary", callback_data="help_page_3"),
            ],
        ]
    )


def help_pannel_page3(_, START: Union[bool, int] = None):
    return inline.ikm(
        [
            [
                inline._button(text=_["H_B_21"], category="success", callback_data="help_callback hb21"),
                inline._button(text=_["H_B_22"], category="primary", callback_data="help_callback hb22"),
            ],
            [
                inline._button(text=_["H_B_23"], category="primary", callback_data="help_callback hb23"),
                inline._button(text=_["H_B_24"], category="success", callback_data="help_callback hb24"),
            ],
            [
                inline._button(text=_["H_B_25"], category="success", callback_data="help_callback hb25"),
                inline._button(text=_["H_B_26"], category="primary", callback_data="help_callback hb26"),
                inline._button(text=_["H_B_27"], category="success", callback_data="help_callback hb27"),
            ],
            [
                inline._button(text=_["H_B_28"], category="primary", callback_data="help_callback hb28"),
                inline._button(text=_["H_B_29"], category="success", callback_data="help_callback hb29"),
                inline._button(text=_["H_B_30"], category="primary", callback_data="help_callback hb30"),
            ],
            [
                inline._button(text="⏮", category="primary", callback_data="help_page_2"),
                inline._button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    category="danger",
                    callback_data="settingsback_helper" if START else "close",
                ),
                inline._button(text="⏭", category="primary", callback_data="help_page_4"),
            ],
        ]
    )


def help_pannel_page4(_, START: Union[bool, int] = None):
    return inline.ikm(
        [
            [
                inline._button(text=_["H_B_31"], category="success", callback_data="help_callback hb31"),
                inline._button(text=_["H_B_32"], category="primary", callback_data="help_callback hb32"),
            ],
            [
                inline._button(text=_["H_B_33"], category="primary", callback_data="help_callback hb33"),
                inline._button(text=_["H_B_34"], category="success", callback_data="help_callback hb34"),
            ],
            [
                inline._button(text=_["H_B_35"], category="success", callback_data="help_callback hb35"),
                inline._button(text=_["H_B_37"], category="primary", callback_data="help_callback hb37"),
            ],
            [
                inline._button(text=_["H_B_38"], category="primary", callback_data="help_callback hb38"),
                inline._button(text=_["H_B_39"], category="success", callback_data="help_callback hb39"),
            ],
            [
                inline._button(text=_["H_B_36"], category="success", callback_data="help_callback hb36"),
            ],   
            [
                inline._button(text="⏮", category="primary", callback_data="help_page_3"),
                inline._button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    category="danger",
                    callback_data="settingsback_helper" if START else "close",
                ),
                inline._button(text="⏭", category="primary", callback_data="help_page_1"),
            ],
        ]
    )


def help_back_markup(_, page: int = 1):
    return inline.ikm(
        [
            [
                inline._button(
                    text=_["BACK_BUTTON"],
                    category="danger",
                    callback_data=f"help_page_{page}",
                )
            ]
        ]
    )


def private_help_panel(_):
    return [
        [
            inline._button(
                text=_["S_B_4"],
                category="success",
                url=f"https://t.me/{app.username}?start=help",
            ),
        ]
    ]
