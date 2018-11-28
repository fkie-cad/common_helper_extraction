import pytest

from common_helper_extraction import cut_at_padding
from common_helper_extraction.padding import _find_next_data_block


@pytest.mark.parametrize('input_data, padding_min_length, padding_pattern, expected', [
    (b'no_padding', 1, b'\x00', [(0, b'no_padding')]),
    (b'before\x00after', 1, b'\x00', [(0, b'before'), (8, 'after')]),
    (b'before\x00\x00after', 1, b'\x00', [(0, b'before'), (9, 'after')]),
    (b'before\x00after', 2, b'\x00', [(0, b'before\x00after')]),
    (b'\xffafter', 1, b'\xff', [(1, 'after')])
])
def test_cut_at_padding(input_data, padding_min_length, padding_pattern, expected):
    result = cut_at_padding(input_data, padding_min_length=padding_min_length, padding_pattern=padding_pattern)
    assert isinstance(result, list)
    assert len(result) == len(expected)
    assert result == expected


@pytest.mark.parametrize('input_data, begin_of_padding, expected', [
    (b'before\x00after', 7, 8),
    (b'before\x00\x00after', 7, 9)
])
def test__find_next_data_block(input_data, begin_of_padding, expected):
    next_data_block_offset = _find_next_data_block(input_data, begin_of_padding, padding_pattern=b'\x00')
    assert next_data_block_offset == expected
