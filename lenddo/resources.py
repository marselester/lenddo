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
        >>> verif.partner_id
        '1005489e7ec70ec34d9zp43l'

    :attribute partner_id: The Lenddo partner id.
    :attribute is_name_verified: Client name is compared with form data
        to social data. It can be `True` (passed), `False` (failed), or `None`.
    :attribute is_birthday_verified: Birthday is compared with form data
        to social data. It can be `True` (passed), `False` (failed), or `None`.
    :attribute is_phone_verified: Phone is compared with form data
        to social data. It can be `True` (passed), `False` (failed), or `None`.
    :attribute is_facebook_verified: Facebook verification is expressed as
        `True` (passed), `False` (failed), or `None` (required data
        was missing, so unable verify).

    """
    _api_path_single = '/ClientVerification/{client_id}'

    def __init__(self, client_id):
        self._client_id = client_id
        self._partner_id = None
        self._is_name_verified = None
        self._is_birthday_verified = None
        self._is_phone_verified = None
        self._is_facebook_verified = None

    def __repr__(self):
        return '<lenddo.Verification {}>'.format(self.client_id)

    @property
    def client_id(self):
        return self._client_id

    @property
    def partner_id(self):
        return self._partner_id

    @property
    def is_name_verified(self):
        return self._is_name_verified

    @property
    def is_birthday_verified(self):
        return self._is_birthday_verified

    @property
    def is_phone_verified(self):
        return self._is_phone_verified

    @property
    def is_facebook_verified(self):
        return self._is_facebook_verified

    def refresh_from(self, attrs):
        self._partner_id = attrs['partner_id']
        self._is_name_verified = attrs['verifications']['name']
        self._is_birthday_verified = attrs['verifications']['birthday']
        # `external_phone` key might not be set.
        self._is_phone_verified = attrs['verifications'].get('external_phone')
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
