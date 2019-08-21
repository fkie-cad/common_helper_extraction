import pytest
from common_helper_extraction.padding import _find_next_data_block, cut_at_padding, get_padding_seperated_sections


@pytest.mark.parametrize('input_data, padding_min_length, padding_pattern, expected', [
    (b'no_padding', 1, b'\x00', [(0, b'no_padding')]),
    (b'before\x00after', 1, b'\x00', [(0, b'before'), (7, b'after')]),
    (b'before\x00\x00after', 1, b'\x00', [(0, b'before'), (8, b'after')]),
    (b'before\x00\x00middle\x00after', 1, b'\x00', [(0, b'before'), (8, b'middle'), (15, b'after')]),
    (b'before\x00after', 2, b'\x00', [(0, b'before\x00after')]),
    (b'\xffafter', 1, b'\xff', [(1, b'after')]),
    (b'before\x00', 1, b'\x00', [(0, b'before')]),
    (b'\x00\xff\x00\xffmiddle\x00\xffafter', 1, b'\x00\xff', [(4, b'middle'), (12, b'after')]),
])
def test_cut_at_padding(input_data, padding_min_length, padding_pattern, expected):
    result = cut_at_padding(input_data, padding_min_length=padding_min_length, padding_pattern=padding_pattern)
    assert isinstance(result, list)
    assert len(result) == len(expected)
    assert result == expected


@pytest.mark.parametrize('input_data, padding_min_length, padding_pattern, expected', [
    (b'no_padding', 1, b'\x00', []),
    (b'before\x00after', 1, b'\x00', [(0, b'before'), (7, b'after')])
])
def test_get_padded_sections(input_data, padding_min_length, padding_pattern, expected):
    result = get_padding_seperated_sections(input_data, padding_min_length=padding_min_length, padding_pattern=padding_pattern)
    assert len(result) == len(expected)
    assert result == expected


@pytest.mark.parametrize('input_data, begin_of_padding, expected', [
    (b'before\x00after', 7, 8),
    (b'before\x00\x00\x00after', 7, 9),
    (b'before\x00\x00\x00', 7, 9)
])
def test__find_next_data_block(input_data, begin_of_padding, expected):
    next_data_block_offset = _find_next_data_block(input_data, begin_of_padding, padding_pattern=b'\x00')
    assert next_data_block_offset == expected
