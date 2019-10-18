import pytest
from common_helper_extraction.fs import extract_fs
from common_helper_extraction.helper_fs import get_endianness

from .helper import get_binary_from_test_file


@pytest.mark.parametrize('test_file, expected_results, expected_offset, expected_length', [
    ('yaffs2_be.img', 1, 0, 14784),
    ('yaffs2_le.img', 1, 0, 14784),
    ('yaffs2_be_off.img', 1, 7, 14784),
    ('fs.sqfs', 1, 0, 401),
    ('test.ubifs', 1, 0, 1573376),
    ('combined_fs', 2, 11, 401)
])
def test_fs_extraction(test_file, expected_results, expected_offset, expected_length):
    result = extract_fs(get_binary_from_test_file(test_file))
    assert len(result) == expected_results
    assert result[0][0] == expected_offset
    assert len(result[0][1]) == expected_length


@pytest.mark.parametrize('size_field_buffer, size_field_type, data_length, expected', [
    (b'\x91\x01\x00\x00\x00\x00\x00\x00', 'Q', 4096, '<'),
    (b'\x00\x00\x01\x91', 'I', 4096, '>')
])
def test_get_endianness(size_field_buffer, size_field_type, data_length, expected):
    assert get_endianness(size_field_buffer, size_field_type, data_length) == expected
