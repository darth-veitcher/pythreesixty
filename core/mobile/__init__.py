__author__ = 'James Veitch'
import requests
from ..helpers import get_token, _url


def projects():
    """ POST /api/projects

    Description: Returns a list of projects available to the currently authenticated user. If the authenticated user is a subcontractor on a project, that project will be excluded from this list.
    Access: FREE
    Return: [JSON] - Array of project hashes.
    Parameters:

        ticket : string - The ticket obtained from the login call.
    """
    url = _url('api/projects')

    json = {
        'ticket': get_token(),
    }

    return requests.post(url, json=json)


def get_issues(project_id, **kwargs):
    """  POST /api/get_issues

    Description: Returns a list of issues for the conditions specified, or the count if count_only is specified. All returned issues will contain
    lists of any attachments, document_references, uri_references and comments.

    Status Codes:
    200 : The request was processed successfully.
    401 : The authenticated user does not have permission to the specified issue filter.
    404 : The specified issue filter ID does not exist.
    Access: FREE
    Return: [JSON] - Array of issues.
    Parameters:

        ticket : string - The ticket obtained from the login call.
        project_id : string - The ID of the project to perform this action against.
        area_ids : string - Comma separated list of area IDs. If specified, only retrieve issues in these areas.
        count_only : string : If non-nil, just return the count of issues. If nil, return the issues themselves.
        issue_filter_id : string : A single issue filter ID. If specified, only retrieve issues from the specified filter.
    """
    url = _url('api/get_issues')

    json = {
        'ticket': get_token(),
        'project_id': project_id,
    }
    for key in kwargs:
        json[key] = kwargs[key]

    return requests.post(url, json=json)
