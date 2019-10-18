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


def extract_ubifs(input_data: bytes) -> list:
    ubifs_regex = b'\x31\x18\x10\x06'
    fs_sections = list()
    offset, index = get_index(input_data, ubifs_regex)
    if (offset, index) == (None, None):
        return fs_sections
    additional_fill = get_data_size(input_data[index + offset:], 24)
    index += get_data_size(input_data[index + offset:], 16) + additional_fill
    fs_sections.append([offset, input_data[offset:index]])
    return fs_sections
