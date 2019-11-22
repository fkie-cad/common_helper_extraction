import pytest
from common_helper_extraction.fs import extract_fs
from common_helper_extraction.helper_fs import get_data_size, get_endianness

from .helper import get_binary_from_test_file


@pytest.mark.parametrize('test_file, expected_offset, expected_length', [
    ('yaffs2_be.img', 0, 14784),
    ('yaffs2_le.img', 0, 14784),
    ('yaffs2_be_off.img', 7, 14784),
    ('fs.sqfs', 0, 401),
    ('test.ubifs', 0, 1573376),
    ('jffs2_le.img', 0, 612),
    ('jffs2_be.img', 0, 612),
])
def test_fs_extraction(test_file, expected_offset, expected_length):
    result = extract_fs(get_binary_from_test_file(test_file))
    assert len(result) == 1
    assert result[0][0] == expected_offset
    assert len(result[0][1]) == expected_length


def test_combined_file():
    result = extract_fs(get_binary_from_test_file('combined_fs'))
    assert result[0][0] == 11
    assert len(result[0][1]) == 401
    assert result[1][0] == 5000
    assert len(result[1][1]) == 14784


def test_get_node_size():
    test_bytes = b'\x19\x85\xff\xff\x00\x00\x00\x0c'
    result = get_data_size(test_bytes, 4, 'I')
    assert result == 12


@pytest.mark.parametrize('size_field_buffer, size_field_type, data_length, expected', [
    (b'\x91\x01\x00\x00\x00\x00\x00\x00', 'Q', 4096, '<'),
    (b'\x00\x00\x01\x91', 'I', 4096, '>')
])
def test_get_endianness(size_field_buffer, size_field_type, data_length, expected):
    assert get_endianness(size_field_buffer, size_field_type, data_length) == expected
