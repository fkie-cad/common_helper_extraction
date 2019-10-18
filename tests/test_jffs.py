from common_helper_extraction.jffs import extract_jffs

from .helper import get_binary_from_test_file


def test_extract_fs():
    result = extract_jffs(get_binary_from_test_file('jffs2_le.img'))
    assert result[0][0] == 0
    assert len(result[0][1]) == 612
