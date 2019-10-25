from common_helper_extraction.ubifs import extract_ubifs

from .helper import get_binary_from_test_file


def test_extract_fs():
    result = extract_ubifs(get_binary_from_test_file('test.ubifs'))
    assert result[0] == 0
    assert len(result[1]) == 1573376
