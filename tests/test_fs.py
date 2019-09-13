import pytest
from common_helper_extraction.fs import (
    SQFS_SIZE_BUFFER_OFFSET, SQFS_SIZE_BUFFER_TYPE, _get_endianness, _get_fs_size, extract_sqfs,
    _get_yaffs_data_size, _get_yaffs_header, _is_yaffs_header, _get_yaffs_object_id
)

from .helper import get_binary_from_test_file


def test_sqfs_extraction():
    result = extract_sqfs(get_binary_from_test_file('combined_fs'))
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0][0] == 11
    assert len(result[0][1]) == 401


def test_is_yaffs_header():
    result = _is_yaffs_header(get_binary_from_test_file('yaffs2_be.img'))
    assert result is True


def test_get_yaffs_header():
    test_data = get_binary_from_test_file('yaffs2_be.img')
    result = _get_yaffs_header(test_data, 0)
    assert result == 62


def test_get_yaffs_first_object_id():
    result = _get_yaffs_object_id(get_binary_from_test_file('yaffs2_be.img'))
    assert result == 1


def test_get_yaffs_first_data_size():
    test_data = get_binary_from_test_file('yaffs2_be.img')
    result = _get_yaffs_data_size(test_data)
    assert result == 62


def test_get_fs_size():
    test_data = get_binary_from_test_file('fs.sqfs')
    result = _get_fs_size(test_data, SQFS_SIZE_BUFFER_OFFSET, SQFS_SIZE_BUFFER_TYPE)
    assert result == 401


@pytest.mark.parametrize('size_field_buffer, size_field_type, data_length, expected', [
    (b'\x91\x01\x00\x00\x00\x00\x00\x00', 'Q', 4096, '<'),
    (b'\x00\x00\x01\x91', 'I', 4096, '>')
])
def test_get_endianness(size_field_buffer, size_field_type, data_length, expected):
    assert _get_endianness(size_field_buffer, size_field_type, data_length) == expected
