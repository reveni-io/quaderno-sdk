#!/usr/bin/env python


__version__ = '0.0.4'

import json
import requests


class QuadernoError(Exception):

    """
    Quaderno.io exception handling
    """

    def __init__(self, response=None):
        self.response = response
        self.code = response.status_code
        self.errors = None

        if response is not None:
            try:
                error = json.loads(response.content)
            except ValueError:
                self.message = 'Unknown Error'
            else:
                if 'errors' in error:
                    self.message = 'Validation Error'
                    self.errors = error['errors']
                else:
                    self.message = error.get('error', 'HTTP Error')

    def get_reatelimit(self):
        """
        https://github.com/quaderno/quaderno-api#rate-limiting
        """
        headers = self.response.headers

        return {
            'remaining': headers.get('x-ratelimit-remaining'),
            'reset': headers.get('x-ratelimit-reset')
        }

    def __str__(self):
        return "{self.code}.{self.message}".format(self=self)

    def __repr__(self):
        return str(self)


class Client(object):

    """
    A client for the Quaderno.io REST API.
    See https://quaderno.io/docs/ and
    https://github.com/quaderno/quaderno-api
    for complete API documentation.
    """

    user_agent = 'QuadernoSdk/api-rest-sdk:' + __version__

    def __init__(self, token, api_host, version=None, ctype='json'):

        self.token = token
        self.ctype = ctype
        self.version = version
        self.host = api_host

    @property
    def headers(self):
        headers = {
            'User-Agent': self.user_agent
        }
        if self.version:
            headers.update({
                'Accept': 'application/json; api_version={}'.format(
                    self.version)})
        return headers

    def request(self, url, method, headers=None, **kwargs):
        http_headers = self.headers
        http_headers.update(headers or {})

        response = requests.request(
            method, url,
            headers=http_headers,
            auth=(self.token, ''),
            **kwargs)

        if not (200 <= response.status_code < 300):
            raise QuadernoError(response)

        return response

    def _endpoint(self, action, method, **kwargs):
        return self.request(
            "{self.host}/api/{action}.{self.ctype}"
            .format(self=self, action=action), method, **kwargs)

    def get(self, action, params=None, **kwargs):
        kwargs.update(params or {})
        return self._endpoint(action, 'GET', params=kwargs)

    def post(self, action, json=None):
        return self._endpoint(action, 'POST', json=json)

    def put(self, action, json=None):
        return self._endpoint(action, 'PUT', json=json)

    def delete(self, action, **kwargs):
        return self._endpoint(action, 'DELETE', **kwargs)

    def ping(self):
        return self.get('ping')

    def contacts(self, params=None, **kwargs):
        """
        A contact is any client or vendor who appears
        on any of your invoices or expenses
        """
        return self.get('contacts', params=None, **kwargs)

    def post_contact(self, json):
        return self.post('contacts', json)

    def get_contact(self, id):
        return self.get("contacts/{0}".format(id))

    def put_contact(self, id, json):
        return self.put("contacts/{0}".format(id), json)

    def delete_contact(self, id):
        return self.delete("contacts/{0}".format(id))

    def invoices(self, params=None, **kwargs):
        """
        An invoice is a detailed list of goods shipped or services rendered,
        with an account of all costs
        """
        return self.get('invoices', params=None, **kwargs)

    def post_invoice(self, json):
        return self.post('invoices', json)

    def add_payment_to_invoice(self, id, json):
        """
        When an invoice is paid, you can record the payment.
        """
        return self.post("invoices/{0}/payments".format(id), json)

    def drop_payment_from_invoice(self, id, payment_id):
        return self.delete("invoices/{0}/payments/{1}".format(
            id, payment_id))

    def get_invoice(self, id):
        return self.get("invoices/{0}".format(id))

    def put_invoice(self, id, json):
        return self.put("invoices/{0}".format(id), json)

    def deliver_invoice(self, id):
        return self.get("invoices/{0}/deliver".format(id))

    def delete_invoice(self, id):
        return self.delete("invoices/{0}".format(id))

    def expenses(self, params=None, **kwargs):
        """
        Expenses are all the invoices that you receive from your vendors
        """
        return self.get('expenses', params=None, **kwargs)

    def post_expense(self, json):
        return self.post('expenses', json)

    def add_payment_to_expense(self, id, json):
        """
        When an invoice is paid, you can record the payment.
        """
        return self.post("expenses/{0}/payments".format(id), json)

    def drop_payment_from_expense(self, id, payment_id):
        return self.delete("expenses/{0}/payments/{1}".format(
            id, payment_id))

    def get_expense(self, id):
        return self.get("expenses/{0}".format(id))

    def put_expense(self, id, json):
        return self.put("expenses/{0}".format(id), json)

    def save_expense(self, id):
        return self.get("expenses/save".format(id))

    def delete_expense(self, id):
        return self.delete("expenses/{0}".format(id))

    def estimates(self, params=None, **kwargs):
        """
        An estimate is an offer that you give a client in order
        to get a specific job. With the time, estimates are usually
        turned into issued invoices.
        """
        return self.get('estimates', params=None, **kwargs)

    def post_estimate(self, json):
        return self.post('estimates', json)

    def get_estimate(self, id):
        return self.get("estimates/{0}".format(id))

    def put_estimate(self, id, json):
        return self.put("estimates/{0}".format(id), json)

    def deliver_estimate(self, id):
        return self.get("estimates/{0}/deliver".format(id))

    def delete_estimate(self, id):
        return self.delete("estimates/{0}".format(id))

    def credits(self, params=None, **kwargs):
        """
        An credit is a detailed list of goods shipped or services rendered,
        with an account of all costs.
        """
        return self.get('credits', params=None, **kwargs)

    def post_credit(self, json):
        return self.post('credits', json)

    def get_credit(self, id):
        return self.get("credits/{0}".format(id))

    def put_credit(self, id, json):
        return self.put("credits/{0}".format(id), json)

    def deliver_credit(self, id):
        return self.get("credits/{0}/deliver".format(id))

    def delete_credit(self, id):
        return self.delete("credits/{0}".format(id))

    def recurring(self, params=None, **kwargs):
        """
        A recurring is a special document that periodically renews itself
        and generating an recurring or an expense.
        """
        return self.get('recurring', params=None, **kwargs)

    def post_recurring(self, json):
        return self.post('recurring', json)

    def get_recurring(self, id):
        return self.get("recurring/{0}".format(id))

    def put_recurring(self, id, json):
        return self.put("recurring/{0}".format(id), json)

    def delete_recurring(self, id):
        return self.delete("recurring/{0}".format(id))

    def items(self, params=None, **kwargs):
        """
        The items are those products or services that you
        sell to your customers.
        """
        return self.get('items', params=None, **kwargs)

    def post_item(self, json):
        return self.post('items', json)

    def get_item(self, id):
        return self.get("items/{0}".format(id))

    def put_item(self, id, json):
        return self.put("items/{0}".format(id), json)

    def delete_item(self, id):
        return self.delete("items/{0}".format(id))

    def webhooks(self, params=None, **kwargs):
        """
        Quaderno Webhooks allows your aplication to receive information
        about document events as they occur.
        """
        return self.get('webhooks', params=None, **kwargs)

    def post_webhook(self, json):
        return self.post('webhooks', json)

    def get_webhook(self, id):
        return self.get("webhooks/{0}".format(id))

    def put_webhook(self, id, json):
        return self.put("webhooks/{0}".format(id), json)

    def delete_webhook(self, id):
        return self.delete("webhooks/{0}".format(id))

    def calculator(self, params=None, **kwargs):
        """
        Calculate the taxes applied for a given customer data
        """
        return self.get('tax_rates/calculate', params=None, **kwargs)
