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

import logging
import re
from struct import unpack

BUFFER_SIZE = {'I': 4, 'Q': 8}


def get_data_size(input_data: bytes, offset: int, size_buffer_type: str, byteorder: str = None) -> int:
    if not byteorder:
        byteorder = get_endianness(input_data[offset:offset + BUFFER_SIZE[size_buffer_type]], size_buffer_type, len(input_data))
    return unpack('{}I'.format(byteorder), input_data[offset:offset + 4])[0]


def get_endianness(size_field_buffer: bytes, size_field_type: str, file_size: int) -> str:
    if unpack('<{}'.format(size_field_type), size_field_buffer)[0] < file_size:
        return '<'
    return '>'


def get_index(input_data: bytes, regex: bytes) -> (int, int):
    first_match = re.search(regex, input_data)
    if first_match is None:
        return None, None
    offset = first_match.start(0)
    fs_stream = input_data[offset:]
    index = [(m.start(0)) for m in re.finditer(regex, fs_stream)][-1]
    return offset, index


def get_fs_sections_with_magic(input_data: bytes, magic_string: bytes, buffer_offset: int, buffer_type: str) -> list:
    fs_sections = list()
    current_offset = _find_next_fs(input_data, 0, magic_string)
    while current_offset < len(input_data):
        fs_end_offset = current_offset + get_data_size(input_data[current_offset:], buffer_offset, buffer_type)
        fs_sections.extend((current_offset, input_data[current_offset:fs_end_offset]))
        current_offset = _find_next_fs(input_data, fs_end_offset, magic_string)
    return fs_sections


def _find_next_fs(input_data: bytes, offset: int, header: bytes) -> int:
    try:
        return input_data.index(header, offset, len(input_data))
    except ValueError:
        logging.debug('no fs found')
        return len(input_data)
