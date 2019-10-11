from .helper import get_binary_from_test_file
from common_helper_extraction.ubifs import Ubifs


def test_extract_fs():
    result = Ubifs().extract_fs(get_binary_from_test_file('test.ubifs'))
    assert result[0][0] == 0
    assert len(result[0][1]) == 1573376


def test_magic():
    test_bytes = b'\x31\x18\x10\x06'
    result = Ubifs()._is_magic(test_bytes)
    assert result is True


def test_magic_false():
    test_bytes = b'\xFF\x18\x10\x06'
    result = Ubifs()._is_magic(test_bytes)
    assert result is False


def test_deffect_offset():
    test_bytes = b'\xFF\x18\x10\x06'
    result = Ubifs()._get_offset(test_bytes)
    assert result == -1


def test_get_offset():
    test_bytes = b'\xFF\xFF\xFF\x31\x18\x10\x06'
    result = Ubifs()._get_offset(test_bytes)
    assert result == 3


def test_get_node_size():
    test_bytes = b'\x31\x18\x10\x06\x57\x51\xf7\xaa\x15\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00'
    result = Ubifs()._get_node_size(test_bytes)
    assert result == 4096
