Quaderno.io Python Sdk
======================

`Quaderno.io`_, centralizes different payment streams and automatically issues beautiful receipts. Invoicing and tax handling on autopilot.

Installation
------------

To install quaderno-sdk, simply:

.. code:: sh

    $ pip install git+https://github.com/aplazame/quaderno-sdk.git

Usage
-----

.. code:: python

    >>> import quaderno_sdk
    >>> client = quaderno_sdk.Client('api_key', 'account_name')
    >>> r = client.invoices()
    >>> r.json()
    [
      ...
    ]
    >>> r.status_code
    200

Exceptions
----------

.. code:: python

    >>> try:
    ...     client.invoices()
    ... except quaderno_sdk.QuadernoError as e:
    ...     print e.status_code, e.get_reatelimit()
    503 {'remaining': 0, 'reset': 10}


Documentation
-------------

Documentation is available at `https://quaderno.io/docs/`_

.. _Quaderno.io: https://quaderno.io
.. _https://quaderno.io/docs/: https://quaderno.io/docs/
