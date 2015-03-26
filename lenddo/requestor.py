"""
lenddo.requestor
~~~~~~~~~~~~~~~~

This module provides REST request abstraction layer.

"""
import hmac
import hashlib
import base64
from datetime import datetime

from dateutil.tz import tzutc
import requests
import six
if six.PY3:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin

from . import conf
from .exceptions import (
    APIConnectionError, APIError, AuthError, InvalidRequestError
)

session = requests.Session()


def rest(method, path, query_params=None, data=None):
    """Makes JSON API request and returns response as dictionary.

    Usage example::

        >>> rest('get', 'Members')

    """
    try:
        resp = session.request(
            method=method,
            url=_api_url(path),
            params=query_params,
            json=data,
            auth=HmacAuth(conf.api_key, conf.api_secret)
        )
    except requests.RequestException as exc:
        raise APIConnectionError(exc)

    try:
        json_resp = resp.json()
    except ValueError as exc:
        raise APIError(exc, resp.content, resp.status_code)

    if resp.status_code in (200, 201):
        return json_resp

    error_msg = json_resp.get('message')
    if resp.status_code in (401, 403):
        raise AuthError(error_msg, resp.content, resp.status_code)
    if resp.status_code in (400, 404):
        raise InvalidRequestError(error_msg, resp.content, resp.status_code)
    raise APIError(error_msg, resp.content, resp.status_code)


def _api_url(path):
    path = path.lstrip('/')
    return urljoin(conf.api_base, path)


class HmacAuth(requests.auth.AuthBase):
    """HMAC authentication.

    https://partners.lenddo.com/documentation/rest_api

    """
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def __call__(self, r):
        date = self.date()
        signature = self.signature(self.str_to_sign(r, date))
        auth_header = 'LENDDO {}:{}'.format(self.api_key, signature)
        r.headers['Date'] = date
        r.headers['Authorization'] = auth_header
        return r

    def date(self):
        now = datetime.now(tzutc())
        return now.strftime('%a %b %d %H:%M:%S %Z %Y')

    def signature(self, str_to_sign):
        hmac_digest = hmac.new(
            self.api_secret.encode('utf-8'),
            str_to_sign,
            hashlib.sha1
        ).digest()
        return base64.b64encode(hmac_digest)

    def str_to_sign(self, r, date):
        if r.body:
            body_md5 = hashlib.md5(r.body.encode('utf-8')).hexdigest()
        else:
            body_md5 = ''
        hmac_message = '\n'.join([r.method, body_md5, date, r.path_url])
        return hmac_message.encode('utf-8')
