init 10 python:
    def _ru_apply_language_on_splash(label_name, *args, **kwargs):
        # change_language() must run even if _preferences.language is already
        # "ru": that value is persisted, but the translation itself is only
        # activated by change_language (Ren'Py does not apply it on startup).
        # change_language() early-returns on its own when the language is
        # already active in this session.
        if label_name == "splashscreen" and persistent.language == "ru":
            renpy.change_language("ru")
        return None

    if _ru_apply_language_on_splash not in config.label_callbacks:
        config.label_callbacks.append(_ru_apply_language_on_splash)


init 2 screen choose_language():
    default local_lang = _preferences.language
    default chosen_lang = _preferences.language

    modal True
    style_prefix "radio"

    add "gui/overlay/confirm.png"

    frame:
        style "confirm_frame"

        has vbox
        xalign .5
        yalign .5
        xsize 760
        spacing 30

        label _("Please select a language"):
            style "confirm_prompt"
            xalign 0.5

        vbox:
            style_prefix "radio"
            label _("Language")


            textbutton "English" text_font "gui/font/Aller_Rg.ttf" action [
                    Language(None),
                    SetField(persistent, "language", "english"),
                    SetScreenVariable("chosen_lang", "english"),
                    Show("dialog", message="It is recommended to restart to apply the changes.", ok_action=Quit())
                ]
            textbutton "Español" text_font "gui/font/Aller_Rg.ttf" action [
                    Language("spanish"),
                    SetField(persistent, "language", "spanish"),
                    SetScreenVariable("chosen_lang", "spanish"),
                    Show("dialog", message="Se recomienda reiniciar el juego\npara aplicar los cambios.", ok_action=Quit())
                ]
            textbutton "Русский" text_font "mod_assets/fonts/NotoSansSC-Regular.ttf" action [
                    Language("ru"),
                    SetField(persistent, "language", "ru"),
                    SetScreenVariable("chosen_lang", "ru"),
                    Show("dialog", message="{font=mod_assets/fonts/NotoSansSC-Regular.ttf}Рекомендуется перезапустить игру,\nчтобы применить изменения.{/font}", ok_action=Quit())
                ]




        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action [
                    Language(None),
                    SetField(persistent, "language", "english"),
                    SetScreenVariable("chosen_lang", "english"),
                    Show("dialog", message="It is recommended to restart to apply the changes.", ok_action=Quit())
                    ] style "ok_button_custom"

style ok_button_custom is button:
    background None
    foreground None
    hover_background None
    hover_foreground None
    insensitive_background None
    insensitive_foreground None

label choose_language:
    call screen choose_language
    return


init 2 screen preferences():
    tag menu


    default tooltip = Tooltip("")

    use game_menu(_("Settings"), scroll="viewport"):


        vbox:
            xoffset 50

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "generic_fancy_check"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                if config.developer:
                    vbox:
                        style_prefix "radio"
                        label _("Rollback Side")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "generic_fancy_check"
                    label _("Gameplay")

                    textbutton _("Repeat Topics"):
                        action [
                            ToggleField(
                                object=persistent,
                                field="fae_repeat_chat",
                                true_value=True,
                                false_value=False
                            )
                        ]
                    if not renpy.android:
                        textbutton _("Notifications") action [
                            ToggleField(
                                object=persistent,
                                field="_fae_notifs_enabled",
                                true_value=True,
                                false_value=False

                                )
                            ]


            null height (4 * gui.pref_spacing)


            hbox:
                style_prefix "slider"
                box_wrap True

                python:

                    if fae_randchat_prev != persistent._fae_random_chat_freq:

                        fae_random_chat_rate.adjustRandFrequency(
                            persistent._fae_random_chat_freq
                        )

                    rc_display = fae_random_chat_rate.getRandChatDisp(
                        persistent._fae_random_chat_freq
                    )

                    store.fae_randchat_prev = persistent._fae_random_chat_freq

                vbox:

                    hbox:
                        label _("Random Chatter  ")
                        label _("[[ " + rc_display + " ]")

                    bar value FieldValue(
                        persistent,
                        "_fae_random_chat_freq",
                        range=4,
                        style="slider"
                    )

                vbox:

                    label _("Text Speed")

                    bar value FieldValue(_preferences, "text_cps", range=170, max_is_zero=False, style="slider", offset=30)

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:
                    label _("Music Volume")
                    hbox:
                        bar value Preference("music volume")

                    label _("Sound Volume")
                    hbox:
                        bar value Preference("sound volume")


                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        style "check_button"
                        action Preference("all mute", "toggle")



                if not renpy.android:
                    vbox:
                        style_prefix "radio"
                        label _("Language")


                        textbutton "English" text_font "DejaVuSans.ttf" action [Language(None), SetField(persistent, "language", "english"), Show("dialog", message="It is recommended to restart to apply the changes.\n\nOtherwise, some things may remain in other languages.", ok_action=Hide("dialog"))]
                        textbutton "Español" text_font "DejaVuSans.ttf" action [Language("spanish"), SetField(persistent, "language", "spanish"), Show("dialog", message="Se recomienda reiniciar el juego\npara aplicar los cambios.\n\nDe lo contrario, es posible\nque algunas cosas se\nconserven en otros idiomas.", ok_action=Hide("dialog"))]
                        textbutton "Русский" text_font "mod_assets/fonts/NotoSansSC-Regular.ttf" action [Language("ru"), SetField(persistent, "language", "ru"), Show("dialog", message="{font=mod_assets/fonts/NotoSansSC-Regular.ttf}Рекомендуется перезапустить игру,\nчтобы применить изменения.\n\nИначе часть текста может остаться\nна других языках.{/font}", ok_action=Hide("dialog"))]



            hbox:


                if not renpy.android:
                    textbutton _("Import DDLC Save Data"):
                        action Function(renpy.call_in_new_context, 'import_ddlc_persistent_in_settings')
                        style "navigation_button"

                textbutton _("Web functions"):
                    action Function(show_ps_overlay)
                    style "navigation_button"

            vbox:
                style_prefix "radio"
                label _("Font Style")

                textbutton _("Default Font"):
                    action [
                        SetVariable("persistent.use_alt_font", False),
                        Show("dialog", message=_("You need to restart the game for the font change to take effect."), ok_action=Hide("dialog"))
                    ]
                    selected If(not persistent.use_alt_font, True, False)

                textbutton _("Alternate Font"):
                    action [
                        SetVariable("persistent.use_alt_font", True),
                        Show("dialog", message=_("You need to restart the game for the font change to take effect."), ok_action=Hide("dialog"))
                    ]
                    selected If(persistent.use_alt_font, True, False)