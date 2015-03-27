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

    def test_member_id_is_expected_string(self):
        verif = Verification.construct_from(self._json)
        expected_member_id = '340a856163880f7661080e67'
        self.assertEqual(verif.member_id, expected_member_id)

    def test_partner_id_is_expected_string(self):
        verif = Verification.construct_from(self._json)
        expected_partner_id = '1005489e7ec70ec34d9zp43l'
        self.assertEqual(verif.partner_id, expected_partner_id)

    def test_is_facebook_verified_is_true(self):
        verif = Verification.construct_from(self._json)
        self.assertTrue(verif.is_facebook_verified)
