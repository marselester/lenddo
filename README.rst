======
Lenddo
======

Lenddo is a Python API client for Lenddo.com.

Usage example:

.. code-block:: python

    import lenddo

    lenddo.conf.api_key = 'YOUR-KEY'
    lenddo.conf.api_secret = 'YOUR-SECRET'
    try:
        verif = lenddo.Verification.retrieve(client_id='0123456789abcdef01234567')
    except lenddo.LenddoException as exc:
        print(exc)
    else:
        print(verif.is_facebook_verified)

Tests
-----

.. code-block:: console

    $ pip install -r requirements.txt
    $ tox
