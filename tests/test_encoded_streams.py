from pathlib import Path

from common_helper_files import get_binary_from_file

import pytest
from common_helper_extraction.encoded_streams import (
    ASCII85_ADOBE_REGEX, INTEL_HEX_REGEX, SRECORD_REGEX, TEKTRONIX_EXT_REGEX, TEKTRONIX_REGEX, extract_encoded_streams
)


@pytest.mark.parametrize('input_stream, regex, expected', [
    (b'abcd', b'not_included', []),
    (b'abcbc', b'bc', [(1, b'bc'), (3, b'bc')]),
    (b'abcdefgcd', b'[a-c]{2,}(d)', [(0, b'abcd')])
])
def test_extraction_function(input_stream, regex, expected):
    result = extract_encoded_streams(input_stream, regex)
    assert result == expected


@pytest.mark.parametrize('test_file, regex, expected_offset, expected_size', [
    ('hello_fact_user.ihex', INTEL_HEX_REGEX, 0, 10508),
    ('combined_test_file', INTEL_HEX_REGEX, 6, 10508),
    ('hello_fact_user.srec', SRECORD_REGEX, 0, 10760),
    ('combined_test_file', SRECORD_REGEX, 10527, 10760),
    ('testfile.tek', TEKTRONIX_REGEX, 0, 185),
    ('hello_fact_user.tekext', TEKTRONIX_EXT_REGEX, 0, 9329),
    ('hello_fact_user.tekext_sec', TEKTRONIX_EXT_REGEX, 0, 8819),
    ('hello_fact_user.asc85', ASCII85_ADOBE_REGEX, 0, 3814)
])
def test_extraction(test_file, regex, expected_offset, expected_size):
    raw_input = get_binary_from_file(_get_test_file(test_file))
    result = extract_encoded_streams(raw_input, regex)
    assert len(result) == 1
    assert result[0][0] == expected_offset
    assert len(result[0][1]) == expected_size


def _get_test_file(file_name: str) -> Path:
    test_dir = Path(Path(__file__).parent, 'data')
    return Path(test_dir, file_name)