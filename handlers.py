from app import db
from constants import DEFAULT_GREETING, HELP_MENU
from models.quote import Quote
from models.person import Person

# Returns an error message stating that command is invalid
def handle_invalid_command(command):
    return f'Sorry, your command "{command}" is invalid'


# Returns a greeting message with instructions on how to get started
def __show_default_greeting():
    return DEFAULT_GREETING


# Returns a greeting message with instructions on how to get started
def __show_help_menu():
    return HELP_MENU


def __add_new_person(name):
    person = Person.make_person(name).save()
    return f'{name} has been saved.'


def __list_persons():
    persons = Person.objects

    if not persons:
        return f'There are no people saved.'

    listed_persons = '- ' + '\n- '.join(map(lambda x: x['name'], persons))
    return listed_persons


def __delete_person(name):
    person = Person.objects(name=name)
    person.delete()
    return f'{name} has been deleted.'


def __add_new_quote(text):
    quote = Quote.make_quote(text).save()
    return f'The quote "{quote.text}" has been saved.'


def __show_random_quote():
    if not Quote.objects:
        return f'There are no quotes saved.'

    pipeline = [
        {'$sample': {'size': 1}}
    ]
    random_quote = Quote.objects.aggregate(pipeline).next()
    return random_quote['text']


def __list_quotes():
    quotes = Quote.objects.order_by('-date')[:10]

    if not quotes:
        return f'There are no quotes.'

    listed_quotes = '- ' + '\n- '.join(map(lambda x: x['text'], quotes))
    return listed_quotes


def __delete_quotes():
    Quote.objects.delete()
    return f'All quotes have been deleted.'


# Dictionary of command actions mapped to a corresponding function that will be executed when user submits said command
COMMAND_HANDLERS = {
    'start': lambda ignored: __show_default_greeting(),
    'help': lambda ignored: __show_help_menu(),
    'addperson': __add_new_person,
    'listpersons': lambda ignored: __list_persons(),
    'deleteperson': __delete_person,
    'addquote': __add_new_quote,
    'showquote': lambda ignored: __show_random_quote(),
    'listquotes': lambda ignored: __list_quotes(),
    'deletequotes': lambda ignored: __delete_quotes(),
}
