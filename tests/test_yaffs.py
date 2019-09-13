from common_helper_extraction.yaffs import Yaffs

from .helper import get_binary_from_test_file


def test_no_fs_found():
    yaffs_object = Yaffs()
    result = yaffs_object.get_fs_offset(get_binary_from_test_file('combined_fs'))
    assert result == -1


yaffs_object = Yaffs()


def test_first_header_offset():
    yaffs_object.get_fs_offset(get_binary_from_test_file('yaffs2_be_off.img'))
    assert yaffs_object._offset == 7


def test_is_yaffs_header():
    assert yaffs_object._is_yaffs_header() is True


def test_get_yaffs_first_object_type():
    assert yaffs_object._get_object_type(get_binary_from_test_file('yaffs2_be.img')) == 1


def test_get_yaffs_first_data_size():
    assert yaffs_object._get_data_size(get_binary_from_test_file('yaffs2_be.img')) == 62


def test_get_first_object_id():
    assert yaffs_object._get_object_id(get_binary_from_test_file('yaffs2_be.img')) == 1


def test_extract_fs():
    result = yaffs_object.extract_fs()
    assert result[0][0] == 7
    assert len(result[0][1]) == 14784


def test_get_first_data():
    assert yaffs_object._confirm_data(get_binary_from_test_file('yaffs2_be.img'), 1, 62) is True
