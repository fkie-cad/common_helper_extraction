import pytest
from common_helper_extraction.yaffs import Yaffs

from .helper import get_binary_from_test_file


@pytest.mark.parametrize('test_file, expected_offset, expected_length', [
    ('yaffs2_le.img', 0, 14784),
    ('yaffs2_be.img', 0, 14784),
    ('yaffs2_be_off.img', 7, 14784),
    ('combined_fs', 5000, 14784),
])
def test_extract_fs(test_file, expected_offset, expected_length):
    result = Yaffs().extract_fs(get_binary_from_test_file(test_file))
    print(len(result))
    assert result[0][0] == expected_offset
    assert len(result[0][1]) == expected_length


def test_false_detection_in_ubi_fs():
    result = Yaffs().extract_fs(get_binary_from_test_file('test.git subifs'))
    assert not result


def test_fs_error():
    false_yaffs = Yaffs()
    false_yaffs.endianess = '<'
    result = false_yaffs.confirm_data(get_binary_from_test_file('fs.sqfs'), 0, 0)
    assert result is False


def test_get_first_offset():
    result = Yaffs().get_first_header(get_binary_from_test_file('combined_fs'))
    assert result == 5000
