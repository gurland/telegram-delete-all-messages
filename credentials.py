import json
import os


def _read_cache(cache_path):
    if not os.path.exists(cache_path):
        return {}

    try:
        with open(cache_path, 'r') as cache_file:
            cache = json.load(cache_file)
    except (json.JSONDecodeError, UnicodeDecodeError):
        # A legacy write may have been interrupted after API_HASH reached disk.
        # Overwrite the unreadable payload before requesting any credentials.
        _write_cache(cache_path, {})
        return {}

    if not isinstance(cache, dict):
        _write_cache(cache_path, {})
        return {}

    return cache


def _write_cache(cache_path, cache):
    with open(cache_path, 'w') as cache_file:
        json.dump(cache, cache_file)


def _write_api_id(cache_path, api_id):
    """Persist the non-secret API ID and discard legacy cached secrets."""
    _write_cache(cache_path, {'API_ID': api_id})


def load_api_credentials(cache_path):
    """Load credentials without ever persisting the secret API hash."""
    cache = _read_cache(cache_path)
    cached_api_id = cache.get('API_ID')

    # Versions before this migration stored API_HASH in plaintext. Remove it
    # before asking for any input so an interrupted run still cleans the cache.
    if cache and cache != {'API_ID': cached_api_id}:
        _write_api_id(cache_path, cached_api_id)

    api_id = os.getenv('API_ID') or cached_api_id
    if api_id is None:
        api_id = int(input('Enter your Telegram API id: '))

    api_hash = os.getenv('API_HASH') or input('Enter your Telegram API hash: ')

    if cached_api_id != api_id:
        _write_api_id(cache_path, api_id)

    return api_id, api_hash
