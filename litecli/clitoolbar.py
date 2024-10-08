from __future__ import unicode_literals

from prompt_toolkit.key_binding.vi_state import InputMode
from prompt_toolkit.enums import EditingMode
from prompt_toolkit.application import get_app


def create_toolbar_tokens_func(cli, show_fish_help):
    """
    Return a function that generates the toolbar tokens.
    """

    def get_toolbar_tokens():
        result = []
        result.append(("class:bottom-toolbar", " "))

        if cli.multi_line:
            result.append(("class:bottom-toolbar", " (Semi-colon [;] will end the line) "))

        if cli.multi_line:
            result.append(("class:bottom-toolbar.on", "[F3] Multiline: ON  "))
        else:
            result.append(("class:bottom-toolbar.off", "[F3] Multiline: OFF  "))
        if cli.prompt_app.editing_mode == EditingMode.VI:
            result.append(("class:botton-toolbar.on", "Vi-mode ({})".format(_get_vi_mode())))

        if show_fish_help():
            result.append(("class:bottom-toolbar", "  Right-arrow to complete suggestion"))

        if cli.completion_refresher.is_refreshing():
            result.append(("class:bottom-toolbar", "     Refreshing completions..."))

        return result

    return get_toolbar_tokens


def _get_vi_mode():
    """Get the current vi mode for display."""
    return {
        InputMode.INSERT: "I",
        InputMode.NAVIGATION: "N",
        InputMode.REPLACE: "R",
        InputMode.INSERT_MULTIPLE: "M",
        InputMode.REPLACE_SINGLE: "R",
    }[get_app().vi_state.input_mode]
