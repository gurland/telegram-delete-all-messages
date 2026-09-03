import json
import os
import tempfile
import unittest
from unittest.mock import patch

from credentials import load_api_credentials


class CredentialCacheTests(unittest.TestCase):
    def test_removes_legacy_api_hash_from_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            cache_path = os.path.join(directory, 'cache')
            with open(cache_path, 'w') as cache_file:
                json.dump({'API_ID': 12345, 'API_HASH': 'legacy-secret'}, cache_file)

            with patch.dict(os.environ, {'API_HASH': 'environment-secret'}, clear=True):
                api_id, api_hash = load_api_credentials(cache_path)

            self.assertEqual(12345, api_id)
            self.assertEqual('environment-secret', api_hash)
            with open(cache_path, 'r') as cache_file:
                self.assertEqual({'API_ID': 12345}, json.load(cache_file))

    def test_prompted_api_hash_is_not_written_to_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            cache_path = os.path.join(directory, 'cache')

            with patch.dict(os.environ, {}, clear=True):
                with patch('builtins.input', side_effect=['12345', 'prompted-secret']):
                    api_id, api_hash = load_api_credentials(cache_path)

            self.assertEqual(12345, api_id)
            self.assertEqual('prompted-secret', api_hash)
            with open(cache_path, 'r') as cache_file:
                self.assertEqual({'API_ID': 12345}, json.load(cache_file))

    def test_removes_secret_from_truncated_legacy_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            cache_path = os.path.join(directory, 'cache')
            with open(cache_path, 'w') as cache_file:
                cache_file.write('{"API_ID": 12345, "API_HASH": "legacy-secret"')

            environment = {'API_ID': '67890', 'API_HASH': 'environment-secret'}
            with patch.dict(os.environ, environment, clear=True):
                api_id, api_hash = load_api_credentials(cache_path)

            self.assertEqual('67890', api_id)
            self.assertEqual('environment-secret', api_hash)
            with open(cache_path, 'r') as cache_file:
                persisted = cache_file.read()
            self.assertNotIn('legacy-secret', persisted)
            self.assertEqual({'API_ID': '67890'}, json.loads(persisted))


if __name__ == '__main__':
    unittest.main()
