import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from qrcode import QRCode

from qr_auth import _print_qr


class SafeQrFallbackTests(unittest.TestCase):
    def test_unicode_failure_uses_local_ascii_qr_without_exposing_token(self):
        output = StringIO()
        unicode_error = UnicodeEncodeError('ascii', 'x', 0, 1, 'unsupported')

        with patch.object(QRCode, 'print_ascii', side_effect=unicode_error):
            with redirect_stdout(output):
                _print_qr(b'sensitive-login-token')

        rendered = output.getvalue()
        self.assertIn('using a local ASCII version instead', rendered)
        self.assertIn('##', rendered)
        self.assertNotIn('tg://login', rendered)
        self.assertNotIn('sensitive-login-token', rendered)


if __name__ == '__main__':
    unittest.main()
