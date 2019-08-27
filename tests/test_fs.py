import pytest
from common_helper_extraction.fs import (
    SQFS_SIZE_BUFFER_OFFSET, SQFS_SIZE_BUFFER_TYPE, _get_endiness, _get_fs_size, extract_sqfs
)

from .helper import get_binary_from_test_file


def test_sqfs_extraction():
    result = extract_sqfs(get_binary_from_test_file('combined_fs'))
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0][0] == 11
    assert len(result[0][1]) == 401


def test_get_fs_size():
    test_data = get_binary_from_test_file('fs.sqfs')
    result = _get_fs_size(test_data, SQFS_SIZE_BUFFER_OFFSET, SQFS_SIZE_BUFFER_TYPE)
    assert result == 401


@pytest.mark.parametrize('size_field_buffer, size_field_type, data_length, expected', [
    (b'\x91\x01\x00\x00\x00\x00\x00\x00', 'Q', 4096, '<'),
    (b'\x00\x00\x01\x91', 'I', 4096, '>')
])
def test_get_endiness(size_field_buffer, size_field_type, data_length, expected):
    assert _get_endiness(size_field_buffer, size_field_type, data_length) == expected
