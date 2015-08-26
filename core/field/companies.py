__author__ = 'James Veitch'
import requests
from ..helpers import get_token, _url


def companies(project_id=None, **kwargs):
    """ GET /fieldapi/companies/v1

    Description: Returns list of companies. If project_id is not given all companies from the user's account will be returned.

    Status Codes:
        200 OK Success.
        401 UNAUTHORIZED Authentication failed.
        500 INTERNAL SERVER ERROR A general system error has occurred.

    Example Result:

        [{"name":"Admin Company API","id":"00000101-0001-0000-0000-000000000013","address":{"country":"US","state":null,"address3":null,"postal_code":"1322","county":null,"city":"Waltham","address2":null,"address1":null},"url":"www.admincompanyapi.com","telephone":"206-340-2256","ctype":"Other","custom_fields":[{"value":null,"default_value":null,"possible_values":null,"display_type":"text","name":"State Identifier"}],"fax":"206-340-2267","ein_no":"00-1234568","description":"General Contractor","category":"Contractor","duns_no":"12-345-6780"},{"name":"Sample Construction API","id":"00000101-0001-0000-0000-000000000014","address":{"country":"US","state":null,"address3":null,"postal_code":"1111","county":null,"city":"Boston","address2":null,"address1":null},"url":"www.sampleconstructionapi.com","telephone":"206-340-2255","ctype":"Other","custom_fields":[{"value":"000-123-456","default_value":null,"possible_values":null,"display_type":"text","name":"State Identifier"}],"fax":"206-340-2266","ein_no":"00-1234567","description":"Engineer","category":"Contractor","duns_no":"12-345-6789"}]

    Access: FREE
    Return: JSON - Hash of companies
    Parameters:

        ticket : string - Authentication token
        no_http_status : string - (optional) If '1' result 200 will always be returned on failure with formatted error string.

        Parameters specific to this request:
            project_id : string - (optional) returns all companies associated with the project if given
    """
    url = _url('fieldapi/companies/v1')

    json = {
        'ticket': get_token(),
    }
    for key in kwargs:
        json[key] = kwargs[key]
    if project_id:
        json['project_id'] = project_id

    return requests.get(url, json=json)


def get_company(company_id, **kwargs):
    """  GET /fieldapi/companies/v1/:id

    Description: Retrieves a single company.

    Status Codes:
        200 OK Success.
        400 BAD REQUEST No company ID was passed in
        401 UNAUTHORIZED Authentication failed.
        404 NOT FOUND Could not find the company with the specified ID
        500 INTERNAL SERVER ERROR A general system error has occurred.

    Example Result:

        {"name":"Admin Company API","id":"00000101-0001-0000-0000-000000000013","address":{"country":"US","state":null,"address3":null,"postal_code":"1322","county":null,"city":"Waltham","address2":null,"address1":null},"url":"www.admincompanyapi.com","telephone":"206-340-2256","ctype":"Other","custom_fields":[{"value":null,"default_value":null,"possible_values":null,"display_type":"text","name":"State Identifier"}],"fax":"206-340-2267","ein_no":"00-1234568","description":"General Contractor","category":"Contractor","duns_no":"12-345-6780"}

    Access: FREE
    Return: JSON - Complete information about a single company including address and custom fields
    Parameters:

        ticket : string - Authentication token
        no_http_status : string - (optional) If '1' result 200 will always be returned on failure with formatted error string.

        Parameters specific to this request:
            id : string - The id of a company to retrieve details for
    """
    url = _url('fieldapi/companies/v1/{id}'.format(id=company_id))

    json = {
        'ticket': get_token(),
    }
    for key in kwargs:
        json[key] = kwargs[key]

    return requests.get(url, json=json)