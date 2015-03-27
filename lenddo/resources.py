"""
lenddo.resources
~~~~~~~~~~~~~~~~

This module represents API resources.

"""
from .requestor import rest

__all__ = ('Verification',)


class Verification(object):
    """Represents a client verification.

    Usage example::

        >>> verif = Verification.retrieve(client_id='0123456789abcdef01234567')
        >>> verif.member_id
        '340a856163880f7661080e67'

    :attribute member_id: The Lenddo member id.
    :attribute partner_id: The Lenddo partner id.
    :attribute is_facebook_verified: Facebook verification is expressed as
        `True` (passed), `False` (failed), or `None` (required data
        was missing, so unable verify).

    """
    _api_path_single = '/ClientVerification/{client_id}'

    def __init__(self, client_id):
        self._client_id = client_id
        self._member_id = None
        self._partner_id = None
        self._is_facebook_verified = None

    def __repr__(self):
        return '<lenddo.Verification {}>'.format(self.client_id)

    @property
    def client_id(self):
        return self._client_id

    @property
    def member_id(self):
        return self._member_id

    @property
    def partner_id(self):
        return self._partner_id

    @property
    def is_facebook_verified(self):
        return self._is_facebook_verified

    def refresh_from(self, attrs):
        self._member_id = attrs['member_id']
        self._partner_id = attrs['partner_id']
        self._is_facebook_verified = attrs['verifications']['facebook_verified']

    def refresh(self):
        path = self._api_path_single.format(client_id=self.client_id)
        json_resp = rest('get', path)
        self.refresh_from(json_resp)

    @classmethod
    def construct_from(cls, attrs):
        user = cls(client_id=attrs.get('client_id'))
        user.refresh_from(attrs)
        return user

    @classmethod
    def retrieve(cls, client_id):
        user = cls(client_id)
        user.refresh()
        return user
