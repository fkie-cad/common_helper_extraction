import pytest
from common_helper_extraction.lzma import LZMA_HEADER, extract_lzma_streams


@pytest.mark.parametrize('input_data, expected', [
    (b'no_header', []),
    (LZMA_HEADER + b'content', [(0, LZMA_HEADER + b'content')]),
    (b'pre' + LZMA_HEADER + b'content', [(3, LZMA_HEADER + b'content')]),
    (b'pre' + LZMA_HEADER + b'content1' + LZMA_HEADER + b'content2', [(3, LZMA_HEADER + b'content1'), (24, LZMA_HEADER + b'content2')]),
])
def test_extract_lzma_streams(input_data, expected):
    assert extract_lzma_streams(input_data) == expected
