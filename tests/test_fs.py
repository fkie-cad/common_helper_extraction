from common_helper_extraction.fs import extract_sqfs

from .helper import get_binary_from_test_file


def test_sqfs_extraction():
    result = extract_sqfs(get_binary_from_test_file('combined_fs'))
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0][0] == 11
