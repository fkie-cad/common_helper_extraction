'''
    common_helper_extraction
    Copyright (C) 2018-2019  Fraunhofer FKIE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


def get_padding_seperated_sections(raw_binary: bytes, padding_min_length: int = 16, padding_pattern: bytes = b'\xff') -> list:
    data_sections = cut_at_padding(raw_binary, padding_min_length=padding_min_length, padding_pattern=padding_pattern)
    if len(data_sections) == 1 and data_sections[0][0] == 0 and len(data_sections[0][1]) == len(raw_binary):  # data_section == raw_binary
        return []
    return data_sections


def cut_at_padding(input_data: bytes, padding_min_length: int = 4, padding_pattern: bytes = b'\x00') -> list:
    fast_search_pattern = padding_min_length * padding_pattern
    area_start = 0
    area_end = 0
    result = list()
    try:
        while area_end < len(input_data):
            area_end = input_data.index(fast_search_pattern, area_start, len(input_data))
            if not area_start == area_end:
                result.append((area_start, input_data[area_start:area_end]))
            area_start = _find_next_data_block(input_data, area_end, padding_pattern)
    except ValueError:
        if area_start < len(input_data):
            result.append((area_start, input_data[area_start:]))

    return result


def _find_next_data_block(input_data: bytes, begin_of_padding: int, padding_pattern: bytes) -> int:
    cursor = begin_of_padding + len(padding_pattern)
    while input_data[cursor:cursor + len(padding_pattern)] == padding_pattern:
        cursor += len(padding_pattern)
    return cursor
