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
from struct import calcsize, unpack

SQFS_MAGIC_STRINGS = [b'sqsh', b'qshs', b'shsq', b'hsqs']
SQFS_SIZE_BUFFER_OFFSET = 0x28
SQFS_SIZE_BUFFER_TYPE = 'Q'


def extract_fs(input_data: bytes, magic_strings: list, size_buffer_offset: int, size_buffer_type: str) -> list:
    fs_sections = list()
    for fs_magic in magic_strings:
        fs_sections.extend(_get_fs_sections_with_magic(input_data, fs_magic, size_buffer_offset, size_buffer_type))
    return fs_sections


def extract_sqfs(input_data: bytes) -> list:
    return extract_fs(input_data, SQFS_MAGIC_STRINGS, SQFS_SIZE_BUFFER_OFFSET, SQFS_SIZE_BUFFER_TYPE)


def _get_fs_sections_with_magic(input_data: bytes, magic_string: bytes, buffer_offset: int, buffer_type: str) -> list:
    fs_sections = list()
    current_offset = _find_next_fs(input_data, 0, magic_string)
    while current_offset < len(input_data):
        fs_end_offset = current_offset + _get_fs_size(input_data[current_offset:], buffer_offset, buffer_type)
        fs_sections.append((current_offset, input_data[current_offset:fs_end_offset]))
        current_offset = _find_next_fs(input_data, fs_end_offset, magic_string)
    return fs_sections


def _find_next_fs(input_data: bytes, offset: int, header: bytes) -> int:
    try:
        return input_data.index(header, offset, len(input_data))
    except ValueError:
        logging.debug('no fs found')
        return len(input_data)


def _get_endianness(size_field_buffer: bytes, size_field_type: str, file_size: int) -> str:
    if unpack('<{}'.format(size_field_type), size_field_buffer)[0] < file_size:
        return '<'
    return '>'


def _get_fs_size(input_data: bytes, size_buffer_offset: int, size_buffer_type: str) -> int:
    size_field_buffer = input_data[size_buffer_offset:size_buffer_offset + calcsize(size_buffer_type)]
    endianness = _get_endianness(size_field_buffer, size_buffer_type, len(input_data))
    return unpack('{}{}'.format(endianness, size_buffer_type), size_field_buffer)[0]
