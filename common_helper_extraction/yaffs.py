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

from .helper_fs import NoMatchFoundException, find_first_and_last_fs_section

HALF_NODE_SIZE = 2112
FULL_NODE_SIZE = 4224
NODE_SIZE_INDEX = 292


def extract_yaffs(input_data: bytes) -> List[Tuple[int, bytes]]:
    yaffs_regex = b'\xff{2}[\x00-\x7f]{255}\xff{3}'
    try:
        offset, last_node = find_first_and_last_fs_section(input_data, yaffs_regex)
    except NoMatchFoundException:
        return []
    offset -= 8
    last_node += FULL_NODE_SIZE
    return [(offset, input_data[offset:last_node])]
