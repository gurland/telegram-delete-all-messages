import io
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
        self.assertIn('using local ASCII versions instead', rendered)
        self.assertIn('##', rendered)
        self.assertIn('light background', rendered)
        self.assertIn('dark background', rendered)
        self.assertNotIn('tg://login', rendered)
        self.assertNotIn('sensitive-login-token', rendered)

    def test_ascii_stream_uses_fallback_before_characters_are_replaced(self):
        raw_output = io.BytesIO()
        ascii_output = io.TextIOWrapper(raw_output, encoding='ascii', errors='replace')

        with patch('sys.stdout', ascii_output):
            _print_qr(b'sensitive-login-token')
            ascii_output.flush()

        rendered = raw_output.getvalue().decode('ascii')
        self.assertIn('using local ASCII versions instead', rendered)
        self.assertNotIn('?', rendered)
        self.assertNotIn('tg://login', rendered)


if __name__ == '__main__':
    unittest.main()
