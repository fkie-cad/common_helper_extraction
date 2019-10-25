import pytest
from common_helper_extraction.yaffs import extract_yaffs

from .helper import get_binary_from_test_file


@pytest.mark.parametrize('test_file, expected_offset, expected_length', [
    ('yaffs2_le.img', 0, 14784),
    ('yaffs2_be.img', 0, 14784),
    ('yaffs2_be_off.img', 7, 14784),
    ('yaffs2_be_def.img', 7, 12672),
    ('combined_fs', 5000, 14784),
    ('yaffs2_mini.img', 7, 297)
])
def test_extract_fs(test_file, expected_offset, expected_length):
    result = extract_yaffs(get_binary_from_test_file(test_file))
    assert result[0] == expected_offset
    assert len(result[1]) == expected_length


def test_false_detection_in_ubi_fs():
    result = extract_yaffs(get_binary_from_test_file('test.git subifs'))
    assert not result
