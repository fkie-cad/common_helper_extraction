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

from .helper_fs import get_index

HALF_NODE_SIZE = 2112
FULL_NODE_SIZE = 4224
NODE_SIZE_INDEX = 292


def extract_yaffs(input_data: bytes):
    yaffs_regex = b'\xff{2}[\x00-\x7f]{255}\xff{3}'
    offset, last_node = get_index(input_data, yaffs_regex)
    if (offset, last_node) == (None, None):
        return ()
    offset -= 8
    last_node += FULL_NODE_SIZE
    return [(offset, input_data[offset:last_node])]
