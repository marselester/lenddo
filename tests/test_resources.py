import unittest

from lenddo import Verification
from .utils import json_from_file


class VerificationConstructFromTest(unittest.TestCase):
    def setUp(self):
        self._json = json_from_file('verification.json')

    def test_client_id_is_expected_string(self):
        verif = Verification.construct_from(self._json)
        expected_client_id = '0123456789abcdef01234567'
        self.assertEqual(verif.client_id, expected_client_id)

    def test_partner_id_is_expected_string(self):
        verif = Verification.construct_from(self._json)
        expected_partner_id = '1005489e7ec70ec34d9zp43l'
        self.assertEqual(verif.partner_id, expected_partner_id)

    def test_is_name_verified_is_true(self):
        verif = Verification.construct_from(self._json)
        self.assertTrue(verif.is_name_verified)

    def test_is_birthday_verified_is_true(self):
        verif = Verification.construct_from(self._json)
        self.assertTrue(verif.is_birthday_verified)

    def test_is_phone_verified_is_none(self):
        verif = Verification.construct_from(self._json)
        self.assertIsNone(verif.is_phone_verified)

    def test_is_facebook_verified_is_true(self):
        verif = Verification.construct_from(self._json)
        self.assertTrue(verif.is_facebook_verified)
