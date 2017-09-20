__author__ = "Aileen Novero"
__date__ = "September 11, 2017"
__email__ = "novero.a@gmail.com"
__status__ = "Prototype"

import json

import requests


#
# ---------------------------------
#
# | Integration Exercise Write  UP |
#
# ---------------------------------
# :Instructions:
#       # Write a Python program to call the getguestcheck endpoint and retrieve guest check data.
#       # Transform that data using the mappings described below into new guest check data.
#       # Post your transformed data to setguestcheck. The server will validated your response
#       # and let you know how you did. Guest check data is sent and retrieved in JSON format and
#       # all calls require a username and password header to be set with the credentials provided
#       # below. All headers, fields, and values are case sensitive.
# Server URL: http://******
# Port: 12345
# :Credentials:
#       # username: ****
#       # password: ****
# :Endpoints:
#      # /getguestcheck/
#       # /setguestcheck/
# :Mappings:
#       # businessDate -> bizDate
#       # checks[] -> GCs[]
#       # checks > totalAmount -> GCs > totalAmnt
#       # checks > taxAmount -> GCs > tax
#       # checks > selections -> GCs > items
#       # checks > selections > displayName -> GCs > items > name
#       # checks > selections > price -> GCs > items > price
#       # checks > selections > quantity -> GCs > items > quantity


def makeRequest(server, port, request, username, password, payload=None):
    """
    Send a request to the given server, port. Authentication is required for endpoint requests.
    :param server: str : Server Url.
    :param port:   int : Assigned Port Number
    :param request: list : python list of type of request ('get', 'post') and the endpoint url (ie. '/getguestcheck/')
    :param username: str : username
    :param password: str : user password
    :param payload: json object | dictionary : dictionary or json object to be sent as post payload. default : None
    :return:
        for endpoints:
            if get request: get response object
            if post request: post response text
        else: returns server status; response text
    """
    try:
        url = '{0}:{1}{2}'.format(server, str(port), request[-1])
        headers = {'content-type': 'application/json', 'username': username, 'password': password}

        if request[0] == 'get':
            r = requests.get(url, headers=headers)
            d = r.json()
            return d
        if request[0] == 'post':
            r = requests.post(url, headers=headers, data=json.dumps(payload))
            d = r.text
            return d
    except:
        url = '{0}:{1}'.format(server, str(port))
        headers = {'content-type': 'application/json', 'username': username, 'password': password}
        r = requests.get(url, headers=headers)
        return 'Check Status:', r.text


def updateDictionary(mydict):
    """
    Updates the keys of the given mydict python dictionary where keys match the given keyMap dictionary.
    :param mydict: dictionary : The original dictionary instance, json response object.
    :return: mydict instance with keys updated.
    """

    newKeys = {'businessDate': 'bizDate',
               'checks': 'GCs',
               'totalAmount': 'totalAmnt',
               'taxAmount': 'tax',
               'selections': 'items',
               'displayName': 'name',
               'price': 'price',
               'quantity': 'quantity'
               }

    def updateKeys(oldDict, keyMap):
        """
        upDateKeys recursively updates the keys of the given oldDict python dictionary instance
        when a key matches the a key in the given keyMap python dictionary. The new value is the
        keyMap value.
        * Note of warning, if the dictionary is nested, with a uplicated key in the nested dictionary both
        instances of the key will be updated.  Yet, in good practice, keys should not be duplicated.
        :param oldDict: dictionary : The original dictionary instance
        :param keyMap:  dictionary : key:value pairs of 'oldkey' : 'newkey'
        :return: oldDictionary returned with key names updated according to the given keyMap.
        """

        for k, v in keyMap.iteritems():
            if oldDict.get(k):
                if isinstance(oldDict[k], list):
                    # One needs to first check if the old dictionary entry is type(list)
                    # ie. dictionary['checks'] = [] ; dictionary['checks'][0]['selections'] = []
                    # If so, one must recursively check and update those key value pairs as well.
                    updateKeys(oldDict[k][0], keyMap)
                # Now update the original dictionary.
                oldDict[v] = oldDict.pop(k)

    updateKeys(mydict, newKeys)

    return mydict


#
if __name__ == '__main__':
    # Parameters as assigned by CrunchTime on Monday September 11, 2017.

    server = "http://****"
    port = 12345
    get_request = ['get', "/getguestcheck/"]
    set_request = ['post', "/setguestcheck/"]
    no_request = []
    username = '******'
    password = '******'

    # Make the initial get request
    responseJson = makeRequest(server, port, get_request, username, password)

    # Update the response object
    updateDictionary(responseJson)

    # Make the post request
    print makeRequest(server, port, set_request, username, password, responseJson)

    # To check status:
    # print makeRequest(server, port, no_request, username, password)
