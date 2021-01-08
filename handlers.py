from constants import DEFAULT_GREETING, HELP_MENU


# Returns an error message stating that command is invalid
def handle_invalid_command(command):
    return f'Sorry, your command "{command}" is invalid'


# Returns a greeting message with instructions on how to get started
def __show_default_greeting():
    return DEFAULT_GREETING


# Returns a greeting message with instructions on how to get started
def __show_help_menu():
    return HELP_MENU


# Dictionary of command actions mapped to a corresponding function that will be executed when user submits said command
COMMAND_HANDLERS = {
    'start': lambda ignored: __show_default_greeting(),
    'help': lambda ignored: __show_help_menu(),
}
