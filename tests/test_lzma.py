import pytest
from common_helper_extraction.lzma import LZMA_HEADER, extract_lzma_streams,\
    _decompress_lzma_stream, get_decompressed_lzma_streams
from helpers.stream_generator import generate_lzma_stream

VALID_LZMA_STREAM = generate_lzma_stream(b'test')
LZMA_STREAM_WITH_ADDITIONAL_DATA = generate_lzma_stream(b'test with additional data') + b'some useless data at the end'
CORRUPTED_STREAM = LZMA_HEADER + b'useless_content'


@pytest.mark.parametrize('input_data, expected', [
    (b'no_header', []),
    (LZMA_HEADER + b'content', [(0, LZMA_HEADER + b'content')]),
    (b'pre' + LZMA_HEADER + b'content', [(3, LZMA_HEADER + b'content')]),
    (b'pre' + LZMA_HEADER + b'content1' + LZMA_HEADER + b'content2', [(3, LZMA_HEADER + b'content1'), (24, LZMA_HEADER + b'content2')]),
])
def test_extract_lzma_streams(input_data, expected):
    assert extract_lzma_streams(input_data) == expected


@pytest.mark.parametrize('input_data, expected', [
    ([], []),
    ([(0, VALID_LZMA_STREAM)], [(0, b'test')]),
    ([(0, VALID_LZMA_STREAM), (100, LZMA_STREAM_WITH_ADDITIONAL_DATA)], [(0, b'test'), (100, b'test with additional data')]),
])
def test_get_decompressed_lzma_streams(input_data, expected):
    assert get_decompressed_lzma_streams(input_data) == expected


@pytest.mark.parametrize('input_data, expected', [
    (VALID_LZMA_STREAM, b'test'),
    (LZMA_STREAM_WITH_ADDITIONAL_DATA, b'test with additional data'),
    (CORRUPTED_STREAM, b'ERROR: lzma decompression failed: Corrupt input data')
])
def test_decompress_lzma_stream(input_data, expected):
    assert _decompress_lzma_stream(input_data) == expected
