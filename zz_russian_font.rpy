

init 100 python:
    if persistent.language == "ru":
        _ru_font = "mod_assets/fonts/NotoSansSC-Regular.ttf"
        _ru_font_bold = "mod_assets/fonts/NotoSansSC-Bold.ttf"

        gui.default_font = _ru_font
        gui.name_font = _ru_font_bold
        gui.interface_font = _ru_font
        gui.button_text_font = _ru_font
        gui.choice_button_text_font = _ru_font

        def _ru_set_style_font(style_name, font_name):
            try:
                getattr(style, style_name).font = font_name
            except Exception:
                
                pass

        for _ru_style_name in (
            "default", "edited", "poemgame_text", "button_text", "label_text",
            "choice_button_text", "talk_choice_button_text", "say_dialogue",
            "input_prompt", "input", "radio_button_text", "check_button_text",
            "slider_button_text", "main_menu_text", "quick_button_text",
            "page_label_text", "slot_button_text", "about_text", "history_text",
            "confirm_prompt_text", "confirm_button_text", "skip_text",
            "notify_text", "nvl_dialogue", "nvl_thought", "nvl_button_text",
            "scrollable_menu_button_text", "sayori_text", "splash_text",
            "gui_text", "console_text",
        ):
            _ru_set_style_font(_ru_style_name, _ru_font)

        for _ru_style_name in (
            "say_label", "navigation_button_text", "game_menu_label_text",
            "pref_label_text", "history_name_text",
        ):
            _ru_set_style_font(_ru_style_name, _ru_font_bold)

        # DDLC-style alias: at runtime `style.say_dialogue = style.normal`
        # (see core/script.rpy, script-ch30.rpy, after_load), so the size must
        # be set on both styles to survive the alias.
        try:
            style.say_dialogue.size = 24
            style.normal.size = 24
        except Exception:
            pass



translate ru style default:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style say_dialogue:
    size 24

translate ru style normal:
    size 24

translate ru style splash_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style edited:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style poemgame_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style sayori_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style gui_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style button_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style say_label:
    font "mod_assets/fonts/NotoSansSC-Bold.ttf"

translate ru style navigation_button_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style game_menu_label_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style pref_label_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style radio_button_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"

translate ru style check_button_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"


translate ru style choice_button_text:
    size 24

translate ru style console_text:
    font "mod_assets/fonts/NotoSansSC-Regular.ttf"
