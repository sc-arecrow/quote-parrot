from pprint import pprint

from flask import request, jsonify

from app import app
from api.telegram_api import send_message
from beans.user import User

# @app.route('/getmsg/', methods=['GET'])
# def respond():
#     # Retrieve the name from url parameter
#     name = request.args.get("name", None)
#
#     # For debugging
#     print(f"got name {name}")
#
#     response = {}
#
#     # Check if user sent a name at all
#     if not name:
#         response["ERROR"] = "no name found, please send a name."
#     # Check if the user entered a number not a name
#     elif str(name).isdigit():
#         response["ERROR"] = "name can't be numeric."
#     # Now the user entered a valid name
#     else:
#         response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"
#
#     # Return the response in json format
#     return jsonify(response)
#
#
# @app.route('/post/', methods=['POST'])
# def post_something():
#     param = request.form.get('name')
#     print(param)
#     # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
#     if param:
#         return jsonify({
#             "Message": f"Welcome {param} to our awesome platform!!",
#             # Add this option to distinct the POST request
#             "METHOD" : "POST"
#         })
#     else:
#         return jsonify({
#             "ERROR": "no name found, please send a name."
#         })


# A welcome message to test our server
from handlers import COMMAND_HANDLERS, handle_invalid_command
from utils import is_not_blank, get_user_from_request, get_user_input_from_request, get_user_command_from_request


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


# Validates incoming webhook request to make sure required fields are present, before processing
@app.route('/webhook', methods=['POST'])
def webhook():
    req_body = request.get_json()

    if req_body is None:
        return 'ERROR: No request body', 400

    user = get_user_from_request(req_body)
    user_input = get_user_input_from_request(req_body)
    commands = get_user_command_from_request(req_body)

    if not commands:
        return ''

    if is_not_blank(user.id, user_input):
        __process_telegram_commands(user, commands)

    return ''


# Processes all individual commands found in user input, concatenating them into a single response for user
# Does not support options for individual commands since we are responding to potentially multiple commands in input
def __process_telegram_commands(user: User, commands):
    individual_responses = filter(is_not_blank, map(__process_individual_telegram_command, commands))
    response = "\n---\n".join(individual_responses)

    send_message(user, ", ".join(commands), response)


def __process_individual_telegram_command(command):
    if is_not_blank(command):
        return COMMAND_HANDLERS.get(command, handle_invalid_command)(command)
    else:
        return ''