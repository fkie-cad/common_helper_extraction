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

from struct import unpack, error


class Ubifs:
    def __init__(self):
        pass

    def extract_fs(self, input_data: bytes):
        fs_sections = list()
        offset = self._get_offset(input_data)

    def _get_offset(self, input_data: bytes) -> int:
        offset = 0
        try:
            while not self._is_magic(input_data[offset:]):
                offset += 1
            return offset
        except error:
            return -1

    def _is_magic(self, input_data: bytes) -> bool:
        if unpack('<I', input_data[0:4])[0] == 101718065:
            return True
        else:
            return False

    def _get_node_size(self, input_data: bytes) -> int:
        return unpack('<I', input_data[16:20])[0]
