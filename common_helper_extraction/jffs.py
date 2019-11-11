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


from .helper_fs import get_data_size, get_index


def extract_jffs(input_data: bytes) -> list:
    jffs_regex = b'(\x85\x19)|(\x19\x85)'
    fs_sections = list()
    offset, last_node = get_index(input_data, jffs_regex)
    if (offset, last_node) == (None, None):
        return fs_sections
    last_node += get_data_size(input_data[last_node + offset:], 4, 'I', )
    fs_sections.extend([offset, input_data[offset:last_node]])
    return fs_sections
