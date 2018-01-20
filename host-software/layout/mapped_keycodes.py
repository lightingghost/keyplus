#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 jem@seethis.link
# Licensed under the MIT license (http://opensource.org/licenses/MIT)

from layout.keycodes import *
from layout.common import *

key_symbols = {
    # start HID normal keycodes
    "none": KC_NONE, "no": KC_NONE, "----": KC_NONE,
    "error_roll_over": KC_ERROR_ROLL_OVER,
    "post_fail": KC_POST_FAIL,
    "error_undefined": KC_ERROR_UNDEFINED,
    "a": KC_A,
    "b": KC_B,
    "c": KC_C,
    "d": KC_D,
    "e": KC_E,
    "f": KC_F,
    "g": KC_G,
    "h": KC_H,
    "i": KC_I,
    "j": KC_J,
    "k": KC_K,
    "l": KC_L,
    "m": KC_M,
    "n": KC_N,
    "o": KC_O,
    "p": KC_P,
    "q": KC_Q,
    "r": KC_R,
    "s": KC_S,
    "t": KC_T,
    "u": KC_U,
    "v": KC_V,
    "w": KC_W,
    "x": KC_X,
    "y": KC_Y,
    "z": KC_Z,
    "1": KC_1, 1: KC_1,
    "2": KC_2, 2: KC_2,
    "2": KC_2, 2: KC_2,
    "3": KC_3, 3: KC_3,
    "4": KC_4, 4: KC_4,
    "5": KC_5, 5: KC_5,
    "6": KC_6, 6: KC_6,
    "7": KC_7, 7: KC_7,
    "8": KC_8, 8: KC_8,
    "9": KC_9, 9: KC_9,
    "0": KC_0, 0: KC_0,
    "ent": KC_ENTER, "enter": KC_ENTER,
    "esc": KC_ESCAPE, "escape": KC_ESCAPE,
    "bspc": KC_BACKSPACE, "backspace": KC_BACKSPACE,
    "tab": KC_TAB,
    "spc": KC_SPACEBAR, "spacebar": KC_SPACEBAR,
    "min": KC_MINUS, "-": KC_MINUS, "hyphen": KC_MINUS, "minus": KC_MINUS,
    "equ": KC_EQUAL, "equal": KC_EQUAL, "=": KC_EQUAL,
    "lbrc": KC_LEFT_BRACKET, "[": KC_LEFT_BRACKET, "left_bracket": KC_LEFT_BRACKET,
    "rbrc": KC_RIGHT_BRACKET, "]": KC_RIGHT_BRACKET, "right_bracket": KC_RIGHT_BRACKET,
    "bsls": KC_BACK_SLASH, "\\": KC_BACK_SLASH, "back_slash": KC_BACK_SLASH,
    "iso#": KC_ISO_HASH, "iso_hash": KC_ISO_HASH,
    "scln": KC_SEMICOLON, ";": KC_SEMICOLON, "semicolon": KC_SEMICOLON,
    "quot": KC_APOSTROPHE, "'": KC_APOSTROPHE, "apostrophe": KC_APOSTROPHE,
    "grv": KC_GRAVE, "`": KC_GRAVE, "grave": KC_GRAVE,
    "comm": KC_COMMA, ",": KC_COMMA, "comma": KC_COMMA,
    "dot": KC_PERIOD, ".": KC_PERIOD, "period": KC_PERIOD,
    "fsls": KC_FORWARD_SLASH, "/": KC_FORWARD_SLASH, "forward_slash": KC_FORWARD_SLASH,
    "caps": KC_CAPS_LOCK, "caps_lock": KC_CAPS_LOCK,
    "f1": KC_F1,
    "f2": KC_F2,
    "f3": KC_F3,
    "f4": KC_F4,
    "f5": KC_F5,
    "f6": KC_F6,
    "f7": KC_F7,
    "f8": KC_F8,
    "f9": KC_F9,
    "f10": KC_F10,
    "f11": KC_F11,
    "f12": KC_F12,
    "pscr": KC_PRINT_SCREEN, "print_screen": KC_PRINT_SCREEN,
    "slck": KC_SCROLL_LOCK, "scroll_lock": KC_SCROLL_LOCK,
    "paus": KC_PAUSE, "pause": KC_PAUSE,
    "ins": KC_INSERT, "insert": KC_INSERT,
    "home": KC_HOME,
    "pgup": KC_PAGE_UP, "page_up": KC_PAGE_UP,
    "del": KC_DELETE, "delete": KC_DELETE,
    "end": KC_END,
    "pgdn": KC_PAGE_DOWN, "page_down": KC_PAGE_DOWN,
    "rght": KC_RIGHT_ARROW, "right": KC_RIGHT_ARROW, "right_arrow": KC_RIGHT_ARROW,
    "left": KC_LEFT_ARROW, "left_arrow": KC_LEFT_ARROW,
    "down": KC_DOWN_ARROW, "down_arrow": KC_DOWN_ARROW,
    "up": KC_UP_ARROW, "up_arrow": KC_UP_ARROW,
    "nlck": KC_NUM_LOCK, "num_lock": KC_NUM_LOCK,
    "kp_/": KC_KP_FORWARD_SLASH,
    "kp_*": KC_KP_ASTERISK,
    "kp_-": KC_KP_MINUS,
    "kp_+": KC_KP_PLUS,
    "kp_ent": KC_KP_ENTER, "kp_enter": KC_KP_ENTER,
    "kp_1": KC_KP_1,
    "kp_2": KC_KP_2,
    "kp_3": KC_KP_3,
    "kp_4": KC_KP_4,
    "kp_5": KC_KP_5,
    "kp_6": KC_KP_6,
    "kp_7": KC_KP_7,
    "kp_8": KC_KP_8,
    "kp_9": KC_KP_9,
    "kp_0": KC_KP_0,
    "kp_.": KC_KP_PERIOD,
    "iso\\": KC_ISO_BACK_SLASH,
    "application": KC_APPLICATION, "app": KC_APPLICATION,
    "power": KC_POWER,
    "kp_=": KC_KP_EQUAL,
    "f13": KC_F13,
    "f14": KC_F14,
    "f15": KC_F15,
    "f16": KC_F16,
    "f17": KC_F17,
    "f18": KC_F18,
    "f19": KC_F19,
    "f20": KC_F20,
    "f21": KC_F21,
    "f22": KC_F22,
    "f23": KC_F23,
    "f24": KC_F24,
    "execute": KC_EXECUTE,
    "help": KC_HELP,
    "menu": KC_MENU,
    "select": KC_SELECT,
    "stop": KC_STOP,
    "again": KC_AGAIN,
    "undo": KC_UNDO,
    "cut": KC_CUT,
    "copy": KC_COPY,
    "paste": KC_PASTE,
    "find": KC_FIND,
    "mute": KC_MUTE,
    "volume_up": KC_VOLUME_UP,
    "volume_down": KC_VOLUME_DOWN,
    "locking_caps_lock": KC_LOCKING_CAPS_LOCK,
    "locking_num_lock": KC_LOCKING_NUM_LOCK,
    "locking_scroll_lock": KC_LOCKING_SCROLL_LOCK,
    "kp_,": KC_KP_COMMA,
    "kp_equal_as400": KC_KP_EQUAL_AS400,
    "international_1": KC_INTERNATIONAL_1,
    "international_2": KC_INTERNATIONAL_2,
    "international_3": KC_INTERNATIONAL_3,
    "international_4": KC_INTERNATIONAL_4,
    "international_5": KC_INTERNATIONAL_5,
    "international_6": KC_INTERNATIONAL_6,
    "international_7": KC_INTERNATIONAL_7,
    "international_8": KC_INTERNATIONAL_8,
    "international_9": KC_INTERNATIONAL_9,
    "lang_1": KC_LANG_1,
    "lang_2": KC_LANG_2,
    "lang_3": KC_LANG_3,
    "lang_4": KC_LANG_4,
    "lang_5": KC_LANG_5,
    "lang_6": KC_LANG_6,
    "lang_7": KC_LANG_7,
    "lang_8": KC_LANG_8,
    "lang_9": KC_LANG_9,
    "alternate_erase": KC_ALTERNATE_ERASE,
    "sys_req": KC_SYS_REQ,
    "cancel": KC_CANCEL,
    "clear": KC_CLEAR,
    "prior": KC_PRIOR,
    "return": KC_RETURN,
    "separator": KC_SEPARATOR,
    "out": KC_OUT,
    "oper": KC_OPER,
    "clear_again": KC_CLEAR_AGAIN,
    "crsel": KC_CRSEL,
    "exsel": KC_EXSEL,
    "kp_00": KC_KP_00,
    "kp_000": KC_KP_000,
    "thousands_separator": KC_THOUSANDS_SEPARATOR,
    "decimal_separator": KC_DECIMAL_SEPARATOR,
    "currency_unit": KC_CURRENCY_UNIT,
    "currency_sub_unit": KC_CURRENCY_SUB_UNIT,
    "kp_(": KC_KP_LEFT_PARENTHESIS,
    "kp_)": KC_KP_RIGHT_PARENTHESIS,
    "kp_[": KC_KP_LEFT_BRACE,
    "kp_]": KC_KP_RIGHT_BRACE,
    "kp_tab": KC_KP_TAB,
    "kp_bspc": KC_KP_BACK_SPACE, "kp_back_space": KC_KP_BACK_SPACE,
    "kp_a": KC_KP_A,
    "kp_b": KC_KP_B,
    "kp_c": KC_KP_C,
    "kp_d": KC_KP_D,
    "kp_e": KC_KP_E,
    "kp_f": KC_KP_F,
    "kp_xor": KC_KP_XOR,
    "kp_^": KC_KP_CARET,
    "kp_%": KC_KP_PERCENT,
    "kp_<": KC_KP_LESS_THAN,
    "kp_>": KC_KP_GREATER_THAN,
    "kp_&": KC_KP_BITWISE_AND,
    "kp_&&": KC_KP_LOGICAL_AND,
    "kp_|": KC_KP_BITWISE_OR,
    "kp_||": KC_KP_LOGICAL_OR,
    "kp_:": KC_KP_COLON,
    "kp_#": KC_KP_HASH,
    "kp_spc": KC_KP_SPACE, "kp_space": KC_KP_SPACE,
    "kp_@": KC_KP_AT_SIGN,
    "kp_!": KC_KP_EXCLAMATION,
    "kp_memory_store": KC_KP_MEMORY_STORE,
    "kp_memory_recall": KC_KP_MEMORY_RECALL,
    "kp_memory_clear": KC_KP_MEMORY_CLEAR,
    "kp_memory_add": KC_KP_MEMORY_ADD,
    "kp_memory_subtract": KC_KP_MEMORY_SUBTRACT,
    "kp_memory_multiply": KC_KP_MEMORY_MULTIPLY,
    "kp_memory_divide": KC_KP_MEMORY_DIVIDE,
    "kp_plus_minus": KC_KP_PLUS_MINUS, "kp_±": KC_KP_PLUS_MINUS,
    "kp_clear": KC_KP_CLEAR,
    "kp_clear_entry": KC_KP_CLEAR_ENTRY,
    "kp_binary": KC_KP_BINARY,
    "kp_octal": KC_KP_OCTAL,
    "kp_decimal": KC_KP_DECIMAL,
    "kp_hexadecimal": KC_KP_HEXADECIMAL,
    # modifiers in modkey get directly mapped to modifier bit mask instead
    # of sending a keycode in 6kro mode
    "lctl": MODKEY_LEFT_CONTROL, "lctrl": MODKEY_LEFT_CONTROL,
    "lsft": MODKEY_LEFT_SHIFT, "lshift": MODKEY_LEFT_SHIFT,
    "lalt": MODKEY_LEFT_ALT,
    "lgui": MODKEY_LEFT_GUI, "lwin": MODKEY_LEFT_GUI,
    "rctl": MODKEY_RIGHT_CONTROL, "rctrl": MODKEY_RIGHT_CONTROL,
    "rsft": MODKEY_RIGHT_SHIFT, "rshift": MODKEY_RIGHT_SHIFT,
    "ralt": MODKEY_RIGHT_ALT, "altgr": MODKEY_RIGHT_ALT,
    "rgui": MODKEY_RIGHT_GUI, "rwin": MODKEY_RIGHT_GUI,
    # end normal HID keycodes

    "!": gen_modkey(KC_1, shift=True),
    "@": gen_modkey(KC_2, shift=True),
    "#": gen_modkey(KC_3, shift=True),
    "$": gen_modkey(KC_4, shift=True),
    "%": gen_modkey(KC_5, shift=True),
    "^": gen_modkey(KC_6, shift=True),
    "&": gen_modkey(KC_7, shift=True),
    "*": gen_modkey(KC_8, shift=True),
    "(": gen_modkey(KC_9, shift=True),
    ")": gen_modkey(KC_0, shift=True),
    "_": gen_modkey(KC_MINUS, shift=True),
    "+": gen_modkey(KC_EQUAL, shift=True),
    "|": gen_modkey(KC_BACK_SLASH, shift=True),
    "{": gen_modkey(KC_LEFT_BRACKET, shift=True),
    "}": gen_modkey(KC_RIGHT_BRACKET, shift=True),
    ":": gen_modkey(KC_SEMICOLON, shift=True),
    "\"": gen_modkey(KC_APOSTROPHE, shift=True),
    "<": gen_modkey(KC_COMMA, shift=True),
    ">": gen_modkey(KC_PERIOD, shift=True),
    "?": gen_modkey(KC_FORWARD_SLASH, shift=True),
    "~": gen_modkey(KC_GRAVE, shift=True),

    "iso~": gen_modkey(KC_ISO_HASH, shift=True),
    "iso|": gen_modkey(KC_ISO_BACK_SLASH, shift=True),

    # special keycodes

    "trans": KC_TRANSPARENT, "____": KC_TRANSPARENT,

# mouse movement keycodes
    "mouse_up": KC_MOUSE_UP, "ms_u": KC_MOUSE_UP,
    "mouse_down": KC_MOUSE_DOWN, "ms_d": KC_MOUSE_DOWN,
    "mouse_left": KC_MOUSE_LEFT, "ms_l": KC_MOUSE_LEFT,
    "mouse_right": KC_MOUSE_RIGHT, "ms_r": KC_MOUSE_RIGHT,

    "mouse_wh_up": KC_MOUSE_WH_UP, "wh_u": KC_MOUSE_WH_UP,
    "mouse_wh_down": KC_MOUSE_WH_DOWN, "wh_d": KC_MOUSE_WH_DOWN,
    "mouse_wh_left": KC_MOUSE_WH_LEFT, "wh_l": KC_MOUSE_WH_LEFT,
    "mouse_wh_right": KC_MOUSE_WH_RIGHT, "wh_r": KC_MOUSE_WH_RIGHT,
# 17-1F reserved

# mouse button keycodes
    "mouse_btn1": KC_MOUSE_BTN1, "btn1": KC_MOUSE_BTN1,
    "mouse_btn2": KC_MOUSE_BTN2, "btn2": KC_MOUSE_BTN2,
    "mouse_btn3": KC_MOUSE_BTN3, "btn3": KC_MOUSE_BTN3,
    "mouse_btn4": KC_MOUSE_BTN4, "btn4": KC_MOUSE_BTN4,
    "mouse_btn5": KC_MOUSE_BTN5, "btn5": KC_MOUSE_BTN5,
    "mouse_btn6": KC_MOUSE_BTN6, "btn6": KC_MOUSE_BTN6,
    "mouse_btn7": KC_MOUSE_BTN7, "btn7": KC_MOUSE_BTN7,
    "mouse_btn8": KC_MOUSE_BTN8, "btn8": KC_MOUSE_BTN8,
# 28-2F reserved

# system control
    "system_power": KC_SYSTEM_POWER,
    "system_sleep": KC_SYSTEM_SLEEP,
    "system_wake": KC_SYSTEM_WAKE,

# media control
    "audio_mute": KC_AUDIO_MUTE, "mute": KC_AUDIO_MUTE,
    "audio_vol_up": KC_AUDIO_VOL_UP, "volu": KC_AUDIO_VOL_UP,
    "audio_vol_down": KC_AUDIO_VOL_DOWN, "vold": KC_AUDIO_VOL_DOWN,
    "media_next_track": KC_MEDIA_NEXT_TRACK, "mnxt": KC_MEDIA_NEXT_TRACK,
    "media_prev_track": KC_MEDIA_PREV_TRACK, "mprv": KC_MEDIA_PREV_TRACK,
    "media_fast_forward": KC_MEDIA_FAST_FORWARD, "mffd": KC_MEDIA_FAST_FORWARD,
    "media_rewind": KC_MEDIA_REWIND, "mrwd": KC_MEDIA_REWIND,
    "media_stop": KC_MEDIA_STOP, "mstp": KC_MEDIA_STOP,
    "media_play_pause": KC_MEDIA_PLAY_PAUSE, "mply": KC_MEDIA_PLAY_PAUSE,
    "media_eject": KC_MEDIA_EJECT, "mjct": KC_MEDIA_EJECT,
    "media_select": KC_MEDIA_SELECT, "msel": KC_MEDIA_SELECT,
    "mail": KC_MAIL,
    "calculator": KC_CALCULATOR, "calc": KC_CALCULATOR,
    "my_computer": KC_MY_COMPUTER, "comp": KC_MY_COMPUTER,
    "www_search": KC_WWW_SEARCH,
    "www_home": KC_WWW_HOME,
    "www_back": KC_WWW_BACK,
    "www_forward": KC_WWW_FORWARD,
    "www_stop": KC_WWW_STOP,
    "www_refresh": KC_WWW_REFRESH,
    "www_favorites": KC_WWW_FAVORITES,

# hardware control
    "dongle_0": KC_DONGLE_0,
    "dongle_1": KC_DONGLE_1,
    "dongle_2": KC_DONGLE_2,
    "dongle_3": KC_DONGLE_3,
    "dongle_4": KC_DONGLE_4,
    "dongle_5": KC_DONGLE_5,
    "dongle_6": KC_DONGLE_6,
    "dongle_7": KC_DONGLE_7,

    "bootloader": KC_BOOTLOADER,
    "bootloader_2": KC_BOOTLOADER_2,
    "reset": KC_RESET,
    "kro_6": KC_KRO_6,
    "kro_n": KC_KRO_N,
    "kro_auto": KC_KRO_AUTO,
    "pair": KC_UNIFYING_PAIR,

    "test_0": KC_TEST_0,
    "test_1": KC_TEST_1,
    "test_2": KC_TEST_2,
    "test_3": KC_TEST_3,
    "test_4": KC_TEST_4,
    "test_5": KC_TEST_5,
    "test_6": KC_TEST_6,
    "test_7": KC_TEST_7,

    # basic layer keycodes, layer is active while key is down
    "l0": KC_L0,
    "l1": KC_L1,
    "l2": KC_L2,
    "l3": KC_L3,
    "l4": KC_L4,
    "l5": KC_L5,
    "l6": KC_L6,
    "l7": KC_L7,
    "l8": KC_L8,
    "l9": KC_L9,
    "l10": KC_L10,
    "l11": KC_L11,
    "l12": KC_L12,
    "l13": KC_L13,
    "l14": KC_L14,
    "l15": KC_L15,

    # sets the base layer
    "set_l0": KC_SET_L0,
    "set_l1": KC_SET_L1,
    "set_l2": KC_SET_L2,
    "set_l3": KC_SET_L3,
    "set_l4": KC_SET_L4,
    "set_l5": KC_SET_L5,
    "set_l6": KC_SET_L6,
    "set_l7": KC_SET_L7,
    "set_l8": KC_SET_L8,
    "set_l9": KC_SET_L9,
    "set_l10": KC_SET_L10,
    "set_l11": KC_SET_L11,
    "set_l12": KC_SET_L12,
    "set_l13": KC_SET_L13,
    "set_l14": KC_SET_L14,
    "set_l15": KC_SET_L15,

    # actives a layer until it is pressed again (toggles it on off on press)
    "toggle_l0": KC_TOGGLE_L0, "tog_l0": KC_TOGGLE_L0,
    "toggle_l1": KC_TOGGLE_L1, "tog_l1": KC_TOGGLE_L1,
    "toggle_l2": KC_TOGGLE_L2, "tog_l2": KC_TOGGLE_L2,
    "toggle_l3": KC_TOGGLE_L3, "tog_l3": KC_TOGGLE_L3,
    "toggle_l4": KC_TOGGLE_L4, "tog_l4": KC_TOGGLE_L4,
    "toggle_l5": KC_TOGGLE_L5, "tog_l5": KC_TOGGLE_L5,
    "toggle_l6": KC_TOGGLE_L6, "tog_l6": KC_TOGGLE_L6,
    "toggle_l7": KC_TOGGLE_L7, "tog_l7": KC_TOGGLE_L7,
    "toggle_l8": KC_TOGGLE_L8, "tog_l8": KC_TOGGLE_L8,
    "toggle_l9": KC_TOGGLE_L9, "tog_l9": KC_TOGGLE_L9,
    "toggle_l10": KC_TOGGLE_L10, "tog_l10": KC_TOGGLE_L10,
    "toggle_l11": KC_TOGGLE_L11, "tog_l11": KC_TOGGLE_L11,
    "toggle_l12": KC_TOGGLE_L12, "tog_l12": KC_TOGGLE_L12,
    "toggle_l13": KC_TOGGLE_L13, "tog_l13": KC_TOGGLE_L13,
    "toggle_l14": KC_TOGGLE_L14, "tog_l14": KC_TOGGLE_L14,
    "toggle_l15": KC_TOGGLE_L15, "tog_l15": KC_TOGGLE_L15,

    # actives a layer until the next non-layer key is pressed
    "sticky_l0": KC_STICKY_L0,
    "sticky_l1": KC_STICKY_L1,
    "sticky_l2": KC_STICKY_L2,
    "sticky_l3": KC_STICKY_L3,
    "sticky_l4": KC_STICKY_L4,
    "sticky_l5": KC_STICKY_L5,
    "sticky_l6": KC_STICKY_L6,
    "sticky_l7": KC_STICKY_L7,
    "sticky_l8": KC_STICKY_L8,
    "sticky_l9": KC_STICKY_L9,
    "sticky_l10": KC_STICKY_L10,
    "sticky_l11": KC_STICKY_L11,
    "sticky_l12": KC_STICKY_L12,
    "sticky_l13": KC_STICKY_L13,
    "sticky_l14": KC_STICKY_L14,
    "sticky_l15": KC_STICKY_L15,

    "sticky_lctrl": KC_STICKY_LCTRL,
    "sticky_lshift": KC_STICKY_LSHIFT,
    "sticky_lalt": KC_STICKY_LALT,
    "sticky_lgui": KC_STICKY_LGUI,
    "sticky_rctrl": KC_STICKY_RCTRL,
    "sticky_rshift": KC_STICKY_RSHIFT,
    "sticky_ralt": KC_STICKY_RALT,
    "sticky_rgui": KC_STICKY_RGUI,

    "": KC_LAYER_RESET,

}

def get_keycode_type(keycode):
    if type(kc) != int:
        raise ParseKeycodeError("keycode must be an int")
    if kc < 0 or kc > 0xffff:
        raise ParseKeycodeError("keycode must be a 16 bit integer")

    if (keycode & EKC_TAG):
        return KC_TYPE_EKC
    elif (keycode & SPECIAL_KC_TAG):
        return KC_TYPE_SPECIAL
    else:
        return KC_TYPE_MODKEY


def keycode_from_binary(kc_raw):
    assert(type(kc_raw) == int and kc_raw >= 0 and kc_raw <= 0xffff)

    kc_type = get_keycode_type(keycode)

    if kc_type == KC_TYPE_MODKEY:
        pass
    elif kc_type == KC_TYPE_SPECIAL:
        pass
    elif kc_type == KC_TYPE_EKC:
        pass
    else:
        raise ParseKeycodeError("Unknown keycode format")


def interpret_keycode(kc_in):
    kc_str = str(kc_in).lower()
    if kc_str in key_symbols:
        return key_symbols[kc_str]
    elif "-" in kc_str:
        if kc_str.count('-') > 2:
            raise ParseKeycodeError("Too many '-' in keycode: '{}'".format(kc_str))
        if kc_str.count('-') == 2:
            if kc_str.count('--') != 1 or kc_str[-1] != '-' or kc_str == "--":
                raise ParseKeycodeError("Couldn't handle keycode: '{}'".format(kc_str))
        mods, kc = kc_str.split("-", 1)
        ctrl = False
        shift = False
        alt = False
        gui = False
        right = False
        left = False
        force = False
        for mod in mods:
            if mod == 'c' and not ctrl:
                ctrl = True
            elif mod == 's' and not shift:
                shift = True
            elif mod == 'a' and not alt:
                alt = True
            elif mod == 'g' or mod == 'w' or mod == 'm' and not gui:
                gui = True
            elif mod == 'r' and not (right or left):
                right = True
            elif mod == 'l' and not (right or left):
                left = True
            elif mod == 'f':
                force = True
            else:
                raise ParseKeycodeError("Unexpected or duplicate character in mods mask: '{}'".format(mod))
        kc = interpret_keycode(kc)
        return gen_modkey(kc, ctrl=ctrl, shift=shift, alt=alt, gui=gui, right=right, force=force)
    else:
        raise ParseKeycodeError("Unexpected keycode: '{}'".format(kc_in))


if __name__ == "__main__":
    print(hex(interpret_keycode('l0')))
    print(hex(interpret_keycode('gr-up')))
    print(hex(interpret_keycode('caslg-up')))
    print(hex(interpret_keycode('casrg-up')))
