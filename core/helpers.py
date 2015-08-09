__author__ = 'James Veitch'

import requests
import config


def _url(path):
    """ Takes an API path and concatenates with the root_url

    :param path: API node (e.g. tasks/list)
    :return: fully formed url for API
    """
    return "{0}/{1}".format(config.SETTINGS.root_url, path)


def get_token():
    """ Returns the authentication token for the user.

    Checks whether we already have one and, if not, calls the mobile.login
    function.
    """
    token = None

    if not config.SETTINGS.__contains__('token'):
        if config.SETTINGS.DEBUG:
            print("Token not found. Login requested.")

        response = __login()
        if config.SETTINGS.DEBUG:
            print(token)

        if response.status_code != 200:
            raise NotImplementedError(response.status_code, response.json())

        else:
            token = response.json()['ticket']

    else:
        token = config.SETTINGS.token

    config.SETTINGS.token = token
    return token


def __login(**kwargs):
    """ POST /api/login

    Description: Attempts to authenticate with the mobile API using BIM 360 Field credentials. On success, returns a
                36 byte GUID "ticket" which needs to be passed in on subsequent calls.

    Status Codes:

    200 User has authenticated and is successfully logged in.
    401 The user's credentials have been rejected.
    426 The user is a subcontractor on their active project, and login has been denied.
    Access: FREE
    Return: JSON - Returns a ticket which must be passed for each subsequent request in the session.
    Parameters:

        username : string - The username to authenticate as.
        password : string - The password to authenticate with.
        device_type : string - (optional) The type of device
        device_identifier : string - (optional) A unique identifier for the device.
    """
    url = _url('/api/login')
    json = {
        'username': config.SETTINGS.user_details['username'],
        'password': config.SETTINGS.user_details['password'],
    }

    return requests.post(url, json=json)


def logout(project_id):
    """ POST /api/logout

    Description: Closes the current active session by expiring the ticket.
    Access: FREE
    Return: Nothing
    Parameters:

    :param project_id : string - The ID of the project to perform this action against.
    :param ticket : string - The ticket obtained from the login call.
    """
    url = _url('/api/logout')
    json = {
        'project_id': project_id,
        'ticket': get_token()
    }

    return requests.post(url, json=json)
