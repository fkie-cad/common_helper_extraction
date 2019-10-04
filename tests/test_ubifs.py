from .helper import get_binary_from_test_file
from common_helper_extraction.ubifs import Ubifs


def test_extract_fs():
    result = Ubifs().extract_fs(get_binary_from_test_file('test.ubifs'))
    assert result is None


def test_magic():
    test_bytes = b'\x31\x18\x10\x06'
    result = Ubifs()._is_magic(test_bytes)
    assert result is True
