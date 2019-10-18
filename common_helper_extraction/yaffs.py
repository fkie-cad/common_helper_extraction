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
import re
from struct import error, unpack

from common_helper_extraction.helper_fs import get_endianness


class Yaffs:
    def __init__(self):
        self._input_data = None
        self._number_of_objects = 0
        self.endianess = None
        self._offset = None

    def extract_fs(self, input_data: bytes):
        fs_sections = list()
        self._input_data = input_data
        if self.set_fs_offset() == -1:
            return fs_sections
        self.endianess = get_endianness(self._input_data[0:4], 'I', len(input_data))
        index = 0
        while index < len(self._input_data):
            index += self.get_next_index(index)
        fs_sections.append([self._offset, self._input_data[:index]])
        return fs_sections

    def get_next_index(self, index: int) -> int:
        chunk = self._input_data[index:]
        if self.get_object_type(chunk) == 1:
            if self.confirm_data(chunk, self.get_object_id(chunk), self.get_data_size(chunk)):
                index += 4224
        else:
            index += 2112
        return index

    def set_fs_offset(self) -> int:
        self._offset = self.get_first_header(self._input_data)
        if self._offset == -1:
            return -1
        self._input_data = self._input_data[self._offset:]
        return 0

    @staticmethod
    def get_first_header(input_data: bytes) -> int:
        first_match = re.search(b'\xff{2}[\x00-\x7f]{255}\xff{3}', input_data)
        if first_match is None:
            return -1
        return first_match.start(0) - 8

    def get_object_type(self, chunk: bytes) -> int:
        return unpack('{}{}'.format(self.endianess, 'I'), chunk[0:4])[0]

    def confirm_data(self, chunk: bytes, object_id: int, data_size: int) -> bool:
        try:
            return (unpack('{}{}'.format(self.endianess, 'I'), chunk[4166:4170])[0] == object_id) & \
                   (unpack('{}{}'.format(self.endianess, 'I'), chunk[4174:4178])[0] == data_size)
        except error:
            return False

    def get_object_id(self, chunk: bytes) -> int:
        return unpack('{}{}'.format(self.endianess, 'I'), chunk[2054:2058])[0]

    def get_data_size(self, chunk: bytes) -> int:
        return unpack('{}{}'.format(self.endianess, 'I'), chunk[292:296])[0]
