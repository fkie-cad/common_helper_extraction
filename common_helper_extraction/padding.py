'''
    common_helper_extraction
    Copyright (C) 2018  Fraunhofer FKIE

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


def cut_at_padding(input_data, padding_min_length=4, padding_pattern=b'\x00'):
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
        result.append((area_start, input_data[area_start:]))

    return result


def _find_next_data_block(input_data, begin_of_padding, padding_pattern):
    cursor = begin_of_padding + len(padding_pattern)
    while input_data[cursor:cursor + len(padding_pattern)] == padding_pattern:
        cursor += len(padding_pattern)
    return cursor
