from .helper import get_binary_from_test_file
from common_helper_extraction.ubifs import Ubifs


def test_extract_fs():
    result = Ubifs().extract_fs(get_binary_from_test_file('test.ubifs'))
    assert result[0][0] == 0
    assert len(result[0][1]) == 1573376


def test_get_node_size():
    test_bytes = b'\x31\x18\x10\x06\x57\x51\xf7\xaa\x15\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00'
    result = Ubifs()._get_node_size(test_bytes)
    assert result == 4096
