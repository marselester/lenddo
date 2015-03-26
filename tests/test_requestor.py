import unittest

from requests import Request
from lenddo.requestor import HmacAuth

API_KEY = 'be22ce0b9875611d10606e1a'
API_SECRET = '$2a$10$Ik0yU.RmEsI8Pr1lLVgTn.SPdFIA2tcoy/frKl3rUcTVD5GvYimli'
MEMBER_URL = 'https://scoreservice.lenddo.com/Members/0123456789abcdef01234567'
MEMBERS_URL = 'https://scoreservice.lenddo.com/Members'
DATE = 'Mon Jan 01 HH:MM:SS GMT 2013'


class HmacAuthStrToSignTest(unittest.TestCase):
    def setUp(self):
        self.hmac = HmacAuth(API_KEY, API_SECRET)

    def test_http_get_method(self):
        r = Request('get', MEMBER_URL).prepare()
        str_ = self.hmac.str_to_sign(r, DATE)
        expected_str = (
            b'GET\n'
            b'\n'
            b'Mon Jan 01 HH:MM:SS GMT 2013\n'
            b'/Members/0123456789abcdef01234567'
        )
        self.assertEqual(str_, expected_str)

    def test_http_post_method(self):
        r = Request('post', MEMBERS_URL, data='hello').prepare()
        str_ = self.hmac.str_to_sign(r, DATE)
        expected_str = (
            b'POST\n'
            b'5d41402abc4b2a76b9719d911017c592\n'
            b'Mon Jan 01 HH:MM:SS GMT 2013\n'
            b'/Members'
        )
        self.assertEqual(str_, expected_str)

    def test_http_put_method(self):
        r = Request('put', MEMBER_URL, data='hello').prepare()
        str_ = self.hmac.str_to_sign(r, DATE)
        expected_str = (
            b'PUT\n'
            b'5d41402abc4b2a76b9719d911017c592\n'
            b'Mon Jan 01 HH:MM:SS GMT 2013\n'
            b'/Members/0123456789abcdef01234567'
        )
        self.assertEqual(str_, expected_str)


class HmacAuthSignatureTest(unittest.TestCase):
    def setUp(self):
        self.hmac = HmacAuth(API_KEY, API_SECRET)

    def test_http_get_method(self):
        str_to_sign = (
            b'GET\n'
            b'\n'
            b'Mon Jan 01 HH:MM:SS GMT 2013\n'
            b'/Members/0123456789abcdef01234567'
        )
        expected_signature = b'l6PxyV73V226B2XvaBsoWaE++Fo='
        signature = self.hmac.signature(str_to_sign)
        self.assertEqual(signature, expected_signature)

    def test_http_post_method(self):
        str_to_sign = (
            b'POST\n'
            b'e9d263d07a1533984e80ef808bd4efff\n'
            b'Mon Jan 01 HH:MM:SS GMT 2013\n'
            b'/Members'
        )
        expected_signature = b'FnSfYYxU+RTJnSr/48yLYgk1eQ0='
        signature = self.hmac.signature(str_to_sign)
        self.assertEqual(signature, expected_signature)

    def test_http_put_method(self):
        str_to_sign = (
            b'PUT\n'
            b'96db961798e74718065e7a06d6d14110\n'
            b'Mon Jan 01 HH:MM:SS GMT 2013\n'
            b'/Members/0123456789abcdef01234567'
        )
        expected_signature = b'ahByLYh9Wc3yh1F+N9iLFA7B12w='
        signature = self.hmac.signature(str_to_sign)
        self.assertEqual(signature, expected_signature)
