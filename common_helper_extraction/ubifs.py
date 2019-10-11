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
import re


class Ubifs:
    def __init__(self):
        pass

    def extract_fs(self, input_data: bytes) -> list:
        fs_sections = list()
        offset = self._get_offset(input_data)
        fs_stream = input_data[offset:]
        index = [(m.start(0)) for m in re.finditer(b'\x31\x18\x10\x06', fs_stream)][-1]
        additional_fill = self._get_node_size(fs_stream[index + 8:])
        index += self._get_node_size(fs_stream[index:]) + additional_fill
        fs_sections.append([offset, fs_stream[:index]])
        return fs_sections

    def _get_offset(self, input_data: bytes, mode: int = 1) -> int:
        offset = 0
        try:
            while not self._is_magic(input_data[offset:]):
                offset += mode
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
