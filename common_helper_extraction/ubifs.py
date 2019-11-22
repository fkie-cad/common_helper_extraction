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
from typing import List, Tuple

from .helper_fs import NoMatchFoundException, find_first_and_last_fs_section, get_data_size


def extract_ubifs(input_data: bytes) -> List[Tuple[int, bytes]]:
    ubifs_regex = b'\x31\x18\x10\x06'
    try:
        offset, last_node = find_first_and_last_fs_section(input_data, ubifs_regex)
    except NoMatchFoundException:
        return []
    additional_fill = get_data_size(input_data[last_node:], 24, 'I')
    last_node += get_data_size(input_data[last_node:], 16, 'I') + additional_fill
    return [(offset, input_data[offset:last_node])]
