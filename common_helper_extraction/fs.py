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

SQFS_HEADERS = [b'sqsh', b'qshs', b'shsq', b'hsqs']


def extract_sqfs(input_data: bytes) -> list:
    sqfs_sections = list()
    for sqfs_magic in SQFS_HEADERS:
        sqfs_sections.extend(_get_sqfs_sections_with_magic(input_data, sqfs_magic))
    return sqfs_sections


def _get_sqfs_sections_with_magic(input_data: bytes, sqfs_magic: bytes) -> list:
    sqfs_sections = list()
    current_offset = _find_next_sqfs(input_data, 0, sqfs_magic)
    while current_offset < len(input_data):
        sqfs_end_offset = current_offset + _get_sqfs_size(input_data, current_offset)
        sqfs_sections.append((current_offset, input_data[current_offset:sqfs_end_offset]))
        current_offset = _find_next_sqfs(input_data, sqfs_end_offset, sqfs_magic)
    return sqfs_sections


def _find_next_sqfs(input_data: bytes, offset: int, header: bytes) -> int:
    try:
        return input_data.index(header, offset, len(input_data))
    except ValueError:
        logging.debug('no sqfs found')
        return len(input_data)


def _get_sqfs_size(input_data: bytes, offset: int) -> int:  # pylint: disable=unused-argument
    # ToDo: Implement this function
    return 100
