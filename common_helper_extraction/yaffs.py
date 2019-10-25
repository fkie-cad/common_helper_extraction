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
from struct import error

from .helper_fs import get_data_size, get_endianness, get_index


def extract_yaffs(input_data: bytes):
    yaffs_regex = b'\xff{2}[\x00-\x7f]{255}\xff{3}'
    fs_sections = list()
    offset, index = get_index(input_data, yaffs_regex)
    if (offset, index) == (None, None):
        return fs_sections
    offset -= 8
    fs_stream = input_data[offset:]
    byteorder = get_endianness(fs_stream[index + 292:index + 296], 'I', len(input_data))
    if get_data_size(fs_stream[index:], 0, 'I') == 1:
        index += get_chunk_size(byteorder, fs_stream, index)
    else:
        index += 2112
    fs_sections.extend([offset, fs_stream[:index]])
    return fs_sections


def get_chunk_size(byteorder, fs_stream, index):
    chunk = fs_stream[index:]
    node_size = get_data_size(chunk, 292, 'I', byteorder)
    object_id = get_data_size(chunk, 2054, 'I', byteorder)
    if confirm_data(chunk, object_id, node_size, byteorder):
        return 4224
    return 2112


def confirm_data(chunk: bytes, object_id: int, data_size: int, byteorder) -> bool:
    try:
        return (get_data_size(chunk, 4166, 'I', byteorder) == object_id) & \
               (get_data_size(chunk, 4174, 'I', byteorder) == data_size)
    except error:
        return False
